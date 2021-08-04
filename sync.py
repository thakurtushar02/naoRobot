import verse1
import verse2
import chorus


def sync(motion, is_verse1):
    if is_verse1:
        [names, times, keys] = verse1.verse1()
    else:
        [names, times, keys] = verse2.verse2()
    motion.angleInterpolation(names, keys, times, True)

    [names, times, keys] = chorus.chorus()
    motion.angleInterpolation(names, keys, times, True)
