# O código desenvolvido foi baseado na aplicação MWScanner,
# disponível abertamente no GitHub. Adaptou-se o código e 
# desenvolveu-se as necessidades do nosso projeto tendo
# como base o projeto citado.

from bs4 import BeautifulSoup

from offer_crawler import BASE_URL
from offer_crawler.Mixins import TableReaderMixin, UrlLoaderMixin
from offer_crawler.Department import Department
from offer_crawler.builders.DisciplinesBuilder import DisciplinesBuilder
from multiprocessing.dummy import Pool as ThreadPool


class DepartmentBuilder(TableReaderMixin, UrlLoaderMixin):

    def getDisciplineListURL(self, code):
        # This method take the url of the
        # disciplines from the department code
        return BASE_URL + 'graduacao/oferta_dis.aspx?cod={}'.format(code)

    def buildFromHtml(self, code, name):
        # This method builds the list of disciplines that belongs
        # to this department. This list will be later used to
        # process the creation of the Discipline object.

        response = self.getFromUrl(self.getDisciplineListURL(code))

        if response.status_code != 200:
            return

        # Make the parse for html
        raw_html = BeautifulSoup(response.content, 'html.parser')
        table_data = self.readDatatableTableFromHTML(raw_html)

        # in table there are 3 types of data:
        # 'Código': the code of a discipline that belongs to the
        #           current department
        # 'Denominação': name of the discipline
        # 'Ementa': garbage (it was a icon with a link on
        #           the table, but those information where
        #           ignored when scrapping)

        # the table_data can be empty

        disciplines = []

        if table_data is not None:

            def createCourses(data):

                discipline = DisciplinesBuilder().buildDiscipline(
                    data['Código'], data['Denominação'], code)

                disciplines.append(
                    discipline
                )

                return discipline

            pool = ThreadPool(16)
            c = pool.map(createCourses, table_data)
            pool.close()
            pool.join()

        print("[Department {}] Finished".format(name))
        return disciplines

    def buildDepartment(self, code, name):

        disciplines = self.buildFromHtml(code, name)

        department = Department()
        department.setDisciplines(disciplines)

        return department
