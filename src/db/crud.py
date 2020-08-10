import logging
import pandas as pd
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.models import Problem
from config import postgres_config

logger = logging.getLogger(__name__)
engine = create_engine(URL(**postgres_config))
Session = sessionmaker(bind=engine)

def create_tables():
    logger.info("Creating the database if it does not already exist")
    Base.metadata.create_all(bind=engine)


create_tables()
