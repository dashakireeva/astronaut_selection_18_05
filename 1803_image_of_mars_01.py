# Изображение Марса
from flask import Flask
from flask import url_for

app = Flask(__name__)

a = ["Человечество вырастает из детства.", 
    "Человечеству мала одна планета.", 
    "Мы сделаем обитаемыми безжизненные пока планеты.", 
    "И начнем с Марса!", 
    "Присоединяйся!"]

@app.route('/index')
def index():
    return "Миссия Колонизация Марса"


@app.route('/countdown')
def countdown():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    global a
    return '</br>'.join(a)


@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MAPS.jpeg')}" alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красивая платена.</p>
                </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!DOCTYPE html>
                <html lang="ru">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                </head>
                <body>
                    <h1 class="active">Жди нас, Марс!</h1>
                    <img src="static/img/MAPS.jpeg" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="p-3 mb-2 bg-secondary text-white">Человечество вырастает из детства.</div>
                    <div class="p-3 mb-2 bg-success text-white">Человечеству мала одна планета.</div>                
                    <div class="p-3 mb-2 bg-secondary text-white">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="p-3 mb-2 bg-warning text-dark">И начнем с Марса!</div>
                    <div class="p-3 mb-2 bg-danger text-white">Присоединяйся!</div>  
                </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


