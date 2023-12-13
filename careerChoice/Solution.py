import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

credentials_path = 'riasec-model-1-c1119188e695.json'  # Replace with the actual path

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/17XYkJYNmepEpBvGu6fcibaHmJ0wUmB-Aup21XXz6UEA/edit?usp=sharing'

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
gc = gspread.authorize(credentials)

spreadsheet = gc.open_by_url(spreadsheet_url)

worksheet = spreadsheet.get_worksheet(0)

data = worksheet.get_all_values()

df = pd.DataFrame(data[1:], columns=data[0])

print(df.head(2))