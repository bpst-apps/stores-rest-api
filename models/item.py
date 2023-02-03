# Importing required packages
from db import db

# Create item model class for database
class ItemModel(db.Model):
    # define database table name
    __tablename__ = "items"
    
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
    price = db.Column(
        db.Float(precision=2), 
        unique=False, 
        nullable=False
    )
    store_id = db.Column(
        db.Integer, 
        db.ForeignKey("stores.id"), 
        unique=False, 
        nullable=False
    )
    
    # define relationship with store model
    store = db.relationship(
        "StoreModel", 
        back_populates="items"
    )