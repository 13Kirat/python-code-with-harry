class Employee:
    # language = "Python" # class attribute   
    # salary = 1200000
    def __init__(self, name, salary, language): # dunder methods will call automitacally
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def great():
        print("Good morning")
        
kirat = Employee("Kirat", 1200000, "Python")
# kirat.name = "Kirat" # object/instance attribute
print(kirat.language, kirat.name)
kirat.getInfo()
