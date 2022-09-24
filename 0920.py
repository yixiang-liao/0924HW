from flask import Flask
from flask import request
import yfinance as yf
import datetime
import requests
import pandas

app = Flask(__name__)

from flask import render_template
@app.route('/post1')
def post1():
    return render_template('index.html')

@app.route('/submit' ,  methods = ['POST'])
def submit():
    name = request.values['name']
    myID = request.values['myID']
    # 日期
    today = datetime.datetime.today # 今天日期

    # 道瓊指數(DJI)
    df_DJI = yf.Ticker("^DJI").history(period="max") # 道瓊指數資料
    DJI_close = round(df_DJI.values[-1][3],2) # 今日道瓊指數
    DJI_close_2 = round(df_DJI.values[-2][3],2) # 昨日道瓊指數
    DJI_Spread = round((DJI_close - DJI_close_2),2) # 道瓊指數價差
    # 那斯達克(IXIC)
    df_IXIC = yf.Ticker("^IXIC").history(period="max") # 那斯達克指數資料
    IXIC_close = round(df_IXIC.values[-1][3],2) # 今日那斯達克指數
    IXIC_close_2 = round(df_IXIC.values[-2][3],2) # 昨日那斯達克指數
    IXIC_Spread = round((DJI_close - DJI_close_2),2) # 道瓊指數價差
    # 美元匯率(USDTWD=X)
    df_usd = yf.Ticker("USDTWD=X").history(period="max") # 美元匯率資料
    usd_close = round(df_usd.values[-1][3],2) # 今日美元匯率
    usd_close_2 = round(df_usd.values[-2][3],2) # 昨日那斯達克指數
    usd_Spread = round((usd_close - usd_close_2),2) # 道瓊指數價差
    # 美國公債10年期(TNX)
    df_TNX = yf.Ticker("^TNX").history(period="max") # 美國公債10年期資料
    TNX_close = round(df_TNX.values[-1][3],2) # 今日美國公債10年期
    TNX_close_2 = round(df_TNX.values[-2][3],2) # 昨日那斯達克指數
    TNX_Spread = round((TNX_close - TNX_close_2),2) # 道瓊指數價差
    # 加權股價指數(TWII)
    df_TWII = yf.Ticker("^TWII").history(period="max") # 加權股價指數資料
    TWII_close = round(df_TWII.values[-1][3],2) # 今日加權股價指數
    TWII_close_2 = round(df_TWII.values[-2][3],2) # 昨日那斯達克指數
    TWII_Spread = round((TWII_close - TWII_close_2),2) # 道瓊指數價差
    # 西德州原油(WTI)
    df_WTI = yf.Ticker("^WTI").history(period="max") # 西德州原油資料
    WTI_close = round(df_WTI.values[-1][3],2) # 今日西德州原油

    return render_template('index2.html' , name=name , myID=myID , today=today , WTI_close=WTI_close , TWII_close=TWII_close , TWII_close_2=TWII_close_2 , TWII_Spread=TWII_Spread , TNX_close=TNX_close , TNX_close_2=TNX_close_2 , TNX_Spread=TNX_Spread , usd_close=usd_close , usd_close_2=usd_close_2 , usd_Spread=usd_Spread , IXIC_close=IXIC_close , IXIC_close_2=IXIC_close_2 , IXIC_Spread=IXIC_Spread , DJI_close=DJI_close , DJI_close_2=DJI_close_2 , DJI_Spread=DJI_Spread)


if __name__ == '__main__':
    app.debug = True
    app.run()