"""Generate self-contained GitHub profile art; no dependencies or network."""
from pathlib import Path
from html import escape
import math

ROOT = Path(__file__).resolve().parent
PAPER, INK, MUTED, LINE, RED = '#f3f4f2', '#232522', '#62665f', '#d6d4cc', '#b63b32'


def text(x, y, value, size=20, color=INK, weight=400, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(value)}</text>'


def line(x1, y1, x2, y2, color=LINE, width=1, extra=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>'


def circle(x, y, r, fill=INK, extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'


def svg(name, height, title, content, background=PAPER):
    doc = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<style>
text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; }}
.mono {{ font-family: 'SFMono-Regular', Consolas, monospace; letter-spacing: 2px; }}
.flow {{ stroke-dasharray: 5 10; animation: travel 5s linear infinite; }}
.pulse {{ animation: breathe 4s ease-in-out infinite; }}
.groove {{ transform-box: fill-box; transform-origin: center bottom; animation: groove 2s ease-in-out infinite; }}
@keyframes travel {{ to {{ stroke-dashoffset: -90; }} }}
@keyframes breathe {{ 0%,100% {{ opacity: .4; }} 50% {{ opacity: 1; }} }}
@keyframes groove {{ 0%,100% {{ transform: rotate(-4deg); }} 50% {{ transform: rotate(4deg); }} }}
@media (prefers-reduced-motion: reduce) {{ .flow,.pulse,.groove {{ animation: none; }} }}
</style>
<rect width="960" height="{height}" fill="{background}"/>
{content}
</svg>
'''
    (ROOT / name).write_text(doc, encoding='utf-8')


def waveform(x, y, width, amplitude, phase=0):
    points = []
    for i in range(int(width) + 1):
        t = i / width
        a = math.sin(t * 39 + phase) * .47 + math.sin(t * 97 + phase) * .22 + math.sin(t * 173) * .13
        a *= .55 + .45 * math.sin(t * 8 + phase) ** 2
        points.append(f'{x+i:.1f},{y+a*amplitude:.1f}')
    return ' '.join(points)


def cover():
    c = line(38, 46, 922, 46, INK)
    c += text(38, 31, 'LITTBOX / RESEARCH & MOTION', 13, extra='class="mono"')
    c += text(922, 31, 'YUNNAN UNIVERSITY', 13, extra='class="mono" text-anchor="end"')
    c += text(38, 90, 'SOFTWARE ENGINEERING · YEAR 03', 15, MUTED, extra='class="mono"')
    c += text(31, 204, 'LittBox.', 108, INK, 750, 'letter-spacing="-6"')
    c += text(39, 253, 'CODE. MOVE. REPEAT.', 23, INK, 600, 'letter-spacing="2"')
    c += text(39, 294, '读懂信号，连接知识。', 25)
    c += text(39, 329, '独立思考，保持热爱。', 20, MUTED)
    c += circle(738, 208, 135, 'none', f'stroke="{LINE}"')
    c += circle(738, 208, 103, 'none', f'stroke="{LINE}" stroke-dasharray="3 8"')
    c += line(582, 208, 894, 208) + line(738, 56, 738, 357)
    nodes = [(666,133),(738,104),(811,136),(636,208),(698,197),(777,204),(842,211),(673,280),(744,302),(804,278)]
    for a,b in [(0,1),(1,2),(0,3),(0,4),(1,4),(2,5),(2,6),(3,4),(3,7),(4,5),(4,7),(5,6),(5,8),(5,9),(6,9),(7,8),(8,9)]:
        c += line(*nodes[a], *nodes[b], LINE, 1.5)
    for i, (x,y) in enumerate(nodes):
        c += circle(x,y,5,RED if i in (1,4,8) else INK)
    c += f'<polyline points="{waveform(577,208,322,47)}" fill="none" stroke="{RED}" stroke-width="2.5"/>'
    c += circle(738,104,12,'none',f'stroke="{RED}" class="pulse"')
    c += text(738, 379, 'SIGNAL → KNOWLEDGE → CONNECTION', 12, MUTED, extra='class="mono" text-anchor="middle"')
    c += line(38, 408, 922, 408, INK)
    c += circle(44,439,4,RED,'class="pulse"')
    c += text(58,444,'RESEARCH IN PROGRESS',13,extra='class="mono"')
    c += text(922,444,'STAY CURIOUS. KEEP MOVING.',17,MUTED,extra='text-anchor="end"')
    c = c.replace(INK, '#f3f4f2').replace(MUTED, '#a7ada9').replace(LINE, '#414541').replace(RED, '#ef6b60')
    svg('cover.svg',470,'LittBox — Research & motion',c, '#171a18')


def research():
    c = text(32,38,'CURRENT CURIOSITIES',14,extra='class="mono"')
    c += text(928,38,'CONCEPT SKETCH / NOT EXPERIMENTAL DATA',11,MUTED,extra='class="mono" text-anchor="end"')
    c += line(32,55,928,55,INK)
    c += text(32,94,'01  /  EEG & BCI',22,weight=650)
    c += text(515,94,'02  /  AGENTS × KNOWLEDGE',22,weight=650)
    c += line(479,80,479,365)
    for row, label in enumerate(['Fp1','C3','O1']):
        y=145+row*64
        c += text(32,y+5,label,15,MUTED,extra='class="mono"')
        c += line(88,y,447,y)
        c += f'<polyline points="{waveform(88,y,359,34,row*1.7)}" fill="none" stroke="{RED if row == 1 else INK}" stroke-width="2"/>'
    c += line(273,122,273,293,RED,1.5,'class="pulse"')
    c += text(32,332,'从复杂信号中寻找线索',20)
    c += text(32,361,'SYNTHETIC SIGNAL / ILLUSTRATION ONLY',10,MUTED,extra='class="mono"')
    for x,y,label,sub in [(515,126,'READ','文献'),(656,126,'EXTRACT','实体 / 关系'),(797,126,'VERIFY','证据校验')]:
        c += f'<rect x="{x}" y="{y}" width="126" height="66" rx="3" fill="none" stroke="{LINE}"/>'
        c += text(x+63,y+26,label,14,INK,600,'text-anchor="middle"')
        c += text(x+63,y+49,sub,14,MUTED,extra='text-anchor="middle"')
    c += line(641,159,656,159,RED,2,'class="flow"') + line(782,159,797,159,RED,2,'class="flow"')
    c += '<path d="M860 198 V240 H784" fill="none" stroke="'+RED+'" stroke-width="2" class="flow"/>'
    for a,b in [((606,248),(652,222)),((652,222),(700,252)),((606,248),(645,285)),((645,285),(700,252)),((700,252),(754,278)),((700,252),(756,221))]:
        c += line(*a,*b,INK,1.5)
    for x,y in [(606,248),(652,222),(700,252),(645,285),(754,278),(756,221)]:
        c += circle(x,y,7,RED if x==700 else PAPER,f'stroke="{RED if x==700 else INK}" stroke-width="2"')
    c += text(515,332,'让知识有连接，也有来处',20)
    c += text(515,361,'COLLABORATION / PROVENANCE / GRAPH',10,MUTED,extra='class="mono"')
    svg('research.svg',392,'EEG signals and a conceptual multi-agent knowledge graph workflow',c)


def life():
    c = text(32,34,'BEYOND THE SCREEN',13,extra='class="mono"') + line(32,49,928,49,INK)
    for x in (248,480,712):
        c += line(x,74,x,233)
    c += '<g class="groove">'+circle(129,91,12,'none',f'stroke="{INK}" stroke-width="3"')
    c += f'<path d="M129 105 L119 141 L153 154 L174 182 M120 142 L103 172 L77 177 M126 117 L99 126 L77 108 M126 117 L151 126 L174 106" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>'
    c += f'<path d="M71 188 H185 M70 139 L60 132 M182 142 L193 134" fill="none" stroke="{RED}" stroke-width="2"/>'
    c += line(306,140,422,140,INK,5)
    for x,h in [(312,42),(327,66),(389,66),(404,42)]:
        c += f'<rect x="{x}" y="{140-h/2}" width="12" height="{h}" rx="2" fill="{INK}"/>'
    c += line(354,169,374,169,RED,3)
    c += f'<rect x="550" y="110" width="98" height="65" rx="6" fill="none" stroke="{INK}" stroke-width="3"/>'
    c += f'<path d="M562 110 V102 H584 V110" fill="none" stroke="{INK}" stroke-width="3"/>'
    c += circle(603,143,22,'none',f'stroke="{INK}" stroke-width="3"')+circle(603,143,14,'none',f'stroke="{LINE}" stroke-width="2"')+circle(633,122,3,RED)
    c += f'<rect x="779" y="110" width="105" height="68" rx="2" fill="none" stroke="{INK}" stroke-width="2"/>'
    for x in range(794,884,15):
        c += line(x,111,x,177,INK)
    for x in (789,804,834,849,864):
        c += f'<rect x="{x}" y="110" width="9" height="41" fill="{INK}"/>'
    c += circle(890,98,4,RED,'class="pulse"')
    for x,label,sub in [(132,'GROOVE','HIPHOP / 街舞'),(364,'REPEAT','TRAINING / 健身'),(596,'OBSERVE','STREET / 摄影'),(828,'RESONATE','PIANO & GUITAR')]:
        c += text(x,217,label,19,INK,650,'text-anchor="middle" letter-spacing="2"')
        c += text(x,246,sub,12,MUTED,extra='text-anchor="middle"')
    svg('life.svg',274,'Hiphop dance, training, street photography, piano and guitar',c)


def signature():
    c = line(32,1,928,1,INK)
    c += text(32,58,'THINK DEEP.',30,INK,700,'letter-spacing="-1"')
    c += text(32,99,'MOVE FREE.',30,RED,700,'letter-spacing="-1"')
    c += '<path d="M797 48 C785 33 763 42 770 58 C775 69 797 82 797 82 C797 82 820 67 824 56 C829 40 809 33 797 48 Z" fill="none" stroke="'+RED+'" stroke-width="2" class="pulse"/>'
    c += text(928,107,'LittBox / KEEP IT REAL',15,MUTED,extra='text-anchor="end"')
    svg('signature.svg',133,'Think deep. Move free. LittBox',c)


if __name__ == '__main__':
    from generate_intro import generate_intro
    generate_intro()
    cover()
    research()
    life()
    signature()
