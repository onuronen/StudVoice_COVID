from sqlalchemy.ext.declarative import declarative_base
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
    isChecked = Column(Boolean, nullable=False)
