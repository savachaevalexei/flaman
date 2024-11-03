import os
import shutil
import sys 

# Доверенные методы, только их можно будет вызвать из командной строки
ACCESSED_METHODS = [
    "new_app",
    "rm_app",
    "run_app",
]

# Обрезаем переданные аргументы, первым всегда является путь к исполняемому файлу
args = sys.argv[1:]

if len(args) < 1:
    print("Не передано название метода. Пример: python main.py function arg1 arg2")
    exit(1)
 
def new_app(app_name):
    # Создаем базовый каталог
    os.mkdir(app_name)
    
    # Создержание файла приложения
    app_source = '''from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title="Home")
    
@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title="Страница не найдена")
    
if __name__ == '__main__':
    app.run(debug=True)'''
    
    # Создержание файла базового шаблона
    app_template_base = '''<!DOCTYPE html>
<html>
<head>
    <link type="text/css" href="{{ url_for('static', filename='css/styles.css')}}" rel="stylesheet" />
    {% block title -%}
        {% if title %}
            <title>{{title}}</title>
        {% else %}
            <title>Flask_APP</title>
        {% endif %}
    {% endblock %}
</head>
<body>
    {% block content -%}
        <div class="clear"></div>
        <div class="content">
            {% if title -%}
            <h1>{{title}}</h1>
        {% else -%}
            <h1>lask_APP</h1>
        {% endif -%}
        {% endblock -%}
        </div>      
</body>
</html>'''

    # Создержание файла шаблона главной страницы
    app_template_index = '''{% extends 'base.html' %}
{% block content %}
{{ super() }}
Содержимое главной страницы
{% endblock %}'''

    # Создержание файла для несуществующей страницы
    app_template_page404 = '''{% extends 'base.html' %}
{% block content %}
{{ super() }}
Страница не найдена, вернуться на <a href="/">главную</a> страницу.
{% endblock %}'''
    
    # Создаем файл приложения
    my_file = open(f"{app_name}/{app_name}.py", "w+")
    my_file.write(app_source)
    my_file.close()
    
    # Создаем базовый каталог для статичных файлов
    os.mkdir(f"{app_name}/static")
    
    # Создаем подкаталог для css файлов
    os.mkdir(f"{app_name}/static/css")
    
    # Создаем пустой файл css
    my_file = open(f"{app_name}/static/css/styles.css", "w+")
    my_file.write(app_template_base)
    my_file.close()
    
    # Создаем подкаталог для js файлов
    os.mkdir(f"{app_name}/static/js")
    
    # Создаем каталог для шаблонов
    os.mkdir(f"{app_name}/templates")
    
    # Создаем файл базового шаблона
    my_file = open(f"{app_name}/templates/base.html", "w+")
    my_file.write(app_template_base)
    my_file.close()
    
    # Создаем html файл для главной страницы
    my_file = open(f"{app_name}/templates/index.html", "w+")
    my_file.write(app_template_index)
    my_file.close()
    
    # Создаем html файл страницы 404
    my_file = open(f"{app_name}/templates/page404.html", "w+")
    my_file.write(app_template_page404)
    my_file.close()
    
    return f"Приложение {app_name} создано"


def rm_app(app_name):
    shutil.rmtree(app_name)
    return f"Приложение {app_name} удалено"


def run_app(app_name):
    os.system(f"python3 {app_name}/{app_name}.py")
    
    


if __name__ == '__main__':
    func = args[0]
    func_args = args[1:]
    if func not in ACCESSED_METHODS:
        print(f"Метода не существует или он запрещён: {func}")
        exit(1)
    # Вызываем функцию и передаём аргументы
    result = eval(func)(*func_args)
    # Результат будет выводиться в консоль
    print(result)