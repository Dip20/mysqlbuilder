## Mysql Builder

Hi! Wellcome to Mysql Builder, Using this library you can easily make your mysql query.
Link: <a href="https://pypi.org/project/mysqlbuilder/">Goto Package link</a>

### Installation
    pip install mysqlbuilder

### Setup
Create  **logs** folder in your project root.

    mkdir logs


import the package in your project

    from mysqlbuilder.Builder import Builder

### Example

    obj = Builder('Your_database_name')
    obj.select('*').from('your_table_name).where({'column1' : 'condition1', 'column2' : 'condition2'}).get().execute()

### Output
> SELECT * FROM your_table_name WHERE column1 = 'condition1' AND column2 = 'condition2';


## Doc
### init the Class

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'Your_database_name',
    }

    obj = Builder(db_config)

> **Note**
> You need to pass the database config in mentioned dictonary with same keyword.


### select
    obj.select('*')

You can also pass the column names as well

    obj.select('id, name, age, mobile number')

You can use alias as well
    
    obj.select('name as username')


> **Note**
> You can use all of those mysql default command in select

### table
    obj.table('your_table_name')
    
set table alias

    obj.table('your_table_name as table')

### where

    obj.where({'id': 1})

> **Note**
> You have to use the python **Dictionary** in _where_ condition


### orWhere
Basically **orWhere** as same as **Where** condition but the difference is it will place 
a **"OR"** in the condition

     obj.orWhere({'si.is_delete': '0', 'si.is_create': '0'})


### join
Basically there are three type of joining we are support right now

1. INNER JOIN
2. LEFT JOIN
3. RIGHT JOIN

#### Example of INNER JOIN <br>
You do not have to pass any additional parameter, by default we will treat join as <code>INNER JOIN</code>

    obj = Builder('Your_database_name').select('u.name as username, a.city as 
    user_city').table('users u').join('address a', 'u.address_id = a.id')

### Output

> SELECT u.name as username, a.city as user_city FROM users u INNER JOIN address a
> ON u.address_id = a.id


#### Example of LEFT JOIN 
You have to pass the <code>left</code> as keyword in the last parameter in join method

    obj = Builder('Your_database_name').select('u.name as username, a.city as 
    user_city').table('users u').join('address a', 'u.address_id = a.id', 'left')

#### Output

> SELECT u.name as username, a.city as user_city FROM users u LEFT JOIN address a
> ON u.address_id = a.id



#### Example of RIGHT JOIN
You have to pass the <code>right</code> as keyword in the last parameter in join method

    obj = Builder('Your_database_name').select('u.name as username, a.city as 
    user_city').table('users u').join('address a', 'u.address_id = a.id', 'right')

#### Output

> SELECT u.name as username, a.city as user_city FROM users u RIGHT JOIN address a
> ON u.address_id = a.id


### raw_Sql
raw sql is given to write the custom query which you want to execute but not given to this library.

    obj.table('your_table_name').select(*).raw_sql("date => '2023-07-23' AND date <= '2023-07-23'")

#### Output

> SELECT * FROM your_table_name WHERE date => '2023-07-23' AND date <= '2023-07-23'


### limit

     obj.table('your_table_name').select(*).limit('100')

### Output

> SELECT * FROM your_table_name limit 100


### limit with offset
you can use the limit offset to query the limit

     obj.table('your_table_name').select(*).limit(100,300)

#### Output

> SELECT * FROM your_table_name limit 100, 300



### Order By 

     obj.table('your_table_name').select(*).orderBy('id', 'ASC')

#### Output

> SELECT * FROM your_table_name ORDER BY id ASC



### GROUP By 

     obj.table('your_table_name').select(*).groupBy('name')

#### Output

> SELECT * FROM your_table_name GROUP BY name


### like

     obj.table('your_table_name').select(*).like('name', 'santu sarkar')

#### Output

> SELECT * FROM your_table_name where name like '%santu sarkar%'


### get
This method is used to combine all of your query params & condition and together generate the sql 

    obj.table('your_table_name').select('id, name, state_id').get()

> Note
> This comman do not produce any additional output but internally it's used to generate the sql


### execute
This method is the used to compile & execute the sql query and produce the output as an python dictionary format

    obj.table('your_table_name').select('id, name, state_id').get().execute

### compiled query
This method is used to check the query as plain text <br>
you can use this in <code>print()</code>

    print(obj.compiled_query())




