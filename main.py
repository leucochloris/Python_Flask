from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

cars = {
    1: {"name": "BMW", "count_in_stock": 16},
    2: {"name": "Skoda", "count_in_stock": 5},
    3: {"name": "Wolksagen", "count_in_stock": 31}
}


class Main(Resource):
    def get(self, cars_id):
        if cars_id == 0:
            return cars
        else:
            return cars[cars_id]

    def delete(self, cars_id):
        del cars[cars_id]
        return cars

    def post(self, cars_id):
        pars = reqparse.RequestParser()

        pars.add_argument('name', type=str, location='form')
        pars.add_argument('count_in_stock', type=int, location='form')

        cars[cars_id] = pars.parse_args()
        return cars

    def put(self, cars_id):
        pars = reqparse.RequestParser()

        pars.add_argument('name', type=str, location='form')
        pars.add_argument('count_in_stock', type=int, location='form')

        cars[cars_id] = pars.parse_args()
        return cars


api.add_resource(Main, "/api/cars/<int:cars_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
