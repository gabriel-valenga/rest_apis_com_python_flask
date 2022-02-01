from flask_restful import Resource, reqparse

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


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'hotel not found.'}, 404     # not found

    def post(self, hotel_id):
        dados = self.argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id, **dados
        }

        hoteis.append(novo_hotel)

    def put(self, hotel_id):
        dados = self.argumentos.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id, **dados
        }
        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
        else:
            hoteis.append(novo_hotel)

        return novo_hotel, 201  # created

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in self.hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}