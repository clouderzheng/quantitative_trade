import pymysql
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import  PooledDB
import Config
class Mysql(object):

    __pool = None

    """初始化参数"""
    def __init__(self):
        self._conn = Mysql.getConn()
        self._cursor = self._conn.cursor()

    """静态方法初始化连接池"""
    @staticmethod
    def getConn():
        if Mysql.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1 , maxcached=20 , \
                              host=Config.DBHOST , port=Config.DBPORT , user=Config.DBUSER , passwd=Config.DBPWD , \
                              db=Config.DBNAME,use_unicode=False,charset=Config.DBCHAR,cursorclass=DictCursor)
        return __pool.connection()

    """获取单条结果集"""
    def getOne(self, sql, param=None):

        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    """获取所有结果集"""
    def getAll(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    """获取指定结果集"""
    def getMany(self, sql, num, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    """插入单条sql占位符  %s  vaelus  uple(tuple)/list[list]"""
    def insertOne(self, sql, value):
        self._cursor.execute(sql, value)
        return self.__getInsertId()
    """插入多条 sql占位符  %s  vaelus  uple(tuple)/list[list]"""
    def insertMany(self, sql, values):
        count = self._cursor.executemany(sql, values)
        return count

    """
        获取当前连接最后一次插入操作生成的id,如果没有则为０
        """
    def __getInsertId(self):
        self._cursor.execute("SELECT @@IDENTITY AS id")
        result = self._cursor.fetchall()
        return result[0]['id']

    """查询总个数"""
    def __queryCount(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    """更新数据  """
    def update(self, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    """删除数据"""
    def delete(self, sql, param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要删除的条件 值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback');
        self._cursor.close()
        self._conn.close()
# mysql = Mysql()
#
# sql = "SELECT * from system_user where account = %s and  password = %s"
# result = mysql.getOne(sql,("night","111"))
#
