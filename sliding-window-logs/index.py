from flask import Flask
from middlewares.limiter import limiter
from dotenv import load_dotenv
from connections.redis_connection import redis_connection

load_dotenv('.env')

app = Flask(__name__)

@app.route('/')
@limiter
def index():
    return 'Hello world!'

app.run(host='0.0.0.0', port=5660, debug=True)