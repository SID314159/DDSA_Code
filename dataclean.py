import pandas as pd
import yaml

class dtclean():
    def retsqldf(self):
        #generating date range
        mlst=pd.date_range(start='2023-10',end="2025-01", freq='ME')
        mnths=pd.DataFrame(mlst).astype(str)
        mlst=[]
        for i in mnths[0]:
            s=i[:-3]
            mlst.append(s)

        df1=pd.DataFrame()

        for i in range(0, len(mlst)-1):
            dtlst = pd.date_range(start=mlst[i],end=mlst[i+1], freq='D')
            dates=pd.DataFrame(dtlst).astype(str)
            dates[0]=dates[0]+'_05-30-00.yaml'
            dtlst=dates[0].to_list()
            for j in dtlst:
                try:
                    path=rf"G:\DS\guvi\Projects\Project2\DDSA\DDSA_Code\data\{mlst[i]}\{j}"
                    with open(path, "r") as file:
                        yml = yaml.safe_load(file)
                        file.close
                        df=pd.DataFrame(yml)
                        df1=pd.concat([df1,df])
                        
                except:
                    continue


        #checking common keys
        secdt=pd.read_csv(r"G:\DS\guvi\Projects\Project2\DDSA\DDSA_Code\data\Sector_data.csv")
        split=secdt['symbol'].str.split(':', expand=True)
        secdt['Ticker']=split[1].str.strip()
        secdt['Ticker']=secdt['Ticker'].replace('ADANIGREEN','ADANIENT')
        secdt['Ticker']=secdt['Ticker'].replace('AIRTEL','BHARTIARTL')
        secdt['Ticker']=secdt['Ticker'].replace('TATACONSUMER','TATACONSUM')
        secdt=secdt.drop_duplicates(subset='Ticker',keep="first").sort_values(by='Ticker',ignore_index=True)

        secdt.to_csv(r"G:\DS\guvi\Projects\Project2\DDSA\DDSA_Code\cleaned_data\sectordata_cleaned.csv") #cleaned sector data
        #merging to final df
        df1["Ticker"]=df1["Ticker"].str.strip()
        df1=df1.sort_values(by=['Ticker','date'],ignore_index=True)
        sqldf=pd.merge(df1,secdt,on='Ticker',how='left')
        return(sqldf)

# objdataclean= dataclean()
# data=objdataclean.retsqldf()
# print(data)