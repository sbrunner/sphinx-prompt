Sphinx Prompt
=============

.. contents:: Table of contents

Initialise
----------

In ``conf.py`` add ``extensions += ['sphinx-prompt']``.

Syntax
------

A default prompt can be created using a ``prompt`` directive:

.. code::

    .. prompt::

       <statements>

The prompt can be further customized in one of two ways:

- Using positional arguments:

    .. code::

        .. prompt:: [<language> [<prompts> [<modifiers>]]]

           <statements>

- Using options:

    .. code::

        .. prompt::
            :language: <language>
            :prompts: <prompts>
            :modifiers: <modifiers>

           <statements>

While these constructs generate the same output, the positional arguments cannot be used
if you want to use a prompt that contains spaces. This is a limitation of reStructuredText.

Positional arguments can be mixed with options **if** they don't overlap
(so if you pass prompts using options, you can only pass the language using positional arguments):

.. code::

    .. prompt:: bash
        :prompts: (cool_project) $

       python -m pip install -U sphinx-prompt

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
