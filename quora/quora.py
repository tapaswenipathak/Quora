import urllib3
from bs4 import BeautifulSoup
import re
import requests

def fetch_digits(s):
    return ([int(s) for s in str.split() if s.isdigit()])

class Quora:

    @staticmethod
    def getUserStats(username):
        username = username.replace(" ","-")
        http = urllib3.PoolManager()
        username = username.replace(" ","-")
        url = "https://www.quora.com/profile/" + username
        res = http.request('GET', url).data
        soup = BeautifulSoup(res, "html.parser")
        for val in soup.find_all('spac', attrs={'class' : 'list_count'}):
            userStatVal.append(val.string)
        userStats = map(fetch_digits, userStatVal)
	dict = {
            'answers'   : userStats[1],
            'questions' : userStats[2],
            'shares'    : userStats[3],
            'spaces'    : userStats[4],
            'posts'     : userStats[5],
            'blogs'     : userStats[6],
            'followers' : userStats[7],
            'following' : userStats[8],
        }
        return(dict)

    @staticmethod
    def getQuestionStats(question):
        http = urllib3.PoolManager()
        question = question.replace(" ","-")
        url = "http://www.quora.com/" + question
        res = http.request('GET', url).data
        soup = BeautifulSoup(res, "html.parser")
        topicsParsed = soup.find_all('span', attrs={'class' : 'TopicNameSpan TopicName'})
        questionTopics = []
        for topic in topicsParsed:
            questionTopics.append(topic.string)
        soup = BeautifulSoup(res)
        followers = soup.find('div', attrs={'class': 'HighlightRow ViewsRow'}).get_text()
        asked = soup.find('div', attrs={'class': 'HighlightRow AskedRow'}).get_text()
        merged_questions = soup.find('div', attrs={'class': 'MergedQuestionsRow HighlightRow'}).get_text()
        views = soup.find('div', attrs={'class': 'ViewsRow HighlightRow'}).get_text()
        dict = {
            'followers': followers,
            'asked':  asked,
            'merged_questions': merged_questions,
            'views': views
        }
        return(dict)

    @staticmethod
    def getAnswer(question, username):
        http = urllib3.PoolManager()
        question = question.replace(" ","-")
        url = "http://www.quora.com/answer/" + username
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        data = str(soup.find_all('div', class_='ui_qtext_expanded'))
        answer_text = soup.get_text()
        dict = {
            'answer_text': answer_text,
        }
        return dict

    @staticmethod
    def getAnswerStats(question, username):
        http = urllib3.PoolManager()
        question = question.replace(" ","-")
        url = "http://www.quora.com/" + question + "/answer" + username
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        data = str(soup.find('span', class_='meta_num'))
        soup = BeautifulSoup(data)
        views = soup.get_text()
        upvotes = str(soup.find('span', attrs={'class': 'ui_button_count_optimistic_count'}))
        dict = {
            'views': views,
            'upvotes':  upvotes,
        }
        return dict

        
    @staticmethod
    def getBlogStats(blog_name):
        http = urllib3.PoolManager()
        url = "https://" + blog_name + ".quora.com/"
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        description = (str(soup.find('span', attrs={'class': 'ui_qtext_para u-ltr'})))
        followers = str(soup.find('span', attrs={'class': 'ui_button_count_static'}))
        view = str(soup.find_all('div', class_='num'))
        dict = {
            'description': description,
            'view':  view,
            'followers': followers,
        }
        return dict

    @staticmethod
    def getUserProfile(username):
        http = urllib3.PoolManager()
        username = username(" ", "-")
        url = "https://www.quora.com/profile/" + username
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        credential = (str(soup.find('span', attrs={'class': 'AnswerViewsAboutListItem AboutListItem'}))).get_text()
        top_writer = str(soup.find('span', attrs={'class': 'TopWriterAboutListItem AboutListItem'})).get_text()
        knows_about = str(soup.find_all('span', attrs={'class'='TopicNameSpan TopicName'))
        dict = {
            'credential': credential,
            'top_writer':  top_writer,
            'knows_about': knows_about,
        }
        return dict
