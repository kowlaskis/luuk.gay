from flask import Flask, redirect, render_template
from datetime import datetime

app = Flask(__name__)

def get_current_year():
	return datetime.now().year

@app.route('/')
def home():
	current_year = datetime.now().year
	title = "Navigation Menu - NinetyGrooves Records"
	description = "NinetyGrooves Records. Bringing The 90s Techno Sound. Based in Utrecht"
	keywords = "techno, label, 90s, old techno, label, record label, Utrecht, Nederland, Holland, The Netherlands, Dutch, Nederlands, Nederlandse, Utrechts, Nederland"
	return render_template('index.html', title=title, description=description, keywords=keywords, year=get_current_year())

@app.route('/releases')
def releases():
	current_year = datetime.now().year
	title = "Official Releases - NinetyGrooves Records"
	description = "All Official Releases by NinetyGrooves Records."
	keywords = "techno, label, releases, label releases, 90s, old techno, label, record label, Utrecht, Nederland, Holland, The Netherlands, Dutch, Nederlands, Nederlandse, Utrechts, Nederland"
	return render_template('releases.html', title=title, description=description, keywords=keywords, year=get_current_year())

@app.route('/live')
def live():
	current_year = datetime.now().year
	title = "Watch Live Video - NinetyGrooves Records"
	description = "The Official Live Video from NinetyGrooves Records. From live video to on-demand video."
	keywords = "techno, label, releases, label releases, 90s, old techno, label, record label, Utrecht, Nederland, Holland, The Netherlands, Dutch, Nederlands, Nederlandse, Utrechts, Nederland"
	return render_template('livestream.html', title=title, description=description, keywords=keywords, year=get_current_year())

if __name__ == '__main__':
	app.run()