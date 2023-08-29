from mysqlbuilder.Builder import Builder

_db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'migration_04_04',
}
obj = Builder(_db_config)
result = obj.table('states s').select('*').limit(10).get().execute()
print(result)