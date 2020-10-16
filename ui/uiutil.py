import matplotlib.pyplot as plt

class UiUtil(object):
    FOREGROUND_COLOR = "#FFFFFF"
    BACKGROUND_COLOR = "#000000"
    # sets the common color properties for an axes
    @staticmethod
    def setAxisColors(ax):
        backgroundColor = UiUtil.BACKGROUND_COLOR
        foregroundColor = UiUtil.FOREGROUND_COLOR
        ax.patch.set_facecolor(backgroundColor)
        plt.setp(ax.spines.values(), color=foregroundColor)
        ax.tick_params(axis='x', colors=foregroundColor)
        ax.tick_params(axis='y', colors=foregroundColor)
        ax.xaxis.label.set_color(foregroundColor)
        ax.yaxis.label.set_color(foregroundColor)
        ax.title.set_color(foregroundColor)
        ax.grid(color=foregroundColor)

    @staticmethod
    def show():
        plt.show()
