from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re

HTML = '<p></p><p></p><p></p><p></p>'

class HSpacerPre(Preprocessor):
    RE = re.compile(r'^===\s*$', re.MULTILINE)

    def run(self, lines):
        text = "\n".join(lines)
        text = self.RE.sub(HTML, text)
        return text.split("\n")

class HSpacerExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(HSpacerPre(md), 'hspacer', 25)