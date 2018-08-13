import collections
import json

# helper functions
def _json_object_hook(d):
    return collections.namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

def _json_dict_hook(d):
    return dict(zip(d.keys(), *d.values()))

def json2dict(data):
    return json.loads(data, object_hook=_json_dict_hook)

def _append_json_ob(a,b):
    return collections.namedtuple('X', a.keys())(*b.values())
# end helper functions

def read_localhost_file(key):
        KEY = key + '.json'
        with open('/graphql/data/'+ KEY) as json_data:
            d = json.load(json_data)
        return d

def resolve_target(sysid):
    s = json.dumps(read_localhost_file(sysid))
    return json2obj(s)
