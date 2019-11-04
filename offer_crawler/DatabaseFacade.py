from offer_crawler.builders.DepartmentBuilder import DepartmentBuilder
from offer_crawler.savers.JsonBuilder import JsonBuilder
from offer_crawler.savers.Saver import Saver


class Facade:
    def __init__(self):
        self.department = DepartmentBuilder().buildDepartment()
        JsonBuilder(self.department)
        Saver()


if __name__ == '__main__':
    Facade()
