from io import StringIO

import docutils.statemachine
import docutils.utils
import pytest

sphinx_prompt = __import__("sphinx_prompt")

testdata = [
    [
        [],
        {},
        ["one line"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: " ";
}
</style><span class="prompt1">one line</span>
</pre></div></div>""",
    ],
    [
        ["bash"],
        {},
        ["one line"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "$ ";
}
</style><span class="prompt1">one<span class="w"> </span>line</span>
</pre></div></div>""",
    ],
    [
        [],
        {"language": "bash"},
        ["one line"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "$ ";
}
</style><span class="prompt1">one<span class="w"> </span>line</span>
</pre></div></div>""",
    ],
    [
        ["bash"],
        {},
        ["tow", "line"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "$ ";
}
</style><span class="prompt1">tow</span>
<span class="prompt1">line</span>
</pre></div></div>""",
    ],
    [
        ["bash"],
        {},
        ["one split \\", "line"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "$ ";
}
</style><span class="prompt1">one<span class="w"> </span>split<span class="w"> </span><span class="se">\\</span>
line</span>
</pre></div></div>""",
    ],
    [
        ["bash"],
        {},
        ["mixed split \\", "line", "second"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "$ ";
}
</style><span class="prompt1">mixed<span class="w"> </span>split<span class="w"> </span><span class="se">\\</span>
line</span>
<span class="prompt1">second</span>
</pre></div></div>""",
    ],
    [
        ["bash", "%"],
        {},
        ["other prompt"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "% ";
}
</style><span class="prompt1">other<span class="w"> </span>prompt</span>
</pre></div></div>""",
    ],
    [
        [],
        {"language": "bash", "prompts": "%"},
        ["other prompt opt"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "% ";
}
</style><span class="prompt1">other<span class="w"> </span>prompt<span class="w"> </span>opt</span>
</pre></div></div>""",
    ],
    [
        ["batch"],
        {},
        ["batch"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "C:\\\\> ";
}
</style><span class="prompt1">batch</span>
</pre></div></div>""",
    ],
    [
        ["powershell"],
        {},
        ["powershell"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "PS C:\\\\> ";
}
</style><span class="prompt1"><span class="n">powershell</span></span>
</pre></div></div>""",
    ],
    [
        ["bash"],
        {},
        ['lexer 1 2 "tree"'],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "$ ";
}
</style><span class="prompt1">lexer<span class="w"> </span><span class="m">1</span><span class="w"> </span><span class="m">2</span><span class="w"> </span><span class="s2">&quot;tree&quot;</span></span>
</pre></div></div>""",
    ],
    [
        ["bash", "$,#", "auto"],
        {},
        ["$ user", "# root"],
        """<div class="highlight-default notranslate"><div class="highlight"><pre><style type="text/css">
span.prompt1:before {
  content: "$ ";
}
span.prompt2:before {
  content: "# ";
}
</style><span class="prompt1">user</span>
<span class="prompt2">root</span>
</pre></div></div>""",
    ],
]


@pytest.mark.parametrize("arguments, options, content, expected", testdata)
def test(arguments, options, content, expected):
    sphinx_prompt._cache.next_index = 1
    sphinx_prompt._cache.prompts.clear()
    stream = StringIO()
    reporter = docutils.utils.Reporter("test data", 2, 4, stream, 1)
    statemachine = docutils.statemachine.StateMachine([], None)
    setattr(statemachine, "reporter", reporter)
    directive = sphinx_prompt.PromptDirective(
        "prompt", arguments, options, content, 0, 0, "", None, statemachine
    )
    result = directive.run()
    assert result[0].astext() == expected
