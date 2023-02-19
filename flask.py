from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)
rait = 'рейтинг где-то в проге'

@app.route('/')
@app.route('/index')
@app.route('/button', methods=['GET', 'POST'])
def entry_page():
    if request.method == 'GET':
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <div>
                        <form class="login_form" method="post">
                            <input type="submit" class="form-control" id="submit" name="submit">
                        </form>
                    </div>
                  </body>
                </html>"""

    if request.method == 'POST':
        print(request.form['submit'])
        return rait

@app.route('/gif_download')
def image():
    return f'''<img src="{url_for('static', filename='гифка загрузки из папки статик в которой будет код и еще одна папка img, '
                                                     'в которой гифка')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')