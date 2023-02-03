# Importing required packages
from db import db

# Create store model class for database
class StoreModel(db.Model):
    # define database table name
    __tablename__ = "stores"
    
    # database table attributes
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    name = db.Column(
        db.String(80), 
        unique=True, 
        nullable=False
    )
    items = db.relationship(
        "ItemModel", 
        back_populates="store", 
        lazy="dynamic"
    )
    tags = db.relationship(
        "TagModel", 
        back_populates="store", 
        lazy="dynamic"
    )