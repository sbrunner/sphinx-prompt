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
- ``batch``
- ``powershell``
- ``python``
- ``scala``

Prompt(s)
~~~~~~~~~

If modifier is auto, a comma-separated list of prompts to find in the statements.

Else the prompt to add on each statements, for Python and Bash language the end
``\`` is supported.

Defaults to empty, except for the shell languages listed below:
- ``bash`` - ``$``
- ``batch`` - ``C:\>``
- ``powershell`` - ``PS C:\>``

Examples
--------

See: http://sbrunner.github.io/sphinx-prompt/

Build
-----

.. code::

    python bootstrap.py --distribute -v 1.7.1
    ./buildout/bin/buildout
