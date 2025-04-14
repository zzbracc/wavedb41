import requests
import pandas as pd
from datetime import datetime

# 使用者分享網址
share_url = "https://wavelive.onelink.me/tEt5/inappshareprofiletw?af_dp=wavelive%3A%2F%2F&w_user=5bd69b10-a6b2-4241-b175-0782596fd706"

# 解析 user_id
user_id = share_url.split("w_user=")[-1]

# API 查昨日日榜
url = f"https://api.wave.com.tw/api/v1/leaderboards/event?type=4&period=4&user_id={user_id}&date_shift=-1"
res = requests.get(url)
data = res.json()["data"]

# 整理成 DataFrame
df = pd.DataFrame([{
    "名次": item["rank"],
    "名字": item["userInfo"]["displayName"],
    "分數": item["score"]
} for item in data])

# 存成 Excel 檔（以日期命名）
today = datetime.today().strftime('%Y-%m-%d')
filename = f"昨日日榜_{today}.xlsx"
df.to_excel(filename, index=False)
print(f"已儲存：{filename}")
