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
                if language == 'auto':
                    prompts = self.arguments[1].split(',')
                else:
                    prompt = self.arguments[1]
            else:
                prompt = '$'
        else:
            language = 'auto'
            prompts = ['$', '#', '>>>']

        html = '<pre>'
        html += '<style type="text/css" scoped>'
        if language == 'auto':
            for index, prompt in enumerate(prompts):
                html += """span.prompt%i:before {
  content: "%s ";
}
""" % (index, prompt)
        else:
            html += """span:before {
  content: "%s ";
}
""" % (prompt)
        html += '</style>'
        latex = "\\begin{Verbatim}[commandchars=\\\\\\{\\}]"

        statement = []
        prompt_index = -1
        for line in self.content:
            if language == 'auto':
                latex += '\n' + line
                for index, prompt in enumerate(prompts):
                    if line.startswith(prompt):
                        if len(statement) > 0:
                            html += '<span class="prompt%i">%s</span>\n' % (
                                prompt_index,
                                '\n'.join(statement).replace('<', '&lt;').replace('>', '&gt;')
                            )
                            statement = []
                        line = line[len(prompt):].strip()
                        prompt_index = index
                        break
                statement.append(line)
            elif language == 'bash':
                statement.append(line)
                if not line[-1] == '\\':
                    html += '<span>' + '\n'.join(statement).replace('<', '&lt;').replace('>', '&gt;') + '</span>\n'
                    latex += '\n%s %s' % (prompt, '\n'.join(statement))
                    statement = []

        html += "</pre>"
        latex += "\n\\end{Verbatim}"

        return [
            nodes.raw('\n'.join(self.content), html, format="html"),
            nodes.raw('\n'.join(self.content), latex, format="latex"),
        ]


def setup(app):
    app.add_directive('prompt', PromptDirective)
