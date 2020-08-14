from scrapper.QuizmeScrapper import  QuizmeScrapper
from urllib.parse import urlparse


class UnknownQuizException(Exception):

    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    pass

def get_domain_from_url(url):
    parsed_uri = urlparse(url)
    result = '{uri.netloc}'.format(uri=parsed_uri)
    return result


def ScrapperChooser(url):
    scrappers = {'www.quizme.co.il': QuizmeScrapper}
    try:
        return scrappers[get_domain_from_url(url)](url)
    except:
        raise UnknownQuizException('could not find a scrapper for the url quiz')

