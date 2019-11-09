from crawler.builders.DepartmentBuilder import DepartmentBuilder
from crawler.transformers.discipline_transformer import DisciplineTransformer
from crawler.transformers.discipline_class_transformer import DisciplineClassTransformer
from crawler.transformers.professor_transformer import ProfessorTransformer
from crawler.transformers.meeting_transformer import MeetingTransformer
from crawler.savers.Saver import Saver
import collections


class JsonBuilder:
    teacher_pk = 1
    discipline_class_pk = 1

    def __init__(self, department):
        self.department = department
        self.teachers = collections.defaultdict(int)
        self.disciplines_json()

    def disciplines_json(self):
        pk = 1
        for discipline in self.department.getDisciplines():
            DisciplineTransformer(discipline).template_offer(discipline)
            self.disciplines_class_json(pk, discipline)
            pk += 1

    def disciplines_class_json(self, fk, discipline):
        for discipline_class in discipline.getClasses():
            professors = []
            for teacher in discipline_class.getTeachers():
                if self.teachers[teacher] == 0:
                    self.teachers[teacher] = JsonBuilder.teacher_pk
                    self.teachers_json(teacher)
                    professors.append(JsonBuilder.teacher_pk)
                    JsonBuilder.teacher_pk += 1
                else:
                    professors.append(self.teachers[teacher])

            self.meetings_json(JsonBuilder.discipline_class_pk, discipline_class.getMettings())
            JsonBuilder.discipline_class_pk += 1

            DisciplineClassTransformer(discipline_class, fk, professors).template_offer(discipline_class)

    def teachers_json(self, teacher):
        ProfessorTransformer(teacher).template_offer(teacher)

    def meetings_json(self, fk, meetings):
        for meeting in meetings:
            MeetingTransformer(fk, meeting).template_offer(meeting)
