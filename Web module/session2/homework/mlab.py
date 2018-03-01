import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds231315.mlab.com:31315/hacanthi1234

host = "ds231315.mlab.com"
port = 31315
db_name = "hacanthi1234"
user_name = "hardihoon"
password = "hahoang2609"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
