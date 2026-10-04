# 시맨틱 구조 보기: python outline.py 파일.html
import sys
from html.parser import HTMLParser
from pathlib import Path

# 구조 트리에 보여 줄 태그: 시맨틱 영역 태그들
LANDMARKS = {"header", "nav", "main", "section", "article", "aside", "footer", "figure", "form", "address", "search"}
# 제목 태그 h1 ~ h6
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
# 닫는 태그가 없는 태그(빈 요소)는 들여쓰기 계산에서 빼요
VOID = {"meta", "link", "img", "br", "hr", "input", "source", "area", "col", "embed", "track", "wbr"}


# HTMLParser 를 물려받아 "태그가 열릴 때 / 닫힐 때 / 글자가 나올 때" 할 일을 정해요
class Outline(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth, self.stack, self.lines, self.capture = 0, [], [], None

    # 태그가 열릴 때: 영역 태그면 한 줄 적고 들여쓰기 한 칸 늘리기
    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        self.stack.append(tag)
        a = dict(attrs)
        if tag in LANDMARKS or tag == "div":
            label = f"<{tag}>" + (f' class="{a["class"]}"' if "class" in a else "") + (f' aria-label="{a["aria-label"]}"' if "aria-label" in a else "")
            # div 는 · , 시맨틱 태그는 ▣ 로 표시해서 구분
            self.lines.append("  " * self.depth + ("· " if tag == "div" else "▣ ") + label)
            self.depth += 1
        elif tag in HEADINGS:
            self.capture = [tag, ""]

    # 태그가 닫힐 때: 들여쓰기 한 칸 줄이기 / 제목이면 모아 둔 글자와 함께 적기
    def handle_endtag(self, tag):
        if tag in VOID or not self.stack:
            return
        self.stack.pop()
        if tag in LANDMARKS or tag == "div":
            self.depth -= 1
        elif tag in HEADINGS and self.capture:
            self.lines.append("  " * self.depth + f"{self.capture[0]}: {self.capture[1].strip()}")
            self.capture = None

    # 제목 태그 안의 글자 모으기
    def handle_data(self, data):
        if self.capture:
            self.capture[1] += data


# 파일 이름을 주면 그 파일만, 안 주면 이 폴더의 ex*.html 전부
HERE = Path(__file__).parent
names = sys.argv[1:] or [p.name for p in sorted(HERE.glob("ex*.html"))]   # 인자가 없으면 이 폴더의 예제 전부
# 파일을 읽어 파서에 넣고, 만들어진 트리를 출력
for name in names:
    path = Path(name) if Path(name).exists() else HERE / name
    p = Outline()
    p.feed(path.read_text(encoding="utf-8"))
    print(f"[{name}]")
    print("\n".join(p.lines))
    print()
