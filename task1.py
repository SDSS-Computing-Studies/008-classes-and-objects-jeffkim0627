#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    name = ""
    grade = int()
    studentnum =""
    grades =[]
    courses =[]
    

    def __init__(self,name,studentnum,grade):
        self.name = name
        self.grade = grade
        self.studentnum = studentnum
        
        

    def getCourses(self,courses):
        self.courses = courses
        
    def getGrades(self,grade1=0,grade2=0,grade3=0,grade4=0,grade5=0,grade6=0,grade7=0):
        gradelist =[]
        gradelist.insert(0,grade1)
        gradelist.insert(1,grade2)
        gradelist.insert(2,grade3)
        gradelist.insert(3,grade4)
        gradelist.insert(4,grade5)
        gradelist.insert(5,grade6)
        gradelist.insert(6,grade7)
        self.grades = gradelist

    def showCourse(self):
        a = print(self.courses)
        return a

    def showGrades(self,ind):
        stclasses = self.courses[ind]
        marks = self.grades[ind]
        response = print(self.name+" has achieved a grade of "+marks+"%"+" in "+stclasses+".")
    def __del__(self):
        print("Thank you for viewing the information of "+self.name)

    def average(self):
        a = len(self.grades)
        b=sum(self.grades)
        average=b/a
        return average
    def getHonorRoll(self):
        stgrades=self.grades
        stgrades.sort(reverse=True)
        a=len(stgrades)
        if a>= 5:
            average=(stgrades[0]+stgrades[1]+stgrades[2]+stgrades[3]+stgrades[4])/5
            if average>=86:
                return True
            else:
                return False
        else:
            print(self.name+" does not have enough courses")
            
def main():
    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])
    st1.average
    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( [71, 98, 93, 95, 68, 81, 71])