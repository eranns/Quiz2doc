from scrapper.AQuizScrapper import AQuizScrapper
from src.obj.choice import Choice
from src.obj.question import Question
import requests
from bs4 import BeautifulSoup


class QuizmeScrapper(AQuizScrapper):

    def __init__(self,url):
        self.url=url
        self.soup = self.handlesoup()
        self._quiz_title = ''
        self._questions = []

    def run(self):
        max_pages = self.find_max_pages()

        for i in range(1, max_pages + 1):
            temp_url = self.url + '?p=' + str(i)
            page = requests.get(temp_url)
            soup = BeautifulSoup(page.content, 'html.parser')
            ul = soup.find('div', {'class': 'quiz--questions'})
            children = ul.find_all('div', {"class": "Question rtl"})
            for question in children:
                self._questions.append(self.get_question(question))
            self.quiz_title = self.soup.find('h1', {"class": "Banner__heading"}).text

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, value):
        self._questions = value

    @property
    def quiz_title(self):
        return self._quiz_title

    @quiz_title.setter
    def quiz_title(self, value):
        self._quiz_title = value

    def handlesoup(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')

    def find_max_pages(self):
        max_pages = 0
        ul = self.soup.find('ul', {'class': 'pagination'})
        children = ul.findChildren("li", recursive=False, )
        for child in children:
            try:
                if int(child.text) > max_pages:
                    max_pages = int(child.text)
            except:
                continue
        return max_pages

    def get_qtitle(self,question):
        return question.find('div', {"class": "Question__title"}).find("h2").text

    def get_question(self, question):
        choices = []
        title = self.get_qtitle(question)
        question_table = question.find('div', {"class": "Media__body"})
        questions = question_table.find_all('tr', {"class": "true"})
        for tr in questions:
            try:
                if not tr.find('i', {"class": "material-icons"}).text is None:
                    choices.append(Choice(tr.find("label").text, True))
            except:
                choices.append(Choice(tr.find("label").text, False))

        return Question(title, choices)
