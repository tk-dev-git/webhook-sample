from flask import Flask, request, Response
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return ('<h1>Flask Webhook サンプルサーバ起動中</h1>', 200, None)


@app.route('/webhook', methods=['POST'])
def respond():
    print('[request]: ', json.dumps(request.json, indent=4));
    return Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
    