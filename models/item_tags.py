# Importing required packages
from db import db

# Create item tag model class for database
class ItemTags(db.Model):
    # define database table name
    __tablename__ = "items_tags"
    
    # database table attributes
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    item_id = db.Column(
        db.Integer, 
        db.ForeignKey("items.id")
    )
    tag_id = db.Column(
        db.Integer, 
        db.ForeignKey("tags.id")
    )