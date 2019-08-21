from python_trade_system.jq_util.get_international_indice import InternationalIndice
import numpy as np
def get_NASDAQ_index(result):

    internationalIndice = InternationalIndice()
    # 获取纳克达斯指数
    data = internationalIndice.get_Nasdaq_Composite_Index(100)

    # 按照时间先后排序 升序
    data = data.sort_values(by="day", axis=0, ascending=True)
    deal_with_data(result,data,"NASDAQ","day")

def get_SSE_50_index(result):
    internationalIndice = InternationalIndice()
    data = internationalIndice.get_SSE_50_Index(100)
    deal_with_data(result,data,"SSE","index")

def deal_with_data(result,data , suff,sort_column):

    # 获取时间作为x轴
    if("SSE" == suff):
        date_ = data.index.date
        times = []
        for _date in date_:
            times.append(_date)
    else:
        times = np.array(data[sort_column]).tolist()

# 开盘价 收盘价 最高价 最低价最为 y轴
    view_data = np.array(data[['open', 'close', 'low', 'high']]).tolist()
    # 指数名称作为提示指标
    code_name =suff
    result["times_" + suff] =  times
    result["view_data_" + suff] =  view_data
    result["code_name_" + suff] =  code_name

import pandas as pd
internationalIndice = InternationalIndice()
data = internationalIndice.get_SSE_50_Index(100)
# print(type(data.index[0]))
date = data.index.date
