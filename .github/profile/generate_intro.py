"""Local animated bio and compact technology badges for the profile README."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
# Technologies already represented in the profile and the user's public projects.
BADGES = [
    ('python', 'Python', 64, '#3776ab', '#ffffff'),
    ('javascript', 'JavaScript', 88, '#f7df1e', '#171a18'),
    ('typescript', 'TypeScript', 89, '#3178c6', '#ffffff'),
    ('java', 'Java', 48, '#b43b32', '#ffffff'),
    ('cpp', 'C++', 46, '#315b85', '#ffffff'),
    ('html', 'HTML', 55, '#b64624', '#ffffff'),
    ('css', 'CSS', 46, '#663399', '#ffffff'),
    ('shell', 'Shell', 50, '#385e35', '#ffffff'),
    ('matlab', 'MATLAB', 72, '#a44614', '#ffffff'),
    ('vue', 'Vue 3', 56, '#42b883', '#171a18'),
    ('spring-boot', 'Spring Boot', 96, '#467a20', '#ffffff'),
    ('fastapi', 'FastAPI', 72, '#007d70', '#ffffff'),
    ('uni-app', 'uni-app', 68, '#326b27', '#ffffff'),
    ('neo4j', 'Neo4j', 58, '#245d86', '#ffffff'),
    ('postgresql', 'PostgreSQL', 95, '#336791', '#ffffff'),
]


def generate_intro():
    badges = ROOT / 'badges'
    badges.mkdir(exist_ok=True)
    for slug, label, width, background, foreground in BADGES:
        (badges / f'{slug}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="22" viewBox="0 0 {width} 22" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title>
<rect width="{width}" height="22" rx="3" fill="{background}"/>
<text x="{width/2}" y="15" text-anchor="middle" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11" fill="{foreground}">{escape(label)}</text>
</svg>
''', encoding='utf-8')
    (ROOT / 'bio.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="116" viewBox="0 0 700 116" role="img" aria-labelledby="bio-title bio-desc">
<title id="bio-title">LittBox / 软件工程在读，持续探索中。</title>
<desc id="bio-desc">云南大学 · 软件工程专业 · 大三在读。居中的纯色打字动画。</desc>
<style>
text { font-family: -apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif; }
.reveal { animation: type 12s steps(32,end) infinite; }
.cursor { animation: blink 1.2s step-end infinite; }
@keyframes type { 0% { width: 0; } 28%,92% { width: 640px; } 100% { width: 0; } }
@keyframes blink { 0%,49% { opacity: 1; } 50%,100% { opacity: 0; } }
@media (prefers-reduced-motion:reduce) { .reveal { animation:none; width:640px; } .cursor { animation:none; opacity:1; } }
</style>
<defs><clipPath id="typing"><rect class="reveal" x="30" y="18" width="640" height="39"/></clipPath></defs>
<text x="350" y="46" text-anchor="middle" font-size="25" font-weight="650" fill="#df6257" clip-path="url(#typing)">LittBox / 软件工程在读，持续探索中。</text>
<text x="350" y="79" text-anchor="middle" font-size="19" fill="#389a88">云南大学 · 软件工程专业 · 大三在读。</text>
<path d="M310 102 H382" stroke="#598fce" stroke-width="2"/>
<path class="cursor" d="M387 97 V107" stroke="#df6257" stroke-width="2"/>
</svg>
''', encoding='utf-8')


if __name__ == '__main__':
    generate_intro()
