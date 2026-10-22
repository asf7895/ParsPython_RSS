# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.db import connections, connection
import feedparser

NewsList1 = {}

def index(request):
    return HttpResponse("Hello, world!!!!")

def about(request):
    return HttpResponse("BLABLABLA")

def initdb(request):

    conn = connections['default']
    cursor = conn.cursor()

    query = """
              CREATE DATABASE IF NOT EXISTS `exmp2`;
              USE `exmp2`;
              CREATE TABLE `news` (
                 `title` varchar(255) NOT NULL,
                 `link` varchar(255) NOT NULL,
                 `category` varchar(255) NOT NULL,
                 `published` varchar(255) NOT NULL,
                 `descr` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
                 `canal` varchar(255) NOT NULL
               ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
               CREATE TABLE `canals` (
                 `id` int NOT NULL AUTO_INCREMENT,
                 `canal1` varchar(255) NOT NULL,
                 PRIMARY KEY (`id`)
               ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
               CREATE TABLE `categories` (
                 `id` int NOT NULL AUTO_INCREMENT,
                 `categ1` varchar(255) NOT NULL,
                 PRIMARY KEY (`id`)
               ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
           """

    cursor.execute(query)
    #conn.commit()
    cursor.close()
    return HttpResponse("Базы инициализированы.")

def pars11(request):

    rss11 = [
            #'https://lenta.ru/rss/news',
            'https://news.rambler.ru/rss/world',
            #'https://news.rambler.ru/rss/army',
            'https://news.rambler.ru/rss/politics',
            #'https://news.rambler.ru/rss/community',
            #'https://news.rambler.ru/rss/moscow_city',
            #'https://news.rambler.ru/rss/incidents',
            #'https://news.rambler.ru/rss/tech',
            #'https://news.rambler.ru/rss/starlife',
            #'https://news.rambler.ru/rss/articles',
            #'https://news.rambler.ru/rss/games',
            #'https://rssexport.rbc.ru/rbcnews/news/100/full.rss',
            #'https://www.kommersant.ru/RSS/news.xml',
            #'https://www.vedomosti.ru/rss/news.xml', 
            'https://aif.ru/rss/politics',
            'https://aif.ru/rss/society',
            'https://aif.ru/rss/culture',
            'https://aif.ru/rss/sport',
            #'https://aif.ru/rss/moscow',
            #'https://aif.ru/rss/techno',
            #'https://aif.ru/rss/health',
            #'https://aif.ru/rss/auto',
            #'https://aif.ru/rss/money',
            #'https://aif.ru/rss/dacha',
            #'https://aif.ru/rss/realty',
            #'https://aif.ru/rss/incidents',
            #'https://tass.ru/rss/v2.xml',
            #'https://fontanka.ru/rss-feeds/rss.xml',
            #'http://www.kp.ru/rss/allsections.xml',
            #'http://www.patriarchia.ru/rss/rss_all.rss',
            #'https://pravoslavie.ru/xml/full.xml',
            #'https://www.pravmir.ru/category/cerkov/feed',
            #'https://www.pravmir.ru/category/obshhestvo/feed',
            #'https://www.pravmir.ru/category/semya/feed',
            #'https://www.pravmir.ru/category/zdorove/feed',
            #'https://www.pravmir.ru/category/obrazovanie/feed',
            #'https://www.pravmir.ru/category/kultura/feed',
            #'https://russian.rt.com/rss',
            #'https://www.drom.ru/export/xml/news.rss',
            #'https://www.zr.ru/rss-news',
            #'https://www.gazeta.ru/export/rss/busnews.xml',
            #'https://www.gazeta.ru/export/rss/sportnews.xml',
            #'https://www.gazeta.ru/export/rss/autonews.xml',
            #'https://www.gazeta.ru/export/rss/social_more.xml',
            #'https://www.gazeta.ru/export/rss/army_news.xml',
            #'https://www.gazeta.ru/export/rss/culture_more.xml',
            #'https://www.gazeta.ru/export/rss/tech_news.xml',
            #'https://www.gazeta.ru/export/rss/science_more.xml',
            #'https://www.gazeta.ru/export/rss/lifestyle_news.xml',
            #'https://www.gazeta.ru/export/rss/politics_news.xml',
            ]

# Укажите URL нужной RSS-ленты
    #rss_url = 'https://aif.ru/rss/sport'
    for rss_url in rss11: 

# Парсим ленту
        feed = feedparser.parse(rss_url)

#print(feed.entries[0].keys())

