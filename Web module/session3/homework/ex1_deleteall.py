import mlab
mlab.connect()

from models.service import Service

delete_all = Service.objects()

delete_all.delete()
