from setuptools import setup

SETUP_INFO = dict(
    name='commondata',
    version='0.0.1',
    install_requires=[],
    description="A structured collection of common knowledge",
    license='GPL',
    test_suite='tests',
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://commondata.lino-framework.org",
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Operating System :: OS Independent""".splitlines())

SETUP_INFO.update(long_description=file('README.rst').read())

SETUP_INFO.update(packages=[str(n) for n in """
commondata
""".splitlines() if n])

SETUP_INFO.update(namespace_packages=['commondata'])

SETUP_INFO.update(test_suite='')

if __name__ == '__main__':
    setup(**SETUP_INFO)
