from offer_crawler.builders.DepartmentBuilder import DepartmentBuilder
from offer_crawler.transformers.discipline_transformer import DisciplineTransformer
from offer_crawler.transformers.discipline_class_transformer import DisciplineClassTransformer
from offer_crawler.transformers.professor_transformer import ProfessorTransformer
from offer_crawler.transformers.meeting_transformer import MeetingTransformer
import collections


class Mediator:
    teacher_pk = 1
    discipline_class_pk = 1

    def __init__(self):
        self.department = self.build_department()
        self.teachers = collections.defaultdict(int)
        self.build_disciplines()

    def build_department(self):
        return DepartmentBuilder().buildDepartment()

    def build_disciplines(self):
        pk = 1
        for discipline in self.department.getDisciplines():
            DisciplineTransformer(discipline).template_offer(discipline)
            self.build_disciplines_class(pk, discipline)
            pk += 1


a = Mediator()
