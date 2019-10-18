from transformer import JsonTransformer


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
        self.map_professor["fields"]["name"] = self.professor.getName()
        print(self.map_professor)
        ProfessorTransformer.professors.append(self.map_professor)
    
    def write_json(self):
        with open('offers/fixtures/professor.json', "w") as f:
            json.dump(ProfessorTransformer.professors, f, indent=4)
            