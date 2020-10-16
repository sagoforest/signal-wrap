from domain.phasor import Phasor
from domain.signal_base import SignalBase


class WrapProcessor(object):
    def __init__(self, phasor: Phasor):
        self._phasor = phasor

    def wrap(self, signal: SignalBase, frequencyHz: float) -> SignalBase:
        self._phasor.frequencyHz = frequencyHz
        vals = self._phasor.value(signal.x)
        return SignalBase(vals.real*signal.y, vals.imag*signal.y)
