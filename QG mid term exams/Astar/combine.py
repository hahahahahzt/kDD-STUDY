"""随时standby！"""import pymysql.cursors  # 请求import pymysqlimport jsonclass MySQL(object):    def __init__(self, user='root', passwords ='580808@Zjm'):  # 连接数据库        self.config = {            'host': "localhost",            'user': user,            'password': passwords,            'db': 'trarecsys',            'charset': 'utf8mb4',            'cursorclass': pymysql.cursors.DictCursor        }        try:            self.db = pymysql.connect(**self.config)            self.cursor = self.db.cursor()        except:            print("connect mysql error.")