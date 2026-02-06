import matplotlib.pyplot as plt

def plot_lightcurve(obstime, flux, title="Light Curve"):
    plt.figure()
    plt.plot(obstime, flux)
    plt.xlabel("Observation Time (Hours)")
    plt.ylabel("Relative Flux")
    plt.title(title)
    plt.show()
