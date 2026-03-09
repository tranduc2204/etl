from pathlib import Path
from src.extract.reader import ufn_reader_csv


def clean(df):
   
    col_str = df.select_dtypes(include = "str").columns
    df[col_str] = df[col_str].apply(lambda col:col.str.strip().str.upper())
    
   
    return df

# if __name__ =="__main__":
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     file_path = BASE_DIR  /"data" / "customers.csv"
#     df_cus = ufn_reader_csv (file_path)
#     print (df_cus)

    