import sync
import no_sync
from threading import Thread
from naoqi import ALProxy

ans = raw_input("Sync? [Y/N/stop]: ")
robot_list = [("192.168.0.100", True), ("192.168.0.104", False)]

for robot in robot_list:
    behavior_mng_service = ALProxy("ALBehaviorManager", robot[0], 9559)
    behavior_mng_service.runBehavior("standup-e2d510/behavior_1", _async=True)

aup = ALProxy("ALAudioPlayer", robot_list[0][0], 9559)
thread = Thread(target=aup.playFile, args=["/home/nao/music.mp3"])
thread.start()

if ans == "Y" or ans == "y":
    for robot in robot_list:
        sync.sync(robot[0], robot[1])
elif ans == "N" or ans == "n":
    for robot in robot_list:
        thread = Thread(target=no_sync.launchBehavior, args=[robot[0], "single-ladies-c4455d/behavior_1"])
        thread.start()
else:
    for robot in robot_list:
        behavior_mng_service = ALProxy("ALBehaviorManager", robot[0], 9559)
        behavior_mng_service.stopAllBehaviors()