# Проверяем, успешно ли загрузились данные
        if feed.status == 200:
    # Перебираем все полученные новости (записи)
            for entry in feed.entries:
                title = entry.title
                link = entry.link
                published = entry.get('published', 'Дата отсутствует')
        #descr = entry.description 
                descr = entry.get('summary', 'No Summary')
        #author = entry.get('author', 'No Author')
        #descr = entry.content[0].value 
                category = entry.category

                if (title.find("Путин") > 0):
                    category = "Путин"
                                         
                if (title.find("Трамп") > 0):
                    category = "Трамп"

                canal11 = link[8:]
                n14 = canal11.find("/")
                if (n14 > 0):
                    canal11 = canal11[:n14]
                                         
                query = """
                    INSERT INTO news (title, link, published, descr, category, canal)
                    SELECT %s, %s, %s, %s, %s, %s
                """
                with connection.cursor() as cursor:
        # Pass parameters as a list/tuple to prevent SQL Injection
                    cursor.execute(query, [title, link, published, descr, category, canal11]) 
            #return HttpResponse("Новости загружены.")
        else:
            print(f"Ошибка загрузки ленты: {feed.status}")
            return HttpResponse("Ошибка загрузки ленты")

    return HttpResponse("Новости загружены.")

def news1(request, page1):

    n1 = 0

    page11 = page1
    int_pg1 = int(page11)
 
    global NewsList1
    if (int_pg1 == 1):

        cursor = connections['default'].cursor()
        cursor.execute("SELECT 1 AS id, title, link, published, descr, category FROM news")
        NewsList11 = cursor.fetchall()

        #print(cursor.description)
        #print(NewsList11)         
       
        columns = [x[0] for x in cursor.description]

        NewsList1 = [
                                  dict(zip([col for col in columns], row))
                                  for row in NewsList11
                              ]

        page11 = str(1)
        n1 = 0
        n2 = 5

        cursor.close()

    else:
        n1 = 5 *  (int(page1) - 1)
        n2 = 5 *  int(page1)

        if (int_pg1 < 1):
            page11 = str(1)
            n1 = 0
            n2 = 5

        l1 = len(NewsList1)
        if (int_pg1*5 + l1 % 5 > l1):
            page11 = str(int((l1 - l1 % 5) / 5 + 1))
            n1 = 5 *  (int(page11) - 1) 
            n2 = l1

    #print(NewsList1)
    #print(l1)

    list11 = NewsList1[n1:n2]

    for row in list11:
        s1 = row['descr'].rstrip().lstrip()
        row['descr'] = s1

    template = loader.get_template("news1.html")
    context = {
            "list1": list11,
            "page1": page11,
            }

    return HttpResponse(template.render(context, request))

def del11(request):
    from django.db import connections
    query = """
                DELETE FROM news 
           """
    #conn = connection.default()   

    conn = connections['default']
    with conn.cursor() as cursor:
        # Pass parameters as a list/tuple to prevent SQL Injection
        cursor.execute(query) 
    conn.commit()
    return HttpResponse("Новости удалены.")

def categ1(request):

    cursor = connections['default'].cursor()
    if request.method == "POST":
        categ1 = request.POST.get("categ1")
        categ11 = u"{str1}".format(str1=categ1)

        cursor.execute("SELECT DISTINCT 1 AS id, title, link, published, descr, category FROM news WHERE category='" + categ11 + "'")

        NewsList11 = cursor.fetchall()

        columns = [x[0] for x in cursor.description]

        NewsList1 = [
                                  dict(zip([col for col in columns], row))
                                  for row in NewsList11
                              ]

        page11 = str(1)
        n1 = 0
        n2 = 5

        cursor.close()

        list11 = NewsList1[n1:n2]

        for row in list11:
            s1 = row['descr'].rstrip().lstrip()

            row['descr'] = s1

        template = loader.get_template("news1.html")
        context = {
            "list1": list11,
            "page1": page11,
            }

    else:
        cursor.execute("SELECT DISTINCT 1 AS id, category FROM news")
        CategList11 = cursor.fetchall()

        columns = [x[0] for x in cursor.description]

        CategList1 = [
                             dict(zip([col for col in columns], row))
                             for row in CategList11
                          ]

        cursor.close()


        template = loader.get_template("categ1.html")
        context = {
            "list1": CategList1,
            }

    return HttpResponse(template.render(context, request))

def canal1(request):

    cursor = connections['default'].cursor()
    if request.method == "POST":
        canal1 = request.POST.get("canal1")
        canal11 = u"{str1}".format(str1=canal1)

        cursor.execute("SELECT DISTINCT 1 AS id, title, link, published, descr, category, canal FROM news WHERE canal='" + canal11 + "'")

        NewsList11 = cursor.fetchall()

        columns = [x[0] for x in cursor.description]

        NewsList1 = [
                                  dict(zip([col for col in columns], row))
                                  for row in NewsList11
                              ]

        page11 = str(1)
        n1 = 0
        n2 = 5

        cursor.close()

        list11 = NewsList1[n1:n2]

        for row in list11:
            s1 = row['descr'].rstrip().lstrip()

            row['descr'] = s1

        template = loader.get_template("news1.html")
        context = {
            "list1": list11,
            "page1": page11,
            }

    else:
        cursor.execute("SELECT DISTINCT 1 AS id, canal FROM news")
        CanalList11 = cursor.fetchall()

        columns = [x[0] for x in cursor.description]

        CanalList1 = [
                             dict(zip([col for col in columns], row))
                             for row in CanalList11
                          ]

        cursor.close()


        template = loader.get_template("canal1.html")
        context = {
            "list1": CanalList1,
            }

    return HttpResponse(template.render(context, request))





