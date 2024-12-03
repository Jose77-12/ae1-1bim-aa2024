from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['local']

class __NoSQL:
    def __init__(self):
        self.__db = db

    def insert(self, collection_name, data):
        collection = self.__db[collection_name]
        collection.insert_one(data)

    def select(self, collection_name, query=None):
        collection = self.__db[collection_name]
        if query is None:
            query = {}
        return list(collection.find(query))

    def update(self, collection_name, query, data):
        collection = self.__db[collection_name]
        collection.update_one(query, {'$set': data})

    def delete(self, collection_name, query):
        collection = self.__db[collection_name]
        collection.delete_one(query)

    def drop_collection(self, collection_name):
        collection = self.__db[collection_name]
        collection.drop()

class FoodStalls(__NoSQL):
    def __init__(self):
        super().__init__()
        self.__collection = 'puestos_de_comida'

    def add(self, nombre, ubicacion, tipo_comida, horario_apertura, horario_cierre):
        data = {
            'nombre': nombre,
            'ubicacion': ubicacion,
            'tipo_comida': tipo_comida,
            'horario_apertura': horario_apertura,
            'horario_cierre': horario_cierre
        }
        self.insert(self.__collection, data)

    def get_all(self):
        return self.select(self.__collection)

class SportsCenters(__NoSQL):
    def __init__(self):
        super().__init__()
        self.__collection = 'centros_deportivos'

    def add(self, nombre, ubicacion, tipo_deporte, horario_apertura, horario_cierre):
        data = {
            'nombre': nombre,
            'ubicacion': ubicacion,
            'tipo_deporte': tipo_deporte,
            'horario_apertura': horario_apertura,
            'horario_cierre': horario_cierre
        }
        self.insert(self.__collection, data)

    def get_all(self):
        return self.select(self.__collection)

try:
    foodStalls = FoodStalls()
    sportsCenters = SportsCenters()

    foodStalls.add('Taco Stand', 'Main Street', 'Mexican', '09:00', '21:00')
    foodStalls.add('Burger Joint', '2nd Avenue', 'American', '10:00', '22:00')
    foodStalls.add('Sushi Place', '3rd Boulevard', 'Japanese', '11:00', '23:00')
    foodStalls.add('Pizza Parlor', '4th Street', 'Italian', '12:00', '00:00')
    foodStalls.add('Curry House', '5th Avenue', 'Indian', '08:00', '20:00')

    sportsCenters.add('Gym A', 'North Side', 'Fitness', '06:00', '22:00')
    sportsCenters.add('Pool B', 'East Side', 'Swimming', '07:00', '21:00')
    sportsCenters.add('Court C', 'South Side', 'Basketball', '08:00', '22:00')
    sportsCenters.add('Field D', 'West Side', 'Soccer', '09:00', '23:00')
    sportsCenters.add('Track E', 'Central Park', 'Running', '05:00', '20:00')

    print(foodStalls.get_all(), sportsCenters.get_all())
    
    foodStalls.drop_collection('puestos_de_comida')
    sportsCenters.drop_collection('centros_deportivos')
except Exception as e:
    print(f'Error: {e}')
finally:
    print('End of script.')

exit(0)