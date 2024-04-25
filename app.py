from flask import Flask, render_template, request
from arithmetic import arithmetic_arranger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/arrange', methods=['POST'])
def arrange():
    problems = request.form.getlist('problem')
    show_answers = request.form.get('show_answers', False)
    arranged_problems = arithmetic_arranger(problems, show_answers)
    return arranged_problems

if __name__ == '__main__':
    app.run(debug=True)