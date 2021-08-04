from naoqi import ALProxy
import time


def no_sync():
    behavior_mng_service = ALProxy("ALBehaviorManager", "192.168.0.100", 9559)

    getBehaviors(behavior_mng_service)
    launchAndStopBehavior(behavior_mng_service, "single-ladies-c4455d/behavior_1")
    defaultBehaviors(behavior_mng_service, "single-ladies-c4455d/behavior_1")


def getBehaviors(behavior_mng_service):
    """
    Know which behaviors are on the robot.
    """

    names = behavior_mng_service.getInstalledBehaviors()
    print "Behaviors on the robot:"
    print names

    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names


def launchAndStopBehavior(behavior_mng_service, behavior_name):
    """
    Launch and stop a behavior, if possible.
    """
    # Check that the behavior exists.
    if behavior_mng_service.isBehaviorInstalled(behavior_name):
        # Check that it is not already running.
        if not behavior_mng_service.isBehaviorRunning(behavior_name):
            # Launch behavior. This is a blocking call, use _async=True if you do not
            # want to wait for the behavior to finish.
            behavior_mng_service.runBehavior(behavior_name, _async=True)
            time.sleep(0.5)
        else:
            print "Behavior is already running."

    else:
        print "Behavior not found."
        return

    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names

    # Stop the behavior.
    if behavior_mng_service.isBehaviorRunning(behavior_name):
        behavior_mng_service.stopBehavior(behavior_name)
        time.sleep(1.0)
    else:
        print "Behavior is already stopped."

    names = behavior_mng_service.getRunningBehaviors()
    print "Running behaviors:"
    print names


def defaultBehaviors(behavior_mng_service, behavior_name):
    """
    Set a behavior as default and remove it from default behavior.
    """

    # Get default behaviors.
    names = behavior_mng_service.getDefaultBehaviors()
    print "Default behaviors:"
    print names

    # Add behavior to default.
    behavior_mng_service.addDefaultBehavior(behavior_name)

    names = behavior_mng_service.getDefaultBehaviors()
    print "Default behaviors:"
    print names

    # Remove behavior from default.
    behavior_mng_service.removeDefaultBehavior(behavior_name)

    names = behavior_mng_service.getDefaultBehaviors()
    print "Default behaviors:"
    print names
