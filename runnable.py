from domain.signal_factory import SignalFactory
from domain.wrap_processor import WrapProcessor
from domain.phasor import Phasor
from ui.signals_view import SignalsView
from ui.interactive_view.interactive_view import InteractiveView
from ui.uiutil import UiUtil

# create a few useful things
phasor = Phasor(1)
signalFactory = SignalFactory()
wrapProcessor = WrapProcessor(phasor)

Ts = 5 # duration of the signals in seconds
fs = 1000  # sampling frequency

# generate some signals
signalA = signalFactory.createSinusoid("Signal A", Ts, fs, 1, 0).offset(1)
signalB = signalFactory.createSinusoid("Signal B", Ts, fs, 3.5, 0).offset(1)
signalC = signalFactory.combineSignals("Signal A + B",
                                       signalA,
                                       signalB).scale(1/4)

# this is the centroid of the wound signal over several winding frequencies
frequencyAmp = signalFactory.createFrequencyAmplitude(signalC,
                                                      6,
                                                      wrapProcessor)

# the art corner
initialWindingFrequencyHz = 1
signalsView = SignalsView()
interactive_view = InteractiveView(initialWindingFrequencyHz,
                                   lambda frequencyHz: wrapProcessor.wrap(signalC, frequencyHz))

signalsView.show([signalA, signalB, signalC])
interactive_view.show(frequencyAmp)
UiUtil.show()
