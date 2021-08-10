import sync
import no_sync
from naoqi import ALProxy

ans = raw_input("Sync? [Y/N]: ")
ip = "192.168.0.100"
motion = ALProxy("ALMotion", ip, 9559)
if ans == "Y":
    sync.sync(ip, motion, False)
else:
    no_sync.no_sync(ip)
