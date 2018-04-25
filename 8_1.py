# -*- coding:utf-8 -*-
"""
@project = 0424-1
@file = 8_1
@author = Liangjisheng
@create_time = 2018/4/24 0024 下午 19:13
"""
import pandas as pd
import numpy as np
# 层次化索引（hierarchical indexing）是pandas的一项重要功能，它使你能在一个轴上拥有多个
# （两个以上）索引级别。抽象点说，它使你能以低维度形式处理高维度数据。我们先来看一个简单的例子：
# 创建一个Series，并用一个由列表或数组组成的列表作为索引
data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
# 对于一个层次化索引的对象，可以使用所谓的部分索引，使用它选取数据子集的操作更简单：
print(data['b'])
print(data['b':'c'])
print(data.loc[['b', 'd']])
# 有时甚至还可以在“内层”中进行选取
print(data.loc[:, 2])
# 层次化索引在数据重塑和基于分组的操作（如透视表生成）中扮演着重要的角色。
# 例如，可以通过unstack方法将这段数据重新安排到一个DataFrame中
print(data.unstack())
# unstack的逆运算是stack
print(data.unstack().stack())
print()

# 对于一个DataFrame，每条轴都可以有分层索引
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
print(frame)
# 各层都可以有名字（可以是字符串，也可以是别的Python对象）。如果指定了名称，
# 它们就会显示在控制台输出中
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
# 注意：小心区分索引名state、color与行标签
print(frame['Ohio'])
print(frame.loc['a'])

# 有时，你需要重新调整某条轴上各级别的顺序，或根据指定级别上的值对数据进行排序。
# swaplevel接受两个级别编号或名称，并返回一个互换了级别的新对象（但数据不会发生变化）
print(frame.swaplevel('key1', 'key2'))
# 而sort_index则根据单个级别中的值对数据进行排序。交换级别时，常常也会用到sort_index，
# 这样最终结果就是按照指定顺序进行字母排序了
print(frame)
print(frame.sort_index(level=1))
print(frame.swaplevel(0, 1).sort_index(level=0))
# 许多对DataFrame和Series的描述和汇总统计都有一个level选项，它用于指定在某条轴上求和的级别
# 再以上面那个DataFrame为例，我们可以根据行或列上的级别来进行求和
print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))
# 这其实是利用了pandas的groupby功能
