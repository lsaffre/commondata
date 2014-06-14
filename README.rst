====================================
The ``commondata`` namespace package
====================================

.. note::

  This package is no longer maintained.
  See http://lino-framework.org/tickets/109.html

.. module:: commondata

This package is the heart of "common data", a new and sustainable way
to maintain and share structured common knowledge.

The package itself contains just some utilities and defines the Python
``commondata`` namespace. It is the base for packages like 

- `commondata.be <https://github.com/lsaffre/commondata-be>`_ : 
  Common knowledge about Belgium
- `commondata.ee <https://github.com/lsaffre/commondata-ee>`_: 
  Common knowledge about Estonia

The ``commondata`` vision
=========================

Did you ever start to write your own list of the countries, the
capitals, the currencies or the languages of the world? Or the
chemical elements, the books of the Bible or the text of the Human
Rights declaration?

These things are considered "common knowledge".  You can find them on
Wikipedia where they are `freely available for everybody
<https://www.mediawiki.org/wiki/API>`_.  There is also `babel.Locale
<http://babel.pocoo.org/docs/locale/>`_, a Python interface to the
`CLDR <http://cldr.unicode.org/>`_ (Unicode Common Locale Data
Repository).

The ``commondata`` project goes a step further: it suggests to also
*write* and *maintain* the data itself in Python.

Maintained in Python
--------------------

The Python programming language brings together two qualities 

- a syntax which makes it easy to use for non-programmers
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

