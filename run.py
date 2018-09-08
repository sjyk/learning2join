"""
Test script
"""

from core.relation import Relation
from core.opt import NWayJoin

data1 = [{"a": 'q', "b": "ny"},
        {"a": 'a', "b": "nyc"},
        {"a": 'f', "b": "chi"},
        {"a": 'g', "b": "mon"}]

data2 = [{"a": 'q', "c": "fyg"}]*1000

data3 = [{"c": 'fyg', "b": "ny"}]*5


r = Relation("a","b")
r.putAll(data1)

s = Relation("a","c")
s.putAll(data2)

t = Relation("c","b")
t.putAll(data3)

n = NWayJoin([r,s,t])
for i in n.eval():
    print(i)


