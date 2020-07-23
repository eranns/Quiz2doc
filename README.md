# Quiz2doc

Creating document of questions and answers out of quizme website quizes for studying purposes 

## Getting Started
Executing is done by running `run.py` with the following arguments : 

* `--url` - the url of the quiz from quizme website . i.e https://www.quizme.co.il/quiz-discussion/2010
* `--highlight` - define if you would like to highlight the answers in your document
* `--out` - output location of the document from the program

### Prerequisites

* Python 3.7
* Python-docx 0.8.10 
* BeautifulSoup4 4.9.1



### Examples

Quiz taken - 

![alt text](https://github.com/eranns/QuizScrapper/blob/master/showcase/quizme_page.png "quiz input")


Output - 

![alt text](https://github.com/eranns/QuizScrapper/blob/master/showcase/output_example.png "Document output")



## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used for web scrapping
* [Python-docx](https://python-docx.readthedocs.io/en/latest/) - Creating dox files within python
* [argParse](https://docs.python.org/3/library/argparse.html) - Used to parse incoming arguments

