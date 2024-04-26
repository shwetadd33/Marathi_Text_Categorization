import requests
from bs4 import BeautifulSoup
import string
import tempfile
import os

def trade_spider(max_pages):
    page_trade = 1

    paper = input('Enter the name of newspaper: ')
    cat = input('enter category of news: ')
    while page_trade <= max_pages:
        #print('inside')

        url = 'http://www.esakal.com/'
            #print(url)

#-----------------to get the main menu tab from main page of sakal newspaper-------------------

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        news_data = soup.find('div' , {'class':'col-lg-7 col-md-7 col-sm-7 col-xs-12 nopadding-right'})

        news_data_cat = news_data.find_all('a')

        #for news_cat in news_data_cat:
        links = 'http://www.esakal.com/' + '/krida'
        #print(links)
        get_single_item_data(links,286,300)
#------------------------------------------------------------------------------------------------
        page_trade += 1
        #print('outside for')


def get_single_item_data(links,start_page,max_page):

    hyperlink = links
    page = start_page
    while page <= max_page:
        hyperlink = links + '?page=' + str(page)
        print(hyperlink)
        source_code = requests.get(hyperlink)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        news_title = soup.findAll('div', {'class': 'newstitle'})
        for news_title_data in news_title:
            news_title_data_link = news_title_data.find('a')
            hyperlink = 'http://www.esakal.com/' + news_title_data_link.get('href')
            # print(hyperlink)
            get_news_heading(hyperlink)

        page += 1


'''--------------Fuction to get heading of news-------------------'''
def get_news_heading(hyperlink):
    source_code = requests.get(hyperlink)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")

    news_para = soup.find('div', {'class':'field field-name-body field-type-text-with-summary field-label-hidden'})
    news_para_data = news_para.find_all('p')

#-----------------------Reading whole news----------------------------------------
    for news_detail in news_para_data:
        words_vector = []
        semisport_vector = []
        if(news_detail.string !=None):
                s = news_detail.string

                exclude = set(string.punctuation)
                s = ''.join(ch for ch in s if ch not in exclude)
                #print(s)
                news = s.split(' ')
                #print(news)
                for data in news:
                    flag = 1
                    text = open("stopword.txt", encoding="utf8").read()
                    words_char = text.split("\n")
                    #print(words_char)
                    for each_word in words_char:
                        if(data == each_word):
                            flag = 0
                            break;
                        else:
                             flag = 1
                    if(flag == 1):
                        words_vector.append(data)
#------------------------------changes made hereeeee-------------------------------

                text = open("noun.txt", encoding="utf8").read()
                noun_vector = text.split("\n")
                # print(noun_vector)

                text = open("adjective.txt", encoding="utf8").read()
                adjective_vector = text.split("\n")

                text = open("adverb.txt", encoding="utf8").read()
                adverb_vector = text.split("\n")

                text = open("verb.txt", encoding="utf8").read()
                verb_vector = text.split("\n")

                for noun in noun_vector:
                    # print(noun)
                    for word in words_vector:
                        if word.find(noun) != -1:
                            # if str.__contains__(word, noun):
                            if len(noun) != 1:
                                semisport_vector.append(noun)
                                #print(noun)
                                break;

                for adjective in adjective_vector:
                    # print(noun)
                    for word in words_vector:
                        if word.find(adjective) != -1:
                            # if str.__contains__(word, noun):
                            if len(adjective) != 1:
                                semisport_vector.append(adjective)
                                #print(adjective)
                                break;

                for adverb in adverb_vector:
                    # print(noun)
                    for word in words_vector:
                        if word.find(adverb) != -1:
                            # if str.__contains__(word, noun):
                            if len(adverb) != 1:
                                semisport_vector.append(adverb)
                                #print(adverb)
                                break;

                for verb in verb_vector:
                    # print(noun)
                    for word in words_vector:
                        if word.find(verb) != -1:
                            # if str.__contains__(word, noun):
                            if len(verb) != 1:
                                semisport_vector.append(verb)
                                #print(verb)
                                break;

                print(semisport_vector)

                #----------------------creating new document file and storing each semisport_vector in it----------------------------------------------------------
                newfp = tempfile.NamedTemporaryFile(mode='a+',encoding="utf8",suffix='.txt',dir='G:\python projects\Crawler\Text',delete=False)
                print(newfp.name)
                for text_word in semisport_vector:
                    newfp.write(text_word + ' ')

                newfp.close()
        else:
            continue

                #-----------------------------end of creating text documents----------------------------------------------------------------------------------------

trade_spider(1)
#os.system('tfidf.py')