import mysql.connector
import logging
import datetime


class Builder:
    _db_name = ''
    _select = ''
    _from = ''
    _where = ''
    _orWhere = ''
    _limit = ''
    _orderBy = ''
    _groupBy = ''
    _join = ''
    _join_method = ''
    __get = ''
    _raw_sql = ''

    _current_date = datetime.date.today()
    _log_file_name = f"logs/log_{_current_date}.log"

    def __init__(self, db_name=''):
        logging.basicConfig(filename=self._log_file_name, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='a')

        if db_name == '':
            logging.error("Database Name not set in object init")
            raise Exception("Database Name not set in object init")
        else:
            self._db_name = db_name

    def select(self, _select='*'):
        self._select = f"SELECT {_select}"
        return self

    def table(self, _from=''):
        if _from == '':
            logging.critical('Table name not set in query')
            raise Exception("Table name not set in query")

        self._from = f" FROM {_from}"
        return self

    def where(self, params=dict):
        where = []
        if not type(params) == dict:
            logging.critical('Invalid type passed in where, Required to pass dict')
            raise Exception("Invalid type passed in where, Required to pass dict")
        else:
            for key, value in params.items():
                if type(value) == int:
                    ex = f"{key} = {value}"
                else:
                    ex = f"{key} = '{value}'"

                where.append(ex)

        separator = ' AND '

        if self._where == '':
            self._where = f" WHERE {separator.join(where)}"
        else:
            self._where += f" AND {separator.join(where)}"

        return self

    def orWhere(self, params=dict):
        where = []
        if not type(params) == dict:
            logging.critical('invalid type passed in orWhere, Required to pass dict')
            raise Exception("invalid type passed in orWhere, Required to pass dict")
        else:
            for key, value in params.items():

                if type(value) == int:
                    ex = f"{key} = {value}"
                else:
                    ex = f"{key} = '{value}'"

                where.append(ex)

        separator = ' OR '

        if self._orWhere == '':
            self._orWhere = f" OR {separator.join(where)}"
        else:
            self._orWhere += f" OR {separator.join(where)}"

        return self

    def limit(self, limit=1, offset=0):
        if offset == 0:
            self._limit = f" LIMIT {limit}"
        else:
            self._limit = f" LIMIT 1, {offset}"
        return self

    def orderBy(self, key, ordering='ASC'):
        if key == '':
            logging.critical('Order By required column name')
            raise Exception("Order By required column name")

        self._orderBy = f" ORDER BY {key} {ordering}"

        return self

    def groupBy(self, ordering):
        if ordering == '':
            logging.critical('Group By Column name Required')
            raise Exception("Group By Column name Required")

        self._groupBy = f" GROUP BY {ordering}"
        return self

    def join(self, table, condition, type=''):
        if table == '':
            logging.critical('Invalid parameter passed in join statement, expected required 2, optional 1')
            raise Exception("Invalid parameter passed in join statement, expected required 2, optional 1")

        if condition == '':
            logging.critical('Invalid parameter passed in join statement, expected required 2, optional 1')
            raise Exception("Invalid parameter passed in join statement, expected required 2, optional 1")

        if type == '':
            self._join_method = ' INNER '
        else:
            self._join_method = type

        if self._join == '':
            self._join = f" {self._join_method.upper()} JOIN {table} ON {condition}"
        else:
            self._join += f" {self._join_method.upper()} JOIN {table} ON {condition}"

        return self

    def raw_sql(self, sql):
        if sql == '':
            logging.critical('Please pass at least one argument in RAW_SQL')
            raise Exception("Please pass at least one argument in RAW_SQL")

        if self._where == '':
            self._where = f" WHERE {sql}"
        else:
            self._where += f" AND {sql}"
        self._raw_sql = sql

        return self

    def like(self, column, statement):
        if column == '':
            logging.critical('Invalid parameter passed in Like statement, expected required 2')
            raise Exception("Invalid parameter passed in Like statement, expected required 2")

        if statement == '':
            logging.critical('Invalid parameter passed in Like statement, expected required 2')
            raise Exception("Invalid parameter passed in Like statement, expected required 2")

        if self._where == '':
            self._where = f" WHERE {column} LIKE '%{statement}%'"
        else:
            self._where += f" AND {column} LIKE '%{statement}%'"

        return self

    def get(self):
        # select
        if self._select == '':
            self._select = "SELECT * "

        query = self._select

        # from table
        if self._from == '':
            raise Exception("Table name not set in query")
        else:
            query += self._from

        # join
        if not self._join == '':
            query += self._join

        # where
        if not self._where == '':
            query += self._where

        # Or Where
        if not self._orWhere == '':
            query += self._orWhere

        #   Group By
        if not self._groupBy == '':
            query += self._groupBy

        #   Order By
        if not self._orderBy == '':
            query += self._orderBy

        # Limit
        if not self._limit == '':
            query += self._limit

        self.__get = query
        return self

    def execute(self):
        if not self.__get == '':
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database=f'{self._db_name}',
                )

                if not conn:
                    raise Exception("Could not connect to database")
                else:
                    mycursor = conn.cursor(dictionary=True)
                    x = mycursor.execute(f"{self.__get}")
                    mysql_result = mycursor.fetchall()
                    return mysql_result
                

            except Exception as e:
                logging.critical(f'Major Exception: {e}')
                raise Exception(e)

    def compiled_query(self):
        return self.__get

    # Deleting (Calling destructor)
    # def __del__(self):
    #     print('Destructor called')
