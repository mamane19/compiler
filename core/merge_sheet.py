import pandas as pd
from os import path

current_dir = path.dirname(path.abspath(__file__))
excel_sheet1_path = path.join(current_dir, 'sheet1.xlsx')
excel_sheet2_path = path.join(current_dir, 'sheet2.xlsx')

sheet1_df = pd.read_excel(excel_sheet1_path)
sheet2_df = pd.read_excel(excel_sheet2_path)
merge = pd.merge(sheet1_df, sheet2_df, on="NAME")
print(f'{merge}\n--------------')

csv_sheet1_path = path.join(current_dir, 'music-data1.csv')
csv_sheet2_path = path.join(current_dir, 'music-data2.csv')

sheet1_df = pd.read_csv(csv_sheet1_path)
sheet2_df = pd.read_csv(csv_sheet2_path)
merge = pd.merge(sheet1_df, sheet2_df, on="ARTIST")
print(merge)
