import json
import functools

def to_json (func) :
    @functools.wraps(func)
    def changed_func(*args, **kwargs) :
        data = func(*args, **kwargs)
        json_data = json.dumps(data)
        return json_data
    return changed_func