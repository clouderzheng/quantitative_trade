from python_trade_system.mysql import mysql_util
"""根据账户名称获取系统用户信息"""
def get_system_user(account):
    """获取数据库连接"""
    mysql = mysql_util.Mysql()
    # 查询 sql
    query_user_by_account = "select id, account , password from system_user where account = %s"
    result = mysql.getOne(query_user_by_account, account)
    # mysql.dispose()
    return result
