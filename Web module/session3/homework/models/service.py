from mongoengine import Document, StringField, IntField, BooleanField, ListField


class Service(Document):
    name = StringField()
    yob = IntField()
    gender = StringField()  #0: female, 1:male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = StringField()
    description = StringField()
    measurements = ListField()
