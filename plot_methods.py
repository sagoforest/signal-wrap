import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
foregroundColor = "#FFFFFF"
backgroundColor = "#000000"

def setAxisColors(ax):
    ax.patch.set_facecolor(backgroundColor)
    plt.setp(ax.spines.values(), color=foregroundColor)
    ax.tick_params(axis='x', colors=foregroundColor)
    ax.tick_params(axis='y', colors=foregroundColor)
    ax.xaxis.label.set_color(foregroundColor)
    ax.yaxis.label.set_color(foregroundColor)
    ax.title.set_color(foregroundColor)
    ax.grid(color=foregroundColor)

def interactive_plot(initialFreqHz, callback, frequencyAmplitude):
    fig = plt.figure(figsize=(13, 10))
    ax = fig.add_subplot(2, 1, 1)
    ax.set_aspect('equal')
    ax.set_title("Winding Plot")
    ax.set_xlabel("Re[phasor(f)]")
    ax.set_ylabel("Im[phasor(f)]")

    plt.subplots_adjust(left=0.1, bottom=0.12, hspace=0.24, top=0.96)

    # update the colors
    fig.patch.set_facecolor(backgroundColor)
    setAxisColors(ax)

    ph = [0]*3
    ph[0], = ax.plot(0, 0, color="yellow")
    ph[1], = ax.plot(0, 0, 's', color="red")

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    ph = initialize_freqAmp(fig, frequencyAmplitude, ph)
    samp = setup_slider(callback, ph, initialFreqHz)
    return fig, ax, samp

def initialize_freqAmp(fig, frequencyAmplitude, ph):
    ax = fig.add_subplot(2, 1, 2)
    setAxisColors(ax)
    ax.plot(frequencyAmplitude.x, frequencyAmplitude.y)
    ax.set_title("Phasor Winding")
    ax.set_xlabel("phasor freq. (Hz)")
    ax.set_ylabel("Re[phasor]")
    ph[2], = ax.plot(0, 0, 'o', color="red")
    return ph

def setup_slider(callback, ph, initialFreqHz):
    freq = plt.axes([0.1, 0.03, 0.8, 0.03], facecolor=foregroundColor)
    samp = Slider(freq, 'Phasor Freq.', 0.0, 6.0, valinit=initialFreqHz)
    samp.label.set_color(foregroundColor)
    samp.valtext.set_color(foregroundColor)
    samp.on_changed(lambda val: _interactive_update(val, callback, ph))
    samp.set_val(initialFreqHz)
    return samp

def _interactive_update(val, callback, ph):
    wrap = callback(val)
    mu = wrap.mean()
    ph[0].set_xdata(wrap.x)
    ph[0].set_ydata(wrap.y)
    ph[1].set_xdata(mu[0])
    ph[1].set_ydata(mu[1])
    ph[2].set_xdata(val)
    ph[2].set_ydata(mu[0])
def show():
    plt.show()

def signal_plots(signalsArray):
    fig = plt.figure(figsize=(7, 10))
    plt.subplots_adjust(hspace=0.4)
    fig.patch.set_facecolor(backgroundColor)
    N = len(signalsArray)
    for index in range(N):
        signal = signalsArray[index]
        ax = fig.add_subplot(N, 1, index+1)
        setAxisColors(ax)
        ax.set_title(signal.name)
        ax.set_xlabel("time (s)")
        ax.set_ylabel("pressure (pa)")
        ax.plot(signal.x, signal.y)
        ax.grid()



