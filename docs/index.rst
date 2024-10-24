.. my_package documentation master file

Welcome to my_package's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   contributing
   changelog

Installation
-----------

To install my_package, run this command in your terminal:

.. code-block:: console

   $ pip install my_package

Usage
-----

Here's a simple example of how to use my_package:

.. code-block:: python

   from my_package import hello_world
   
   # Get a friendly greeting
   greeting = hello_world()
   print(greeting)

API Reference
------------

.. automodule:: my_package.core
   :members:
   :undoc-members:
   :show-inheritance:

Contributing
-----------

We love your input! We want to make contributing to my_package as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

Development Process
~~~~~~~~~~~~~~~~~

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code follows the project's style guidelines.
6. Issue that pull request!

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`