import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from ui.uiutil import UiUtil

class FrequencySlider(object):

    def __init__(self, callback, initialFreqHz):
        freq = plt.axes([0.1, 0.03, 0.8, 0.03], facecolor=UiUtil.FOREGROUND_COLOR)
        self.slider = Slider(freq, 'Phasor Freq.', 0.0, 6.0, valinit=initialFreqHz)
        self.slider.label.set_color(UiUtil.FOREGROUND_COLOR)
        self.slider.valtext.set_color(UiUtil.FOREGROUND_COLOR)
        self.slider.on_changed(lambda val: callback(val))
        self.slider.set_val(initialFreqHz)
