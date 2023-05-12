from riaps.run.comp import Component
import spdlog


class Ticker(Component):

    def __init__(self):
        super(Ticker, self).__init__()

    def on_clock(self):
        msg = self.clock.recv_pyobj()
        self.logger.info(f"Hello world! at {msg}")
        