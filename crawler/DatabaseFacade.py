from crawler.builders.DepartmentBuilder import DepartmentBuilder
from crawler.savers.JsonBuilder import JsonBuilder
from crawler.savers.Saver import Saver


class Facade:
    def __init__(self):
        self.department = DepartmentBuilder().buildDepartment()
        JsonBuilder(self.department)
        Saver()


if __name__ == '__main__':
    Facade()
