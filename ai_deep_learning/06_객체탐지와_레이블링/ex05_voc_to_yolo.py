# labelImg 의 기본 저장 형식(Pascal VOC, .xml)을 YOLO 형식(.txt)으로 바꾸기
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).parent
CLASSES = ["bottle", "can", "bag"]

# labelImg 가 PascalVOC 모드에서 저장하는 xml 과 같은 모양 (일부만)
xml_text = """<annotation>
  <filename>beach_010.jpg</filename>
  <size><width>640</width><height>480</height><depth>3</depth></size>
  <object><name>bottle</name><difficult>0</difficult>
    <bndbox><xmin>120</xmin><ymin>200</ymin><xmax>160</xmax><ymax>300</ymax></bndbox></object>
  <object><name>bag</name><difficult>0</difficult>
    <bndbox><xmin>400</xmin><ymin>100</ymin><xmax>480</xmax><ymax>160</ymax></bndbox></object>
</annotation>"""
(HERE / "beach_010.xml").write_text(xml_text, encoding="utf-8")


def voc_to_yolo(xml_path):
    root = ET.parse(xml_path).getroot()
    W = int(root.find("size/width").text)
    H = int(root.find("size/height").text)
    lines = []
    for obj in root.iter("object"):
        c = CLASSES.index(obj.find("name").text)         # 이름 → 번호
        b = obj.find("bndbox")
        x1, y1, x2, y2 = (float(b.find(k).text) for k in ("xmin", "ymin", "xmax", "ymax"))
        lines.append(f"{c} {(x1 + x2) / 2 / W:.6f} {(y1 + y2) / 2 / H:.6f} {(x2 - x1) / W:.6f} {(y2 - y1) / H:.6f}")
    return lines


lines = voc_to_yolo(HERE / "beach_010.xml")
(HERE / "beach_010.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
