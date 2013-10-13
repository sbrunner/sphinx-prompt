Sphinx Prompt
=============

.. contents:: Table of contents

Inititlise
----------

In ``conf.py`` add ``extensions += ['sphinx-prompt']``.

Directive
---------

.. code::

    .. prompt::

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
    .. prompt:: bash #

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

Build
-----

.. code::

    python bootstrap.py --distribute -v 1.7.1
    ./buildout/bin/buildout
