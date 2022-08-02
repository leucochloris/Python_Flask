from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()

cars = {
    1: {"name": "BMW", "count in stock": 16},
    2: {"Name": "Skoda", "count in stock": 5},
    3: {"Name": "Wolksagen", "count in stock": 31}
}

class Main(Resource):
    def get(self, cars_id):
        if cars_id == 0:
            return cars
        else:
            return cars[cars_id]


api.add_resource(Main, "/api/cars/<int:cars_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
