import numpy as np
import cmath
class Phasor(object):
    TWO_PI_I = 2*1j*np.pi
    def __init__(self, frequencyHz):
        self.frequencyHz = frequencyHz

    def value(self, timeSeconds):
        return np.exp(-Phasor.TWO_PI_I*self.frequencyHz*timeSeconds)
