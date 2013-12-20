#!/usr/bin/python
# coding: utf-8


from docutils import nodes
from docutils.parsers import rst

from pygments import highlight
from pygments.lexers import TextLexer
from pygments.lexers import BashLexer
from pygments.lexers import PythonLexer
from pygments.lexers import ScalaLexer
from pygments.formatters import HtmlFormatter


class PromptDirective(rst.Directive):

    optional_arguments = 3
    has_content = True

    def run(self):
        self.assert_has_content()

        language = 'text'
        prompt = None
        modifiers = []

        if self.arguments:
            language = self.arguments[0]
            if len(self.arguments) > 1:
                prompt = self.arguments[1]
            elif language == 'bash':
                prompt = '$'
            if len(self.arguments) > 2:
                modifiers = self.arguments[2].split(',')
            if 'auto' in modifiers:
                prompts = prompt.split(',')

        html = '<pre class="highlight">'
        html += '<style type="text/css" scoped>'
        if 'auto' in modifiers:
            for index, prompt in enumerate(prompts):
                html += """span.prompt%i:before {
  content: "%s ";
}
""" % (index, prompt)
        else:
            if prompt is not None:
                html += """span.prompt:before {
  content: "%s ";
}
""" % (prompt)
        html += '</style>'
        latex = "\\begin{Verbatim}[commandchars=\\\\\\{\\}]"

        Lexer = TextLexer
        if language == 'bash':
            Lexer = BashLexer
        elif language == 'python':
            Lexer = PythonLexer
        elif language == 'scala':
            Lexer = ScalaLexer

        statement = []
        prompt_index = -1
        for line in self.content:
            if 'auto' in modifiers:
                latex += '\n' + line

                for index, prompt in enumerate(prompts):
                    if line.startswith(prompt):
                        if len(statement) > 0:
                            html += '<span class="prompt%i">%s</span>\n' % (
                                prompt_index,
                                highlight(
                                    '\n'.join(statement),
                                    Lexer(),
                                    HtmlFormatter(nowrap=True)
                                ).strip('\r\n')
                            )
                            statement = []
                        line = line[len(prompt):].strip()
                        prompt_index = index
                        break

                statement.append(line)
            elif language == 'bash' or language == 'python':
                statement.append(line)
                if len(line) == 0 or not line[-1] == '\\':
                    html += '<span class="prompt">%s</span>\n' % (
                        highlight(
                            '\n'.join(statement),
                            Lexer(),
                            HtmlFormatter(nowrap=True)
                        ).strip('\r\n')
                    )
                    if prompt is not None:
                        latex += '\n%s %s' % (prompt, '\n'.join(statement))
                    else:
                        latex += '\n' + '\n'.join(statement)
                    statement = []
            else:
                html += '<span class="prompt">%s</span>\n' % (
                    highlight(
                        line,
                        Lexer(),
                        HtmlFormatter(nowrap=True)
                    ).strip('\r\n')
                )
                if prompt is not None:
                    latex += '\n%s %s' % (prompt, line)
                else:
                    latex += '\n' + line

        # Add last prompt
        if 'auto' in modifiers and len(statement) > 0:
            html += '<span class="prompt%i">%s</span>\n' % (
                prompt_index,
                highlight(
                    '\n'.join(statement),
                    Lexer(),
                    HtmlFormatter(nowrap=True)
                ).strip('\r\n')
            )

        html += "</pre>"
        latex += "\n\\end{Verbatim}"

        return [
            nodes.raw('\n'.join(self.content), html, format="html"),
            nodes.raw('\n'.join(self.content), latex, format="latex"),
        ]


def setup(app):
    app.add_directive('prompt', PromptDirective)
