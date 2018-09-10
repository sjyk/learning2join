"""
Defines the basic relational algebra operations
"""

def select(input, pred=lambda t: True):
    for src, ids, tup in input:
        if pred(tup):
            yield (src, ids, tup)

def project(input, attrs):
    for src, ids, tup in input:
        tup = {t: tup[t] for t in tup if t in attrs}
        yield (src, ids, tup)



def _build_hash_table(input, attrs):
    
    build = {}

    for src, ids, tup in input:
        key = tuple([tup[t] for t in tup if t in attrs])

        if key not in build:
            build[key] = []

        build[key].append((src, ids, tup))

    return build


def _join_update_tuple(src, ids, tup, val):
    ns = src + val[0]
    nid = ids + val[1]
    ntup = tup.copy()
    ntup.update(val[2])

    return (ns, nid, ntup)



def join(input1, input2, attrs):
    
    build = _build_hash_table(input1, attrs)

    for src, ids, tup in input2:
        key = tuple([tup[t] for t in tup if t in attrs])

        if key in build:

            for val in build[key]:

                yield _join_update_tuple(src, ids, tup, val)
        #else:

            #print("Miss", key)

