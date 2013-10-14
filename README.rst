Sphinx Prompt
=============

.. contents:: Table of contents

Inititlise
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

If modifier is auto, a coma separated list of prompts to find in the statements.

Else the prompt to add on each statements, for Python and Bash language the end
``\`` is supported.

Default to ``$,#,>>>``.

Examples
--------

.. code::

    .. prompt:: bash $ noauto

        cd <folder>
        cp <src> \
            <dst>
        cd -

=>

.. code:: html

    <pre>
    <style type="text/css" scoped>
    span:before {
        content: "$ ";
    }
    </style>
    <span>cd &lt;folder&gt;</span>
    <span>cd -</span>
    <span>cp &lt;src&gt; \
        &lt;dst&gt;</span>
    </pre>

----

.. code::

    .. prompt:: bash # noauto

        cd <folder>
        cd -

=>

.. code:: html

    <pre>
    <style type="text/css" scoped>
    span:before {
        content: "# ";
    }
    </style>
    <span>cd &lt;folder&gt;</span>
    <span>cd -</span>
    </pre>

----

.. code::

    .. prompt::

        $ sudo
        # exit
        $

=>

.. code:: html

    <pre>
    <style type="text/css" scoped>
    span.prompt0:before {
        content: "$ ";
    }
    span.pompt1:before {
        content: "# ";
    }
    span.promt2:before {
        content: ">>> ";
    }
    </style>
    <span class="prompt0">sudo</span>
    <span class="prompt1">exit</span>
    <span class="prompt0"></span>
    </pre>

----

.. code::

    .. prompt:: bash $,(env)...$

        $ source env/bin/activate
        (env)...$ deactivate
        $

=>

.. code:: html

    <pre>
    <style type="text/css" scoped>
    span.prompt0:before {
        content: "$ ";
    }
    span.pompt1:before {
        content: "(env)...$ ";
    }
    </style>
    <span class="prompt0">source env/bin/activate</span>
    <span class="prompt0">deactivate</span>
    <span class="prompt0"></span>
    </pre>

Build
-----

.. code::

    python bootstrap.py --distribute -v 1.7.1
    ./buildout/bin/buildout
