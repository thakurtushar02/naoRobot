from robot import Robot
from constants import DanceVer, SONG_FILE_PATH
from threading import Thread
from naoqi import ALProxy

ans = raw_input("Sync? [Y/N/stop]: ")
robot_list = [Robot("127.0.0.1", 60746, DanceVer.dance1)]

# all robots stand up
for robot in robot_list:
    robot.stand_up()

# first robot plays song
# does not work with virtual robot as there is no file system
# thread = Thread(target=robot_list[0].play_song, args=[SONG_FILE_PATH])
# thread.start()

if ans == "Y" or ans == "y":
    for robot in robot_list:
        thread = Thread(target=robot.dance_sync)
        thread.start()
elif ans == "N" or ans == "n":
    for robot in robot_list:
        thread = Thread(target=robot.dance_no_sync)
        thread.start()
else:
    for robot in robot_list:
        behavior_mng_service = ALProxy("ALBehaviorManager", robot[0], 9559)
        behavior_mng_service.stopAllBehaviors()
