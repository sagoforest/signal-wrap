from phasor import Phasor
from signal_base import SignalBase

class FourierWrapProcessor(object):
    
    def wrap(self, signal: SignalBase, phasor: Phasor)->SignalBase:
        vals = phasor.value(signal.x)
        return SignalBase(vals.real*signal.y, vals.imag*signal.y)
