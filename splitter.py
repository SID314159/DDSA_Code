from sqlget import sqlgt
import pandas as pd

class split():
    def splitfif(self):
        obj=sqlgt()
        query= "select distinct ticker from stocks order by ticker"
        l,c=obj.getdb(query)
        lst=[i[0] for i in l]



        for i in lst:
            query="select * from stocks where ticker=(%s)"
            ans,colmn=obj.getdb(query,(i))
            df=pd.DataFrame(ans,columns=colmn)
            df.to_csv(rf"G:\DS\guvi\Projects\Project2\DDSA\DDSA_Code\cleaned_data\splitted_50\{i}.csv")

        return("Splitted")



