#Title:  Student  Management

#Create a class Student  with below attributes:
#studentId - int - student id, it is unique number
#studentName – String - studentName represents the student name 
#studentEmail - String - studentEmail represents the student email
#studentAddress – String - represents the student address which is a string  (ex:- HYD,CHN,BAN,DEL etc)

class Student:

    #Define the __init__ method to initialize the attributes in the above sequence.
    def __init__(self,sId,sName,sEmail,sAddress):
        self.studentId      = sId
        self.studentName    = sName
        self.studentEmail   = sEmail
        self.studentAddress = sAddress 

#Create a class StudentDirectory  with below attributes:
#directoryId – int - represents an uniqiue id for the StudentDirectory object
#studentList – list of type Student - studentList is a list of Students

class StudentDirectory:
    
    #Define the __init__ method to initialize the attribuutes in the above sequence.
    def __init__(self,dId,sList):
        self.directoryId = dId
        self.studentList = sList
        
    # findPatternMatchFromStudentName method:
    # This method will find the pattern match for a given student name. 
    # The match should be the student name 
    # pattern --> first character and last character must be same and might be case insensitive
    # This method should return the list of all student names which are matching with the pattern.
    # If no match pattern found on student name return empty list
    # Note:- names are case insensitive

    def findPatternMatchFromStudentName(self):
        sList = self.studentList        # Create a dictionary with key as first name + last name of student
        sFnLNameDict = {}               # list of names with matched paattern as the values 
        for student in sList:
            try:
                fChar = student.studentName[0].casefold()
                lChar = student.studentName[-1].casefold()
                key  = fChar+lChar
                sFnLNameDict[key].append(student.studentName)
            except KeyError:
               sFnLNameDict[key] = [student.studentName] 

        # Add names( values) of student if a key has atleast two students 
        sPattern = []
        for key in sFnLNameDict.keys():
            if sFnLNameDict[key] >= 2:
                sPattern.append(sFnLNameDict[key])
        return sPattern


        # getEmailCount method:

        # This method will take an input parameter -  a domain name.
        # The method will return the count of Student objects from the list of  Students 
        # belonging to the StudentDirectory whose email domain name is same as the given domain name. 
        # Here domain name is case insensitive i.e gmail.com and GMAIL.COM both are same

        # The domain name of an email is the string after the '@' character.

        # e.g. If the email address is xyz@gmail.com, the domain is gmail.com or GMAIL.COM (case insensitive)

    def getEmailCount(self,domainName):
        sList = self.studentList
        domainDict = {}

        for student in sList:
            index_at = student.studentEmail.index('@')
            domain = student.studentEmail[index_at+1:]
            try:
                domainDict[domain] += 1
            except KeyError:
                domainDict[domain] = 1 
            
        return domainDict[domainName]


#These methods should be called from the main section.
def main():


#call main
main()