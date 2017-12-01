# coding: utf-8

from pymongo import MongoClient


c1 = MongoClient()['test']['test']
c2 = MongoClient()['test']['test']



print c1
print c2

print c1 == c2