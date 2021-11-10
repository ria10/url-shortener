from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from form import UrlForm
import shortuuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6be9d9483e7cf90554cb2790ec2f204'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class UrlModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200),unique=True, nullable=False)
    url_short = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"UrlModel('{self.url}', '{self.url_short}')"


def find_url(url):
    found = UrlModel.query.filter_by(url=url).first()
    print(found)
    return found

def find_short(short):
    found = UrlModel.query.filter_by(url_short=short).first()
    print(found)
    return found

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/shorten", methods=['GET', 'POST'])
def shorten():
    form = UrlForm()
    if request.method == 'POST':
        if find_url(form.url.data):
            found_url = find_url(form.url.data).url
            found_short = find_url(form.url.data).url_short
            return render_template('result.html', url=found_url, url_short=found_short)
        else:
            short = shortuuid.uuid()[:7]
            url = UrlModel(url=form.url.data, url_short=short)
            db.session.add(url)
            db.session.commit()
            return render_template('result.html', url=url.url, url_short=short)
    else:
        return render_template('shorten.html', form=form)

@app.route("/<string:id>")
def change(id):
    url = find_short(id).url
    return redirect(url)
        

if __name__ == '__main__':
    app.run(debug=True)