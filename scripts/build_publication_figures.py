"""Regenerate publication figures from the frozen census and survey synthesis.

Run from any working directory. Requires matplotlib and Pillow. No network access.
"""
from pathlib import Path
import collections
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path as CurvePath

BASE = Path(__file__).resolve().parents[1]
DATA = BASE/'data'
with (DATA/'selected_evidence.csv').open(encoding='utf-8-sig') as f:
    STUDY_COUNT = sum(1 for _ in csv.DictReader(f))
OUT = BASE / 'figures'
OUT.mkdir(exist_ok=True)
from figure_palette import NAVY, BLUE, TEAL, RED, AMBER, SLATE, MUTED, BLUE_FILL, TEAL_FILL, RED_FILL, AMBER_FILL, SLATE_FILL, RULE, configure_figure_fonts
configure_figure_fonts()
GREEN, GOLD = TEAL, AMBER

def card(ax, x, y, w, h, text, color=BLUE, fs=10, bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.015,rounding_size=0.12',
                              facecolor=TEAL_FILL if color==TEAL else BLUE_FILL,edgecolor=color,linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,
            color=NAVY,fontweight='bold' if bold else 'normal',linespacing=1.35)

def arrow(ax,a,b):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='-|>',color=SLATE,lw=1.25))

def save(fig, name, tiff=False):
    for ext in ['pdf','png']:
        fig.savefig(OUT/f'{name}.{ext}',facecolor='white')
    if tiff:
        fig.savefig(OUT/f'{name}.tiff',facecolor='white',pil_kwargs={'compression':'tiff_lzw'})
    plt.close(fig)

# The graphical abstract states supported synthesis findings, not a prevalence estimate.
fig,ax=plt.subplots(figsize=(13.28,5.31),dpi=200)
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.01)
ax.set(xlim=(0,13),ylim=(0,5.1));ax.axis('off')
ax.text(6.5,4.82,'LLM and Agent Security in Energy Systems',ha='center',va='center',
        fontsize=29.68,fontweight='bold',color=NAVY)
ax.text(6.5,4.38,'A critical survey of access, authority and evaluation evidence',ha='center',
        fontsize=20.14,color=BLUE)
for x,label in [(2,'1  ACCESS'),(6.5,'2  AUTHORITY'),(11,'3  EVIDENCE')]:
    ax.text(x,3.87,label,ha='center',fontsize=21.2,fontweight='bold',color=NAVY)
card(ax,.2,2.70,3.6,.85,'Injected instructions\nCorrupted tool values',fs=20)
card(ax,.2,1.55,3.6,.85,'Private documents\nModels and tool servers',fs=20)
card(ax,4.65,1.55,3.7,2.0,'Answers\nSandboxed tools\nOperational proposals\nReleased actions',GREEN,20)
card(ax,9.2,2.70,3.6,.85,'Answer errors and leaks\nAuthorized completion',fs=20)
card(ax,9.2,1.55,3.6,.85,'Physical constraint checks\nMismatch and trajectories',fs=19)
arrow(ax,(3.88,2.55),(4.57,2.55));arrow(ax,(8.43,2.55),(9.12,2.55))
ax.text(6.5,1.13,f'Compare {STUDY_COUNT} selected studies without pooling incompatible success rates',
        ha='center',fontsize=19.08,fontweight='bold',color=NAVY)
ax.text(6.5,.70,'Reuse: coding framework | claim guide | metrics | evaluation worksheet',
        ha='center',fontsize=19.08,color=BLUE)
ax.text(6.5,.28,'AI-assisted synthesis; exploratory census and classification sensitivity are documented separately.',
        ha='center',fontsize=14.84,color=MUTED)
save(fig,'graphical_abstract',tiff=True)

rows=list(csv.DictReader((DATA/'evidence_census.csv').open(encoding='utf-8-sig')))
counts=collections.Counter(r['stream'] for r in rows)
order=[('T_energy_llm_threat_or_risk','Threat or risk'),('C_energy_llm_action_control','Action control'),
       ('D_llm_grid_cyber_detection','Grid cyber detection'),('V_energy_llm_safety_benchmark','Benchmark / safe operation'),
       ('E_energy_llm_capability_or_deployment','Capability / deployment'),('R_review_or_perspective','Review / perspective'),
       ('G_general_llm_security','General LLM security'),('B_classical_background','Classical background'),('X_off_topic','Off topic')]
fig,ax=plt.subplots(figsize=(8,4.3),dpi=200)
items=order[::-1]
bars=ax.barh([x[1] for x in items],[counts[x[0]] for x in items],color=BLUE)
for b in bars:ax.text(b.get_width()+.5,b.get_y()+b.get_height()/2,str(int(b.get_width())),va='center',fontsize=9.54)
ax.set_xlim(0,52);ax.set_xlabel('Archived primary-purpose assignments (143 collected records)')
ax.set_title('Exploratory census: counts are not validated eligibility estimates',loc='left',fontsize=10.6)
ax.spines[['top','right']].set_visible(False)
fig.text(.02,.02,'AI-coded collection; benchmark streams may include security tests. Classification sensitivity is discussed in the paper.',fontsize=8.48,color=MUTED)
fig.tight_layout(rect=(0,.05,1,1));save(fig,'evidence_census')

