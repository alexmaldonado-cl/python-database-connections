import config.database as database

class Model:

    def get_connection():
        return database.get_connection()

    # @staticmethod
    @classmethod
    def all(cls):
        try:
            query = "SELECT * FROM {}".format(cls.table)
            return cls.get_results(query)
        except Exception as e:
            print(e)

    @classmethod
    def select(cls, *fields):
        try:
            if not fields:
                cls.select_value = "SELECT *"
            else:
                fields_str = ', '.join(fields)
                cls.select_value = "SELECT {}".format(fields_str)
            return cls
        except Exception as e:
            print(e)


    @classmethod
    def where(cls, field, operator='=', value=None):
        try:
            cls.filter_column   = field
            cls.filter_operator = operator
            cls.filter_value    = value
            return cls
        except Exception as e:
            print(e)


    @classmethod
    def order_by(cls, field='id', order='ASC'):
        try:
            cls.order_column = field
            cls.order_value  = order
        except Exception as e:
            print(e)

    @classmethod
    def get(cls):
        try:

            query = "FROM {}".format(cls.table)

            return cls.get_results(query)
        except Exception as e:
            print(e)

    @classmethod
    def take(cls, n):
        # Método para limitar el número de registros a obtener
        # Se puede encadenar con otros métodos de la clase
        cls.limit = n
        return cls
    

    @classmethod
    def _apply_select(cls, query):
        # Método interno para aplicar el SELECT a la consulta SQL
        if hasattr(cls, 'select_value'):
            query = cls.select_value + ' ' + query
        else:
            query = 'SELECT *' + ' ' + query

        return query

    @classmethod
    def _apply_filters(cls, query):
        # Método interno para aplicar filtros a la consulta SQL

        operator = cls.filter_operator


        print(operator)

        if hasattr(cls, 'filter_column') and hasattr(cls, 'filter_value'):
            query += " WHERE {} {} {}".format(cls.filter_column, cls.filter_operator, cls.filter_value)
        return query
    
    @classmethod
    def _apply_order(cls, query):
        # Método interno para aplicar filtros a la consulta SQL
        if hasattr(cls, 'order_column'):
            column = cls.order_column
        else:
            column = 'id'

        if hasattr(cls, 'order_value'):
            position = cls.order_value
        else:
            position = 'ASC'

        query += " ORDER BY {} {}".format(column, position)

        return query

    @classmethod
    def _apply_limit(cls, query):
        # Método interno para aplicar límite a la consulta SQL
        if hasattr(cls, 'limit'):
            query += " LIMIT {}".format(cls.limit)
        return query

    @classmethod
    def _reset_filters(cls):
        # Método interno para reiniciar los filtros y límites aplicados
        if hasattr(cls, 'filter_column'):
            delattr(cls, 'filter_column')
        if hasattr(cls, 'filter_value'):
            delattr(cls, 'filter_value')
        if hasattr(cls, 'limit'):
            delattr(cls, 'limit')

    @classmethod
    def execute_query(cls, query):
        # Método para ejecutar una consulta SQL
        try:
            with Model.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    @classmethod
    def get_results(cls, query):
        # Método para obtener los resultados de una consulta
        # Reinicia los filtros y límites aplicados después de obtener los resultados
        query = cls._apply_select(query)
        query = cls._apply_filters(query)
        query = cls._apply_order(query)
        query = cls._apply_limit(query)
        cls._reset_filters()
        print(query)
        return cls.execute_query(query)