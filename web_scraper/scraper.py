import requests
from bs4 import BeautifulSoup

wiki_url = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(wiki_url):
    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all(
        'sup', class_='noprint Inline-Template Template-Fact')
    return len(content)


def get_citations_needed_report(wiki_url):
    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('a', {"title": "Wikipedia:Citation needed"})
    result = ""

    for p in content:

        new_p = p.parent.parent.parent
        result += new_p.text

    return result


print(get_citations_needed_count(wiki_url))
print(get_citations_needed_report(wiki_url))
