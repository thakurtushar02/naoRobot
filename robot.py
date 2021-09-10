from naoqi import ALProxy
from constants import DanceVer, dance1Info, dance2Info


class Robot:
    def __init__(self, ip, port, dance_ver):
        self.ip = ip
        self.port = port
        self.dance_ver = dance_ver

    def stand_up(self):
        try:
            postureProxy = ALProxy("ALRobotPosture", self.ip, self.port)
            postureProxy.goToPosture("StandInit", 1.0)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e

    def play_song(self, file_path):
        try:
            audioPlayerProxy = ALProxy("ALAudioPlayer", self.ip, self.port)
            audioPlayerProxy.playFile(file_path)
        except Exception, e:
            print "Could not create proxy to ALAudioPlayer"
            print "Error was: ", e

    def dance_no_sync(self):
        behavior_name = self.dance_ver
        try:
            behaviorMgrProxy = ALProxy("ALBehaviorManager", self.ip, self.port)
            # Check that the behavior exists.
            if behaviorMgrProxy.isBehaviorInstalled(behavior_name):
                # Check that it is not already running.
                if behaviorMgrProxy.isBehaviorRunning(behavior_name):
                    behaviorMgrProxy.stopBehavior(behavior_name)
                behaviorMgrProxy.runBehavior(behavior_name, _async=True)
            else:
                print "Behavior not found."
                return
        except Exception, e:
            print "Could not create proxy to ALBehaviorManager"
            print "Error was: ", e

    def dance_sync(self):
        try:
            motionProxy = ALProxy("ALMotion", self.ip, self.port)
            [names, times, keys] = dance1Info() if self.dance_ver == DanceVer.dance1 else dance2Info()
            motionProxy.angleInterpolationBezier(names, times, keys)
        except Exception, e:
            print "Could not create proxy to ALMotion"
            print "Error was: ", e