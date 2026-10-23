"""Draw Figure 2 as a vector diagram with explicit information and release paths."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path as CurvePath

OUT=Path(__file__).resolve().parents[1]/'figures'
from figure_palette import NAVY, BLUE, TEAL, RED, AMBER, SLATE, MUTED, BLUE_FILL, TEAL_FILL, RED_FILL, AMBER_FILL, SLATE_FILL, RULE, configure_figure_fonts
configure_figure_fonts()
fig,ax=plt.subplots(figsize=(11.0,5.5),dpi=240)
fig.subplots_adjust(left=.012,right=.988,top=.99,bottom=.025)
ax.set(xlim=(0,16),ylim=(0,8.2));ax.axis('off')

def panel(x,y,w,h,title,detail,color,tint):
    ax.add_patch(FancyBboxPatch((x,y),w,h,
        boxstyle='round,pad=0.025,rounding_size=0.17',
        facecolor=tint,edgecolor=color,linewidth=1.3,zorder=2))
    if detail:
        ax.text(x+w/2,y+h*.77,title,ha='center',va='center',fontsize=14.84,
            fontweight='bold',color=color,zorder=3)
        ax.text(x+w/2,y+h*.35,detail,ha='center',va='center',fontsize=12.72,
            color=NAVY,linespacing=1.35,zorder=3)
    else:
        ax.text(x+w/2,y+h/2,title,ha='center',va='center',fontsize=14.31,
            fontweight='bold',color=color,zorder=3)

def flow(start,c1,c2,end,color,direction='right'):
    # Fixed cardinal arrowheads follow a short straight landing, never a spline tangent.
    ux,uy={'right':(1,0),'down':(0,-1),'up':(0,1)}[direction]
    x,y=end
    landing=(x-.22*ux,y-.22*uy)
    shaft_end=(x-.10*ux,y-.10*uy)
    path=CurvePath([start,c1,c2,landing,shaft_end],
        [CurvePath.MOVETO,CurvePath.CURVE4,CurvePath.CURVE4,CurvePath.CURVE4,CurvePath.LINETO])
    ax.add_patch(PathPatch(path,fill=False,lw=1.8,color=color,
        capstyle='round',joinstyle='round',zorder=0))
    bx,by=x-.17*ux,y-.17*uy
    px,py=-uy*.065,ux*.065
    ax.add_patch(Polygon([(bx+px,by+py),(bx-px,by-py),(x,y)],closed=True,
        facecolor=color,edgecolor=color,lw=.4,joinstyle='round',zorder=1))

for x,w,label,color in [(.25,3.0,'1  INPUTS',BLUE),(4.4,2.9,'2  REASONING',BLUE),
                         (8.6,3.0,'3  AUTHORIZATION',TEAL),(12.8,2.9,'4  ACTION',SLATE)]:
    ax.add_patch(FancyBboxPatch((x,7.55),w,.45,
        boxstyle='round,pad=0.025,rounding_size=0.12',facecolor=color,edgecolor='none'))
    ax.text(x+w/2,7.775,label,ha='center',va='center',fontsize=12.4,fontweight='bold',color='white')

panel(.25,4.75,3.0,1.30,'Authorized task','Operator intent / role',TEAL,TEAL_FILL)
panel(.25,2.80,3.0,1.50,'Untrusted inputs','Documents / tool returns\nInstructions or values',RED,RED_FILL)
panel(4.4,3.5,2.9,1.6,'LLM / agent','Retrieval, reasoning\nand tool proposals',BLUE,BLUE_FILL)
panel(4.4,6.0,2.9,1.05,'Answer /\ndata output','',AMBER,AMBER_FILL)
panel(8.6,3.5,3.0,1.6,'Release controls','Authorization policy\nPhysical constraints',TEAL,TEAL_FILL)
panel(8.6,6.0,3.0,1.05,'Trusted reference','State, topology, ratings',SLATE,SLATE_FILL)
panel(12.8,3.5,2.9,1.6,'Action channel','Sandbox or operation\nRecord actual authority',SLATE,SLATE_FILL)
panel(8.6,1.45,3.0,1.05,'Block / escalate','Log decision and reason',AMBER,AMBER_FILL)

# Input trust is explicitly separate from the action release decision.
ax.plot([3.83,3.83],[2.7,6.25],color=RED,lw=1.15,
        linestyle=(0,(4,4)),alpha=.65,zorder=0)
ax.text(3.83,2.40,'Input trust\nboundary',ha='center',va='top',fontsize=11.13,color=RED)
flow((3.32,5.4),(3.70,5.4),(3.76,4.65),(4.32,4.65),TEAL)
flow((3.32,3.55),(3.70,3.55),(3.76,3.98),(4.32,3.98),RED)
flow((5.85,5.18),(5.85,5.4),(5.85,5.55),(5.85,5.92),AMBER,'up')
ax.text(6.16,5.55,'Disclosure\nchecks',ha='left',va='center',fontsize=11.34,color=AMBER)
flow((7.38,4.3),(7.68,4.3),(7.90,4.3),(8.52,4.3),BLUE)
ax.text(7.95,3.88,'Proposal',ha='center',fontsize=11.34,color=BLUE)
flow((10.1,5.92),(10.1,5.70),(10.1,5.50),(10.1,5.18),SLATE,'down')
flow((11.68,4.3),(12.0,4.3),(12.20,4.3),(12.72,4.3),TEAL)
ax.text(12.2,3.88,'Release',ha='center',fontsize=11.34,color=TEAL)
flow((10.1,3.42),(10.1,3.2),(10.1,2.95),(10.1,2.58),AMBER,'down')
ax.text(1.75,1.65,'Retrieval access and source\nchecks apply before content\nreaches the agent.',
        ha='center',va='center',fontsize=11.13,color=NAVY,linespacing=1.4)
ax.text(8,.46,'Proposed pattern: separate information disclosure from action release.\nProtection depends on enforcement and trusted-reference fidelity.',
        ha='center',va='center',fontsize=12.19,color=MUTED,linespacing=1.4)
for ext in ['pdf','png']:
    fig.savefig(OUT/f'trust_boundary_architecture.{ext}',facecolor='white')
plt.close(fig)
print('Redrew trust-boundary figure: trust boundaries, disclosure and action release.')
