from flask import Flask, Blueprint
from flask_restx import Api
import os

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Sample Flask-SQLAlchemy')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.book_ns = self.book_ns()

    def book_ns(self, ):
        return self.api.namespace(name='Books', description='books related operations', path='/')

    
    def run(self, ): 
        port = int(os.environ.get('PORT', 5000))       
        self.app.run(            
            host='0.0.0.0',
            port = port,
            debug=True
        )

server = Server()