from sqlalchemy import Column, Integer, String, Float # type: ignore
from database import Base
class Destination(Base):

    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    category = Column(String)
    rating = Column(Float)
    estimated_cost = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)