import mlab
from models.service import Service

from random import randint,choice

from faker import Faker

mlab.connect()

fake = Faker()

des = ['ngoan hiền', 'dễ thương', 'damdang', 'lễ phép với gia đình', 'hư hỏng']

for i in range (50):
    print ('Saving service', i +1, '.....')
    service = Service(name= fake.name(),
                        yob=randint(1990,2000),
                        gender = "nữ",
                        height =randint(150, 180),
                        phone = fake.phone_number(),
                        address= fake.address(),
                        status = choice([True, False ]),
                        image = choice(['https://anhdephd.com/wp-content/themes/anhdep/js/jquery.bxslider.min.js?ver=4.1.2',
                                        'https://anhdephd.com/wp-content/themes/anhdep/js/colormag-slider-setting.js?ver=4.9.3',
                                        'https://anhdephd.com/wp-content/themes/anhdep/js/navigation.js?ver=4.9.3',
                                        'https://anhdephd.com/wp-content/themes/anhdep/js/fitvids/jquery.fitvids.js?ver=20150311',
                                        'https://anhdephd.com/wp-content/themes/anhdep/js/fitvids/fitvids-setting.js?ver=20150311',
                                        'https://anhdephd.com/wp-content/themes/anhdep/js/post-format.js?ver=20150422',
                                        'https://anhdephd.com/wp-content/plugins/lazy-load/js/jquery.sonar.min.js?ver=0.6.1',
                                        'https://anhdephd.com/wp-content/plugins/lazy-load/js/lazy-load.js?ver=0.6.1',
                                        'https://anhdephd.com/wp-includes/js/wp-embed.min.js?ver=4.9.3'] ),
                        description = choice(des),
                        measurements = [90 + randint(-10,10), 60 + randint(-10,10), 90 + randint(-10,10) ])

    service.save()

# print(fake.phone_number())
