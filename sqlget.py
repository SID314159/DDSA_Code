import pymysql
from pymysql import Error

class sqlgt():
    def getdb(self,query,i=None):
        try:
            connection = pymysql.connect(
            host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
            port = 4000,
            user = "3LHApunfAprgwZ4.root",
            password = "UTR1eix9QCrXfwML",
            database = "nifty50",
            ssl_verify_cert = True,
            ssl_verify_identity = True,
            ssl_ca = ""
            )

            if connection:
                cursor=connection.cursor()
                cursor.execute(query,i)
                ans=cursor.fetchall()
                colmn=[i[0] for i in cursor.description]
                

        except Error as e:
            print(e)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")
                return ans,colmn


