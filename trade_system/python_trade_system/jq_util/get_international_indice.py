import jqdatasdk as jq
from jqdatasdk import finance
import login_util
import json
import numpy
import datetime
"""获取国际化指标"""
class InternationalIndice(object):

    """初始化登陆聚宽"""
    def __init__(self):
        login_util.login()

    """获取纳克达斯指数"""
    def get_Nasdaq_Composite_Index(self,count = 10  ):
        return  self.get_International_Index("IXIC" , count)

    """获取国际指数"""
    def get_International_Index(self, code ,count = 1):
        q = jq.query(finance.GLOBAL_IDX_DAILY).filter(finance.GLOBAL_IDX_DAILY.code == code).order_by(
            finance.GLOBAL_IDX_DAILY.day.desc()).limit(count)
        return finance.run_query(q)

    """获取上证50信息"""
    def get_SSE_50_Index(self,count = 100):
        return jq.get_price('000001.XSHG', count= count, end_date='2019-08-21',fq='pre',)

    """获取指定某一只股票信息"""
    def get_Stock_Price(self, code , end_date, count = 10 ,start_date=None,):
        if( start_date == None ):
            return jq.get_price(code , count= 100, end_date= end_date,fq='pre',)
        else:
            return jq.get_price(code , start_date= start_date, end_date= end_date,fq='pre',)
# query = InternationalIndice()
# data = query.get_Nasdaq_Composite_Index()
# print(data[['open','close','low','high']])
# print(data[['day','open','close','low','high']].to_json())
# print(numpy.array(data[['open','close','low','high']]))
# print(query.get_SSE_50_Index())