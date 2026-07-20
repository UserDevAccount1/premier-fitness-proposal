"""Generate the NFAC Scoring Calculation Insight PDF.

Documents the calculation knowledge base: how every field input maps to a
score, category by category, with the Broadstone worked example. Run from
the repo root: python docs/generate_insight_pdf.py
"""
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)

NAVY = colors.HexColor("#14264e")
NAVY_D = colors.HexColor("#0e1c3d")
RED = colors.HexColor("#c8102e")
BLUE = colors.HexColor("#2f6fb3")
GREEN = colors.HexColor("#3d8b4f")
AMBER = colors.HexColor("#e8a020")
LINE = colors.HexColor("#dde3ee")
MUTED = colors.HexColor("#5a6478")
BG = colors.HexColor("#f4f6fb")

OUT = os.path.join(os.path.dirname(__file__), "NFAC-Scoring-Calculation-Insight.pdf")

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Title"], textColor=NAVY, fontSize=24, leading=29, spaceAfter=6)
H2 = ParagraphStyle("H2", parent=styles["Heading1"], textColor=NAVY, fontSize=15, leading=19, spaceBefore=16, spaceAfter=6)
H3 = ParagraphStyle("H3", parent=styles["Heading2"], textColor=RED, fontSize=12, leading=15, spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("BODY", parent=styles["Normal"], fontSize=9.5, leading=13.5, textColor=colors.HexColor("#1b2437"))
SMALL = ParagraphStyle("SMALL", parent=BODY, fontSize=8.5, leading=12, textColor=MUTED)
CELL = ParagraphStyle("CELL", parent=BODY, fontSize=8.5, leading=11.5)
CELLW = ParagraphStyle("CELLW", parent=CELL, textColor=colors.white)

def table(data, widths, header_bg=NAVY, zebra=True, align_left=True):
    rows = [[Paragraph(str(c), CELLW if r == 0 else CELL) for c in row] for r, row in enumerate(data)]
    t = Table(rows, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                style.append(("BACKGROUND", (0, i), (-1, i), BG))
    t.setStyle(TableStyle(style))
    return t

def hdr_footer(canvas, doc):
    canvas.saveState()
    w, h = letter
    canvas.setFillColor(NAVY_D)
    canvas.rect(0, h - 0.55 * inch, w, 0.55 * inch, stroke=0, fill=1)
    canvas.setFillColor(RED)
    canvas.rect(0.55 * inch, h - 0.43 * inch, 0.52 * inch, 0.24 * inch, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(0.62 * inch, h - 0.36 * inch, "NFAC")
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(1.25 * inch, h - 0.36 * inch, "NATIONAL FITNESS AMENITY COUNCIL™  ·  SCORING CALCULATION INSIGHT")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(w - 0.55 * inch, h - 0.36 * inch, "Powered by Premier Fitness")
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(0.55 * inch, 0.4 * inch, "NFAC Scoring Framework v2 — Calculation Knowledge Base")
    canvas.drawRightString(w - 0.55 * inch, 0.4 * inch, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=letter, topMargin=0.95 * inch, bottomMargin=0.7 * inch,
                        leftMargin=0.65 * inch, rightMargin=0.65 * inch,
                        title="NFAC Scoring Calculation Insight",
                        author="Premier Fitness / NFAC")
S = []

# ---------- Cover / overview ----------
S.append(Paragraph("NFAC Scoring — Calculation Insight", H1))
S.append(Paragraph(
    "How every field input becomes a score. This document is the calculation knowledge base behind the "
    "analytics dashboard and the per-property PDF report: the exact formulas, deduction tiers, rubric weights, "
    "and a fully worked example from the evaluation dataset — so no scoring step is ever a black box.", BODY))
S.append(Spacer(1, 10))

S.append(Paragraph("The Model at a Glance", H2))
S.append(Paragraph(
    "Six categories are each scored out of 100, then averaged. Every category is driven by concrete, "
    "observable field inputs captured in the on-site evaluation form.", BODY))
S.append(Spacer(1, 6))
S.append(table([
    ["Category", "Raw scale", "Weight to /100", "Driven by"],
    ["Safety & Risk", "Severity tier", "Direct (tier value)", "Equipment inspection findings mapped to severity tiers"],
    ["Asset Condition", "5 metrics × (1–5) = /25", "× 4", "Operational readiness, cosmetics, lifecycle, maintenance, stewardship"],
    ["User Experience", "4 metrics × (1–5) = /20", "× 5", "Cleanliness, comfort/environment, layout, aesthetics"],
    ["Utilization", "4 metrics × (1–5) = /20", "× 5", "Wear patterns, equipment selection, space use, throughput"],
    ["Exercise Coverage", "10 modalities × (0/1) = /10", "× 10", "Presence of core movement categories"],
    ["Sanitation Readiness", "1 rubric (1–5) = /5", "× 20", "Sanitizer + wipe availability, stock, placement"],
], [1.35 * inch, 1.5 * inch, 1.15 * inch, 3.2 * inch]))
S.append(Spacer(1, 8))
S.append(Paragraph(
    "<b>FINAL NFAC SCORE = (Safety + Asset + Experience + Utilization + Coverage + Sanitation) ÷ 6</b>", BODY))
S.append(Paragraph(
    "Grade bands: A ≥ 90 · B 80–89 · C 70–79 · D 60–69 · F &lt; 60. Percentile rank is computed against "
    "every prior evaluation in the benchmark dataset, filtered by property type and market.", SMALL))

# ---------- Safety ----------
S.append(Paragraph("1 · Safety &amp; Risk — Severity Tier Deduction", H2))
S.append(Paragraph(
    "The score starts from a perfect state and is set by the worst finding class present. Every yes/no "
    "inspection answer (belt test, cable condition, e-stop, structure, power sharing, debris) maps to a tier. "
    "The category score is the tier value of the most severe condition found:", BODY))
S.append(Spacer(1, 6))
S.append(table([
    ["Tier", "Score", "Trigger condition (what the evaluator saw)"],
    ["Excellent", "100", "No findings"],
    ["Attention needed", "94", "Minor findings only (e.g., lubrication lacking, debris present)"],
    ["Moderate risk", "84", "Major finding present (e.g., belt hesitates slightly under load)"],
    ["Urgent risk", "69", "One critical finding (e.g., belt slows significantly; frayed cable, steel exposed)"],
    ["Immediate risk", "49", "Multiple critical findings"],
    ["Critical risk", "25", "Immediate life-safety hazard (e.g., compromised steel cable, belt stops under load)"],
], [1.3 * inch, 0.7 * inch, 5.2 * inch], header_bg=RED))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "The NFAC Safety Matrix in the dashboard is the visual form of the same inputs: each hazard family "
    "(high-speed equipment, cable systems, structural, electrical, fall hazards, user controls) shows "
    "Pass / Major / Critical based on the underlying checklist answers.", SMALL))

# ---------- 1-5 rubric categories ----------
S.append(Paragraph("2 · Asset Condition — 5 Metrics × 4", H2))
S.append(table([
    ["Metric (1–5)", "5 means", "1 means"],
    ["Operational Readiness", "Every machine fully operational", "Significant portion unusable / out of order"],
    ["Cosmetic Condition", "Like new", "Poor appearance influencing perception"],
    ["Equipment Lifecycle", "Modern portfolio, little capital planning", "End-of-life portfolio, large capex approaching"],
    ["Preventative Maintenance", "Consistent professional maintenance evident", "Obvious neglect"],
    ["Asset Stewardship", "Proactive care of equipment and facility", "Extensive deferred maintenance"],
], [1.55 * inch, 2.8 * inch, 2.85 * inch]))
S.append(Paragraph("Calculation: sum of the five metrics (max 25) × 4 → score out of 100.", SMALL))

S.append(Paragraph("3 · User Experience — 4 Metrics × 5", H2))
S.append(Paragraph(
    "Cleanliness &amp; Care · Comfort &amp; Environment · Layout &amp; Accessibility · Aesthetic Appeal — each rated "
    "1–5 against written rubrics (e.g., Layout 5 = excellent traffic flow, ADA-conscious spacing; 1 = unsafe spacing). "
    "Sum (max 20) × 5 → /100.", BODY))

S.append(Paragraph("4 · Utilization — 4 Metrics × 5", H2))
S.append(Paragraph(
    "Wear Pattern Analysis · Equipment Selection Effectiveness · Space Utilization · Throughput Capacity — each 1–5. "
    "Throughput is judged against property size (e.g., an apartment at 200–350 units or a hotel at 100 rooms has a "
    "defined expected workout capacity). Sum (max 20) × 5 → /100.", BODY))

S.append(Paragraph("5 · Exercise Coverage — 10 Modalities × 10", H2))
S.append(Paragraph(
    "One point for each core movement category present: treadmill, elliptical, stationary bike, stepmill, rower, "
    "free weights, chest/multi press, leg curl/extension, lat/low pulldown, leg press (a functional trainer counts "
    "for the strength stations). Count (max 10) × 10 → /100.", BODY))

S.append(Paragraph("6 · Sanitation Readiness — Rubric × 20", H2))
S.append(Paragraph(
    "Single 1–5 rubric: 5 = both hand sanitizer and wipes readily available, stocked, well distributed; "
    "3 = both present but placement/quantity lacking; 1 = neither present. Score × 20 → /100.", BODY))

S.append(PageBreak())

# ---------- Worked example ----------
S.append(Paragraph("Worked Example — Broadstone Archive (from the evaluation dataset)", H1))
S.append(Paragraph(
    "Actual figures from the NFAC Scoring Framework v2 sample grade. Every number below traces directly "
    "to a field input recorded on site.", BODY))
S.append(Spacer(1, 8))
S.append(table([
    ["Category", "Field inputs recorded", "Raw", "Weight", "Score /100"],
    ["Safety & Risk", "Multiple critical findings: treadmill belts unlubricated (hesitate under load), non-responsive console → Immediate-risk tier", "tier", "direct", "49"],
    ["Asset Condition", "Readiness 4 + Cosmetic 3 + Lifecycle 3 + Maintenance 3 + Stewardship 4", "17 / 25", "× 4", "68"],
    ["User Experience", "Cleanliness 5 + Comfort 4 + Layout 4 + Aesthetics 5", "18 / 20", "× 5", "90"],
    ["Utilization", "Wear 5 + Selection 5 + Space 4 + Throughput 5", "19 / 20", "× 5", "95"],
    ["Exercise Coverage", "All 10 movement categories present", "10 / 10", "× 10", "100"],
    ["Sanitation Readiness", "Sanitizer + wipes fully stocked and distributed", "5 / 5", "× 20", "100"],
], [1.25 * inch, 3.3 * inch, 0.75 * inch, 0.65 * inch, 0.85 * inch]))
S.append(Spacer(1, 8))
S.append(table([
    ["Final calculation", ""],
    ["Sum of category scores", "49 + 68 + 90 + 95 + 100 + 100 = 502"],
    ["Divide by 6", "502 ÷ 6 = 83.67"],
    ["Grade band", "83.67 → B- (80–89 = B band, lower third)"],
    ["Benchmark percentile", "83.67 vs. all prior DFW apartment evaluations → 82nd percentile"],
], [2.2 * inch, 5.0 * inch], header_bg=GREEN, zebra=False))
S.append(Spacer(1, 10))

S.append(Paragraph("Don't-Miss-A-Mark Checklist (calculation integrity)", H2))
S.append(Paragraph(
    "These are the specific points the automation highlights on every evaluation so no scoring step is missed:", BODY))
S.append(Spacer(1, 6))
S.append(table([
    ["#", "Checkpoint", "Why it matters"],
    ["1", "Every equipment inspected has a severity tier assigned", "One missed critical finding inflates Safety by up to 75 points"],
    ["2", "All 5 Asset Condition metrics scored (no blanks)", "A blank metric silently drops the category by up to 20 points"],
    ["3", "All 4 UX and 4 Utilization metrics scored", "Same blank-input risk; the engine blocks submission if missing"],
    ["4", "10/10 modality checklist completed", "Coverage is the easiest category to under-count on site"],
    ["5", "Sanitation rubric selected (1–5), never inferred", "×20 weight — a 1-point error moves the final score 3.3 points"],
    ["6", "Photo evidence attached for every non-Pass finding", "Backs every deduction in the customer-facing report"],
    ["7", "Property type + unit count recorded", "Required for correct benchmark peer group and throughput rubric"],
], [0.3 * inch, 3.0 * inch, 3.9 * inch], header_bg=RED))
S.append(Spacer(1, 10))

S.append(Paragraph("Where These Numbers Surface", H2))
S.append(Paragraph(
    "Analytics dashboard: executive score dial, six category donuts, score-composition bars (each 1–5 metric "
    "visualized), NFAC Safety Matrix, benchmark percentile bar, and portfolio comparisons. "
    "PDF report: the same figures rendered as a branded, print-ready document generated automatically from "
    "each form submission — dashboard and PDF always agree because both read the same calculation output.", BODY))
S.append(Spacer(1, 6))
S.append(Paragraph(
    "Live demo: https://userdevaccount1.github.io/premier-fitness-proposal/", SMALL))

doc.build(S, onFirstPage=hdr_footer, onLaterPages=hdr_footer)
print("written:", OUT)
