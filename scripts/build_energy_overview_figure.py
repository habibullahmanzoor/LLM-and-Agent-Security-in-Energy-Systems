"""Vector overview: information, transformer agent and an illustrative energy network."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Circle,Polygon,PathPatch
from matplotlib.path import Path as MP
from figure_palette import *
configure_figure_fonts()
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
OUT=Path(__file__).resolve().parents[1]/'figures'
# Light canvas, coordinated tinted panels and dark readable ink.
INK = '#18344D'
DARK_BLUE = '#B9CEDF'
DARK_TEAL = '#9CCDBF'
DARK_SLATE = '#D3DEE6'
LIGHT_TEXT = INK
SOFT_TEXT = '#4D6578'
CANVAS = '#FFFFFF'
BLUE = '#2C6096'
TEAL = '#237A70'
SLATE = '#52677E'
MUTED = SOFT_TEXT
BLUE_FILL = '#ACC9E0'
TEAL_FILL = '#A6CFC2'
SLATE_FILL = '#B3C6D6'

fig,ax=plt.subplots(figsize=(11.5,6.8),dpi=260,facecolor=CANVAS)
fig.subplots_adjust(left=.012,right=.988,top=.985,bottom=.015)
ax.set(xlim=(0,16),ylim=(0,8.5));ax.axis('off')
def txt(x,y,s,fs=12,b=False,c=LIGHT_TEXT,ha='center'):
 ax.text(x,y,s,ha=ha,va='center',fontsize=fs,weight='bold'if b else'normal',color=c,linespacing=1.25,zorder=8)
def line(points,c=SLATE,lw=1.5,z=5):
 ax.plot(*zip(*points),c=c,lw=lw,solid_capstyle='round',solid_joinstyle='round',zorder=z)
def card(x,y,w,h,fill='white',edge=RULE,r=.16,shadow=False):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=.02,rounding_size={r}',fc=fill,ec=edge,lw=1.1,zorder=3))
def arrow(a,b,c=BLUE,lw=1.8):
 ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='-|>',color=c,lw=lw,shrinkA=3,shrinkB=3,mutation_scale=12),zorder=6)
def curve(a,c1,c2,b,col=TEAL):
 ax.add_patch(PathPatch(MP([a,c1,c2,b],[MP.MOVETO,MP.CURVE4,MP.CURVE4,MP.CURVE4]),fc='none',ec=col,lw=1.7,capstyle='round',zorder=4))
def disk(x,y,kind,col=TEAL,r=.43):
 ax.add_patch(Circle((x,y),r,fc=('#85ADCF' if kind in ['person','doc','data'] else '#90BDAF'),ec='none',lw=0,zorder=3))
 if kind=='wind':
  line([(x,y-.29),(x,y+.10)],col)
  for a in [90,210,330]:
   t=math.radians(a);line([(x,y+.10),(x+.27*math.cos(t),y+.10+.27*math.sin(t))],col,2)
 elif kind=='solar':
  ax.add_patch(Polygon([(x-.28,y-.12),(x+.23,y-.12),(x+.30,y+.17),(x-.21,y+.17)],fc=BLUE_FILL,ec=col,lw=1.4,zorder=6))
  line([(x,y-.12),(x,y-.27),(x-.17,y-.27),(x+.17,y-.27)],col)
  line([(x-.17,y+.02),(x+.26,y+.02)],col,1)
  line([(x-.03,y-.12),(x+.03,y+.17)],col,1)
 elif kind=='grid':
  line([(x-.23,y-.30),(x,y+.31),(x+.23,y-.30)],col)
  for yy,ww in [(y+.14,.23),(y-.03,.28),(y-.21,.18)]:line([(x-ww,yy),(x+ww,yy)],col)
  line([(x-.14,y-.19),(x+.13,y+.10),(x-.10,y+.10),(x+.18,y-.19)],col,1)
 elif kind=='building':
  card(x-.23,y-.29,.46,.58,SLATE_FILL,col,.025)
  for dx in [-.12,.07]:
   for dy in [-.08,.12]:ax.add_patch(plt.Rectangle((x+dx,y+dy),.09,.10,fc=col,zorder=7))
 elif kind=='battery':
  card(x-.28,y-.18,.52,.36,TEAL_FILL,col,.04)
  line([(x+.25,y-.07),(x+.31,y-.07),(x+.31,y+.07),(x+.25,y+.07)],col)
  line([(x-.17,y),(x-.05,y)],col);line([(x-.11,y-.06),(x-.11,y+.06)],col)
  line([(x+.08,y),(x+.18,y)],col)
 elif kind=='ev':
  card(x-.28,y-.12,.56,.25,BLUE_FILL,col,.06)
  line([(x-.20,y+.14),(x-.11,y+.27),(x+.12,y+.27),(x+.23,y+.14)],col)
  for dx in [-.17,.17]:ax.add_patch(Circle((x+dx,y-.16),.065,fc=col,zorder=7))
 elif kind=='doc':
  card(x-.18,y-.25,.36,.50,BLUE_FILL,col,.025)
  for yy in [-.12,0,.12]:line([(x-.11,y+yy),(x+.11,y+yy)],col,1.1)
 elif kind=='data':
  for dx,h in [(-.21,.15),(-.05,.32),(.11,.43)]:ax.add_patch(plt.Rectangle((x+dx,y-.23),.10,h,fc=col,zorder=7))
 elif kind=='person':
  ax.add_patch(Circle((x,y+.13),.115,fc=BLUE_FILL,ec=col,lw=1.3,zorder=7))
  curve((x-.23,y-.23),(x-.22,y+.02),(x+.22,y+.02),(x+.23,y-.23),col)
# Three comparable panels; caption supplies the overall title.
for x,label,color in [(2.0,'Information sources',BLUE),(6.70,'LLM and agent',TEAL),(13.12,'Energy applications',SLATE)]:
 txt(x,8.08,label,14,True,color)
 line([(x-1.65,7.76),(x+1.65,7.76)],RULE,1)
# Source cards, with recognizable document/data/user glyphs
for y,t,d,k in [(6.48,'Operator intent','Task and permissions','person'),(5.08,'Documents','Standards / manuals','doc'),(3.68,'Operational data','SCADA and forecasts','data')]:
 card(.30,y,3.35,1.12,DARK_BLUE,DARK_BLUE,shadow=True);disk(.88,y+.56,k,'#275D9F',.33)
 txt(1.39,y+.76,t,13,True,LIGHT_TEXT,ha='left');txt(1.39,y+.35,d,11.5,c=SOFT_TEXT,ha='left')
# Merge source routes to a common context line
for y in [7.04,5.64,4.24]:line([(3.68,y),(4.0,y)],BLUE,1.25)
line([(4,4.24),(4,7.04)],BLUE,1.25);arrow((4,5.64),(4.62,5.64),BLUE)
txt(4.18,7.37,'Context',11.5,c=BLUE)
txt(2,3.24,'Documents support RAG',11.5,c=BLUE)
# Model, visually rendered as a chip with stacked transformer layers
card(4.73,3.94,3.94,3.56,DARK_TEAL,DARK_TEAL,.25,True)
txt(6.7,7.12,'Transformer LLM',14,True,LIGHT_TEXT)
txt(6.7,6.76,'Decoder-only model',11.5,c=SOFT_TEXT)
card(5.08,6.06,3.24,.44,'#CDE5DB','#B4CDC4',.07);txt(6.7,6.28,'Embeddings + positions',12,c=NAVY)
# repeated blocks as an inset stack, grouping attention and feed-forward layers
card(5.23,4.89,2.98,.94,'#CDE5DB',TEAL,.10)
card(5.15,4.97,2.98,.94,'#CDE5DB',TEAL,.10)
card(5.07,5.05,2.98,.94,'#CDE5DB',TEAL,.10)
txt(6.56,5.68,'Masked self-attention',12,True,TEAL)
line([(5.28,5.46),(7.86,5.46)],RULE,1)
txt(6.56,5.25,'Feed-forward network',12,c=NAVY)
arrow((6.7,6.06),(6.7,5.97),TEAL)
txt(8.39,5.45,'× N',11.5,True,LIGHT_TEXT)
arrow((6.7,4.90),(6.7,4.73),TEAL)
card(5.08,4.23,3.24,.48,'#CDE5DB','#B4CDC4',.07);txt(6.7,4.47,'Text or tool request',12,c=NAVY)
# Agent loop
card(4.73,2.28,3.94,1.02,DARK_BLUE,DARK_BLUE,.18,True)
txt(6.7,2.96,'External tools',13.2,True,LIGHT_TEXT);txt(6.7,2.53,'Retrieval / power flow',11.5,c=SOFT_TEXT)
arrow((5.90,3.94),(5.90,3.30),BLUE);arrow((7.48,3.30),(7.48,3.94),TEAL)
txt(5.30,3.62,'Request',11.5,c=BLUE);txt(8.10,3.62,'Result',11.5,c=TEAL)
# Illustrated energy network; lines indicate relationships rather than physical dispatch routes
ax.add_patch(FancyBboxPatch((10.58,2.25),5.08,5.26,boxstyle='round,pad=.03,rounding_size=.30',fc=DARK_SLATE,ec='none',zorder=1))
hub=(13.12,4.90)
nodes=[(11.52,6.61,'wind','Generation'),(14.74,6.61,'solar','Solar / DERs'),(11.52,4.76,'grid','Power grid'),(14.74,4.76,'building','Buildings'),(11.52,2.98,'battery','Storage'),(14.74,2.98,'ev','EV charging')]
for x,y,k,l in nodes:
 ax.plot([hub[0],x],[hub[1],y],color='#8299AA',lw=1.25,ls=(0,(3,3)),zorder=2)
for x,y,k,l in nodes:disk(x,y,k,'#52677E' if k in ['grid','building']else '#14756D');txt(x,y-.64,l,11.5,True,LIGHT_TEXT)
ax.add_patch(Circle(hub,.61,fc=TEAL,ec='#A1C9BE',lw=2,zorder=5));txt(*hub,'Energy\noperations',11.7,True,'white')
txt(13.12,7.25,'Analysis and operational support',11.5,c=SOFT_TEXT)
# Advice and operational release are distinct paths, not one ambiguous arrow.
arrow((8.69,6.28),(10.50,6.28),BLUE)
txt(9.60,6.66,'Advice',11.5,True,BLUE)
arrow((8.69,4.91),(9.30,4.91),TEAL)
ax.add_patch(Circle((9.63,4.91),.27,fc='#C0DFD2',ec=TEAL,lw=1.35,zorder=5))
line([(9.49,4.91),(9.59,4.81),(9.79,5.04)],TEAL,1.7,z=6)
arrow((9.94,4.91),(10.50,4.91),TEAL)
txt(9.60,5.48,'Action release',11.5,True,TEAL)
txt(9.60,4.18,'Permission +\nphysical checks',11.5,c=TEAL)
# Compact lower ribbon ties the overview to the survey structure
for x,w,t,d,c,fill in [(.30,4.90,'Attack surfaces','Inputs / retrieval / models / tools','#A05245','#DBB3A8'),(5.55,4.90,'Defenses and governance','Permissions / checks / oversight',TEAL,DARK_TEAL),(10.80,4.90,'Evaluation outcomes','Quality / privacy / constraints',BLUE,DARK_BLUE)]:
 card(x,.53,w,1.05,fill,'none',.16)
 line([(x+.16,.72),(x+.16,1.39)],c,3)
 txt(x+.38,1.23,t,12.5,True,LIGHT_TEXT,ha='left');txt(x+.38,.83,d,11.5,c=SOFT_TEXT,ha='left')
txt(8,.17,'Arrows: information or release paths. Dashed links: application associations, not electrical connections.',11.5,c=MUTED)
for ext in ['pdf','png']:fig.savefig(OUT/f'energy_llm_overview.{ext}',facecolor=CANVAS)
plt.close(fig)
print('Built graphical survey overview with explicit paths, release checks and energy applications.')
