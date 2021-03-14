import argparse
import json
import tempfile
import os

def read_dict (file_name, key) : 
    with open(file_name, "a+") as f :
        if f.tell() == 0 :
            print(None)
            return None
        else : 
            f.seek(0)
            data_json = f.read()
            data = json.loads(data_json)
            if key in data.keys() :
                print(", ".join(data.get(key)))
            else  :
                print(None)
            #print(data.get(key))
            return data
    

def write_dict (file_name, key, value) :
    data = {}
    with open(file_name, "a+") as f :
        if f.tell() != 0 :
            f.seek(0)
            data_json = f.read()
            data = json.loads(data_json)
    if key not in data.keys() : 
        data[key] = [value]
    else :  
        data[key].append(value)  
    with open(file_name, "w") as f : 
        data_json = json.dumps(data)
        f.write(data_json)

parser = argparse.ArgumentParser(description='key-value storage')
parser.add_argument('--key', type=str)
parser.add_argument('--val', type=str)
args = parser.parse_args()

file_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if args.val == None :
    read_dict(file_path, args.key)
else :
    write_dict(file_path, args.key, args.val)