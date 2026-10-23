"""Regenerate Figure 1 with the shared palette; preserve its coding content and geometry."""
from pathlib import Path
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from figure_palette import NAVY, BLUE, TEAL, AMBER, SLATE, MUTED, BLUE_FILL, TEAL_FILL, AMBER_FILL, SLATE_FILL, configure_figure_fonts
configure_figure_fonts()

OUT=Path(__file__).resolve().parents[1]/'figures'
dimensions=[
    ('Surface S',['Model / artifact','User / retrieved input','Numerical data','Tool metadata / output','Human workflow']),
    ('Mechanism M',['Instruction redirection','Numerical corruption','Poisoning / backdoor','Disclosure','Non-adversarial error']),
    ('Attacker control C',['Query-only access','Content insertion','Tool / server control','Training / artifact control','No adversary / NR']),
    ('Authority A',['A0: advisory answer','A1: sandbox / simulation','A2: operational proposal','A3: real execution','Code evaluated authority']),
    ('Consequence K',['Task / answer failure','Privacy disclosure','Financial error','Physical violation','Service / equipment impact'])]

fig,ax=plt.subplots(figsize=(10,5.2));ax.axis('off');ax.set_xlim(0,25);ax.set_ylim(0,11.7)
def box(x,y,w,h,text,fill,edge,color=NAVY,bold=False,fs=11.1):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04,rounding_size=0.055',
        facecolor=fill,edgecolor=edge,linewidth=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,
        color=color,fontweight='bold' if bold else 'normal')

box(.25,10.1,24.5,.85,'Classification record: surface | mechanism | control | authority | consequence; evidence',
    NAVY,NAVY,'white',True,11)
colors=[(BLUE,BLUE_FILL),(BLUE,BLUE_FILL),(BLUE,BLUE_FILL),(TEAL,TEAL_FILL),(AMBER,AMBER_FILL)]
for i,((name,values),(accent,tint)) in enumerate(zip(dimensions,colors)):
    x=.25+i*5.0
    box(x,8.65,4.5,.85,name,accent,accent,'white',True)
    for j,label in enumerate(values):
        box(x,7.4-j*1.15,4.5,.86,textwrap.fill(label,width=22),tint,accent)
box(.25,1.25,24.5,.86,'Evidence E: conceptual (E0) | text (E1) | tools (E2) | physics simulation (E3) | operation (E4)',
    SLATE_FILL,SLATE,fs=10.6)
ax.text(12.5,.35,'Record measured and possible consequences separately. Evidence codes describe test outcomes, not study quality.\n'
    'Multiple codes are allowed; NR = not recorded / not established. This framework is a survey synthesis.',
    ha='center',fontsize=10.6,color=MUTED)
ax.set_title('Independent dimensions for energy LLM security evidence',fontsize=12.72,fontweight='bold',color=NAVY)
fig.tight_layout()
for ext in ['pdf','png']:fig.savefig(OUT/f'taxonomy_tree.{ext}',dpi=240,bbox_inches='tight',facecolor='white')
plt.close(fig)
print('Redrew coding framework with the shared publication palette.')
