from transformer import JsonTransformer
from offer_crawler.Class import Class
import collections
import json


class DisciplineClassTransformer(JsonTransformer):
    pk = 1
    disciplines_class = []

    def __init__(self, discipline_class):
        self.map_discipline_class = collections.defaultdict(dict)
        self.discipline_class = discipline_class

    def define_model(self) -> None:
        self.map_discipline_class["model"] = "offers.disciplineclass"

    def define_pk(self) -> None:
        self.map_discipline_class["pk"] = DisciplineClassTransformer.pk
        DisciplineClassTransformer.pk += 1

    def define_fields(self, discipline_class) -> None:
        self.map_discipline_class["fields"]["name"] = self.discipline_class.getName()
        self.map_discipline_class["fields"]["vacancies"] = self.discipline_class.getVacancies()
        self.map_discipline_class["fields"]["shift"] = self.discipline_class.getShift()
        self.map_discipline_class["fields"]["discipline"] = self.discipline_class.getDiscipline()
        self.map_discipline_class["fields"]["teachers"] = self.discipline_class.getTeachers()
        print(self.map_discipline_class)
        DisciplineClassTransformer.disciplines_class.append(self.map_discipline_class)
    
    def write_json(self):
        with open('offers/fixtures/discipline_class.json', "w") as f:
            json.dump(DisciplineClassTransformer.disciplines_class, f, indent=4)



myDis = Class()
myDis.setName('A')
myDis.setVacancies(60)
myDis.setShift('Diurno')

DisciplineClassTransformer(myDis).template_offer(myDis)