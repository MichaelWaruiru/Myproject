from flask import Flask, render_template
from faker import Faker

# Create the Flask app
app = Flask(__name__)


@app.route('/')
def index():
    """Render the project.html template."""
    return render_template('project.html')


@app.route('/names/<letter>')
def get_a_name(letter):
    """Generate a dummy name that starts with the given letter."""
    # Create a Faker instance
    fake = Faker()
    while True:
        # Generate a female name if the letter is a vowel, otherwise a male name
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            name = fake.first_name_female()
        else:
            name = fake.first_name_male()
        # If the name starts with the requested letter, return it
        if name.startswith(letter.upper()):
            return name

if __name__ == '__main__':
    # Run the app
    app.run()
