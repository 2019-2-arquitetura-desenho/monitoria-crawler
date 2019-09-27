# O código desenvolvido foi baseado na aplicação MWScanner,
# disponível abertamente no GitHub. Adaptou-se o código e 
# desenvolveu-se as necessidades do nosso projeto tendo
# como base o projeto citado.

class Discipline:
    # This class represents a Discipline present on
    # matriculaweb. it contains data about the discipline
    # and holds its classes

    def __init__(self,):

        # name of the discipline
        self.__name = ""

        # identificator code for the discipline
        # (it's unique among disciplines)
        self.__code = ""

        # department to which this discipline belongs
        self.__department = ""

        # aumount of credits that this discipline
        # is worth
        self.__credits = None

        # list with the Classes objects for this discipline
        self.__classes = []

    def getName(self):
        return self.__name

    def setName(self, name):
        if isinstance(name, type(self.__name)):
            self.__name = name

    def getCode(self):
        return self.__code

    def setCode(self, code):
        if isinstance(code, type(self.__code)):
            self.__code = code

    def setDepartment(self, department):
        if isinstance(department, type(self.__department)):
            self.__department = department

    def getCredits(self):
        return self.__credits

    def setCredits(self, credit):
        self.__credits = credit

    def getClasses(self):
        return self.__classes

    def setClasses(self, classes):
        if isinstance(classes, list):
            self.__classes = classes
