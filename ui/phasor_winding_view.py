class PhasorWindingView(object):

    def __init__(self, ax):
        self.ax = ax
        self.ax.set_title("Phasor Winding")
        self.ax.set_xlabel("phasor freq. (Hz)")
        self.ax.set_ylabel("Re[phasor]")
        self.handle, = ax.plot(0, 0, 'o', color="red")

    # the phasor winding plot
    def show(self, frequencyAmplitude):
        self.ax.plot(frequencyAmplitude.x, frequencyAmplitude.y)

   # the phasor winding plot
    def update(self, point):
        self.handle.set_xdata(point[0])
        self.handle.set_ydata(point[1])
