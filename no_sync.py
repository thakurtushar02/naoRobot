from naoqi import ALProxy
import time


def getBehaviors(ip):
    """
    Know which behaviors are on the robot.
    """
    behavior_mng_service = ALProxy("ALBehaviorManager", ip, 9559)

    names = behavior_mng_service.getInstalledBehaviors()
    print "Behaviors on the robot:"
    print names

    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names


def launchBehavior(ip, behavior_name):
    behavior_mng_service = ALProxy("ALBehaviorManager", ip, 9559)

    # Check that the behavior exists.
    if behavior_mng_service.isBehaviorInstalled(behavior_name):
        # Check that it is not already running.
        if behavior_mng_service.isBehaviorRunning(behavior_name):
            behavior_mng_service.stopBehavior(behavior_name)

        behavior_mng_service.runBehavior(behavior_name, _async=True)
        time.sleep(0.5)

    else:
        print "Behavior not found."
        return
