import requests
from bs4 import BeautifulSoup
import re
from random import choice as takeRandomElement
from typing import List


def __get_page_content(url) -> str:
    """
    Returns page content from url
    """
    session = requests.Session()
    session.headers.update({'User-Agent': 'fuck you'})
    return session.get(url).content.decode('ascii', errors='ignore')


def __get_page_soup(url) -> BeautifulSoup:
    """
    Returns bs4 instance of url
    """
    
    html_doc = __get_page_content(url)
    return BeautifulSoup(html_doc)
    

def get_rbc_articles(url='https://tv.rbc.ru/') -> List[str]:
    """
    Returns list of url-articles from rbc main page
    """
    
    soup = __get_page_soup(url)

    articles = soup.find_all('a', id=re.compile('id_newsfeed'))
    
    return list(map(lambda page: page['href'], 
                    filter(lambda page: 'rbc' in page['href'], 
                            articles)))


def get_meduza_articles(url="https://meduza.io/api/w5/screens/news") -> List[str]:
    """
    Returns list of url-articles from meduza API
    """
    
    content = __get_page_content(url)
    articles = re.findall('{"key":"(.*?)"', content)
    
    def contains_any(url) -> bool:
        """
        Returns true if url contains any element of allowed
        """
        allowed = ['shapito', 'cards', 'news', 'feature', 'episodes']
        return bool(sum(list(
                    map(lambda name: name in url, 
                        allowed))))

    return list(map(lambda url: "https://meduza.io/" + url, 
                    filter(contains_any, 
                           articles)))


def get_random_article(get_articles_function, url=None) -> str:
    """
    Takes any article from list of articles
    produces by get_articles function
    """

    if url is None:
        return takeRandomElement(get_articles_function())

    else:
        return takeRandomElement(get_articles_function(url))




print("RBC:", get_random_article(get_rbc_articles))
print("MEDUZA:", get_random_article(get_meduza_articles))