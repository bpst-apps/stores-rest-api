'''
Marshmallow is a Python library for simplifying the serialization of complex datatypes, such as SQLAlchemy models. In a Flask application, Marshmallow can be used to serialize and deserialize objects to and from JSON, making it easier to pass data between the Flask backend and client. 
'''
from marshmallow import Schema, fields

# Creating plain item schema
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    
# Creating plain store schema
class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

# Creating plain tag schema
class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

# Creating item update schema
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()
    
# Creating item schema; inherit plain item schema
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

# Creating store schema; inherit plain store schema
class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)
    
# Creating tag schema; inherit plain tag schema
class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)