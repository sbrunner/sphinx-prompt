Sphinx Prompt
=============

.. contents:: Table of contents

Initialise
----------

In ``conf.py`` add ``extensions += ['sphinx-prompt']``.

Syntax
------

.. code::

    .. prompt:: [<language> [<prompts> [<modifier>]]]

       <statements>

Language
~~~~~~~~

Supported language:

- ``text`` (no pigments, default)
- ``bash``
- ``python``
- ``scala``

Prompt(s)
~~~~~~~~~

If modifier is auto, a comma-separated list of prompts to find in the statements.

Else the prompt to add on each statements, for Python and Bash language the end
``\`` is supported.

Default to empty, ``$`` for bash language.

Examples
--------

See: http://sbrunner.github.io/sphinx-prompt/

Build
-----

.. code::

    python bootstrap.py --distribute -v 1.7.1
    ./buildout/bin/buildout
