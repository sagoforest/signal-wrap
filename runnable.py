from signal_factory import SignalFactory
from fourier_wrap_processor import FourierWrapProcessor
from phasor import Phasor
import plot_methods as plots

# generate signal
signalFactory = SignalFactory()
fourierWrapProcessor = FourierWrapProcessor()

T = 12
fs = 1000
signalA = signalFactory.createSinusoid("Signal A", T, fs, 1, 0).offset(1)
signalB = signalFactory.createSinusoid("Signal B", T, fs, 5.5, 0).offset(1)
signalC = signalFactory.combineSignals("Signal A + B", signalA, signalB).scale(1/4)

# this is the centroid of the wound signal over several winding frequencies
frequencyAmp = signalFactory.createFrequencyAmplitude(signalC, 6, fourierWrapProcessor)

# this phasor is used in the plot callback
phasor = Phasor(1)
def generate_wrap(val):
    phasor.frequencyHz = val
    return fourierWrapProcessor.wrap(signalC, phasor)

# the art corner
plots.signal_plots([signalA, signalB, signalC])
p = plots.interactive_plot(phasor.frequencyHz, generate_wrap, frequencyAmp)
plots.show()


