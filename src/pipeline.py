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
    country_map = {
            "VN":"Viet Nam",
            "VIET NAM": "Viet Nam",
            "VIETNAM": "Viet Nam"
    }
    df_cus["country"] = df_cus["country"].replace(country_map)

    df_ord = clean(df_ord)
    df_prod = clean(df_prod)


    df = df_ord.merge(df_prod, left_on="product_id", right_on= "product_id", how= "left")[["order_id","customer_id","product_id","quantity","order_date","product_name","price"]]

    df = df.merge(df_cus, left_on="customer_id", right_on= "customer_id",how= "left")[["order_id","customer_id","product_id","quantity","order_date","product_name","price","customer_name","email", "country"]]
    print (df)
   


if __name__ == "__main__":
    df_cus = pipeline_run()
