"""
Test script
"""

from core.relation import Relation
from core.opt import NWayJoinLearn, NWayJoin

people = [{"id": 1, "name": "John"},
        {"id": 2, "name": "James"},
        {"id": 3, "name": "Sally"},
        {"id": 4, "name": "Fred"}]

following = [{"follower_id": 1, "id": 1}, 
             {"follower_id": 2, "id": 1},
             {"follower_id": 3, "id": 1}]

idmap = [{"follower_id": 1, "name": "John"}, 
         {"follower_id": 2, "name": "James"},
         {"follower_id": 3, "name": "Sally"}]*1000


r = Relation("id","name")
r.putAll(people)

s = Relation("follower_id","id")
s.putAll(following)

t = Relation("folower_id","name")
t.putAll(idmap)

import datetime

now = datetime.datetime.now()

n = NWayJoinLearn([r,s, t], True)
for i in n.eval():
    i##print(i)

print((datetime.datetime.now()-now).total_seconds())

now = datetime.datetime.now()

n = NWayJoinLearn([r,s,t], True)
for i in n.eval():
    i##print(i)

print((datetime.datetime.now()-now).total_seconds())




