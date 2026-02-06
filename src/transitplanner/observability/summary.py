import pandas as pd

def check_observability_table(planet_list, export_csv=None, export_excel=None):
    summary_data = []

    for planet in planet_list:
        print(f"\n--- Observability Check for {planet['Object']} ---")
        print(f"Host star: {planet['Object']}")
        print(f"Rp/Rs: {planet['RpRs']:.4f}")
        print(f"a/Rs: {planet['aRs']:.2f}")
        print(f"Inclination: {planet['inclination']:.2f} deg")
        print(f"Transit depth: {planet['Transit Depth (mmag)']:.2f} mmag")
        print(f"Transit duration: {planet['duration_min']:.1f} min ({planet['Duration (hours)']:.3f} hours)")
        print(f"R magnitude (merged): {planet['R Magnitude']:.2f}")
        print(f"SNR: {planet['SNR']:.2f}")
        print(f"RA/DEC: {planet['RA']}, {planet['Dec']:.2f}°")
        print(f"Status: {planet['Status']}")
        summary_data.append({
            "Planet": planet['Object'],
            "Transit Start (UTC)": planet['Transit Start (UTC)'],
            "Mid-Transit (UTC)": planet['Mid-Transit (UTC)'],
            "Transit End (UTC)": planet['Transit End (UTC)'],
            "Rp/Rs": planet.get('RpRs'),
            "a/Rs": planet.get('aRs'),
            "Inclination (deg)": planet.get('inclination'),
            "Transit depth (mmag)": planet.get('Transit Depth (mmag)'),
            "Duration (min)": planet['Duration (hours)']*60,
            "R mag": planet.get('R Magnitude'),
            "SNR": planet.get('SNR'),
            "RA": planet['RA'],
            "DEC": planet['Dec'],
            "Status": planet['Status']
        })

    df = pd.DataFrame(summary_data)
    if export_csv:
        df.to_csv(export_csv, index=False)
    if export_excel:
        df.to_excel(export_excel, index=False)
    return df




