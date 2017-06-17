import requests 
import os
import codecs
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

algo_url = "https://www.hackerrank.com/domains/algorithms"
algo_page = "algorithms.html" 

fullusername = 'SavitaSeetaraman'
username = ''
password = '' 

response = requests.get(algo_url, auth = (username, password))

with open(algo_page, 'wb') as fd:
    for chunk in response.iter_content(chunk_size=1024):
        fd.write(chunk)

algo_file = codecs.open(algo_page, 'r', encoding = 'utf-8')
bs_algo = BeautifulSoup(algo_file, "html.parser")

for topic in bs_algo.find_all('a', attrs={'data-analytics':'PracticeChapterList'}):
    topic_name = topic.get('data-attr1')
    topic_url = algo_url + '/' + topic_name
    topic_page = topic_name + '.html'
    topic_response = requests.get(topic_url)
    with open(topic_page, 'wb') as topic_fd:
        for chunk in topic_response.iter_content(chunk_size=1024):
            topic_fd.write(chunk)
    topic_file = codecs.open(topic_page, 'r', encoding = 'utf-8')
    bs_topic = BeautifulSoup(topic_file, "html.parser") 
    print(topic_name + topic_url)
    
    for page_num in bs_topic.find_all('a', attrs={'class':'first-page-link', 'class':'page-link', 'data-analytics':'Pagination'}):
        topic_page_num = page_num.get('data-attr8')
        topic_page_url = topic_url + '/' + topic_page_num
        topic_page_name = topic_name + topic_page_num + '.html'
        response = requests.get(topic_page_url)
        with open(topic_page_name, 'wb') as topic_fd: 
            for chunk in response.iter_content(chunk_size=1024):
                topic_fd.write(chunk)
        topic_page_file = codecs.open(topic_page_name, 'r', encoding = 'utf-8') 
        bs_topic_page = BeautifulSoup(topic_page_file, "html.parser")
        print(topic_name + topic_page_name + " " + topic_page_url)

        for tag in bs_topic_page.find_all('a', attrs={'data-analytics':'ChallengeListChallengeName'}):
            data_attribute = tag.get('data-attr1')
            solution_url = str("https://www.hackerrank.com/rest/contests/master/challenges/" + data_attribute + "/hackers/" + fullusername + "/download_solution")
            solution_name = data_attribute + ".cpp"
            ua = UserAgent()
            header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}
            params = {'':'', 'render':'download'}
            response = requests.get( solution_url, headers=header, auth = (username, password), params = params, allow_redirects=False)
            print(solution_url, response.text, response.status_code)
            if (response.status_code == 200):
                with open(solution_name, 'wb') as solution_fd:
                    for chunk in response.iter_content(chunk_size=1024):
                        solution_fd.write(chunk)

#            print(solution_name)
            #os.remove(solution_name)
        os.remove(topic_page_name)
    os.remove(topic_page)
os.remove(algo_page)
