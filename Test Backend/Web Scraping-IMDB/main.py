import requests
import mysql.connector
from typing import List
from pyquery import PyQuery



def get_url(url, headers):
    response = requests.get(url, headers=headers)
    html = PyQuery(response.text)

    urls = []

    for a in html.find('div[class="sc-3450242-3 fLFQmt ipc-page-grid__item ipc-page-grid__item--span-2"] ul li a'):
        urls.append(PyQuery(a).attr('href'))

    return urls


def save_database(data):
    config = {
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'database': 'data_imdb'
    }

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    sql = "INSERT IGNORE INTO movie_imdb (title, rating, year, month, certificate, runtime, director, stars, genre, filming_location, budget, income, country_of_origin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, ( 
        data["Title"], data["Rating"], data["Year"], data["Month"], data["Certificate"], data["Runtime"],
        data["Director"], ", ".join(data["Stars"]), data["Genre"], data["Filming Location"], data["Budget"],
        data["Income"], data["Country of Origin"]
    ))

    conn.commit()
    conn.close()


def extract(web_url, headers):
    try:
        response = requests.get(web_url, headers=headers)
        html = PyQuery(response.text)

        results = {
            "Title": html.find('div[class="sc-69e49b85-0 jqlHBQ"] h1').text(),
            "Rating": html.find('div[class="sc-bde20123-2 cdQqzc"] span[class="sc-bde20123-1 cMEQkK"]').text().split(" ")[0],
            "Year": html.find('li[data-testid="title-details-releasedate"] div ul li a').text().split(" ")[2],
            "Month": html.find('li[data-testid="title-details-releasedate"] div ul li a').text().split(" ")[0],
            "Certificate": html.find('ul[class="ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt"] li a').text().split(" ")[1],
            "Runtime": html.find('div[class="sc-69e49b85-0 jqlHBQ"] ul li').eq(2).text(),
            "Director": html.find('li[data-testid="title-pc-principal-credit"] div ul li a').eq(0).text(),
            "Stars": [
                html.find('div[class="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid"] div div[class="sc-bfec09a1-7 gWwKlt"] a').eq(0).text(),
                html.find('div[class="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid"] div div[class="sc-bfec09a1-7 gWwKlt"] a').eq(1).text(),
                html.find('div[class="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid"] div div[class="sc-bfec09a1-7 gWwKlt"] a').eq(2).text()
            ],
            "Genre": html.find('div[class="ipc-chip-list__scroller"] a span').text(),
            "Filming Location": html.find('li[data-testid="title-details-filminglocations"] div ul li a').text(),
            "Budget": html.find('li[data-testid="title-boxoffice-budget"] div ul li span').text().split(" ")[0],
            "Income": html.find('li[data-testid="title-boxoffice-cumulativeworldwidegross"] div ul li span').text(),
            "Country of Origin": html.find('li[data-testid="title-details-origin"] div ul li a').text()
        }

        save_database(results)
    except Exception as exc:
        print(f'data tidak ada dari {web_url}: {str(exc)}')


def execute():
    base_url = 'https://m.imdb.com'
    main_url = 'https://m.imdb.com/chart/top/?ref_=nv_mv_250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
    }

    web_url = 0
    while True:
        urls = get_url(main_url, headers)
        for url in urls:
            extract(base_url+url, headers)
            web_url += 1
            if web_url == 201:
                return
        
            


execute()
