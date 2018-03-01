from mongoengine import Document, StringField, IntField, BooleanField

class Customer(Document):
    name = StringField()
    yob = IntField()   #gender, email, phone number, job, company, contacted
    email = StringField()
    gender = StringField() #0: female, 1: male
    phone_number = StringField()
    job = StringField()
    contacted = StringField()
