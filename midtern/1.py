import yfinance as yf
from datetime import datetime, timedelta

# 取得今天的日期
today = datetime.today().strftime('%Y-%m-%d')
# 股票代號列表
stock_codes = ["2330.TW", "2303.TW", "2317.TW", "3481.TW"]  # 你可以在這裡新增其他股票代碼

# 用來儲存所有股票資料的字典
stock_data = {}
no_update_data = []

# 下載並處理每一隻股票的資料
for stock_code in stock_codes:
    # 下載今天的資料
    df_today = yf.download(stock_code, start=today, end=today)

    # 檢查是否有資料
    if not df_today.empty:
        # 只保留需要的欄位：開盤、最高、最低、收盤
        df_today = df_today[['Open', 'High', 'Low', 'Close']]

        # 儲存該股票的資料到字典中，以股票代碼作為鍵
        stock_data[stock_code] = df_today
    else:
        # 記錄沒有更新資料的股票
        no_update_data.append(stock_code)

# 讓用戶輸入股票代碼或關掉
while True:
    user_input = input("請輸入股票代碼（例如：2330）或輸入「off」來結束程式：")
    
    if user_input == "off":
        print("程式結束。")
        break
    else:
        # 檢查輸入的股票代碼是否在字典中
        stock_code = user_input + ".TW"
        
        if stock_code in stock_data:
            print(f"\n股票代號: {stock_code}")
            print(stock_data[stock_code])
        elif stock_code in no_update_data:
            print(f"\n股票代號: {stock_code} 有資料但今日未更新。")
        else:
            print(f"股票代號 {stock_code} 不在資料中或今天沒有交易資料。")
