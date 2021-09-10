from robot import Robot
import constants
from threading import Thread
from naoqi import ALProxy

ans = raw_input("Sync? [Y/N/stop]: ")
robot_list = [Robot("127.0.0.1", 60746, constants.Dance.dance1)]

# all robots stand up
for robot in robot_list:
    robot.stand_up()

# first robot plays song
# thread = Thread(target=robot_list[0].play_song, args=[constants.SONG_FILE_PATH])
# thread.start()

if ans == "Y" or ans == "y":
    for robot in robot_list:
        print("TODO")
elif ans == "N" or ans == "n":
    for robot in robot_list:
        thread = Thread(target=robot.dance_no_sync)
        thread.start()
else:
    for robot in robot_list:
        behavior_mng_service = ALProxy("ALBehaviorManager", robot[0], 9559)
        behavior_mng_service.stopAllBehaviors()
