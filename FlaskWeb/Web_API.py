from flask import Flask, url_for, request,json, Response,jsonify
import logging
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.errorhandler(404)
def not_found(error=None):
    message = { 'status': 404, 'message': 'Not Found: ' + request.url, }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

# Response Json
@app.route('/GetDirectoryJson/<string:path>', methods = ['GET'])
def api_Get_Directory_Json(path):
    # data = { 'hello' : 'world', 'number' : 3 }

    file = open( "json/" + path + ".json", 'r')
    data = json.load(file)

    resp = jsonify(data)
    # js = json.dumps(data)
    # resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(debug = True)