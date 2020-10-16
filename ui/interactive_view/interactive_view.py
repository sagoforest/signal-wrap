import matplotlib.pyplot as plt
from ui.signal_winding_view import SignalWindingView
from ui.phasor_winding_view import PhasorWindingView
from ui.uiutil import UiUtil
from ui.interactive_view.frequency_slider import FrequencySlider


class InteractiveView(object):

    def __init__(self, initialFrequency, callback):
        self.initialFrequency = initialFrequency
        self.callback = callback

        self.fig = plt.figure(figsize=(13, 10))
        self.fig.patch.set_facecolor(UiUtil.BACKGROUND_COLOR)
        plt.subplots_adjust(top=0.96)

        # add signal winding view
        ax = self.fig.add_subplot(2, 1, 1)
        UiUtil.setAxisColors(ax)
        self.signal_winding_view = SignalWindingView(ax)
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        # add phasor winding view
        ax = self.fig.add_subplot(2, 1, 2)
        UiUtil.setAxisColors(ax)
        self.phasor_winding_view = PhasorWindingView(ax)
        self.slider = FrequencySlider(self._slider_callback, initialFrequency)

    def show(self, frequencyAmplitude):
        self.phasor_winding_view.show(frequencyAmplitude)

    def _slider_callback(self, val):
        wrap = self.callback(val)
        centroid = wrap.mean()
        self.signal_winding_view.update(wrap, centroid)
        self.phasor_winding_view.update([val, centroid[0]])
