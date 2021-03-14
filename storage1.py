import argparse
import json

def read_dict (file_name, key) : 
    with open(file_name, "a+") as f :
        if f.tell() == 0 :
            print(None)
        else : 
            f.seek(0)
            data_json = f.read()
            data = json.loads(data_json)
            print(data.get(key))
    

def write_dict (file_name, key, value) :
    data = {}
    with open(file_name, "a+") as f :
        if f.tell() != 0 :
            f.seek(0)
            data_json = f.read()
            data = json.loads(data_json)
    if key not in data.keys() : 
        data[key] = set()
    data[key].add(value)
    with open(file_name, "w") as f : 
        data_json = json.dumps(data)
        f.write(data_json)

parser = argparse.ArgumentParser(description='key-value storage')
parser.add_argument('--key', type=str)
parser.add_argument('--val', type=str)
args = parser.parse_args()

file_name = "storage.data"
if args.val == None :
    read_dict(file_name, args.key)
else :
    write_dict(file_name, args.key, args.val)