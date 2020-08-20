from sqlalchemy.ext.declarative import declarative_base
import datetime as dt
from sqlalchemy import(
    Column,
    Boolean,
    String,
    Integer,
    Float,
    DateTime,
    JSON,
    ARRAY,
    ForeignKey
)

Base = declarative_base()

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, autoincrement = True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    added_on = Column(DateTime, default=dt.datetime.utcnow())
    isChecked = Column(Boolean, default=False)

class Approved_Problem(Base):
    __tablename__ = "approved_problems"
    id = Column(Integer, primary_key=True, autoincrement = True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    score = Column(Integer, default=0)
    added_on = Column(DateTime, default=dt.datetime.utcnow())
    isChecked = Column(Boolean, default=True)

    


if __name__ == "__main__":
    pass
