import panda as pd
file_path = "D:\ISO Audit\CAIQ_v3.0.1_FINAL - Cloud Nautical (002)"
excel_file = pd.ExcelFile(file_path)
sheet_names = excel_file.sheet_names
sheet_names