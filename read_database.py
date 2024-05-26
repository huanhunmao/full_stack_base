# 导入所需的模块
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# 创建数据库引擎
engine = create_engine('sqlite:///restaurantmenu.db')
# 将创建好的数据库引擎绑定到Base.metadata上，这样后续创建的session就可以直接访问这个数据库
Base.metadata.bind = engine

# 创建session对象
DBSession = sessionmaker(bind=engine)
session = DBSession()

# 添加新的餐厅记录
myFirstRestaurant = Restaurant(name="Pizza Palace")
session.add(myFirstRestaurant)

# 提交更改到数据库
session.commit()

# 查询所有的餐厅记录
restaurants = session.query(Restaurant).all()
print(restaurants)

# 创建一个新的MenuItem对象
cheese_pizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
# 将新创建的对象添加到session中
session.add(cheese_pizza)
# 提交session的更改到数据库
session.commit()
# 查询所有的MenuItem对象
items = session.query(MenuItem).all()
# print(items)
# firstResult = session.query(Restaurant).first()
# print('firstResult', firstResult.name)

# for item in items:
#     print('name', item.name)

# foodOfBurgers = session.query(MenuItem).filter_by(name = 'Cheese Pizza')
# for item in foodOfBurgers:
#     print(item.id)
#     print(item.name)    # Cheese Pizza
#     print(item.price)   # $8.99

    # update 更新数据
updateBurgers = session.query(MenuItem).filter_by(id = 8).one()
updateBurgers.name = 'ppx'
updateBurgers.price = "$99"
session.add(updateBurgers)
session.commit()

foodOfBurgersUpdated = session.query(MenuItem).filter_by(id = 8).one()
print('foodOfBurgersUpdated', foodOfBurgersUpdated.name, foodOfBurgersUpdated.price) # foodOfBurgersUpdated ppx $99