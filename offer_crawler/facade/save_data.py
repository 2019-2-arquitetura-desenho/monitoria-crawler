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

    def build_disciplines_class(self, fk, discipline):
        for discipline_class in discipline.getClasses():
            professors = []
            for teacher in discipline_class.getTeachers():
                if self.teachers[teacher] == 0:
                    self.teachers[teacher] = Mediator.teacher_pk
                    self.build_teachers(teacher)
                    professors.append(Mediator.teacher_pk)
                    Mediator.teacher_pk += 1
                else:
                    professors.append(self.teachers[teacher])

            self.build_meetings(Mediator.discipline_class_pk, discipline_class.getMettings())
            Mediator.discipline_class_pk += 1

            DisciplineClassTransformer(discipline_class, fk, professors).template_offer(discipline_class)

    def build_teachers(self, teacher):
        ProfessorTransformer(teacher).template_offer(teacher)

    def build_meetings(self, fk, meetings):
        for meeting in meetings:
            MeetingTransformer(fk, meeting).template_offer(meeting)

a = Mediator()
