
from . import toc
from direct.task import Task
from toontown.toonbase.ToontownModules import ConfigVariableString

class TTToc(toc.TocTalk):

    def __init__(self):
        screenName = ConfigVariableString("AIM-screenname", "").getValue()
        password = ConfigVariableString("AIM-password", "").getValue()
        self.taskName = "TTToc"
        toc.TocTalk.__init__(self, screenName, password)
        self.connect()
        self.startTask()

    def startTask(self):
        self._running = 1
        self._socket.setblocking(0)
        taskMgr.add(self.taskProc, self.taskName)

    def stopTask(self):
        self._running = 0
        taskMgr.remove(self.taskName)

    def taskProc(self, task):
        event = self.recv_event()
        if event:
            print(event)
            self.handle_event(event)
        return Task.cont

    def on_IM_IN(self,data):
        screenname = data.split(":")[0]
        message = self.strip_html(data.split(":",2)[2])
        print(screenname, message)
        localAvatar.setSystemMessage(0, "%s: %s" % (screenname, message))
