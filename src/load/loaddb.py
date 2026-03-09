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

 