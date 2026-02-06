import pandas as pd

def check_observability_table(planet_list, export_csv=None, export_excel=None):
    summary_data = []

    for planet in planet_list:
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




