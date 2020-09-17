from requests_html import HTMLSession
from box import Box
import json

session = HTMLSession()

class Crawler:

    def __init__(self):
        self.session = session

    def _get_json_content(self, resp):
        content = resp.html.find("script")[-1].text[len("window.__INITIAL_SSR_STATE__="):]
        return content.replace("undefined", "null")

    def _get_box(self, content):
        box = Box(json.loads(content))
        return box

    def run(self):
        resp = self.session.get("https://www.xiaohongshu.com/explore")
        content = self._get_json_content(resp)
        box = self._get_box(content)
        return box