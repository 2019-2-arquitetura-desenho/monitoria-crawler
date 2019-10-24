from offer_crawler.builders.DepartmentBuilder import DepartmentBuilder
from offer_crawler.transformers.discipline_transformer import DisciplineTransformer
from offer_crawler.transformers.discipline_class_transformer import DisciplineClassTransformer
from offer_crawler.transformers.professor_transformer import ProfessorTransformer
from offer_crawler.transformers.meeting_transformer import MeetingTransformer
from offer_crawler.savers.Saver import Saver
import collections


class Mediator:
    teacher_pk = 1
    discipline_class_pk = 1

    def __init__(self):
        self.department = self.build_department()
        self.teachers = collections.defaultdict(int)
        self.disciplines_json()
        self.save()

    def build_department(self):
        return DepartmentBuilder().buildDepartment()

    def disciplines_json(self):
        pk = 1
        for discipline in self.department.getDisciplines():
            DisciplineTransformer(discipline).template_offer(discipline)
            self.disciplines_class_jason(pk, discipline)
            pk += 1

    def disciplines_class_jason(self, fk, discipline):
        for discipline_class in discipline.getClasses():
            professors = []
            for teacher in discipline_class.getTeachers():
                if self.teachers[teacher] == 0:
                    self.teachers[teacher] = Mediator.teacher_pk
                    self.teachers_json(teacher)
                    professors.append(Mediator.teacher_pk)
                    Mediator.teacher_pk += 1
                else:
                    professors.append(self.teachers[teacher])

            self.meetings_json(Mediator.discipline_class_pk, discipline_class.getMettings())
            Mediator.discipline_class_pk += 1

            DisciplineClassTransformer(discipline_class, fk, professors).template_offer(discipline_class)

    def teachers_json(self, teacher):
        ProfessorTransformer(teacher).template_offer(teacher)

    def meetings_json(self, fk, meetings):
        for meeting in meetings:
            MeetingTransformer(fk, meeting).template_offer(meeting)

    def save(self):
        Saver()

a = Mediator()
