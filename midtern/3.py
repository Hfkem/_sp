import yfinance as yf
import threading

# 用來儲存所有股票資料的字典
stock_data = {}
no_update_data = []

def fetch_stock_data(stock_code):
    """下載股票數據"""
    try:
        stock = yf.Ticker(stock_code)
        df_today = stock.history(period="5d")  # 抓取最近 5 天的數據

        if not df_today.empty:
            df_today.index = df_today.index.strftime('%Y-%m-%d')  # 格式化日期
            df_today = df_today[['Open', 'High', 'Low', 'Close']]

            stock_data[stock_code] = df_today
        else:
            no_update_data.append(stock_code)

    except Exception as e:
        print(f" 下載 {stock_code} 時發生錯誤: {e}")
        no_update_data.append(stock_code)

# 讓用戶輸入股票代碼或關閉程式
while True:
    user_input = input("請輸入股票代碼（若需輸入多組股票請以空格分開）或輸入「off」來結束程式：")

    if user_input.lower() == "off":
        print("程式結束。")
        break
    else:
        # 將輸入的股票代碼分割成列表
        stock_codes = [code.strip() + ".TW" for code in user_input.split()]

        # 建立多執行緒來加速數據獲取
        threads = []
        for stock_code in stock_codes:
            thread = threading.Thread(target=fetch_stock_data, args=(stock_code,))
            threads.append(thread)
            thread.start()

        # 等待所有執行緒完成
        for thread in threads:
            thread.join()

        # 顯示結果
        for stock_code in stock_codes:
            if stock_code in stock_data:
                print(f"\n 股票代號: {stock_code}")
                print(stock_data[stock_code])
            elif stock_code in no_update_data:
                print(f"\n 股票代號: {stock_code} 有資料但今日未更新或獲取失敗。")
            else:
                print(f" 股票代號 {stock_code} 不在資料中或今天沒有交易資料。")