fig,ax=plt.subplots(figsize=(8.1,5.4),dpi=240)
fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.02)
ax.set(xlim=(0,12),ylim=(0,9));ax.axis('off')

def census_card(x,y,w,h,text,edge,fill,fs=9,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,
        boxstyle='round,pad=0.025,rounding_size=0.17',
        facecolor=fill,edgecolor=edge,linewidth=1.25,zorder=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,
        color=NAVY,fontweight='bold' if bold else 'normal',linespacing=1.42,zorder=3)

def census_curve(start,c1,c2,end,color,lw=2):
    # End the curve before the arrowhead. An explicit vertical landing and a
    # fixed downward triangle avoid tangent-based rotation on shallow curves.
    x,y=end
    landing=(x,y+.22)
    path=CurvePath([start,c1,c2,landing,(x,y+.12)],
        [CurvePath.MOVETO,CurvePath.CURVE4,CurvePath.CURVE4,
         CurvePath.CURVE4,CurvePath.LINETO])
    ax.add_patch(PathPatch(path,fill=False,linewidth=lw,color=color,
        capstyle='round',joinstyle='round',zorder=0))
    ax.add_patch(Polygon([(x-.065,y+.17),(x+.065,y+.17),(x,y)],
        closed=True,facecolor=color,edgecolor=color,linewidth=.4,
        joinstyle='round',zorder=1))

streams=[
    (.12,'ARCHIVE',BLUE,BLUE_FILL,
     '13 October 2026\n1,051 candidate rows\n988 screened; 472 PDFs retrieved',
     '104 LLM + energy matches\n+ 1 targeted source\n(EnergyAgentBench)'),
    (4.16,'JOURNAL-INDEXED SEARCH',TEAL,TEAL_FILL,
     'OpenAlex, 15 October 2026\n16 queries; 800 results returned\n693 unique records',
     '52 new keyword matches\n23 added for coding\n29 not added'),
    (8.20,'CITATION CHASING',SLATE,SLATE_FILL,
     'OpenAlex, 15 October 2026\n14 seeds; 437 citing/cited works\n(2023 or later)',
     '49 new keyword matches\n15 added for coding\n34 not added'),
]
for x,title,color,tint,collection,screened in streams:
    ax.add_patch(FancyBboxPatch((x,8.35),3.6,.47,
        boxstyle='round,pad=0.025,rounding_size=0.13',
        facecolor=color,edgecolor='none',zorder=2))
    ax.text(x+1.8,8.585,title,ha='center',va='center',fontsize=9.43,
        fontweight='bold',color='white',zorder=3)
    census_card(x,6.75,3.6,1.35,collection,color,tint,8.8)
    census_card(x,4.65,3.6,1.40,screened,color,tint,9.1)
    mid=x+1.8
    census_curve((mid,6.67),(mid,6.49),(mid,6.31),(mid,6.13),color,1.8)

# Each source enters a separate port; cubic paths turn smoothly without sharp elbows.
census_curve((1.92,4.57),(1.92,4.12),(4.55,4.28),(4.55,3.78),BLUE)
census_curve((5.96,4.57),(5.96,4.31),(5.96,4.04),(5.96,3.78),TEAL)
census_curve((10.00,4.57),(10.00,4.12),(7.37,4.28),(7.37,3.78),SLATE)
census_card(2.7,2.30,6.5,1.40,'', BLUE,BLUE_FILL)
ax.text(5.95,3.28,'143 RECORDS',ha='center',va='center',
    fontsize=16.96,fontweight='bold',color=NAVY,zorder=3)
ax.text(5.95,2.91,'in the frozen exploratory census',ha='center',va='center',
    fontsize=11.02,fontweight='bold',color=NAVY,zorder=3)
ax.text(5.95,2.56,'104 + 1 + 23 + 15; historical AI codes preserved',
    ha='center',va='center',fontsize=9.75,color=NAVY,zorder=3)

census_curve((4.45,2.23),(4.45,1.98),(3.2,2.11),(3.2,1.85),AMBER,1.8)
census_curve((7.45,2.23),(7.45,1.98),(8.8,2.11),(8.8,1.85),SLATE,1.8)
census_card(.55,.43,5.3,1.34,
    'Primary-purpose coding is not eligibility\nBenchmarks may also contain security tests\n13 codes differ from the later AI source pass',
    AMBER,AMBER_FILL,8.6)
census_card(6.15,.43,5.3,1.34,
    f'Source pass: 118 full texts, 25 abstracts\nNo independent human confirmation\nSeparate from the {STUDY_COUNT}-study synthesis',
    SLATE,SLATE_FILL,8.6)
save(fig,'census_flow')
print('Regenerated graphical abstract, census chart and census flow from current sources.')

# Keep Figure 2 reproducible from the same publication build entry point.
import runpy
runpy.run_path(str(Path(__file__).with_name('build_trust_boundary_figure.py')),run_name='__main__')
runpy.run_path(str(Path(__file__).with_name('build_paired_evaluation_figure.py')),run_name='__main__')

# Figure 1 now shares the same palette and is reproducible from this entry point.
runpy.run_path(str(Path(__file__).with_name('build_taxonomy_figure.py')),run_name='__main__')

runpy.run_path(str(Path(__file__).with_name('build_energy_overview_figure.py')),run_name='__main__')
