#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    button_csharp = request.form.get('button_csharp')
    return render_template('index.html', button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db,
                           button_csharp=button_csharp)



@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form.get('email')
    comment = request.form.get('text')
    with open('Feedback.txt', 'a', encoding='UTF-8') as f:
        f.write(email+ '\n')
        f.write(comment + '\n')
        f.write('------------------\n')
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)