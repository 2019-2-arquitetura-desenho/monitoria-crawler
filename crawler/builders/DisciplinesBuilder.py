# O código desenvolvido foi baseado na aplicação MWScanner,
# disponível abertamente no GitHub. Adaptou-se o código e 
# desenvolveu-se as necessidades do nosso projeto tendo
# como base o projeto citado.

from bs4 import BeautifulSoup

from crawler import BASE_URL
from crawler.Mixins import TableReaderMixin, UrlLoaderMixin
from crawler.builders.ClassBuilder import ClassBuilder
from crawler.classes.Discipline import Discipline


class DisciplinesBuilder(TableReaderMixin, UrlLoaderMixin):

    def getDisciplineOfferURL(self, code, department):
        # This method take the url of the
        # disciplines from the department code
        return BASE_URL + 'graduacao/oferta_dados.aspx?cod={}&dep={}'.format(
            code, department)

    def getDisciplineURL(self, code):
        # This method take the url of the
        # disciplines from the department code
        return BASE_URL + 'graduacao/disciplina.aspx?cod={}'.format(
            code)

    def getCredits(self, code, department):
        # This method get the credits from current disciplines

        response = self.getFromUrl(
            self.getDisciplineOfferURL(code, department))

        if response.status_code != 200:
            return

        # Get the pattern in html evidenced by xxx-xxx-xxx-xxx
        raw_html = BeautifulSoup(response.content, 'lxml')
        credits_th = raw_html.findAll(
            'small', text='(Teor-Prat-Ext-Est)')

        if len(credits_th) == 0:
            return

        # Get the td respected pattern from text filtered
        credits_tr = credits_th[0].parent.parent
        discipline_credits_td = credits_tr.findAll('td')
        discipline_credits = discipline_credits_td[0].text

        return discipline_credits

    def getClassesData(self, code, department, name):

        response = self.getFromUrl(
            self.getDisciplineOfferURL(code, department))

        # Verify if the status cod is ok
        if response.status_code != 200:
            return

        # Make the parse for html
        # And read the table indentify in parse html
        raw_html = BeautifulSoup(response.content, 'lxml')

        classes_tables = raw_html.find_all(
            'table',
            {
                'id': 'datatable',
            }
        )

        if len(classes_tables) <= 0:
            return

        # The first element is always a table with discipline informations
        # it can be discarded before the next step
        del classes_tables[0]

        classes_names = []

        classes = []

        for class_table in classes_tables:
            c = ClassBuilder().buildFromHtml(raw_html=class_table,
                                             discipline=code, department=department)
            classes.append(c)
            classes_names.append(c.getName())

        print('[Discipline {}] finished with classes {}'.format(
            name, classes_names))

        return classes

    def buildDiscipline(self, code, name, department):

        discipline = Discipline()
        discipline.setCredits(self.getCredits(code, department))
        discipline.setClasses(self.getClassesData(code, department, name))
        discipline.setName(name)
        discipline.setCode(code)
        discipline.setDepartment(department)

        return discipline