from core.relation import Relation 
from ops import join

"""
Implements a n-way natural join
"""
class NWayJoin(object):

    def __init__(self, rels):
        self.rels = rels
        self.reliter = [r.get() for r in rels]

    def _onejoin(self):
        for i, r in enumerate(self.rels):
            for j, s in enumerate(self.rels):

                if i == j:
                    continue

                rattrs = set(r.attributes)
                sattrs = set(s.attributes)
                intersect = rattrs.intersection(sattrs)
                union = list(rattrs.union(sattrs))

                #take first eligible join by default
                if len(intersect) > 0:
                    joiniter = join(self.reliter[i],self.reliter[j], intersect)
                    joinrel = Relation(*union)

                    self.rels.append(joinrel)
                    self.reliter.append(joiniter)  

                    self.rels = [r for ti, r in enumerate(self.rels) if ti != i and ti != j]
                    self.reliter = [r for ti, r in enumerate(self.reliter) if ti != i and ti != j]
                    return;

    def eval(self):
        while len(self.rels) > 1:
            self._onejoin()

        for val in self.reliter[0]:
            yield val










