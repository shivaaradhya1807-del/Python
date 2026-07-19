class student():
    
    def _init_(self):
        self.__marks=0
    
    def set_marks(self,marks):
        self.__marks=marks
    
    def get_marks(self):
        return self.__marks
    
student=student()
student.set_marks(85)
print(student.get_marks())