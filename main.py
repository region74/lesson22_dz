from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import datetime
from hh_api import get_info

app = Flask(__name__)

data_set = []


@app.route("/")
def index():
    # main_data = {
    #     'a': 'A',
    #     'b': 'B',
    #     'c': 'C'
    # }

    # context = {
    #     'name': 'Leo',
    #     'age': 35
    # }
    return render_template('index.html')
    # аналогично
    # return render_template('index.html', main_data=main_data, name='Leo', age=35)


# @app.post('/form/')
# def form_post():
#     # гдето взяли данные
#     # develop_name = 'Alex'
#     # creation_date = datetime.date.today()
#     # Контекст name=develop_name - те данные которые мы передаем из контроллера(view) в шаблон
#     # Словарь контекста
#     # context = {'name': develop_name}
#     # return render_template('contacts.html', props=context)
#     # return render_template('contacts.html', name=develop_name, date=creation_date)
#     text = request.form['text']
#     result = get_info(text)
#
#     data_set = result
#     print('Мы в дате')
#     print(data_set)
#     return render_template('form.html')


@app.route('/form/')
def form_get():
    return render_template('form.html')


@app.get('/result/')
def form_result():
    # data = data_set
    # data = ['python', 'js', 'c++', 'c#', 'java']
    # print('Я в резалте')
    # print(data_set)
    return render_template('result.html')

@app.post('/result/')
def form_post():
    text = request.form['text']
    result = get_info(text)

    return render_template('result.html', data=result)

if __name__ == "__main__":
    # debug mode нужен чтобы мониторить как работает внутри сервер
    app.run(debug=True)
