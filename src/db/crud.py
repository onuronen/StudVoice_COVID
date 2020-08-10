import logging
import pandas as pd
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.db.models import Problem, Base
from config import postgres_config

logger = logging.getLogger(__name__)
conn_str = f"postgresql://{postgres_config['user']}:{postgres_config['password']}@{postgres_config['host']}/{postgres_config['database']}"
engine = create_engine(conn_str)
Session = sessionmaker(bind=engine)

def create_tables():
    logger.info("Creating the database if it does not already exist")
    Base.metadata.create_all(bind=engine)


def fetch_rows(BaseClass):
    session = Session()

    try:
        result = session.query(BaseClass)
    
    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


def update_table(new_df, BaseClass):

    session = Session()
    session.bulk_insert_mappings(
            BaseClass,
            new_df.to_dict(orient="records"))
    session.commit()
    session.close()


if __name__ == '__main__':
    pass
