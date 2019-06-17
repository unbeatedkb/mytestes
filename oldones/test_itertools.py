# coding: utf-8


import itertools

def test_count():
    nums = itertools.count(2, 1)
    for i in nums:
        print i


def test_cycle():
    nums = itertools.cycle('jkd')
    for i in nums:
        print i

def test_repeat():
    nums = itertools.repeat('dakb', 4)
    print list(nums)
    for i in nums:
        print i

def test_chain():
    nums = itertools.chain('ab', [1, 2])
    print nums.count()
    print list(nums)
    for i in nums:
        print i

def test_product():
    # 用于求多个可迭代对象的笛卡尔积
    # product(iter1, iter2, ... iterN, [repeat=1])
    nums = itertools.product('ab', 'bc', range(3))
    for i in nums:
        print i

# test_count()  
# test_cycle()
# test_repeat()
test_chain()
# test_product()

# print zip([1, 3, 5], [2, 4, ])

# values = {'': [[u'true'],
#  [u'-14.6'],
#  [u'xueqiu.com_1565017754'],
#  [u'\u6c34\u6728\u4e00\u53f7', 'tt'],
#  [u'1565017754'],
#  [u'1416970817633'],
#  [u'\u4e2d\u7ebf\u80a1'],
#  [u'1468546217913'],
#  [u'14653'],
#  [u'-9.07'],
#  [u'cn'],
#  [u'102'],
#  [u'0.0'],
#  [u'6.56'],
#  [u'null'],
#  [u'ZH014753'],
#  [u'0.854'],
#  [u'-1.89']]
#  }
# _tmp_values = [zip(*value) for value in values.values()]
# print [list(itertools.chain(*x)) for x in itertools.product(*_tmp_values)]



# for x in itertools.product([(1, 5), (2, 4)], [1]):
#     print x















