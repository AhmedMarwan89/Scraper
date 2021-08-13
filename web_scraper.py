'''
web scraper project 
It's idea is :
if you are intersted in the news form the website ( Hacker News) . but you only want the important news to appear to you . news with more than100 votes. 
in this project only important news will apear to you 
and it will list from the most important to less important , a title with votes and with it's url will apear to you
'''


import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/') # take the html of the first page 
res2 = requests.get('https://news.ycombinator.com/news?p=2')#of the second

soup = BeautifulSoup(res.text , 'html.parser')
soup2 = BeautifulSoup(res2.text , 'html.parser') # make them soup


elements = soup.select('.storylink')#list of the news ( it needs a little of modify)
subtext = soup.select('.subtext') # list of points ( it needs a little of modify)

elements2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_elements = elements + elements2
mega_subtext = subtext + subtext2

def sort_the_list(hnlist) : 
    return sorted(hnlist , key=lambda k :k['points' ] , reverse=True)



def custom (elements , subtext) :
    hn = []
    for idx , itm in enumerate(elements ) :
        link = itm.get('href', None ) # take the link (url)
        title = itm.getText() # take the name of news
        vote = subtext[idx].select('.score')
        if len(vote) :
            points = int(vote[0].getText().replace(' points' , ''))
            pass
        if points >99 :
            hn.append({'title':title , 'link' :link , 'points' :points         })
    return sort_the_list(hn)
pprint.pprint(custom(mega_elements, mega_subtext) )