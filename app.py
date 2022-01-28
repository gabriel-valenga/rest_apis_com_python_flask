from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hotel_id': 1,
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420,
        'cidade': 'Curitiba'
    },
    {
        'hotel_id': 2,
        'nome': 'Bravo Hotel',
        'estrelas': 3.1,
        'diaria': 270,
        'cidade': 'Belo Horizonte'
    },
    {
        'hotel_id': 3,
        'nome': 'Charlie Hotel',
        'estrelas': 3.4,
        'diaria': 300,
        'cidade': 'Rio de Janeiro'
    },
{
        'hotel_id': 3,
        'nome': 'Delta Hotel',
        'estrelas': 4.5,
        'diaria': 500,
        'cidade': 'São Paulo'
    },
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)
