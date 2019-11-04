# O código desenvolvido foi baseado na aplicação MWScanner,
# disponível abertamente no GitHub. Adaptou-se o código e 
# desenvolveu-se as necessidades do nosso projeto tendo
# como base o projeto citado.

class Department:

    def __init__(self):
        # department attributes
        self.__campus = 4
        self.__code = "650"
        self.__name = "UNB - FACULDADE DO GAMA"
        self.__initials = "FGA"

        self.__disciplines = []

    def getDisciplines(self):
        return self.__disciplines

    def setDisciplines(self, disciplines):
        if isinstance(disciplines, type(self.__disciplines)):
            self.__disciplines = disciplines
