# -*- coding: UTF-8 -*-
# Copyright 2014-2016 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""

Note that Town is a subclass of Municipality. E.g. Võru vald and Võru
linn are the same object while Võru maakond is a separat object.

"""

from collections import namedtuple

# FIELDS = ('entity', 'name', 'desc', 'isoCode2', 'isoCode3', 'zipCode')
FIELDS = ('entity', 'name', 'isoCode2', 'isoCode3', 'zipCode', 'population')

Country = namedtuple("Country", FIELDS)


class Place(object):
    value = None

    def __init__(self, pg, parent, *args, **kwargs):
        self.children = []
        self.parent = parent
        if parent is not None:
            parent.children.append(self)
        for i, v in enumerate(args):
            k = pg.args[i]
            if k in kwargs:
                raise Exception("Multiple values for %s" % k)
            kwargs[k] = v

        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def factory(self, pg):

        def create(*args, **kwargs):
            prev = pg.current
            if prev is None:
                parent = None
            elif prev.value < self.value:
                parent = prev
            else:
                parent = prev.parent
                while parent and not self.can_be_child(parent):
                    parent = parent.parent
            i = self(pg, parent, *args, **kwargs)
            pg.current = i
            return i

        return create

    @classmethod
    def can_be_child(self, p):
        if p.value < self.value:
            return True
        return False

    def match(self, **kwargs):
        for k, v in kwargs.items():
            if getattr(self, k) != v:
                return False
        return True

    def find(self, **kwargs):

        def f(i):
            return i.match(**kwargs)

        return list(filter(f, self.children))

    def get(self, **kwargs):
        q = self.find(**kwargs)
        if len(q) != 1:
            raise Exception("Found %d items!" % len(q))
        return q[0]


class PlaceGenerator(object):

    def __init__(self):
        self.current = None

    def install(self, *classes):
        for c in classes:
            k = c.__name__.lower()
            if hasattr(self, k):
                raise Exception("Attempt to redefine name %r" % k)
            setattr(self, k, c.factory(self))

    def set_args(self, args):
        self.args = tuple(args.split())
