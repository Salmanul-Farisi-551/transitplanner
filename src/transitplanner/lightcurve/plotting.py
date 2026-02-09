import matplotlib.pyplot as plt

def plot_lightcurve(obstime, flux, info, title="Light Curve"):
    ingress, indepth, egress = info["markers"]
    error = info["error"]

    plt.figure()
    plt.plot(obstime, flux)
    plt.errorbar(obstime[[ingress, indepth, egress]], flux[[ingress, indepth, egress]], error, fmt="o", color="red")
    plt.xlabel("Observation Time (Hours)")
    plt.ylabel("Relative Flux")
    plt.title(title)
    plt.savefig("lightcurve.png", dpi=150, bbox_inches="tight")
    plt.show()

