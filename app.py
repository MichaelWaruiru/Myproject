from flask import Flask, render_template
from faker import Faker

fake = Faker()

@app.route('/')
def index():
    names = []
    for _ in range(10):
        names.append(fake.name())
    return render_template('project.html', names=names)

if __name__ == '__main__':
    app.run()
