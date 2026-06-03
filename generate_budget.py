#!/usr/bin/env python3
"""Generate a business budget & cost calculator workbook (.xlsx).

Two sheets:
  - Dashboard: high-level summary + cost-breakdown pie chart
  - Budget:    editable line items with live formulas

All numbers are EDITABLE assumptions. Formulas recalculate automatically in
Excel and in Google Sheets (upload the .xlsx to Drive -> opens natively).
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.chart import PieChart, Reference
from openpyxl.utils import get_column_letter

# ---------------------------------------------------------------- styling ----
NAVY   = "1F3864"   # headers / title bar
BLUE   = "2E5496"   # section headers
LBLUE  = "D9E1F2"   # subtotal / soft fill
GREY   = "F2F2F2"   # zebra
GREEN  = "C6EFCE"
GREEN_T= "006100"
RED    = "FFC7CE"
RED_T  = "9C0006"
WHITE  = "FFFFFF"

CUR = '$#,##0.00'         # currency
CUR0 = '$#,##0'           # currency, no cents
PCT = '0.0%'

thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

def fill(hex_):  return PatternFill("solid", fgColor=hex_)
def f_white(sz=11, b=True): return Font(name="Calibri", size=sz, bold=b, color=WHITE)
def f_dark(sz=11, b=False): return Font(name="Calibri", size=sz, bold=b, color="000000")

CENTER = Alignment(horizontal="center", vertical="center")
LEFT   = Alignment(horizontal="left",   vertical="center", wrap_text=True)
RIGHT  = Alignment(horizontal="right",  vertical="center")

# ------------------------------------------------------------------ data -----
# (item name, frequency, amount per period, note)
INCOME = ("INCOME", [
    ("Business income / revenue", "Annually", 100000, "Client's stated annual earnings"),
    ("Other income",             "Annually",      0, "Grants, interest, side jobs, etc."),
])

EXPENSES = [
    ("VEHICLE COSTS", [
        ("Servicing & logbook",      "Quarterly",  375, "~$1,500 / year"),
        ("Tyres",                    "Annually",  1200, "Set of tyres incl. fitting"),
        ("Fuel",                     "Weekly",      80, "~$80 / week"),
        ("Registration & CTP",       "Annually",   850, "Annual rego renewal"),
        ("Vehicle insurance",        "Monthly",    120, "Comprehensive cover"),
        ("Repairs & maintenance",    "Annually",   800, "Wear & tear buffer"),
    ]),
    ("SUBSCRIPTIONS", [
        ("ServiceM8 (job management)", "Monthly", 99, "Adjust to your plan tier"),
        ("Xero (accounting)",          "Monthly", 70, "Standard plan"),
    ]),
    ("BUSINESS COSTS & LICENSING", [
        ("Public liability insurance", "Annually", 1100, "$5m / $10m cover"),
        ("Business name registration", "Annually",   60, "ASIC renewal"),
        ("Trade licence / certification","Annually", 350, "Licence renewal + CPD"),
        ("Phone & internet",           "Monthly",   110, "Mobile + data"),
        ("Tools & equipment",          "Annually", 2000, "Replacement / new tools"),
        ("Marketing & advertising",    "Monthly",   150, "Website, ads, signage"),
        ("Bank & merchant fees",       "Monthly",    40, "Card / EFTPOS fees"),
    ]),
]

FREQS = ["Weekly", "Fortnightly", "Monthly", "Quarterly", "Half-yearly", "Annually", "One-off"]

def freq_factor(freq_cell):
    """Nested IF mapping a frequency label -> periods per year."""
    return (f'IF({freq_cell}="Weekly",52,'
            f'IF({freq_cell}="Fortnightly",26,'
            f'IF({freq_cell}="Monthly",12,'
            f'IF({freq_cell}="Quarterly",4,'
            f'IF({freq_cell}="Half-yearly",2,'
            f'IF({freq_cell}="Annually",1,'
            f'IF({freq_cell}="One-off",1,0)))))))')

# ============================================================= build BUDGET ==
wb = Workbook()
bud = wb.active
bud.title = "Budget"

# columns: A item | B freq | C amount | D monthly | E annual | F %income | G notes
widths = {"A": 30, "B": 14, "C": 14, "D": 13, "E": 13, "F": 12, "G": 34}
for col, w in widths.items():
    bud.column_dimensions[col].width = w

# title
bud.merge_cells("A1:G1")
c = bud["A1"]; c.value = "Business Budget & Cost Calculator"
c.font = f_white(18); c.fill = fill(NAVY); c.alignment = Alignment(horizontal="left", vertical="center")
bud.row_dimensions[1].height = 30
bud.merge_cells("A2:G2")
c = bud["A2"]; c.value = "Currency: AUD ($).  Blue cells are editable — change Amount or Frequency and totals update automatically."
c.font = Font(italic=True, size=9, color="595959"); c.alignment = LEFT

HEADERS = ["Item", "Frequency", "Amount", "Monthly", "Annual", "% of Income", "Notes"]
hrow = 4
for i, h in enumerate(HEADERS):
    cell = bud.cell(row=hrow, column=i + 1, value=h)
    cell.font = f_white(11); cell.fill = fill(BLUE)
    cell.alignment = CENTER; cell.border = BORDER
bud.freeze_panes = "A5"

r = hrow + 1
input_fill = fill("FFF7E1")  # editable amount/freq cells (soft amber)

def write_section_header(title):
    global r
    bud.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    cell = bud.cell(row=r, column=1, value=title)
    cell.font = f_white(11); cell.fill = fill(NAVY); cell.alignment = LEFT
    for col in range(1, 8):
        bud.cell(row=r, column=col).fill = fill(NAVY)
    r += 1

def write_item(name, freq, amount, note, income_row_ref):
    """income_row_ref = absolute ref of income annual cell for %; None on income rows."""
    global r
    bud.cell(row=r, column=1, value=name).alignment = LEFT
    fc = bud.cell(row=r, column=2, value=freq); fc.alignment = CENTER; fc.fill = input_fill
    ac = bud.cell(row=r, column=3, value=amount); ac.number_format = CUR; ac.alignment = RIGHT; ac.fill = input_fill
    e = bud.cell(row=r, column=5)  # annual
    e.value = f'=IF(C{r}="","",C{r}*{freq_factor(f"B{r}")})'
    e.number_format = CUR
    d = bud.cell(row=r, column=4)  # monthly = annual / 12
    d.value = f'=IF(E{r}="","",E{r}/12)'
    d.number_format = CUR
    fcell = bud.cell(row=r, column=6)
    if income_row_ref:
        fcell.value = f'=IF({income_row_ref}=0,"",E{r}/{income_row_ref})'
        fcell.number_format = PCT
    nt = bud.cell(row=r, column=7, value=note); nt.alignment = LEFT
    nt.font = Font(size=9, color="595959")
    for col in range(1, 8):
        bud.cell(row=r, column=col).border = BORDER
    r += 1

def write_subtotal(label, first, last, income_row_ref, strong=False):
    global r
    cell = bud.cell(row=r, column=1, value=label); cell.font = f_dark(b=True); cell.alignment = LEFT
    d = bud.cell(row=r, column=4, value=f"=SUM(D{first}:D{last})"); d.number_format = CUR
    e = bud.cell(row=r, column=5, value=f"=SUM(E{first}:E{last})"); e.number_format = CUR
    f = bud.cell(row=r, column=6)
    f.value = f'=IF({income_row_ref}=0,"",E{r}/{income_row_ref})'; f.number_format = PCT
    fillc = LBLUE if not strong else "BDD7EE"
    for col in range(1, 8):
        cc = bud.cell(row=r, column=col)
        cc.fill = fill(fillc); cc.border = BORDER
        if col in (4, 5, 6): cc.font = f_dark(b=True)
    sub_row = r
    r += 1
    return sub_row

# --- INCOME -----------------------------------------------------------------
write_section_header(INCOME[0])
inc_first = r
for name, freq, amount, note in INCOME[1]:
    write_item(name, freq, amount, note, income_row_ref=None)
inc_last = r - 1
# income subtotal (annual cell becomes the reference for all % calcs)
inc_sub_label = "TOTAL INCOME"
cell = bud.cell(row=r, column=1, value=inc_sub_label); cell.font = f_dark(b=True); cell.alignment = LEFT
d = bud.cell(row=r, column=4, value=f"=SUM(D{inc_first}:D{inc_last})"); d.number_format = CUR
e = bud.cell(row=r, column=5, value=f"=SUM(E{inc_first}:E{inc_last})"); e.number_format = CUR
for col in range(1, 8):
    cc = bud.cell(row=r, column=col); cc.fill = fill("C6E0B4"); cc.border = BORDER
    if col in (4, 5): cc.font = f_dark(b=True)
income_sub_row = r
INC_ANNUAL = f"$E${income_sub_row}"
INC_MONTHLY = f"$D${income_sub_row}"
r += 2

# --- EXPENSE SECTIONS -------------------------------------------------------
cat_subtotals = []  # (name, monthly_cell, annual_cell)
for sec_name, items in EXPENSES:
    write_section_header(sec_name)
    first = r
    for name, freq, amount, note in items:
        write_item(name, freq, amount, note, income_row_ref=INC_ANNUAL)
    last = r - 1
    sub_row = write_subtotal(f"Subtotal — {sec_name.title()}", first, last, INC_ANNUAL)
    cat_subtotals.append((sec_name.title(), f"D{sub_row}", f"E{sub_row}"))
    r += 1

# --- TOTALS -----------------------------------------------------------------
month_sum = "+".join(c[1] for c in cat_subtotals)
ann_sum   = "+".join(c[2] for c in cat_subtotals)
# TOTAL EXPENSES
cell = bud.cell(row=r, column=1, value="TOTAL EXPENSES"); cell.font = f_white(12); cell.alignment = LEFT
d = bud.cell(row=r, column=4, value=f"={month_sum}"); d.number_format = CUR
e = bud.cell(row=r, column=5, value=f"={ann_sum}"); e.number_format = CUR
f = bud.cell(row=r, column=6, value=f'=IF({INC_ANNUAL}=0,"",E{r}/{INC_ANNUAL})'); f.number_format = PCT
for col in range(1, 8):
    cc = bud.cell(row=r, column=col); cc.fill = fill(BLUE); cc.border = BORDER
    if col in (1, 4, 5, 6): cc.font = f_white(12)
tot_exp_month, tot_exp_ann = f"D{r}", f"E{r}"
r += 1

# NET PROFIT
cell = bud.cell(row=r, column=1, value="NET PROFIT (before tax)"); cell.font = f_white(12); cell.alignment = LEFT
d = bud.cell(row=r, column=4, value=f"={INC_MONTHLY}-{tot_exp_month}"); d.number_format = CUR
e = bud.cell(row=r, column=5, value=f"={INC_ANNUAL}-{tot_exp_ann}"); e.number_format = CUR
f = bud.cell(row=r, column=6, value=f'=IF({INC_ANNUAL}=0,"",E{r}/{INC_ANNUAL})'); f.number_format = PCT
for col in range(1, 8):
    cc = bud.cell(row=r, column=col); cc.fill = fill(NAVY); cc.border = BORDER
    if col in (1, 4, 5, 6): cc.font = f_white(12)
net_ann = f"E{r}"
r += 2

# assumptions note
bud.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
note = bud.cell(row=r, column=1,
    value=("NOTE: All amounts are editable estimates — replace them with your real figures. "
           "'NET PROFIT (before tax)' is income minus expenses and does NOT account for income tax, GST or super. "
           "Frequencies supported: Weekly, Fortnightly, Monthly, Quarterly, Half-yearly, Annually, One-off."))
note.font = Font(italic=True, size=9, color="595959"); note.alignment = LEFT
bud.row_dimensions[r].height = 42

# data validation dropdown on all frequency cells
dv = DataValidation(type="list", formula1='"%s"' % ",".join(FREQS), allow_blank=True)
bud.add_data_validation(dv)
dv.add(f"B{inc_first}:B{income_sub_row-1}")
# expense freq cells span from first expense item to the row before TOTAL EXPENSES
dv.add(f"B{inc_last+3}:B{r-4}")

# =========================================================== build DASHBOARD ==
dash = wb.create_sheet("Dashboard", 0)  # make it the first sheet
for col, w in {"A": 28, "B": 18, "C": 16, "D": 2, "E": 22, "F": 16, "G": 14}.items():
    dash.column_dimensions[col].width = w

dash.merge_cells("A1:G1")
c = dash["A1"]; c.value = "Business Budget — Summary"
c.font = f_white(18); c.fill = fill(NAVY); c.alignment = Alignment(horizontal="left", vertical="center")
dash.row_dimensions[1].height = 32
dash.merge_cells("A2:G2")
c = dash["A2"]; c.value = "Figures pull live from the 'Budget' tab. Edit line items there."
c.font = Font(italic=True, size=9, color="595959"); c.alignment = LEFT

# KPI block
kpis = [
    ("Annual income",          f"='Budget'!{INC_ANNUAL}",  CUR0),
    ("Total annual expenses",  f"='Budget'!{tot_exp_ann}", CUR0),
    ("Net annual profit",      f"='Budget'!{net_ann}",     CUR0),
    ("Net monthly profit",     f"='Budget'!{net_ann}/12",  CUR0),
    ("Average monthly expenses",f"='Budget'!{tot_exp_ann}/12", CUR0),
    ("Net margin",             f"=IF('Budget'!{INC_ANNUAL}=0,\"\",'Budget'!{net_ann}/'Budget'!{INC_ANNUAL})", PCT),
]
row = 4
for label, formula, fmt in kpis:
    lc = dash.cell(row=row, column=1, value=label); lc.font = f_dark(b=True); lc.alignment = LEFT
    lc.fill = fill(GREY); lc.border = BORDER
    vc = dash.cell(row=row, column=2, value=formula); vc.number_format = fmt
    vc.font = Font(bold=True, size=12, color=NAVY); vc.alignment = RIGHT; vc.border = BORDER
    vc.fill = fill(GREY)
    row += 1
# green/red on net annual profit + net monthly profit + margin
for rr in (6, 7, 9):
    dash.conditional_formatting.add(f"B{rr}",
        CellIsRule(operator="greaterThan", formula=["0"], fill=fill(GREEN), font=Font(color=GREEN_T, bold=True)))
    dash.conditional_formatting.add(f"B{rr}",
        CellIsRule(operator="lessThan", formula=["0"], fill=fill(RED), font=Font(color=RED_T, bold=True)))

# breakdown table (cols E:G) feeding the chart
tbl_top = 4
dash.cell(row=tbl_top, column=5, value="Cost category").font = f_white(11)
dash.cell(row=tbl_top, column=6, value="Annual cost").font = f_white(11)
dash.cell(row=tbl_top, column=7, value="% of total").font = f_white(11)
for col in (5, 6, 7):
    cc = dash.cell(row=tbl_top, column=col); cc.fill = fill(BLUE); cc.alignment = CENTER; cc.border = BORDER

br = tbl_top + 1
cat_rows = []
for name, _m, ann in cat_subtotals:
    dash.cell(row=br, column=5, value=name).alignment = LEFT
    v = dash.cell(row=br, column=6, value=f"='Budget'!{ann}"); v.number_format = CUR0; v.alignment = RIGHT
    p = dash.cell(row=br, column=7, value=f"=IF('Budget'!{tot_exp_ann}=0,\"\",F{br}/'Budget'!{tot_exp_ann})")
    p.number_format = PCT; p.alignment = RIGHT
    for col in (5, 6, 7):
        dash.cell(row=br, column=col).border = BORDER
    cat_rows.append(br)
    br += 1
# total row
dash.cell(row=br, column=5, value="Total expenses").font = f_dark(b=True)
tv = dash.cell(row=br, column=6, value=f"=SUM(F{cat_rows[0]}:F{cat_rows[-1]})")
tv.number_format = CUR0; tv.font = f_dark(b=True); tv.alignment = RIGHT
for col in (5, 6, 7):
    cc = dash.cell(row=br, column=col); cc.fill = fill(LBLUE); cc.border = BORDER

# pie chart
pie = PieChart()
pie.title = "Where the money goes (annual)"
labels = Reference(dash, min_col=5, min_row=cat_rows[0], max_row=cat_rows[-1])
data = Reference(dash, min_col=6, min_row=tbl_top, max_row=cat_rows[-1])
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.height = 8.5
pie.width = 15
dash.add_chart(pie, "A12")

dash.sheet_view.showGridLines = False
bud.sheet_view.showGridLines = False

out = "Business_Budget_Calculator.xlsx"
wb.save(out)
print("Saved", out)
print("Income annual cell:", INC_ANNUAL, "| Total exp annual:", tot_exp_ann, "| Net annual:", net_ann)
print("Category subtotals:", cat_subtotals)
