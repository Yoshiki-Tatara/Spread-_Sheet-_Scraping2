import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g

# CSVデータの読み込み
def load_csv(csv_file_path):
    return pd.read_csv(csv_file_path)

# データ処理（ここでは仮の処理として列の合計を計算）
def process_data(df):
    df['Total'] = df.sum(axis=1)
    return df

# Googleスプレッドシートへの出力
def upload_to_spreadsheet(df, spreadsheet_key, worksheet_name, creds_json):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
    d2g.upload(df, spreadsheet_key, worksheet_name, credentials=creds, row_names=True)

# 実行
if __name__ == "__main__":
    # CSVファイルパス
    csv_file_path = 'path/to/your/csv_file.csv'
    
    # スプレッドシートの設定
    spreadsheet_key = 'your_spreadsheet_key_here'
    worksheet_name = 'Sheet1'
    creds_json = 'path/to/your/google-credentials.json'

    # CSVデータの読み込み
    df = load_csv(csv_file_path)

    # データ処理
    processed_df = process_data(df)

    # スプレッドシートへの出力
    upload_to_spreadsheet(processed_df, spreadsheet_key, worksheet_name, creds_json)
