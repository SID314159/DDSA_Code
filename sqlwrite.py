import pandas as pd 
from sqlalchemy import create_engine, URL,exc

class sqlwrt():
    def writedb(self, data):
        connect_args = {
                "ssl_verify_cert": True,
                "ssl_verify_identity": True,
                "ssl_ca": r"G:\DS\guvi\Projects\Project2\DDSA\DDSA_Code\certificate\isrgrootx1.pem",
            }
            
        engine = create_engine(
                URL.create(
                drivername="mysql+pymysql",
                username="3LHApunfAprgwZ4.root",
                password="UTR1eix9QCrXfwML",
                host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
                port=4000,
                database="nifty50",
            ), connect_args=connect_args)

        try:
            #columntype={"ratingsCount": Integer}
            data.to_sql(
                name="stocks",       # Table name
                con=engine,              # SQLAlchemy engine
                if_exists="append",     # Options: 'fail', 'replace', 'append'
                index=False,             # Do not write the DataFrame index as a column
                #dtype=columntype
            )

        except exc.SQLAlchemyError as e:
            print(e)

        finally:
            engine.dispose()
            return "Engine closed"
