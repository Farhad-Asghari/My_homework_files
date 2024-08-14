# Creat a class School with attributes name and students (a list of Student object). Provide methods to add and remove students. 
class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade
    
class School:
    def __init__(self,name):
        self.name = name
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        print(f"sudent {student.name} is added in {self.name} school")
        
    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"student {student_name} is deleted from {self.name} school")
                return print(f"student {student_name} is not found in {self.name} school")
school1 = School("Dough Abad")
student1 = Student("Ali", "12th")
student2 = Student("Hussain", "10th")
school1.add_student(student1)
school1.add_student(student2)
school1.remove_student("Ali")