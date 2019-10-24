import collections
from offer_crawler.transformers.transformer import JsonTransformer


class DisciplineClassTransformer(JsonTransformer):
    pk = 1
    disciplines_class = []

    def __init__(self, discipline_class, fk, teachers):
        self.map_discipline_class = collections.defaultdict(dict)
        self.fk = fk
        self.teachers = teachers
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
        self.map_discipline_class["fields"]["discipline"] = self.fk
        self.map_discipline_class["fields"]["teachers"] = self.teachers

        DisciplineClassTransformer.disciplines_class.append(self.map_discipline_class)
