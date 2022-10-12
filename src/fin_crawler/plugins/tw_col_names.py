

"""
    法人英文縮寫:
        法人:institutional investor => II
        外資:foreign investors => IIFI
        自營商:dealer => IID
        投信:investment trust => IIIT

    三大法人:
        "證券代號":stock_id
        "證券名稱":stock_name
        "外陸資買進股數(不含外資自營商)":IIFI_buy_amount_woIIFD
        "外陸資賣出股數(不含外資自營商)":IIFI_sell_amount_woIIFD
        "外陸資買賣超股數(不含外資自營商)":IIFI_net_amount_woIIFD
        "外資自營商買進股數":IIFD_buy_amount
        "外資自營商賣出股數":IIFD_sell_amount
        "外資自營商買賣超股數":IIFD_net_amount
        "投信買進股數":IIIT_buy_amount
        "投信賣出股數":IIIT_sell_amount
        "投信買賣超股數":IIIT_net_amount
        "自營商買賣超股數":IID_net_amount
        "自營商買進股數(自行買賣)":IID_buy_amount_self
        "自營商賣出股數(自行買賣)":IID_sell_amount_self
        "自營商買賣超股數(自行買賣)":IID_net_amount_self
        "自營商買進股數(避險)":IID_buy_amount_hedging
        "自營商賣出股數(避險)":IID_sell_amount_hedging
        "自營商買賣超股數(避險)":IID_net_amount_hedging
        "三大法人買賣超股數":II_net_amount

    股價:
        證券代號:stock_id
        證券名稱:stock_name
        交易股數:vol
        成交筆數:trade_num
        成交金額:trade_amount
        開盤價:open
        最高價:high
        最低價:low
        收盤價:close
        漲跌(+/-):direction
        漲跌價差:spread
        最後揭示買價:last_buy_price
        最後揭示買量:last_buy_amount
        最後揭示賣價:last_sell_price
        最後揭示賣量:last_sell_amount
        本益比:PE
        日期:date





"""

template = {
    "stock_id":"證券代號",
    "stock_name":"證券名稱",
    "vol":"交易股數",
    "trade_num":"成交筆數",
    "trade_amount":"成交金額",
    "open":"開盤價",
    "high":"最高價",
    "low":"最低價",
    "close":"收盤價",
    "spread":"漲跌價差",
    "stock_id":"證券代號",
    "stock_id":"證券代號",
    "date":"日期",
    "IIFI_buy_amount_woIIFD":"外陸資買進股數(不含外資自營商)",
    "IIFI_sell_amount_woIIFD":"外陸資賣出股數(不含外資自營商)",
    "IIFI_net_amount_woIIFD":"外陸資買賣超股數(不含外資自營商)",
    "IIFD_buy_amount":"外資自營商買進股數",
    "IIFD_sell_amount":"外資自營商賣出股數",
    "IIFD_net_amount":"外資自營商買賣超股數",
    "IIIT_buy_amount":"投信買進股數",
    "IIIT_sell_amount":"投信賣出股數",
    "IIIT_net_amount":"投信買賣超股數",
    "IID_net_amount":"自營商買賣超股數",
    "IID_buy_amount_self":"自營商買進股數(自行買賣)",
    "IID_sell_amount_self":"自營商賣出股數(自行買賣)",
    "IID_net_amount_self":"自營商買賣超股數(自行買賣)",
    "IID_buy_amount_hedging":"自營商買進股數(避險)",
    "IID_sell_amount_hedging":"自營商賣出股數(避險)",
    "IID_net_amount_hedging":"自營商買賣超股數(避險)",
    "II_net_amount":"三大法人買賣超股數"
}

def gen_col_names(items:list):
    col_names = {}
    for name,value in template.items():
        if name in items:
            col_names[name]=value
    return col_names