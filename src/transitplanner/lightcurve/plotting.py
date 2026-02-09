import matplotlib.pyplot as plt

def plot_lightcurve(obstime, flux, info, title="Light Curve"):
       """

    This function visualises the simulated transit flux as a function of
    observation time. It also overlays error bars at key transit phases,
    specifically ingress, mid transit and egress.

    Marker indices and photometric uncertainty are provided through the
    info dictionary, which is produced by the light curve simulation stage.

    Parameters
    obstime
    Array of observation times in hours

    flux
    Array of relative flux values corresponding to obstime

    info
    Dictionary containing plotting metadata.
    Expected keys are
    markers, a tuple of ingress, mid transit and egress indices
    error, photometric uncertainty value

    title
    Title string for the plot

    Outputs
    Saves the light curve plot as lightcurve.png and displays it on screen
    """
    
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


