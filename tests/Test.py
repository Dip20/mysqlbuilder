from mysqlbuilder.Builder import Builder

'''
This is local Test database Config
'''
_db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'migration_04_04',
}


def basic_test():
    obj = Builder(_db_config)
    obj.table('states s').select('*').limit(10)
    result = obj.get().execute()

    obj.select('id, name').where({'id': 19})

    result = obj.get().execute()
    print(result)
    print(obj.get_last_query())


basic_test()
