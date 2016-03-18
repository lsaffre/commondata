====================================
The ``commondata`` namespace package
====================================

Note: we are discussing whether this package is meaningful.  See
http://lino-framework.org/tickets/109.html

This package is the heart of "common data", a sustainable way of
maintaining and sharing structured common knowledge.  The Python
package itself contains just some utilities_ and defines the
``commondata`` namespace. It is the base for packages like

- `commondata.be <https://github.com/lsaffre/commondata-be>`_ : 
  Common knowledge about Belgium
- `commondata.ee <https://github.com/lsaffre/commondata-ee>`_: 
  Common knowledge about Estonia
- `commondata.eg <https://github.com/ExcellentServ/commondata-eg>`_: 
  Common knowledge about Egypt

Features
========


Maintained in Python
--------------------

The Python programming language brings together two qualities 

- a syntax which makes it easy (or at least possible) to be used by
  non-programmers
- a powerful programming language working behind the scenes


Freely available under the GPL
------------------------------

Free software should not depend on non-free material.

Designed to be imported
-----------------------

The library does **not** provide much querying functionality.  Just
the basic minimum, used to write test cases.  This is a design
choice. This data is meant to be imported into existing systems which
offer their own querying facilities.


Installation
============

- The easiest way is to type::

    pip install commondata.ee commondata.be

- Alternatively you might prefer to use the development version::

    $ git clone https://github.com/lsaffre/commondata.git
    $ git clone https://github.com/lsaffre/commondata-ee.git
    $ git clone https://github.com/lsaffre/commondata-be.git

    $ pip install -e commondata
    $ pip install -e commondata.ee
    $ pip install -e commondata.be

Online version of this document on https://github.com/lsaffre/commondata


Utilities
=========

How to use the Place and PlaceGenerator classes.

You define a subclass of Place for each "type" of place:

>>> from commondata.utils import Place, PlaceGenerator
>>> class PlaceInFoo(Place):
...     def __str__(self):
...        return self.name
>>> class Kingdom(PlaceInFoo):
...     value = 1
>>> class County(PlaceInFoo):
...     value = 2
>>> class Borough(PlaceInFoo):
...     value = 3
>>> class Village(PlaceInFoo):
...     value = 3

The PlaceGenerator is used to instantiate to populate

Part 1 : configuration:

>>> pg = PlaceGenerator()
>>> pg.install(Kingdom, County, Borough, Village)
>>> pg.set_args('name')

Part 2 : filling data

>>> root = pg.kingdom("Kwargia")
>>> def fill(pg):
...    pg.county("Kwargia")
...    pg.borough("Kwargia")
...    pg.village("Virts")
...    pg.village("Vinks")
...    pg.county("Gorgia")
...    pg.village("Girts")
...    pg.village("Ginks")

>>> fill(pg)

Part 3 : using the data

>>> [str(x) for x in root.children]
['Kwargia', 'Gorgia']
>>> kwargia = root.children[0]
>>> [str(x) for x in kwargia.children]
['Kwargia', 'Virts', 'Vinks']


Multilingual place names
-------------------------

You use the `commondata.utils.PlaceGenerator.set_args()` method to
specify the names of the fields of subsequent places.

>>> pg = PlaceGenerator()
>>> pg.install(Kingdom, County, Borough, Village)
>>> pg.set_args('name name_ar')
>>> root = pg.kingdom("Egypt", u'\u0645\u0635\u0631')
>>> print(root.name_ar)
مصر

