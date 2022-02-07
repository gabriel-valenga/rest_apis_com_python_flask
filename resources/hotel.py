from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help='Field nome cannot be blank')
    argumentos.add_argument('estrelas', type=float, required=True, help='Field estrelas cannot be blank')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'hotel not found.'}, 404     # not found

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel_id {hotel_id} already exists.'}, 400
        dados = self.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except Exception as e:
            return {'message': 'An internal error occurred saving hotel'}, 500
        return hotel.json()

    def put(self, hotel_id):
        dados = self.argumentos.parse_args()
        hotel_encontrado = self.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except Exception as e:
            return {'message': 'An internal error occurred saving hotel'}, 500
        return hotel.json(), 201  # created

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel(self)
                return {'message': 'Hotel deleted.'}
            except Exception as e:
                return {'message': 'An internal error occurred deleting hotel'}, 500
        return {'message': 'hotel not found'}, 404
