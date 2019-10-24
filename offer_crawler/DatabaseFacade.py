from offer_crawler.builders.DepartmentBuilder import DepartmentBuilder
from offer_crawler.savers.JsonBuilder import JsonBuilder
from offer_crawler.savers.Saver import Saver

if __name__ == '__main__':
    department = DepartmentBuilder().buildDepartment()
    JsonBuilder(department)
    Saver()
