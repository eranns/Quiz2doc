from src.obj.choice import Choice
from src.obj.question import Question
import requests
from bs4 import BeautifulSoup

class Scrapper:

    def __init__(self,url):
        self.url=url
        self.soup=self.handlesoup()

    def handlesoup(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')

    def find_max_pages(self):
        max = 0
        ul = self.soup.find('ul', {'class': 'pagination'})
        children = ul.findChildren("li", recursive=False, )
        for child in children:
            try:
                if int(child.text) > max:
                    max = int(child.text)
            except:
                continue
        return max

    def get_qtitle(self,question):
        return question.find('div', {"class": "Question__title"}).find("h2").text

    def get_question(self,question):
        choices = []
        title = self.get_qtitle(question)
        question_table = question.find('div', {"class": "Media__body"})
        questions = question_table.find_all('tr', {"class": "true"})
        for tr in questions:
            try:
                if not tr.find('i', {"class": "material-icons"}).text == None:
                    choices.append(Choice(tr.find("label").text, True))
            except:
                choices.append(Choice(tr.find("label").text, False))

        return Question(title, choices)

    def make(self):
        max_pages = self.find_max_pages()
        q_collect = []
        for i in range(1, max_pages + 1):
            URL = self.url + '?p=' + str(i)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            ul = soup.find('div', {'class': 'quiz--questions'})
            children = ul.find_all('div', {"class": "Question rtl"})
            for question in children:
                q_collect.append(self.get_question(question))
        return q_collect , self.get_quiz_name()
    def get_quiz_name(self):
        return self.soup.find('h1', {"class": "Banner__heading"}).text



