from toontown.launcher.ToontownWebLauncher import ToontownWebLauncher
from otp.launcher.ExploreDirectory import exploreDirectory

launcher = None
def main(appRunner = None):
    if not appRunner:
        print("Not running in a web environment; using dummyAppRunner.")
        from direct.p3d.AppRunner import dummyAppRunner
        from toontown.toonbase.ToontownModules import PandaSystem
        appRunner = dummyAppRunner()

        # In this case, simulate that we've already downloaded tt_3, since
        # that is guaranteed in the web environment.
        hostUrl = PandaSystem.getPackageHostUrl()
        appRunner.addPackageInfo('tt_3', None, None, hostUrl)

    if int(appRunner.tokenDict.get('download', '0')):
        # When the download token is set, it means we only want to use
        # this p3d file to download the required files, and then exit.
        print("Download token set; not running launcher.")
        import sys
        sys.exit(0)


    exploreDirectory(appRunner)

    global launcher
    launcher = ToontownWebLauncher(appRunner)
    print("Reached end of StartToontownLauncher.py.")
