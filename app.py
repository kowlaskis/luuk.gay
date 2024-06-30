from flask import Flask, redirect, render_template
from datetime import datetime

app = Flask(__name__)

def get_current_year():
	return datetime.now().year

@app.route('/')
def home():
	current_year = datetime.now().year
	title = "Gay Profile page, @luuk.gay"
	description = "Home Menu of Gay Profile page, @luuk.gay"
	keywords = "Gay, profile, luuk.gay"
	return render_template('index.html', title=title, description=description, keywords=keywords, year=get_current_year())

if __name__ == '__main__':
	app.run()