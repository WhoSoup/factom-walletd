import time
import threading
from ctypes import *

class FactomWalletd(threading.Thread):

    def __init__(self, *args, **kwargs):
        self.factom_walletd = cdll.LoadLibrary("./factom-walletd.so")
        self.factom_walletd.Serve.argtypes = []
        self.factom_walletd.Shutdown.argtypes = []
        super(FactomWalletd, self).__init__(*args, **kwargs)

    def run(self):
        self.factom_walletd.Serve()

    def join(self, *args, **kwargs):
        self.factom_walletd.Shutdown()
        super(FactomWalletd, self).join(*args, **kwargs)

node = FactomWalletd()
node.start()
time.sleep(30)
node.join()
