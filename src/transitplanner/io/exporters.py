def export_table(df, csv_path=None, excel_path=None):
    if csv_path:
        df.to_csv(csv_path, index=False)
    if excel_path:
        df.to_excel(excel_path, index=False)
