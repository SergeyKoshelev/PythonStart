import json

def read_dict (file_name, key) : 
    with open(file_name, "a+") as f :
        if f.tell() == 0 :
            print(None)
            return None
        else : 
            f.seek(0)
            data_json = f.read()
            data = json.loads(data_json)
            print(data.get(key))
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
    elif value not in data[key] : 
        data[key].append(value)  
    print(data)
    with open(file_name, "w") as f : 
        data_json = json.dumps(data)
        f.write(data_json)

file_name = "test.data"
key = "key1"
value = "val1"
write_dict(file_name, key, value)
read_dict(file_name, key)