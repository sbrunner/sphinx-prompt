#!/usr/bin/python
# coding: utf-8

from docutils import nodes
from docutils.parsers import rst

class PromptDirective(rst.Directive):

    optional_arguments = 2
    has_content = True

    def run(self):
        self.assert_has_content()
        if self.arguments:
            language = self.arguments[0]
            if len(self.arguments) > 1:
                prompt = self.arguments[1]
            else:
                prompt = '$'
        else:
            language = 'bash'
            prompt = '$'

        html = """<pre>
<style type="text/css" scoped>
span:before {
  content: "%s ";
}
</style>""" % prompt
        latex = "\\begin{Verbatim}[commandchars=\\\\\\{\\}]"

        statement = []
        for line in self.content:
            statement.append(line)
            if not line[-1] == '\\':
                html += '<span>' + '\n'.join(statement).replace('<', '&lt;').replace('>', '&gt;') + '</span>\n'
                latex = '\n$ ' + '\n'.join(statement)
                statement = []

        html += "</pre>"
        latex += "\n\\end{Verbatim}"

        return [
            nodes.raw('\n'.join(self.content), html, format="html"),
            nodes.raw('\n'.join(self.content), latex, format="latex"),
        ]

def setup(app):
    app.add_directive('prompt', PromptDirective)
