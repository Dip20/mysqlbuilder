## Mysql Builder

Hi! Wellcome to Mysql Builder, Using this library you can easily make your mysql query.


## Setup

place the source file in your project directory and you are ready to go.
Then you need to import the library as following:

    from mysqlbuilder import *
## Use

    obj = Builder('Your_database_name')
    obj.select('*').from('your_table_name).where({'column1' : 'condition1', 'column2' : 'condition2'}).get().execute()

## Output
    SELECT * FROM your_table_name where column1 = 'condition1' AND column2 = 'condition2';
