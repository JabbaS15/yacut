# YaCut - Cервис укорачивания ссылок.
[![Python](https://img.shields.io/badge/-Python_3.10-464646?style=flat&logo=Python&logoColor=ffffff&color=013220)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask_2.0.2-464646?style=flat&logo=Flask&logoColor=ffffff&color=013220)](https://flask.palletsprojects.com/)
[![Jinja2](https://img.shields.io/badge/-Jinja2_3.0.3-464646?style=flat&logo=Jinja2&logoColor=ffffff&color=013220)](https://jinja.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy_1.4.29-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=013220)](https://www.sqlalchemy.org/)

## Описание проекта:
Ключевые возможности сервиса:

- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

### Формат для ссылки по умолчанию.
Шесть случайных символов, в качестве которых можно использовать:  
- большие латинские буквы,
- маленькие латинские буквы,
- цифры в диапазоне от 0 до 9.


## Инструкция по развёртыванию:
1. Загрузите проект:
```bash
git clone https://github.com/JabbaS15/yacut.git
```
2. Установите и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
python3 -m pip install --upgrade pip
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Создать файл настроек окружения .env и заполнить его:
```bash
touch .env
```
```bash
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI='MY DATABASE'
SECRET_KEY='MY SECRET KEY'
```
5. Запустить проект.
```
flask run
```
### Автор проекта:
[Шведков Роман](https://github.com/JabbaS15)
