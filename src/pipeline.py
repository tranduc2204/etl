import pandas as pd
from src.extract.reader import ufn_reader_csv
from src.transform.clearn import clean
from pathlib import Path


def pipeline_run ():
    print ("test")
    
    BASE_DIR = Path(__file__).resolve().parent.parent

    file_path = BASE_DIR / "src" /"data" / "customers.csv"
    df_cus = ufn_reader_csv (file_path)
    
    file_path = BASE_DIR / "src" /"data" / "orders.csv"
    df_ord = ufn_reader_csv (file_path)

    file_path = BASE_DIR / "src" /"data" / "products.csv"
    df_prod = ufn_reader_csv (file_path)
    
    df_cus = clean(df_cus)
    # df_ord = clean(df_ord)
    # df_prod = clean(df_prod)

    print (df_cus)
    print (df_ord)
    print (df_prod)


if __name__ == "__main__":
    df_cus = pipeline_run()
