from flask import Flask, request, abort

def hello(request):
    request_json = request.get_json(silent=True)
    
    return "Hello "+request_json['name']+"!"

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/hello', methods=['POST'])
    def index():
      return hello(request)

    app.run('127.0.0.1', 8000, debug=True)