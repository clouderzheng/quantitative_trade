import jqdatasdk as jq
from jqdatasdk import finance
import login_util
import json
import numpy

"""获取国际化指标"""
class InternationalIndice(object):

    """初始化登陆聚宽"""
    def __init__(self):
        login_util.login()

    """获取纳克达斯指数"""
    def get_Nasdaq_Composite_Index(self,count = 10):
        return  self.get_International_Index("IXIC" , count)

    """获取国际指数"""
    def get_International_Index(self, code ,count = 1):
        q = jq.query(finance.GLOBAL_IDX_DAILY).filter(finance.GLOBAL_IDX_DAILY.code ==  code).order_by(
            finance.GLOBAL_IDX_DAILY.day.desc()).limit(count)
        return finance.run_query(q)



query = InternationalIndice()
data = query.get_Nasdaq_Composite_Index()
# print(data[['open','close','low','high']])
# print(data[['day','open','close','low','high']].to_json())
# print(numpy.array(data[['open','close','low','high']]))
print(str(data['day'][0]))