from offer_crawler.transformers.discipline_transformer import DisciplineTransformer
from offer_crawler.transformers.discipline_class_transformer import DisciplineClassTransformer
from offer_crawler.transformers.professor_transformer import ProfessorTransformer
from offer_crawler.transformers.meeting_transformer import MeetingTransformer
import json


class Saver:

    def __init__(self):
        self.save_disciplines()
        self.save_disciplines_class()
        self.save_professors()
        self.save_meetings()

    def save_disciplines(self):
        with open('offers/fixtures/discipline.json', 'w', encoding='utf8') as f:
            json.dump(DisciplineTransformer.disciplines, f, indent=4, ensure_ascii=False)

    def save_disciplines_class(self):
        with open('offers/fixtures/discipline_class.json', 'w', encoding='utf8') as f:
            json.dump(DisciplineClassTransformer.disciplines_class, f, indent=4,  ensure_ascii=False)

    def save_professors(self):
        with open('offers/fixtures/professor.json', 'w', encoding='utf8') as f:
            json.dump(ProfessorTransformer.professors, f, indent=4, ensure_ascii=False)

    def save_meetings(self):
        with open('offers/fixtures/meeting.json', 'w', encoding='utf8') as f:
            json.dump(MeetingTransformer.meetings, f, indent=4, ensure_ascii=False)
