import datetime
from toontown.shtiker import HtmlView

class InGameNewsFrame(HtmlView.HtmlView):

    TaskName = 'HtmlViewUpdateTask'

    def __init__(self, parent = aspect2d):
        HtmlView.HtmlView.__init__(self, parent)
        self.initialLoadDone = False
        self.accept("newsSnapshot", self.doSnapshot)

    def activate(self):
        self.quad.show()
        # our first run through on contructor gives wrong results if coming from shticker book
        self.calcMouseLimits()
        if not self.initialLoadDone:
            inGameNewsUrl = self.getInGameNewsUrl()
            #import pdb; pdb.set_trace()
            self.webView.loadURL2(inGameNewsUrl)
            self.initialLoadDone = True
        taskMgr.add(self.update, self.TaskName)

    def deactivate(self):
        self.quad.hide()
        taskMgr.remove(self.TaskName)

    def unload(self):
        self.deactivate()
        HtmlView.HtmlView.unload(self)
        self.ignore("newsSnapshot")

    def doSnapshot(self):
        "Save the current browser contents to a png file."""
        curtime = datetime.datetime.now()
        filename = "news_snapshot_" + curtime.isoformat()
        filename = filename.replace(":", "-")
        filename = filename.replace(".", "-")
        pngfilename =filename + ".png"
        self.writeTex(pngfilename)
        jpgfilename = filename + ".jpg"
        self.writeTex(jpgfilename)
        return jpgfilename
