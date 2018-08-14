from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/echo')
def echo():
    body = request.get_json()
    return jsonify(body)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
