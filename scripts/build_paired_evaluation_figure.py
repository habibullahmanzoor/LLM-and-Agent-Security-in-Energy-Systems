"""Draw Figure 4: four paired conditions and shared independent outcome checks."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

OUT=Path(__file__).resolve().parents[1]/'figures'
from figure_palette import NAVY, BLUE, TEAL, RED, AMBER, SLATE, MUTED, BLUE_FILL, TEAL_FILL, RED_FILL, AMBER_FILL, SLATE_FILL, RULE, configure_figure_fonts
configure_figure_fonts()
fig,ax=plt.subplots(figsize=(11.0,5.67),dpi=240)
fig.subplots_adjust(left=.012,right=.988,top=.985,bottom=.02)
ax.set(xlim=(0,15),ylim=(0,8.25));ax.axis('off')

def box(x,y,w,h,color,fill,shadow=True):
    ax.add_patch(FancyBboxPatch((x,y),w,h,
        boxstyle='round,pad=0.025,rounding_size=0.17',
        facecolor=fill,edgecolor=color,lw=1.25,zorder=2))

def triangle(tip,unit,color,size=.14):
    x,y=tip;ux,uy=unit;bx,by=x-size*ux,y-size*uy
    px,py=-uy*size*.43,ux*size*.43
    ax.add_patch(Polygon([(bx+px,by+py),(bx-px,by-py),(x,y)],
        facecolor=color,edgecolor=color,lw=.4,joinstyle='round',zorder=4))

def comparison(a,b,color=SLATE):
    dx,dy=b[0]-a[0],b[1]-a[1];length=(dx*dx+dy*dy)**.5;ux,uy=dx/length,dy/length
    ax.plot([a[0]+ux*.10,b[0]-ux*.10],[a[1]+uy*.10,b[1]-uy*.10],
        color=color,lw=1.8,solid_capstyle='round',zorder=3)
    triangle(a,(-ux,-uy),color);triangle(b,(ux,uy),color)

box(.30,6.70,14.25,1.14,BLUE,BLUE_FILL)
ax.text(7.425,7.51,'HOLD THE EVALUATION CONDITIONS FIXED',ha='center',va='center',
    fontsize=16.96,fontweight='bold',color=BLUE,zorder=3)
ax.text(7.425,7.08,'Same tasks, model, tools, data snapshot and access budgets.\nDisclose adaptive attack optimization separately.',
    ha='center',va='center',fontsize=12.19,color=NAVY,linespacing=1.3,zorder=3)

# The group boundary makes clear that the same checks apply to every condition.
box(.16,1.13,8.65,4.36,RULE,SLATE_FILL,False)
for x,label in [(.35,'ATTACK ABSENT'),(4.9,'ATTACK PRESENT')]:
    ax.add_patch(FancyBboxPatch((x,5.72),3.6,.43,
        boxstyle='round,pad=0.025,rounding_size=0.12',facecolor=NAVY,edgecolor='none',zorder=2))
    ax.text(x+1.8,5.935,label,ha='center',va='center',fontsize=12.19,
        fontweight='bold',color='white',zorder=3)

def condition(x,y,title,defense,attack,color,fill):
    box(x,y,3.6,1.65,color,fill)
    ax.text(x+1.8,y+1.23,title,ha='center',va='center',fontsize=15.9,
        fontweight='bold',color=color,zorder=3)
    ax.text(x+1.8,y+.63,f'Defense {defense}\nAttack {attack}',ha='center',va='center',
        fontsize=13.14,color=NAVY,linespacing=1.4,zorder=3)

condition(.35,3.65,'Clean','OFF','absent',BLUE,BLUE_FILL)
condition(4.9,3.65,'Attacked','OFF','present',RED,RED_FILL)
condition(.35,1.35,'Defended-clean','ON','absent',TEAL,TEAL_FILL)
condition(4.9,1.35,'Defended-attacked','ON','present',TEAL,TEAL_FILL)
comparison((4.03,4.475),(4.82,4.475))
comparison((4.03,2.175),(4.82,2.175))
comparison((2.15,3.57),(2.15,3.08),TEAL)
comparison((6.70,3.57),(6.70,3.08),TEAL)

box(9.8,1.35,4.75,3.95,SLATE,SLATE_FILL)
ax.add_patch(FancyBboxPatch((9.8,5.72),4.75,.43,
    boxstyle='round,pad=0.025,rounding_size=0.12',facecolor=SLATE,edgecolor='none',zorder=2))
ax.text(12.175,5.935,'INDEPENDENT CHECKS',ha='center',va='center',fontsize=12.19,
    fontweight='bold',color='white',zorder=3)
ax.text(12.175,4.87,'APPLY TO ALL FOUR CONDITIONS',ha='center',va='center',fontsize=11.66,
    fontweight='bold',color=SLATE,zorder=3)
checks=['Task quality and authorization','Attacker goal and protected data','Physical state and action sequence']
for i,line in enumerate(checks):
    y=4.24-i*.66
    ax.add_patch(plt.Circle((10.14,y),.045,facecolor=SLATE,edgecolor='none',zorder=3))
    ax.text(10.37,y,line,ha='left',va='center',fontsize=11.77,color=NAVY,zorder=3)
    if i<2:ax.plot([10.10,14.22],[y-.32,y-.32],color=RULE,lw=.8,zorder=3)
ax.text(12.175,1.94,'Log blocks, aborts\nand missing outcomes.',ha='center',va='center',
    fontsize=12.3,fontweight='bold',color=SLATE,linespacing=1.35,zorder=3)
ax.plot([8.89,9.60],[3.325,3.325],lw=1.9,color=SLATE,solid_capstyle='round',zorder=3)
triangle((9.72,3.325),(1,0),SLATE)

ax.text(7.425,.75,'Horizontal links compare attack effects; vertical links compare defense effects.',
    ha='center',va='center',fontsize=12.08,color=NAVY)
ax.text(7.425,.36,'Report protection AND utility: counts, denominators, uncertainty, cost and failure traces.\nLinks indicate paired comparisons, not a sequence of agent actions.',
    ha='center',va='center',fontsize=11.24,color=MUTED,linespacing=1.3)
for ext in ['pdf','png']:
    fig.savefig(OUT/f'paired_evaluation_design.{ext}',facecolor='white')
plt.close(fig)
print('Redrew paired-evaluation figure: four conditions, paired comparisons and shared checks.')
