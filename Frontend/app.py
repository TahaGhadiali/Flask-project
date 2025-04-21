from flask import Flask ,render_template,request,redirect
from datetime import datetime
import requests



BACKEND_URI = 'http://127.0.0.1:9000'

app = Flask(__name__)
@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A') +' '+ datetime.today().strftime('%B') + ' ' + datetime.today().strftime('%d') + ', ' + datetime.today().strftime('%Y')
    current_time = datetime.now().strftime('%H:%M:%S')
    print(day_of_week)
    return render_template('index.html',day_of_week=day_of_week,current_time=current_time)



@app.route('/todo')
def todo():
    return render_template('todo.html')


@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.form)

    try:
        response = requests.post(BACKEND_URI + '/submit', json=form_data)

        if response.ok:
            return 'Data successfully submited'
        else:
            error_message = f"Submission failed: {response.text}"
            return render_template('form.html', error=error_message, form_data=form_data)
    except requests.exceptions.RequestException as e:
        error_message = f"Connection error: {e}"
        return render_template('form.html', error=error_message, form_data=form_data)
    
    
@app.route('/get_data')
def view():
    response = requests.get(BACKEND_URI+'/view')
    
    return response.json()
    
if __name__ == '__main__':
     app.run(host='127.0.0.1',port=8000,debug=True)