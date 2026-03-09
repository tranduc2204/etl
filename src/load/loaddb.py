import pandas as pd
from src.extract.reader import ufn_reader_csv
from src.transform.clearn import clean
from pathlib import Path
from sqlalchemy import create_engine


def load_to_db (df):

    engine = create_engine(
        "postgresql://etl:etl@localhost:5433/etl_db"
    )
    df.to_sql(
        "posts",
        engine,
        if_exists="replace",
        index=False
    )

    print (engine.connect())

    df = pd.read_sql(
        "SELECT * FROM posts",
        engine
    )
    print(df)

if __name__ =="__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path = BASE_DIR  /"data" / "customers.csv"
    df_cus = ufn_reader_csv (file_path)
    df_cus = clean(df_cus)
    print (df_cus)
    load_to_db(df_cus)