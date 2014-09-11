====================================
The ``commondata`` namespace package
====================================

Note: we are discussing whether this package is meaningful.  See
http://lino-framework.org/tickets/109.html

This package is the heart of "common data", a sustainable way of
maintaining and sharing structured common knowledge.  The Python
package itself contains just some utilities and defines the
``commondata`` namespace. It is the base for packages like

- `commondata.be <https://github.com/lsaffre/commondata-be>`_ : 
  Common knowledge about Belgium
- `commondata.ee <https://github.com/lsaffre/commondata-ee>`_: 
  Common knowledge about Estonia


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

