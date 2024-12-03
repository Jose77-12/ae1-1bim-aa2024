import sqlite3

connection = sqlite3.connect('./relational-database.sqlite')

class __Relational:
    def __init__(self):
        self.__connection = self._connection()
        self.__cursor = self.__connection.cursor()

    @staticmethod
    def _connection():
        return connection

    def insert(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        self.__cursor.execute(sql, tuple(data.values()))
        self.__connection.commit()

    def select(self, table_name, columns='*', where_clause='', params=()):
        sql = f'SELECT {columns} FROM {table_name}'
        if where_clause:
            sql += f' WHERE {where_clause}'
        self.__cursor.execute(sql, params)
        return self.__cursor.fetchall()

    def update(self, table_name, data, where_clause='', params=()):
        assignments = ', '.join([f"{k}=?" for k in data.keys()])
        sql = f'UPDATE {table_name} SET {assignments}'
        if where_clause:
            sql += f' WHERE {where_clause}'
        self.__cursor.execute(sql, tuple(data.values()) + params)
        self.__connection.commit()

    def delete(self, table_name, where_clause='', params=()):
        sql = f'DELETE FROM {table_name}'
        if where_clause:
            sql += f' WHERE {where_clause}'
        self.__cursor.execute(sql, params)
        self.__connection.commit()
        
    def drop_table(self, table_name):
        sql = f'DROP TABLE IF EXISTS {table_name}'
        self.__cursor.execute(sql)
        self.__connection.commit()

class FoodStalls(__Relational):
    #Private vars
    __connection = None
    __cursor = None

    def __init__(self) -> None:
        super().__init__()
        self.__connection = self._connection()
        self.__cursor = self.__connection
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS puestos_de_comida (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ubicacion TEXT NOT NULL,
            tipo_comida TEXT NOT NULL,
            horario_apertura TEXT NOT NULL,
            horario_cierre TEXT NOT NULL
            )
        ''')
        self.__connection.commit()

    def add(self, nombre, ubicacion, tipo_comida, horario_apertura, horario_cierre):
        data = {
            'nombre': nombre,
            'ubicacion': ubicacion,
            'tipo_comida': tipo_comida,
            'horario_apertura': horario_apertura,
            'horario_cierre': horario_cierre
        }
        self.insert('puestos_de_comida', data)

    def get_all(self):
        return self.select('puestos_de_comida')

class SportsCenters(__Relational):
        
    #Private vars
    __connection = None
    __cursor = None
    
    def __init__(self) -> None:
        super().__init__()
        self.__connection = self._connection()
        self.__cursor = self.__connection
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS centros_deportivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ubicacion TEXT NOT NULL,
            tipo_deporte TEXT NOT NULL,
            horario_apertura TEXT NOT NULL,
            horario_cierre TEXT NOT NULL
            )
        ''')
        self.__connection.commit()

    def add(self, nombre, ubicacion, tipo_deporte, horario_apertura, horario_cierre):
        data = {
            'nombre': nombre,
            'ubicacion': ubicacion,
            'tipo_deporte': tipo_deporte,
            'horario_apertura': horario_apertura,
            'horario_cierre': horario_cierre
        }
        self.insert('centros_deportivos', data)

    def get_all(self):
        return self.select('centros_deportivos')

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
    
    foodStalls.drop_table('puestos_de_comida')
    sportsCenters.drop_table('centros_deportivos')
except:
    print('Error')
finally:
    print('End of script.')

exit(0)