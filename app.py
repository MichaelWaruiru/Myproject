from flask import Flask, render_template, request
app = Flask(__name__)

from faker import Faker


@app.route('/')
def get_a_name():
    name = []
    fake = Faker()
    letter = request.args.get('letter', default='A', type=str)
    for _ in range(10):
        name = fake.first_name()
    return render_template('project.html', letter=letter, name=name)

if __name__ == '__main__':
    app.run()