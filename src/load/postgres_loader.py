from sqlalchemy import create_engine


def load(df):

    engine = create_engine(
        "postgresql://etl:etl@localhost:5433/etl_db"
    )

    df.to_sql(
        "posts",
        engine,
        if_exists="replace",
        index=False
    )