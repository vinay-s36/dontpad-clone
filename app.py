from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, template_folder='templates')
CORS(app)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.Text, unique=True, nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route('/<path:page>', methods=['GET', 'POST'])
def page_handler(page):
    if request.method == 'GET':
        page_data = Page.query.filter_by(page_name=page).first()
        if page_data:
            return make_response(render_template('page.html', title=page, data=page_data.content), 200)
        else:
            return make_response(render_template('page.html', title=page, data=""), 200)

    if request.method == 'POST':
        data = request.json
        if not data or 'content' not in data:
            return jsonify({'error': 'Invalid data'}), 400

        page_data = Page.query.filter_by(page_name=page).first()
        if page_data:
            page_data.content = data['content']
        else:
            page_data = Page(page_name=page, content=data['content'])
            db.session.add(page_data)

        db.session.commit()
        return jsonify({'message': 'Page updated'}), 200


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
