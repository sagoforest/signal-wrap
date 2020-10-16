import matplotlib.pyplot as plt
from ui.uiutil import UiUtil

class SignalsView(object):

    def __init__(self):
        self.fig = plt.figure(figsize=(7, 10))
        self.fig.patch.set_facecolor(UiUtil.BACKGROUND_COLOR)
        plt.subplots_adjust(hspace=0.4)

    # shows a stacked array of signal plots
    def show(self, signalsArray):
        N = len(signalsArray)
        for index in range(N):
            signal = signalsArray[index]
            ax = self.fig.add_subplot(N, 1, index+1)
            UiUtil.setAxisColors(ax)
            ax.set_title(signal.name)
            ax.set_xlabel("time (s)")
            ax.set_ylabel("pressure (pa)")
            ax.plot(signal.x, signal.y)
            ax.grid()
