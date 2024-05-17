from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


# fk e.g. items = relationship("Item", back_populates="owner")
class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    line_id = Column(String, unique=True, index=True)
    avatar = Column(String)
    points_balance = Column(Integer)
    agreement = Column(Boolean, default=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    del_tag = Column(Boolean, default=False)


class RedeemCode(Base):
    __tablename__ = "RedeemCode"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    point = Column(Integer)
    comment = Column(String)
    count = Column(Integer)
    due_date = Column(DateTime)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    del_tag = Column(Boolean, default=False)


class GeneratedLipSyncVideo(Base):
    __tablename__ = "GeneratedLipSyncVideo"

    id = Column(Integer, primary_key=True, autoincrement=True)
