import os
import csv

class CarBase:

    def __init__(self, brand, photo_file_name, carrying):

        if len(brand) == 0 or len(photo_file_name) == 0 or len(carrying) == 0 :
            raise ValueError

        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

        self.ext = self.set_photo_file_ext()

    def set_photo_file_ext(self) : 
        path_splitted = os.path.splitext(self.photo_file_name)
        ext_list = [".jpeg", ".png", ".jpg", ".gif"]
        if path_splitted[1] not in ext_list : 
            raise ValueError
        else :
            return path_splitted[1]

    def get_photo_file_ext(self) :
        return self.ext

class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)

        try : 
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError: 
            raise

        self.car_type = "car"


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        sizes_list = body_whl.split(sep = "x")
        if len(sizes_list) != 3 :
            sizes_list = [0, 0, 0]
        self._set_sizes(sizes_list)

    def _set_sizes(self, sizes_list) :
        try : 
            self.body_length = float(sizes_list[0])
            self.body_width = float(sizes_list[1])
            self.body_height = float(sizes_list[2])
        except ValueError: 
            self.body_length = self.body_width = self.body_height = float(0)

    def get_body_volume(self) :
        return self.body_height * self.body_length * self.body_width



class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):

        if len(extra) == 0 :
            raise ValueError

        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):

    car_list = []
    try: 
        with open(csv_filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                try :              
                    if row[0] == "car" : 
                        item = Car(row[1], row[3], row[5], row[2])
                    elif row[0] == "truck" :
                        item = Truck(row[1], row[3], row[5], row[4])
                    elif row[0] == "spec_machine" :
                        item = SpecMachine(row[1], row[3], row[5], row[6])
                    else :
                        #print("No such type")
                        continue
                    car_list.append(item)
                except (IndexError, ValueError) as excpt :
                    #print(row)
                    pass
        return car_list
    except FileNotFoundError :
        raise

#cars = get_car_list("coursera_week3_cars.csv")
#print(len(cars))

#for car in cars:
#    print(type(car))

#print(cars[0].passenger_seats_count)
#print(cars[1].get_body_volume())
#print(cars[3].get_photo_file_ext())