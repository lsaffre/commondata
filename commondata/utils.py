# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
# This file is part of the commondata library.
# The commondata library is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3 of
# the License, or (at your option) any later version.
# The commondata library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with the commondata library; if not, see
# <http://www.gnu.org/licenses/>.

"""

Note that Town is a subclass of Municipality. E.g. Võru vald and Võru
linn are the same object while Võru maakond is a separat object.

"""

class Place(object):
    value = None

    def __init__(self, parent, *args, **kwargs):
        self.children = []
        self.parent = parent
        if parent is not None:
            parent.children.append(self)
        self.setup(*args, **kwargs)
        
    def setup(self):
        pass
        
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
            i = self(parent, *args, **kwargs)
            pg.current = i
            return i
        return create

    @classmethod
    def can_be_child(self, p):
        if p.value < self.value:
            return True
        return False


class PlaceGenerator(object):
    def __init__(self):
        self.current = None

    def install(self, *classes):
        for c in classes:
            k = c.__name__.lower()
            if hasattr(self, k):
                raise Exception("Attempt to redefine name %r" % k)
            setattr(self, k, c.factory(self))
        # self.country = Country.factory(self)
        # self.county = County.factory(self)
        # self.town = Town.factory(self)
        # self.township = Township.factory(self)
        # self.municipality = Municipality.factory(self)
        # self.borough = Borough.factory(self)
        # self.smallborough = SmallBorough.factory(self)
        # self.village = Village.factory(self)



