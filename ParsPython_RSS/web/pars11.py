import feedparser

# Укажите URL нужной RSS-ленты
#rss_url = "http://bbci.co.uk" 
#rss_url = "https://lenta.ru/rss/news" 
rss_url = 'https://aif.ru/rss/sport'

# Парсим ленту
feed = feedparser.parse(rss_url)

print(feed.entries[0].keys())

# Проверяем, успешно ли загрузились данные
if feed.status == 200:
    # Перебираем все полученные новости (записи)
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.get('published', 'Дата отсутствует')
        #descr = entry.description 
        descr = entry.get('summary', 'No Summary')
        author = entry.get('author', 'No Author')
        #descr = entry.content[0].value 
        category = entry.category

        #print(entry)        
        print(f"Заголовок: {title}")
        print(f"Ссылка: {link}")
        print(f"Дата: {published}")
        #print(f"Автор: {author}")
        print(f"Описание: {descr}")
        print(f"Категория: {category}")
        print("-" * 50)
else:
    print(f"Ошибка загрузки ленты: {feed.status}")
