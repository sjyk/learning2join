"""
Defines adaptive operations
"""
from ops import _build_hash_table, _join_update_tuple

def symjoin(input1, input2, attrs):
    usedKeys = set()

    build = _build_hash_table(input1, attrs)

    for src, ids, tup in input2:
        key = tuple([tup[t] for t in tup if t in attrs])

        if key in build:
            
            usedKeys.add(key)

            for val in build[key]:
                yield _join_update_tuple(src, ids, tup, val)

        else:
            _updateIdx(src,ids, key, attrs)


    for b in build:
        if b not in usedKeys:
            for src, ids, _ in build[b]:
                _updateIdx(src,ids, b, attrs)


def asymjoin(input1, input2, attrs):
    build = _build_hash_table(input1, attrs)

    for src, ids, tup in input1:
        key = tuple([tup[t] for t in tup if t in attrs])

        if key not in build:
            build[key] = []

        build[key].append((src, ids, tup))


    for src, ids, tup in input2:
        key = tuple([tup[t] for t in tup if t in attrs])

        if key in build:

            for val in build[key]:
                yield _join_update_tuple(src, ids, tup, val)

        else:
            _updateIdx(src, ids, key, attrs)



def _updateIdx(src, ids, key, attrs):

    for i in range(len(src)):

        if src[i].geti(ids[i], attrs) == key:
            #print(attrs, src[i].geti(ids[i], attrs))
            src[i].updateAppend(ids[i], "idx", tuple(sorted([s.name for s in src])) )
