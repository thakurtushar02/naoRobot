import verse1
import verse2
import chorus
import httplib, urllib
import requests
from threading import Thread
from naoqi import ALProxy

# IP address of leader robot
flask_ip = "192.168.0.101:5000"
flaskWebIP = "http://192.168.0.101:5000"


def sync(motion, is_verse1):
    behavior_mng_service = ALProxy("ALBehaviorManager", "192.168.0.100", 9559)
    behavior_mng_service.runBehavior("stand-166579/behavior_1", _async=True)

    if is_verse1:
        [names, times, keys] = verse1.verse1()
    else:
        [names, times, keys] = verse2.verse2()

    [chorus_names, chorus_times, chorus_keys] = chorus.chorus()

    motion.angleInterpolationBezier(names, times, keys)

    motion.angleInterpolationBezier(chorus_names, chorus_times, chorus_keys)
