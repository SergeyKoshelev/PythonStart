import os.path
import tempfile

class File :

    def __init__(self, path) :
        self.path = path
        with open(path, "a+") as f:
            pass

    def read(self) :
        with open(self.path, "r") as f:
            return f.read()

    def write(self, data) :
        with open(self.path, "w") as f:
            return f.write(data)

    def __add__(self, other) :
        #dir = tempfile.gettempdir()
        #new_path = os.path.join(dir, self.path)
        new_path = tempfile.mkstemp()[1]
        self_data = self.read()
        other_data = other.read()

        new_file = File(new_path)
        new_file.write(self_data + other_data)
        return new_file

    def __str__(self) :
        return self.path

    def __iter__(self) :
        with open(self.path, "r") as f:
            self.lines = f.readlines()
        self.current = 0
        return self

    def __next__(self) :
        if self.current >= len(self.lines) :
            raise StopIteration
            
        line = self.lines[self.current]

        self.current += 1
        return line



"""
path_to_file = 'some_filename'
#print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
file_obj.write('some text')


file_obj_1 = File(path_to_file + '_1')
file_obj_1.write('line1\nline2\nline3\n')

new_file_obj = file_obj_1 + file_obj

for line in new_file_obj :
    print(ascii(line))
"""