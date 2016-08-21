from setuptools import setup

SETUP_INFO = dict(
    name='commondata',
    version='0.0.2',
    install_requires=[],
    description="A structured collection of common knowledge",
    license='GPL',
    test_suite='tests',
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="https://github.com/lsaffre/commondata",
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Operating System :: OS Independent""".splitlines())

SETUP_INFO.update(long_description=open('README.rst').read())

SETUP_INFO.update(packages=[str(n) for n in """
commondata
""".splitlines() if n])

SETUP_INFO.update(namespace_packages=['commondata'])

if __name__ == '__main__':
    setup(**SETUP_INFO)
