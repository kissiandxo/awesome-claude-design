#!/usr/bin/env python3
"""Render a PNG preview of the budget (mirrors the spreadsheet's computed values)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

NAVY = "#1F3864"; BLUE = "#2E5496"; LBLUE = "#D9E1F2"
GREEN = "#C6E0B4"; AMBER = "#FFF2CC"; GREY = "#F2F2F2"

FACT = {"Weekly":52,"Fortnightly":26,"Monthly":12,"Quarterly":4,
        "Half-yearly":2,"Annually":1,"One-off":1}

INCOME = [("Business income / revenue","Annually",100000),
          ("Other income","Annually",0)]
SECTIONS = [
    ("VEHICLE COSTS", [
        ("Servicing & logbook","Quarterly",375),
        ("Tyres","Annually",1200),
        ("Fuel","Weekly",80),
        ("Registration & CTP","Annually",850),
        ("Vehicle insurance","Monthly",120),
        ("Repairs & maintenance","Annually",800)]),
    ("SUBSCRIPTIONS", [
        ("ServiceM8 (job management)","Monthly",99),
        ("Xero (accounting)","Monthly",70)]),
    ("BUSINESS COSTS & LICENSING", [
        ("Public liability insurance","Annually",1100),
        ("Business name registration","Annually",60),
        ("Trade licence / certification","Annually",350),
        ("Phone & internet","Monthly",110),
        ("Tools & equipment","Annually",2000),
        ("Marketing & advertising","Monthly",150),
        ("Bank & merchant fees","Monthly",40)]),
]

def ann(amount, freq): return amount * FACT[freq]

# ---- compute -----------------------------------------------------------------
income_ann = sum(ann(a,f) for _,f,a in INCOME)
cat_tot = []
rows = []  # (kind, name, freq, monthly, annual)
rows.append(("section","INCOME","",None,None))
for n,f,a in INCOME:
    rows.append(("item",n,f,ann(a,f)/12,ann(a,f)))
rows.append(("subtotal","TOTAL INCOME","",income_ann/12,income_ann))
for sec,items in SECTIONS:
    rows.append(("section",sec,"",None,None))
    s=0
    for n,f,a in items:
        av=ann(a,f); s+=av
        rows.append(("item",n,f,av/12,av))
    rows.append(("subtotal",f"Subtotal — {sec.title()}","",s/12,s))
    cat_tot.append((sec.title(),s))
total_exp = sum(s for _,s in cat_tot)
net = income_ann - total_exp
rows.append(("total","TOTAL EXPENSES","",total_exp/12,total_exp))
rows.append(("net","NET PROFIT (before tax)","",net/12,net))

def money(v): return f"${v:,.0f}"

# ---- figure ------------------------------------------------------------------
fig = plt.figure(figsize=(8.6, 12.4), dpi=130)
fig.patch.set_facecolor("white")

# header band
fig.add_artist(Rectangle((0,0.945),1,0.055,transform=fig.transFigure,color=NAVY,zorder=0))
fig.text(0.04,0.972,"Business Budget & Cost Calculator",color="white",
         fontsize=20,fontweight="bold",va="center")
fig.text(0.04,0.952,"Preview · currency AUD ($) · all figures editable in the .xlsx",
         color="#C9D3E8",fontsize=9.5,va="center")

# KPI cards
kpis=[("Annual income",money(income_ann),BLUE),
      ("Annual expenses",money(total_exp),"#843C0C"),
      ("Net profit (pre-tax)",money(net),"#2E7D32"),
      ("Net margin",f"{net/income_ann*100:.1f}%","#2E7D32")]
x0,w,gap=0.04,0.224,0.013
for i,(lab,val,col) in enumerate(kpis):
    x=x0+i*(w+gap)
    fig.add_artist(Rectangle((x,0.875),w,0.055,transform=fig.transFigure,
                   facecolor=GREY,edgecolor="#D0D0D0",lw=1,zorder=1))
    fig.text(x+0.012,0.918,lab,fontsize=9,color="#555",va="center")
    fig.text(x+0.012,0.893,val,fontsize=15.5,fontweight="bold",color=col,va="center")

# table
ax=fig.add_axes([0.04,0.30,0.92,0.55]); ax.axis("off")
n=len(rows); ax.set_xlim(0,1); ax.set_ylim(0,n+1)
cx_name,cx_freq,cx_mon,cx_ann=0.012,0.60,0.79,0.985
def yt(i): return n-i+0.5
# header
ax.add_patch(Rectangle((0,n),1,1,color=BLUE));
for t,x,ha in [("Item",cx_name,"left"),("Frequency",cx_freq,"center"),
               ("Monthly",cx_mon,"right"),("Annual",cx_ann,"right")]:
    ax.text(x,yt(0),t,color="white",fontsize=10.5,fontweight="bold",ha=ha,va="center")
for i,(kind,name,freq,mon,annv) in enumerate(rows,start=1):
    y=yt(i)
    if kind=="section":
        ax.add_patch(Rectangle((0,n-i),1,1,color=NAVY))
        ax.text(cx_name,y,name,color="white",fontsize=10.5,fontweight="bold",va="center")
    elif kind=="item":
        if i%2==0: ax.add_patch(Rectangle((0,n-i),1,1,color="#FAFBFD"))
        ax.text(cx_name,y,name,fontsize=10,va="center")
        ax.text(cx_freq,y,freq,fontsize=9,color="#666",ha="center",va="center")
        ax.text(cx_mon,y,money(mon),fontsize=10,ha="right",va="center")
        ax.text(cx_ann,y,money(annv),fontsize=10,ha="right",va="center")
    elif kind=="subtotal":
        col = GREEN if name=="TOTAL INCOME" else LBLUE
        ax.add_patch(Rectangle((0,n-i),1,1,color=col))
        ax.text(cx_name,y,name,fontsize=10,fontweight="bold",va="center")
        ax.text(cx_mon,y,money(mon),fontsize=10,fontweight="bold",ha="right",va="center")
        ax.text(cx_ann,y,money(annv),fontsize=10,fontweight="bold",ha="right",va="center")
    elif kind in ("total","net"):
        col = BLUE if kind=="total" else NAVY
        ax.add_patch(Rectangle((0,n-i),1,1,color=col))
        ax.text(cx_name,y,name,color="white",fontsize=11,fontweight="bold",va="center")
        ax.text(cx_mon,y,money(mon),color="white",fontsize=11,fontweight="bold",ha="right",va="center")
        ax.text(cx_ann,y,money(annv),color="white",fontsize=11,fontweight="bold",ha="right",va="center")

# pie
axp=fig.add_axes([0.06,0.035,0.42,0.235])
labels=[c for c,_ in cat_tot]; vals=[v for _,v in cat_tot]
colors=["#2E5496","#9DC3E6","#BDD7EE"]
wedges,_,_=axp.pie(vals,colors=colors,autopct=lambda p:f"{p:.0f}%",
                   startangle=90,textprops={"fontsize":9,"color":"#1F3864","fontweight":"bold"},
                   wedgeprops={"edgecolor":"white","linewidth":1.5})
axp.set_title("Where the money goes (annual)",fontsize=11,fontweight="bold",color=NAVY,pad=8)

# legend / breakdown beside pie
axl=fig.add_axes([0.52,0.035,0.44,0.235]); axl.axis("off"); axl.set_xlim(0,1); axl.set_ylim(0,1)
axl.text(0,0.92,"Annual cost breakdown",fontsize=11,fontweight="bold",color=NAVY)
for j,((c,v),col) in enumerate(zip(cat_tot,colors)):
    yy=0.74-j*0.15
    axl.add_patch(Rectangle((0,yy-0.03),0.05,0.07,color=col))
    axl.text(0.08,yy,c,fontsize=10,va="center")
    axl.text(1.0,yy,money(v),fontsize=10,va="center",ha="right",fontweight="bold")
axl.plot([0,1],[0.27,0.27],color="#CCC",lw=1)
axl.text(0.08,0.18,"Total expenses",fontsize=10.5,fontweight="bold",va="center")
axl.text(1.0,0.18,money(total_exp),fontsize=10.5,fontweight="bold",va="center",ha="right")
axl.text(0.08,0.06,"Net profit (pre-tax)",fontsize=10.5,fontweight="bold",color="#2E7D32",va="center")
axl.text(1.0,0.06,money(net),fontsize=10.5,fontweight="bold",color="#2E7D32",va="center",ha="right")

fig.savefig("/tmp/budget_preview.png",facecolor="white",bbox_inches="tight")
print("income",income_ann,"expenses",total_exp,"net",net,"margin",round(net/income_ann*100,1))
print("categories",cat_tot)
