# icon.svg와 같은 도형을 PNG로 그린다(4배로 그린 뒤 줄여 테두리를 부드럽게).
# 실행: python scripts/make-icons.py  → icon-32.png, apple-touch-icon.png(180), icon-512.png
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
K = 4  # 4배로 그린다
BLUE, WHITE = '#2f4fb5', '#ffffff'
GREEN, GREEN_LINE, ORANGE, TODO_LINE = '#16a34a', '#4ade80', '#f59e0b', '#9fb1e6'


def s(*v):
    return [x * K for x in v]


def draw():
    im = Image.new('RGBA', (512 * K, 512 * K), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(s(0, 0, 511, 511), radius=112 * K, fill=BLUE)
    # 관공서: 지붕(모서리 둥글게), 처마, 기둥 3개, 바닥
    roof = [tuple(s(256, 70)), tuple(s(410, 146)), tuple(s(102, 146))]
    d.polygon(roof, fill=WHITE)
    d.line(roof + [roof[0]], fill=WHITE, width=20 * K, joint='curve')
    for x, y in roof:
        d.ellipse((x - 10 * K, y - 10 * K, x + 10 * K, y + 10 * K), fill=WHITE)
    d.rounded_rectangle(s(112, 166, 400, 190), radius=8 * K, fill=WHITE)
    for x in (140, 234, 328):
        d.rounded_rectangle(s(x, 204, x + 44, 300), radius=6 * K, fill=WHITE)
    d.rounded_rectangle(s(96, 312, 416, 340), radius=10 * K, fill=WHITE)
    # 단계 타임라인: 완료·완료·현 단계
    d.line(s(140, 412, 256, 412), fill=GREEN_LINE, width=18 * K)
    d.line(s(256, 412, 372, 412), fill=TODO_LINE, width=18 * K)
    for cx, color in ((140, GREEN), (256, GREEN), (372, ORANGE)):
        d.ellipse(s(cx - 46, 366, cx + 46, 458), fill=WHITE)
        d.ellipse(s(cx - 34, 378, cx + 34, 446), fill=color)
    return im


big = draw()
for size, name in ((32, 'icon-32.png'), (180, 'apple-touch-icon.png'), (512, 'icon-512.png')):
    big.resize((size, size), Image.LANCZOS).save(ROOT / name)
    print(name, size)
