from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

pages = {}


@app.route('/<page>', methods=['GET', 'POST'])
def page_handler(page):
    if request.method == 'GET':
        if page in pages:
            return make_response(render_template('page.html', title=page, data=pages[page]), 200)
        else:
            return make_response(render_template('page.html', title=page, data=""), 200)

    if request.method == 'POST':
        data = request.json
        if not data or 'content' not in data:
            return jsonify({'error': 'Invalid data'}), 400
        pages[page] = data['content']
        return jsonify({'message': 'Page updated successfully'})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
