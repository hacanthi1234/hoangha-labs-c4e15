import mlab

from models.customer import Customer

from random import randint,choice

from faker import Faker

mlab.connect()

fake = Faker()

for i in range (50):
    print ('Saving customer', i +1, '.....')
    customer = Customer(name= fake.name(),       #gender, email, phone number, job, company, contacted
                        yob=randint(1990,2018),
                        gender = choice(["male","female"]),
                        email =fake.email(),
                        phone_number = fake.phone_number(),
                        job= fake.job(),
                        contacted = choice(["not_yet_contacted", "contacted" ]))

    customer.save()
