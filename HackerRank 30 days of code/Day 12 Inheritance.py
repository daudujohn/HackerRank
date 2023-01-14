class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = []

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grade = ''
        try:
            avg = sum(self.scores)/len(self.scores)
        except ZeroDivisionError:
            return None
        
        if avg <= 100 and avg >= 90:
            grade = 'O'
        elif avg < 90 and avg >= 80:
            grade = 'E'
        elif avg < 80 and avg >= 70:
            grade = 'A'
        elif avg < 70 and avg >= 55:
            grade = 'P'
        elif avg < 55 and avg >= 40:
            grade = 'D'
        else:
            grade = 'T'
        return grade
line = input().split()