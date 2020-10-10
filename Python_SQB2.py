
#Title:  Student  Management

#Create a class Student with below attributes:
#studentId - String
#studentName – String 
#courseEnrolled - String
#studentScore - float

class Student:

    #Define the __init__ method to initialize the attributes in the above sequence.

    def __init__(self, sId, sName, sCourse, sScore):
        self.studentId      = sId
        self.studentName    = sName 
        self.courseEnrolled = sCourse
        self.studentScore   = sScore

#Create a class Department with below attributes:
#departmentName – String - the name of the department
#studentList – list of Student type - studentList represents the list of Students.

class Department:

    #Define the __init__ method to initialize the attribuutes in the above sequence.
    
    def __init__(self, dName, sList):
        self.departmentName = dName
        self.studentList    = sList

    # findCourseWiseStudents:
    # This method will find the count of students enrolled for each course from the studentList of the Department class 
    # and returns a dictionary having the courseEnrolled and studentCount (count of students) as key:value pair.
    
    def findCourseWiseStudents(self):
        sList = self.studentList
        
        courseDict = {}
        for student in sList:
            try:
                courseDict[student.courseEnrolled] += 1
            except KeyError:
                courseDict[student.courseEnrolled] = 1  
        
        return courseDict


    #findStudentGrade:

    #This method will take a  studentId  as parameter and return the grade of the Student with 
    #the given studentId passed as argument from the studentList in the Department class. 
    #The grade is calculated based on the studentScore as below:
    #If the studentScore >= 80 , grade should be 'A'.
    #If the studentScore<80 and >=65 , grade should be 'B'
    #If the studentScore<65 and >=55, grade should be 'C'
    #otherwise grade should be 'F'
    #If no student with given student id  found in the studentList , 
    #the method should return  None.

    def findStudentGrade(self,sId):
        sList = self.studentList
        flag  = 0                   #flag to check whether the student with the given ID 'sId' exits 

        for student in sList:
            if student.studentId == sId:
                flag = 1
                if student.studentScore >= 80:
                    return 'A'
                elif student.studentScore < 80 and student.studentScore >= 65:
                    return 'B'
                elif student.studentScore < 65 and student.studentScore >= 55:
                    return 'C'
                else:
                    return 'F'

        if flag == 0:
            return None


#These methods should be called from the main section.
def main():

    #Create 2 Departments A and B with 2 students each
    #First Create student object and then Department object

    #Department A
    student_a    = Student(1,'student_A','course_A',70)
    student_b    = Student(2,'student_B','course_A',90) 
    sList_a      = [student_a,student_b]
    department_a = Department('A',sList_a)

    #Department B
    student_c    = Student(3,'student_C','course_A',60)
    student_d    = Student(4,'student_D','course_B',90) 
    sList_b       = [student_c,student_d]
    department_b = Department('B',sList_b)

    print(department_a.findCourseWiseStudents())
    print(department_b.findCourseWiseStudents())

    print(department_a.findStudentGrade(1))
    print(department_a.findStudentGrade(2)) 
    print(department_b.findStudentGrade(3))
    print(department_b.findStudentGrade(1))    

#Call main
main()
