# Importing required packages
from db import db

# Create tag model class for database
class TagModel(db.Model):
    # define database table name
    __tablename__ = "tags"
    
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
    store_id = db.Column(
        db.Integer, 
        db.ForeignKey("stores.id"), 
        nullable=False
    )
    
    # define relationship with store model
    store = db.relationship(
        "StoreModel", 
        back_populates="tags"
    )
    items = db.relationship(
        "ItemModel",
        back_populates="tags",
        secondary="items_tags"
    )