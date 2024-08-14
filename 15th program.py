# Creat a class Student with private attributes name, grade and age. Provide methods to get and set these attributes and a method to dispaly student's deatils.
class Student:
    def __init__(self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
        
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, new_grade):
        self.__grade = new_grade
        
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        self.__age = new_age
    
    def display_detail(self):
        print("name :",self.__name )
        print("grade :", self.__grade)
        print("age :", self.__age)
        
student1 = Student("Ahamd", "12th", 18)
student1.display_detail()



        
        