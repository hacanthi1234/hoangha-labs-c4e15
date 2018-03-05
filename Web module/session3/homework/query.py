import mlab
from models.service import Service

mlab.connect()

# all_services = Service.objects()
#
# first_service = all_services[0]
#
# print(first_service.name)

id_to_find = "5a955ef49e06832bc82a05d1"

service = Service.objects().with_id(id_to_find) #cach thong dung de tim id sau nay

print(service.to_mongo())

# print(kelly.to_mongo()) #show specific infomation


if service is not None:
    service.update(set__status= False)
    service.reload()   #update cai moi trong may
    print(service.to_mongo())
else:
    print('Not found')
