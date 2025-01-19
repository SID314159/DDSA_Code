import pandas as pd
import yaml
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

print(df1, df1.shape)



