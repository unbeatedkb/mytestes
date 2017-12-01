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
	for i in nums:
		print i 

def test_chain():
	nums = itertools.chain('ab', [1, 2])
	for i in nums:
		print i

# test_count()	
# test_cycle()
# test_repeat()
test_chain()


