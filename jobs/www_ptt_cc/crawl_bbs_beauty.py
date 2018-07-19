import requests
import time
from bs4 import BeautifulSoup
import os
import re
import urllib.request
import json
import sys
import datetime

"""
This is a sample modified from the following tutorial
http://blog.castman.net/%E6%95%99%E5%AD%B8/2016/12/24/python-data-science-tutorial-4.html
"""

PTT_URL = 'https://www.ptt.cc'
BOARD = "beauty"
BASE_DIR = "bbs/" + BOARD

def get_web_page(url):
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html.parser')

    # 取得上一頁的連結
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []  # 儲存取得的文章資料
    divs = soup.find_all('div', 'r-ent')
    min_date = datetime.datetime.now()

    for d in divs:
        """
        <div class="r-ent">
            <div class="nrec"><span class="hl f3">33</span></div>
            <div class="title">
                <a href="/bbs/Beauty/M.1531971984.A.7E2.html">[正妹] 舞蹈班學生妹 </a>
            </div>
            <div class="meta">
                <div class="author">teramars</div>
                <div class="article-menu">
                    <div class="trigger">⋯</div>
                    <div class="dropdown">
                    <div class="item"><a href="/bbs/Beauty/search?q=thread%3A%5B%E6%AD%A3%E5%A6%B9%5D+%E8%88%9E%E8%B9%88%E7%8F%AD%E5%AD%B8%E7%94%9F%E5%A6%B9+">搜尋同標題文章</a></div>
                    <div class="item"><a href="/bbs/Beauty/search?q=author%3Ateramars">搜尋看板內 teramars 的文章</a></div>
                </div>
            </div>
            <div class="date"> 7/19</div>
            <div class="mark"></div>
        </div>
        """
        if d.find('div', 'date').string.strip() == date:  # 發文日期正確
            # 取得推文數
            push_count = 0
            if d.find('div', 'nrec').string:
                try:
                    push_count = int(d.find('div', 'nrec').string)  # 轉換字串為數字
                except ValueError:  # 若轉換失敗，不做任何事，push_count 保持為 0
                    pass

            # 取得文章連結及標題
            if d.find('a'):  # 有超連結，表示文章存在，未被刪除
                href = d.find('a')['href']
                title = d.find('a').string
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count
                })
        elif datetime.datetime.strptime(str(min_date.year)+"/"+d.find('div', 'date').string.strip(), '%Y/%m/%d') < min_date:

            # 取得文章連結及標題
            if d.find('a'):  # 有超連結，表示文章存在，未被刪除
                title = d.find('a').string
                print("title = "+ title)
                if title.startswith("[公告]"):
                    pass
                else:
                    print("before min_date="+ str(min_date))
                    min_date = datetime.datetime.strptime(str(min_date.year)+"/"+d.find('div', 'date').string.strip(), '%Y/%m/%d')
                    print("after min_date="+ str(min_date))                    
            
    return articles, prev_url, min_date


def parse(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    links = soup.find(id='main-content').find_all('a')
    img_urls = []
    for link in links:
        """
        print(link['href'])
        http://i.imgur.com/rjYBCNT.jpg
        """
        if re.match(r'^https?://(i.)?(m.)?imgur.com', link['href']):
            img_urls.append(link['href'])
        elif (link['href'].endswith(".jpg")):
            print("pre_check_link="+link['href'])
            img_urls.append(link['href'])
    return img_urls


def save(img_urls, title):
    if img_urls:
        try:
            dname = title.strip()  # 用 strip() 去除字串前後的空白
            target_dir_name = os.path.join(BASE_DIR,dname)
            os.makedirs(target_dir_name)
        except Exception as e:
            if(isinstance(e, FileExistsError)):
                print(" === Directory existed " + dname + " pass ===")
            else:
                print(e)            

        try:
            for img_url in img_urls:
                if "imgur.com" in img_url.split('//')[1]:
                    if img_url.split('//')[1].startswith('m.'):
                        img_url = img_url.replace('//m.', '//i.')
                    if not img_url.split('//')[1].startswith('i.'):
                        img_url = img_url.split('//')[0] + '//i.' + img_url.split('//')[1]
                    if not img_url.endswith('.jpg'):
                        img_url += '.jpg'
                fname = img_url.split('/')[-1]
                if not os.path.exists(os.path.join(target_dir_name, fname)):
                    urllib.request.urlretrieve(img_url, os.path.join(target_dir_name, fname))
                    print("fetched img_url="+ img_url)
                else:
                    print(" === Photo existed " + os.path.join(target_dir_name, fname) + " pass ===")
                
        except Exception as e:
            print(" === Skipping post " + dname + " ===")
            print(e)

def operator_trigger(execution_date):
    current_page = get_web_page(PTT_URL + '/bbs/'+BOARD+'/index.html')
    if current_page:
        articles = []  # 全部的文章 for execution_date
        date = execution_date.strftime("%m/%d").lstrip('0')  # execution_date 去掉開頭的 '0' 以符合 PTT 網站格式
        current_articles, prev_url, min_date = get_articles(current_page, date)  # 目前頁面的今日文章
        while current_articles or execution_date <= min_date:  # 若目前頁面有execution_date文章則加入 articles，並回到上一頁繼續尋找是否有execution_Date文章
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url, min_date = get_articles(current_page, date)

        # 已取得文章列表，開始進入各文章讀圖
        for article in articles:
            print('Processing', article)         
            page = get_web_page(PTT_URL + article['href'])
            if page:
                img_urls = parse(page)
                save(img_urls, article['title'])
                article['num_image'] = len(img_urls)

        # 儲存文章資訊
        with open('data'+execution_date.strftime("%Y-%m-%d")+'.json', 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    operator_trigger()