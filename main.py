from dataclean import dtclean
from sqlwrite import sqlwrt
from splitter import split
import streamlit as st
def main():
    objdataclean= dtclean()
    data=objdataclean.retsqldf() # getting transformed data
    
    objsqlwrt=sqlwrt()           # writing to database
    print(objsqlwrt.writedb(data))

    st.write("Split each index data")
    if st.button("Split"):
        objectsplit=split()
        st.write(objectsplit.splitfif())


if __name__ == "__main__":
    main()