##a class for every person
import datetime
import random

class Person :
    def __init__(self,name="",birthday=datetime.datetime(1970,1,1)):
        self.name = name
        self.birthday = birthday

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday

    def set_name(self,new_name):
        self.name = new_name

    def set_birthday(self,year,month,day):
        self.birthday = datetime.datetime(year,month,day)

    def get_age(self):
        return datetime.date.today().year-self.birthday.year

    def __str__(self):
        return self.name+" 's age is %d"%(self.get_age())


class Student(Person):
    def __init__(self,name,vision=0, height=0):
        Person.__init__(self,name)
        self.vision = vision
        self.height = height
        self.noise = False
        self.grade = 0
        self.last_grade={}
        self.other_Property={}
        self.story={}
        self.close_to=[]
        self.against_to=[]
        self.last_seat = []
        self.now_seat = 0
        self.prefer_seat = 0

    def get_prefer_seat(self):
        return self.prefer_seat

    def set_seat(self,new_seat):
        self.last_seat.extend(self.now_seat)
        self.now_seat = new_seat

    def get_seat(self):
        return self.now_seat

    def describe(self):
        print("my name is "+self.name)
        print("my birthday "+str(self.get_birthday()))
        print("I am %d years old and My seat is %d." % (self.get_age(), self.now_seat))

    def accurate_describe(self):
        return


class TheClass:
    def __init__(self,class_name,number):
        self.name = class_name
        self.story = {}
        self.students = {}
        self.members = 0
        self.number = number
        self.glory = {}
        self.changes = {}

    def __str__(self):
        return self.number + " 'class name is " + self.name + ". This class has " + str(self.members)+ " students"

    def add_student_all(self, student_list):
        for i in student_list:
            self.add_student(self, i)
        return

    def add_student(self, student, student_name=""):
        if not type(student) is Student:
            return False
        if student_name == "":
            self.students[student.get_name()] = student
        else:
            self.students[student_name] = student

    def remove_student(self, student_name):
        if student_name in self.students:
            return self.students.pop(student_name)
        else:
            return False

    def show_seat(self):
        return


class ClassObject():

    def __init__(self):
        self.seat_shape=""
        self.seat_judge={}
        self.seats_number = 0
        self.shape_list=[]
        self.seats_column = 0

    def auto_init(self, auto_grade = False):
        seats_number = input("how many seats in this class (*) : ")
        column = input("how many columns in this class(if you have specific plan, left this option) : ")
        shape_list_str = input("specific every row's desktop number (may overwrite last parameter) : ")
        shape_list_org=[]
        wrong_flag = 0
        if len(shape_list_str) == 0:
            shape_list_org = []
        else:
            for i in shape_list_str.split(" "):
                shape_list_org.append(int(i))
        try:
            self.seats_number = int(seats_number)
        except:
            self.seats_number = int(input("please input seat number again : "))
        try:
            self.seats_column = int(column)
        except:
            wrong_flag += 1
        self.set_seat_shape(shape_list_org)
        if len(shape_list_org) == 0 and wrong_flag == 1:
            print("you input too little parameter and this will work as 6 column")
        if auto_grade :
            self.auto_set_seat_judge()

    def set_seats_column(self,num):
        if 0< num < self.seats_number:
            self.seats_column = num
        else:
            return False

    def get_seats_column(self):
        if  self.seats_column == 0:
            return 6
        else:
            return self.seats_column

    def set_seats_column(self,num):
        self.seats_column = num

    def set_seat_shape(self, shape_list=[]):
        row = self.get_seats_column()
        if not len(shape_list) %2 == 0 :
            return False
        self.shape_list = shape_list
        if len(self.shape_list)== 0:
            strange = self.seats_number % row
            if strange == 0:
                self.shape_list=[row,self.seats_number//row]
            else:
                self.shape_list=[strange,1,row,self.seats_number//row]

    def add_seats(self, num):
        for i in range(0, num):
            self.add_seat()

    def add_seat(self):
        self.seats_number += 1
        self.seat_judge[self.seats_number] = ""

    def set_seat_judge(self, number, grade):
        self.seat_judge[number] = grade

    def init_judge(self):
        for i in self.seat_judge:
            self.seat_judge[i] = 0

    def get_column_by_row(self,row):
        before_row = 0
        for i in range(1,len(self.shape_list),2):
            if before_row < row <= (before_row + self.shape_list[i]):
                return self.shape_list[i-1]
            before_row += self.shape_list[i]
        return False

    def get_seat_score(self,num):
        best_row = 2
        basic_grade = 100
        rows = 0
        if num > self.seats_number:
            return False
        row,column = self.get_seat_row_column(num)
        for i in range(1,len(self.shape_list),2):
            rows += self.shape_list[i]
        row_diff = abs(row - best_row)
        current_column = self.get_column_by_row(row)
        if column > (current_column+1)//2:
            column = current_column+1-column
        column_diff = (current_column+1)//2-column
        ##print("row_diff %d column diff %d"%(row_diff,column_diff))
        for i in range(1,row_diff+1):
            basic_grade -= pow(i,2)
        for i in range(1,column_diff+1):
            basic_grade -= pow(i,2)
        return basic_grade-random.random()*6

    def get_seat_row_column(self,num):
        rows = 0
        begin = 0
        rows_index = 0
        row = 0
        if num > self.seats_number:
            return
        for i in range(1, len(self.shape_list), 2):
            rows += self.shape_list[i]
        ##print("there is %d rows"%(rows))
        for i in range(0,len(self.shape_list),2):
            if begin < num <=(begin+self.shape_list[i]*self.shape_list[i+1]):
                left = num - begin
                row = rows_index + left//self.shape_list[i]+1
                column = left%self.shape_list[i]
                if column == 0:
                    column = self.shape_list[i]
                    row -=1
            rows_index += self.shape_list[i+1]
            begin += self.shape_list[i]*self.shape_list[i+1]
        return [row, column]

    def auto_set_seat_judge(self):
        for i in range(1,self.seats_number+1):
            score = self.get_seat_score(i)
            self.seat_judge[i]=score

    def print_seats(self):
        num_offset = 1
        for i in range(1,len(self.shape_list),2):
            for j in range(1,self.shape_list[i]+1):
                row_str = ""
                for h in range(num_offset,num_offset+self.shape_list[i-1]):
                    row_str = row_str+str(self.seat_judge[h])+" "
                print(row_str)
                num_offset += self.shape_list[i-1]


if __name__ == "__main__":
    print("test class Student")
    a = Student("苏佳妮")
    a.set_birthday(2004, 4, 3)
    a.describe()
#    b = ClassObject()
#    b.add_seats(28)
#    b.get_seats_column()
#    b.set_seat_shape()
#    print(b.shape_list)
#    b.auto_set_seat_judge()
#    b.print_seats()
    b = ClassObject()
    b.auto_init(True)
    b.print_seats()