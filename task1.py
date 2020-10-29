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

    # properties should be listed first
    # You will need to create your own input parameters for all methods

    name = ""
    StuNum = ""
    grade = ""

    def __init__(self, name, StuNum, grade): 
        self.name = name
        self.StuNum = StuNum
        self.grade = grade
        print("student name: " + self.name)
        pass


    

    def commands(self):
        print("-----------------------")
        print("What do you want to get")
        print("1. Find out your average of all courses.")
        print("2. Check to see if you are on the honmor roll.")
        print("3. Show courses.")
        print("4. ")
        print("5. ")
        print("6. ")
        command = input("Choose a number[1-6]:")
        print("")
        return int(command)

    def leadingFunc(self, command):
        if command == 1:
            self.average()
        elif command == 2:
            self.getHonorRoll()
        elif command == 3:
            self.showCourses()
        elif command == 4:
            self.showGrade(int)
        elif command == 5:
            self.getCourses(list)
        elif command == 6:
            self.getGrades(list)

    def average(self):
        totSum = float(list.append(st1.getGrades))
        average = totSum/7
        print("Your average grade af all course is " + average)
        
    def getHonorRoll():
        pass

    def showCourses():
        print(st1.getCourses)

    def showGrade(int):
        print(st1.getGrades)

    def getCourses(list):
        print("")

    def getGrades(list):
        pass

    def __del__():
        pass

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( [71, 98, 93, 95, 68, 81, 71])
 
main()