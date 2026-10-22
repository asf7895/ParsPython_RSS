# Dockerfile

# Берем готовую основу: Python 3.11 на упрощенной системе Linux
FROM python:3.14-slim-bookworm
#FROM python:3.14

# Говорим Python не создавать временные файлы (.pyc) - чтобы не захламлять контейнер
ENV PYTHONDONTWRITEBYTECODE 1

# Говорим Python сразу показывать все сообщения в консоли (без задержек)
ENV PYTHONUNBUFFERED 1

# Создаем папку /app внутри контейнера и переходим в нее
# Это как создать рабочую папку на новом компьютере
WORKDIR /app

# Копируем файл с зависимостями (список что нужно установить)
COPY requirements.txt .

RUN apt-get update -y
RUN apt-get install pkg-config -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev


# Устанавливаем все нужные библиотеки из requirements.txt
# Флаг --no-cache-dir говорит не сохранять временные файлы установки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЕ файлы из нашей текущей папки в папку /app контейнера
#COPY . .
ADD . /app/

# Сообщаем что наше приложение будет работать на порту 8000
EXPOSE 8000

# Самая главная команда - что запускать когда контейнер стартует
# Запускаем Django-сервер так, чтобы он был доступен снаружи
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]