from scrapper.QuizmeScrapper import  QuizmeScrapper
from urllib.parse import urlparse

def get_domain_from_url(url):
    parsed_uri = urlparse(url)
    result = '{uri.netloc}'.format(uri=parsed_uri)
    return result


def ScrapperChooser(url):
    scrappers = {'www.quizme.co.il': QuizmeScrapper}
    return scrappers[get_domain_from_url(url)](url)

