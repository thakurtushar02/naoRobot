import sync
import no_sync
from naoqi import ALProxy

ans = raw_input("Sync? [Y/N] :")
motion = ALProxy("ALMotion", "192.168.0.100", 9559)
if ans == "Y":
    sync.sync(motion, True)
else:
    no_sync.no_sync()