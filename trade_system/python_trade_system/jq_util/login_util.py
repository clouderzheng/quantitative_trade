import jqdatasdk
from python_trade_system.mysql import Config
# data = jqdatasdk.get_price(security="000001.XSHE",frequency="1m")
# print(__vers?on__)

#
# print(jqdatasdk.get_all_securities())
# print(data)

def login():
    # jqdatasdk.logout()
    jqdatasdk.auth(Config.jq_account, Config.jq_password)

    print(jqdatasdk.__version__)
    print(jqdatasdk.get_query_count())
# jqdatasdk.logout()
