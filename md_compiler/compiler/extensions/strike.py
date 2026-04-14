import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree

class StrikeProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element("del")
        el.text = m.group(1)
        return el, m.start(0), m.end(0)

class StrikeExtension(Extension):
    def extendMarkdown(self, md):
        pattern = r'~~(.*?)~~'
        md.inlinePatterns.register(StrikeProcessor(pattern, md), 'strike', 175)
