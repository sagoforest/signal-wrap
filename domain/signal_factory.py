from domain.signal_base import SignalBase
from domain.phasor import Phasor
import numpy as np
class SignalFactory(object):

    def createSinusoid(self, name, timeSeconds, samplingRateHz, signalFrequencyHz, phase) -> SignalBase:
        ts = 1/samplingRateHz
        t = np.arange(0, timeSeconds, ts)
        y = np.cos(2*np.pi*signalFrequencyHz*t + phase)
        return SignalBase(t, y, name)

    def combineSignals(self, name, signalA: SignalBase, signalB: SignalBase) -> SignalBase:
        x = signalA.x
        y = signalA.y + signalB.y
        return SignalBase(x, y, name)

    def createFrequencyAmplitude(self, signal, maxFreqHz, fourierWrapProcessor):
        freqsHz = np.arange(0, maxFreqHz, 0.01)
        freqAmp = [0]*len(freqsHz)
        for index in range(len(freqsHz)):
            wrap = fourierWrapProcessor.wrap(signal, freqsHz[index])
            mu = wrap.mean()
            freqAmp[index] = mu[0]
        return SignalBase(freqsHz, freqAmp)

