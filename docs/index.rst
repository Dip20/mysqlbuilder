result = Builder('santu').table('cities').select('id, name, state_id as state').get().compiled_query()
# result = Builder('santu').table('cities').select('id, name, state_id').get().execute()
print(result)


# print(obj.compiled_query())
# obj.where({'id': 1})
# obj.join('sales_ACparticu sa', 'sa.account = ac.id')
# obj.join('account ac', 'gl.id = ac.gl_group', 'left')
# obj.join('sales_ACinvoice si', 'si.id = sa.parent_id', 'right')
# obj.where({'gl.id': 123})
# obj.orWhere({'si.is_delete': '0', 'si.is_create': '0'})
# obj.where({'si.is_Active': '0'})
# obj.raw_sql("date => '2023-07-23' AND date <= '2023-07-23'")
# obj.raw_sql(f'(id = {213} AND username = 35)')
# obj.where({'ac.istwo': '0'})
# obj.where({'ac.isone': '0'})
# obj.limit('100')
# obj.like('name', 'santu')
# obj.get()
# print(obj.compiled_query())

# result = obj.execute()

# print(result)
# print(len(result))
# for x in result:
#     print(x)