class SignalWindingView(object):
    def __init__(self, ax):
        self.ax = ax
        self.ax.set_aspect('equal')
        self.ax.set_title("Winding Plot")
        self.ax.set_xlabel("Re[phasor(f)]")
        self.ax.set_ylabel("Im[phasor(f)]")
        self.handle, = ax.plot(0, 0, color="yellow")
        self.centroid_handle, = ax.plot(0, 0, 's', color="red")

    # the phasor winding plot
    def update(self, signal, centroid):
        self.handle.set_xdata(signal.x)
        self.handle.set_ydata(signal.y)
        self.centroid_handle.set_xdata(centroid[0])
        self.centroid_handle.set_ydata(centroid[1])

