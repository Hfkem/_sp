import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# 股票代號列表
stock_codes = ["2330.TW", "2303.TW", "2317.TW", "3481.TW"]

# 用來儲存所有股票資料的字典
stock_data = {}
no_update_data = []

# 下載並處理每一隻股票的資料
for stock_code in stock_codes:
    try:
        #  改用 `Ticker.history()` 來獲取數據**
        stock = yf.Ticker(stock_code)
        df_today = stock.history(period="5d")  # 改用 5 日內數據，避免當日數據為空

        # 檢查是否有資料
        if not df_today.empty:
            #  調整索引格式**
            df_today.index = df_today.index.strftime('%Y-%m-%d')  # 讓日期顯示更清楚
            df_today = df_today[['Open', 'High', 'Low', 'Close']]
            


            # 儲存股票數據
            stock_data[stock_code] = df_today
        else:
            no_update_data.append(stock_code)

    except Exception as e:
        print(f"下載 {stock_code} 時發生錯誤: {e}")
        no_update_data.append(stock_code)


# 讓用戶輸入股票代碼或關掉
while True:
    user_input = input("請輸入股票代碼（例如：2330）或輸入「off」來結束程式：")

    if user_input.lower() == "off":
        print("程式結束。")
        break
    else:
        stock_code = user_input + ".TW"

        if stock_code in stock_data:
            print(f"\n股票代號: {stock_code}")
            print(stock_data[stock_code])
        elif stock_code in no_update_data:
            print(f"\n股票代號: {stock_code} 有資料但今日未更新或獲取失敗。")
        else:
            print(f"股票代號 {stock_code} 不在資料中或今天沒有交易資料。")