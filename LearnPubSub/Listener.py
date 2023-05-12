from riaps.run.comp import Component
import spdlog



class Listener(Component):

    def __init__(self):
        super(Listener, self).__init__()
        
    def on_newMsg(self):
        msg = self.newMsg.recv_pyobj()
        self.logger.info(f"Received {msg}")