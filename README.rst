==========================
The ``commondata`` package
==========================

The main package ``commondata`` defines the ``commondata`` namespace,  some
utilities and world-wide data such as the list of countries.  Country-specific
data is contained in individual packages.

- `commondata.be <https://github.com/lsaffre/commondata-be>`_ :
  Common data about Belgium
- `commondata.ee <https://github.com/lsaffre/commondata-ee>`_:
  Common data about Estonia
- `commondata.eg <https://github.com/ExcellentServ/commondata-eg>`_:
  Common data about Egypt


Minimalistic

The library does **not** provide querying functionality.  Just the basic minimum
to write test cases.  This is a design choice. This data is meant to be imported
into existing systems that use their own preferences for rendering and querying
data.

Showcase

>>> from commondata.countries import COUNTRIES, FIELDS
>>> FIELDS
('entity', 'name', 'isoCode2', 'isoCode3', 'zipCode', 'population')
>>> COUNTRIES[1]
Country(entity='http://www.wikidata.org/entity/Q971', name={'en': 'Republic of the Congo', 'de': 'Republik Kongo', 'fr': 'République du Congo', 'nl': 'Congo-Brazzaville', 'et': 'Kongo Vabariik', 'bn': 'কঙ্গো প্রজাতন্ত্র', 'es': 'República del Congo'}, isoCode2='CG', isoCode3='COG', zipCode=None, population='5260750')
>>> len(COUNTRIES)
195


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


Don't read on
=============

The remaining part of this document is obsolete but still valid.

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
>>> root = pg.kingdom("Egypt", u'مصر')
>>> print(root.name_ar)
مصر
