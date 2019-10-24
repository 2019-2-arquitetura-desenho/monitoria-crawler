import json
import collections
from offer_crawler.transformers.transformer import JsonTransformer


class DisciplineTransformer(JsonTransformer):
    pk = 1
    disciplines = []

    def __init__(self, discipline):
        self.map_discipline = collections.defaultdict(dict)
        self.discipline = discipline

    def define_model(self) -> None:
        self.map_discipline["model"] = "offers.discipline"

    def define_pk(self) -> None:
        self.map_discipline["pk"] = DisciplineTransformer.pk
        DisciplineTransformer.pk += 1

    def define_fields(self, discipline) -> None:
        self.map_discipline["fields"]["name"] = self.discipline.getName()
        self.map_discipline["fields"]["code"] = self.discipline.getCode()
        self.map_discipline["fields"]["department"] = 650
        self.map_discipline["fields"]["credits"] = self.discipline.getCredits()

        DisciplineTransformer.disciplines.append(self.map_discipline)

    def write_json(self):
        with open('offers/fixtures/discipline.json', 'w', encoding='utf8') as f:
            json.dump(DisciplineTransformer.disciplines, f, indent=4, ensure_ascii=False)
