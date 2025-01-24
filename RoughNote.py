import pymysql
from pymysql import Error
import pandas as pd
from tabulate import tabulate

class getsql():

    def sql(self,query,i=None):
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


obj=getsql()
query= "select distinct ticker from stocks order by ticker"
l,c=obj.sql(query)
lst=[i[0] for i in l]

for i in lst:
    query="select * from stocks where ticker=(%s)"
    ans,colmn=obj.sql(query,(i))
    df=pd.DataFrame(ans,columns=colmn)
    df.to_csv(rf"G:\DS\guvi\Projects\Project2\DDSA\DDSA_Code\cleaned_data\splitted_50\{i}.csv")

