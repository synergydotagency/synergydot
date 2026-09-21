from pathlib import Path
from PIL import Image, ImageChops
import pypdfium2 as pdf
import json, re

base=Path('C:/Users/Aspire/Desktop/Branding Projects')
out=Path('assets/projects'); out.mkdir(exist_ok=True)
books=[('chameleon',base/'Chameleon Seasonings/cameleon branding.pdf'),('pixi',base/'pixi/pixi branding.pdf')]
for slug,source in books:
    doc=pdf.PdfDocument(str(source))
    for i,page in enumerate(doc):
        im=page.render(scale=1600/page.get_width()).to_pil().convert('RGB')
        im.save(out/f'{slug}-{i+1}.jpg',quality=86,optimize=True)

logos=[('dot-academy','Dot Academy/logo dot academy-01.jpg'),('orlune','Albushja/Orlune-01.png'),('grow-academy','Grow Academy/GrowAcademy Logo vector-02.jpg'),('nazi-fert','Nazi Fert/LOGO AI-01.jpg'),('street-myth','Street Myths/logo01-01.png')]
for slug,source in logos:
    src=Image.open(base/source).convert('RGBA')
    im=Image.new('RGB',src.size,'white'); im.paste(src,mask=src.getchannel('A'))
    bg=im.getpixel((0,0))
    diff=ImageChops.difference(im,Image.new('RGB',im.size,bg)).convert('L').point(lambda p:255 if p>35 else 0)
    bounds=diff.getbbox()
    mark=im.crop(bounds) if bounds else im
    mark.thumbnail((1080,540),Image.Resampling.LANCZOS)
    canvas=Image.new('RGB',(1400,1000),bg)
    canvas.paste(mark,((1400-mark.width)//2,(1000-mark.height)//2))
    canvas.save(out/f'{slug}.jpg',quality=90,optimize=True)
svg=(base/'Hostera/logo/hostera logo-01.svg').read_text(encoding='utf-8')
if re.search(r'<script|<foreignObject|(?:href|src)\s*=\s*["\'](?:https?:|javascript:)',svg,re.I):raise ValueError('Unexpected active SVG content')
(out/'hostera.svg').write_text(svg,encoding='utf-8')

projects=[
dict(slug='chameleon',name='Chameleon Seasonings',category='Brand identity & packaging',type='Branding',industry='Food & seasonings',image='projects/chameleon-4.jpg',intro='A vibrant identity built around transformation, versatility and the world of flavor.',description='The chameleon becomes the central symbol of a seasoning brand shaped by variety. Color distinguishes the blends, while a consistent logo system connects packaging, stationery and physical brand applications.',deliverables=['Logo & color system','Packaging design','Stationery & brand applications'],gallery=[dict(image=f'projects/chameleon-{i}.jpg',alt=t) for i,t in [(1,'Chameleon Seasonings identity and chameleon imagery'),(3,'Color-coded Chameleon logo variations'),(5,'Chameleon branded identification cards'),(6,'Chameleon glass signage application'),(7,'Chameleon stationery collection'),(8,'Chameleon phone case applications'),(9,'Chameleon environmental branding')]]),
dict(slug='pixi',name='Pixi',category='Brand identity & art direction',type='Branding',industry='Creative agency',image='projects/pixi-3.jpg',intro='A playful digital identity with room for creativity.',description='Square-based letterforms connect the identity to pixels and the digital world. The open space within the wordmark creates room for expression, while the dots represent communication and collaboration. Blue anchors a lively palette of yellow, pink and turquoise.',deliverables=['Logo design','Visual identity system','Stationery & digital applications'],gallery=[dict(image=f'projects/pixi-{i}.jpg',alt=t) for i,t in [(1,'Pixi logo and colorful visual elements'),(2,'Pixi logo construction and brand storytelling'),(4,'Pixi social media brand application'),(5,'Pixi exterior signage application')]]),
dict(slug='hostera',name='Hostera Group',category='Logo design',image='projects/hostera.svg',intro='An elegant identity in black and gold.',description='Fine serif letterforms and a restrained gold secondary line give the Hostera Group wordmark a composed, refined presence.'),
dict(slug='orlune',name='Orlune',category='Logo design',image='projects/orlune.jpg',intro='Expressive letterforms. A character all its own.',description='A distinctive black wordmark with sculptural curves, playful proportions and a confident silhouette.'),
dict(slug='dot-academy',name='Dot Academy',category='Logo design',image='projects/dot-academy.jpg',intro='Connected dots. A shared identity.',description='A geometric arrangement of open and filled circles pairs with a clear wordmark. The red accent and “By Synergy Dot” signature connect the academy to the parent brand.'),
dict(slug='grow-academy',name='Grow Academy',category='Logo design',image='projects/grow-academy.jpg',intro='A clear identity with the energy to grow.',description='Connected green shapes and contrasting typographic weights form a recognizable identity against a deep blue background.'),
dict(slug='nazi-fert',name='Nazi Fert',category='Logo design',image='projects/nazi-fert.jpg',intro='A bold mark built from precise geometry.',description='Blue and yellow triangular elements create a sharp symbol, paired with a wordmark that balances light and bold lettering.'),
dict(slug='street-myth',name='Street Myth',category='Logo design',image='projects/street-myth.jpg',intro='A wordmark with an independent spirit.',description='Soft curves and expressive serif details create a distinctive typographic signature in charcoal black.')
]
for p in projects:
    p.setdefault('type','Visual identity'); p.setdefault('industry','Logo collection'); p.setdefault('deliverables',['Logo design']); p.setdefault('gallery',[]); p['alt']=p['name']+' — '+p['category']
Path('projects.json').write_text(json.dumps(projects,indent=2,ensure_ascii=False),encoding='utf-8')
print('Prepared 8 projects and optimized portfolio imagery.')
