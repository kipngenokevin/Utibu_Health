#!/usr/bin/python3
"""
This is a class for the medicine items that
will be passed and retrived from storage
"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Text, INTEGER
import models


class Medicine(BaseModel, Base):
    """
    This class defines medicine items with various attributes
    """
    __tablename__ = 'Medicine_Records'

    item_name = Column(String(255), nullable=False)
    item_description = Column(Text)
    item_category = Column(String(100))
    item_count = Column(INTEGER)
