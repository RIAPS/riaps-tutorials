from riaps.run.comp import Component
import spdlog

class Doubler(Component):

    def __init__(self):
        super(Doubler, self).__init__()

    def on_answerPort(self):
        msg = self.answerPort.recv_pyobj()
        self.logger.info(f"Doubling {msg}...")
        answer = msg * 2
        # Remember to send a message back with the same port!
        self.answerPort.send_pyobj(answer)