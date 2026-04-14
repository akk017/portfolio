from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


HTML = '''
<details>
<summary><span>{type}</span><span>{title}</span><div class='divider'></div></summary>
<div>{content}</div>
</details>
'''

class CallOutPreprocessor(Preprocessor):
    RE = re.compile(
        r'^!!!\s+(\S+)\s+(.*)\n([\s\S]*?)\n!!!',
        re.MULTILINE
    )

    def run(self, lines):
        text = "\n".join(lines)

        def repl(match):
            type = match.group(1).strip()
            title = match.group(2).strip()
            content = match.group(3).strip()
            return HTML.format(title=title, type=type, content=content)

        text = self.RE.sub(repl, text)
        return text.split("\n")

class CalloutExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(CallOutPreprocessor(md), 'danger_block', 25)