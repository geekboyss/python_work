#from pizza import make_pizza
#
#make_pizza(16,'pepperoni')
#make_pizza(12,'mushrooms', 'gren peppers')

#8.6.3 给函数指定别名
#from pizza import make_pizza as mp
#
#mp(16,'pepperoni')
#mp(12,'mushrooms', 'gren peppers')


#8.6.4 给模块指定别名
#import pizza as p

#p.make_pizza(16, 'pepperoni')
#p.make_pizza(12, 'mushrooms', 'green peppers')


#8.6.5 导入模块中所有函数
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'gren peppers')

