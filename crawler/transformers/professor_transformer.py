from crawler.transformers.transformer import JsonTransformer
import collections

class ProfessorTransformer(JsonTransformer):
    pk = 1
    professors = []

    def __init__(self, professor):
        self.map_professor = collections.defaultdict(dict)
        self.professor = professor

    def define_model(self) -> None:
        self.map_professor["model"] = "offers.professor"

    def define_pk(self) -> None:
        self.map_professor["pk"] = ProfessorTransformer.pk
        ProfessorTransformer.pk += 1

    def define_fields(self, professor) -> None:
        self.map_professor["fields"]["name"] = self.professor

        ProfessorTransformer.professors.append(self.map_professor)
