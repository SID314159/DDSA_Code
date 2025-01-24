from dataclean import dtclean
from sqlwrite import sqlwrt
def main():
    objdataclean= dtclean()
    data=objdataclean.retsqldf() # getting transformed data
    
    objsqlwrt=sqlwrt()           # writing to database
    print(objsqlwrt.writedb(data))
    

if __name__ == "__main__":
    main()