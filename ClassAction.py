from student import TheClass


class ClassMachine:

    def __init__(self, class_name, class_object):
        self.the_class = class_name
        self.class_object = class_object

    def analyse_seat(self):
        return

    def show_seat_result(self):
        self.the_class.show_seat()
        return

    ##what should fate and power action
    ##I think radom should be 20% percent and ablility should be 80%
    ## ability should be judge by grade, relationship with me, attitude to study, relationship with other students
    def set_seat(self):
        if  self.the_class.members > self.class_object.seats_number:
            return False

