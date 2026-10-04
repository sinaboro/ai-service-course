# 시맨틱 구조 보기: python outline.py 파일.html
import sys
from html.parser import HTMLParser
from pathlib import Path

LANDMARKS = {"header", "nav", "main", "section", "article", "aside", "footer", "figure", "form", "address", "search"}
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
VOID = {"meta", "link", "img", "br", "hr", "input", "source", "area", "col", "embed", "track", "wbr"}


class Outline(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth, self.stack, self.lines, self.capture = 0, [], [], None

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        self.stack.append(tag)
        a = dict(attrs)
        if tag in LANDMARKS or tag == "div":
            label = f"<{tag}>" + (f' class="{a["class"]}"' if "class" in a else "") + (f' aria-label="{a["aria-label"]}"' if "aria-label" in a else "")
            self.lines.append("  " * self.depth + ("· " if tag == "div" else "▣ ") + label)
            self.depth += 1
        elif tag in HEADINGS:
            self.capture = [tag, ""]

    def handle_endtag(self, tag):
        if tag in VOID or not self.stack:
            return
        self.stack.pop()
        if tag in LANDMARKS or tag == "div":
            self.depth -= 1
        elif tag in HEADINGS and self.capture:
            self.lines.append("  " * self.depth + f"{self.capture[0]}: {self.capture[1].strip()}")
            self.capture = None

    def handle_data(self, data):
        if self.capture:
            self.capture[1] += data


HERE = Path(__file__).parent
names = sys.argv[1:] or [p.name for p in sorted(HERE.glob("ex*.html"))]   # 인자가 없으면 이 폴더의 예제 전부
for name in names:
    path = Path(name) if Path(name).exists() else HERE / name
    p = Outline()
    p.feed(path.read_text(encoding="utf-8"))
    print(f"[{name}]")
    print("\n".join(p.lines))
    print()
