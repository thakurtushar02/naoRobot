import verse1
import verse2
import chorus

from naoqi import ALProxy
from flask import Flask, request, session, jsonify

def sync(ip, motion, is_verse1):
    behavior_mng_service = ALProxy("ALBehaviorManager", ip, 9559)
    behavior_mng_service.runBehavior("stand-166579/behavior_1", _async=True)

    if is_verse1:
        [names, times, keys] = verse1.verse1()
    else:
        [names, times, keys] = verse2.verse2()

    [chorus_names, chorus_times, chorus_keys] = chorus.chorus()

    motion.angleInterpolationBezier(names, times, keys)

    motion.angleInterpolationBezier(chorus_names, chorus_times, chorus_keys)
