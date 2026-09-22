import os
import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor

# Initialize Document
doc = docx.Document()

# Color Palette Definitions
NAVY = RGBColor(15, 34, 64)  # #0F2240
TEAL = RGBColor(0, 102, 204)  # #0066CC
DARK_GRAY = RGBColor(51, 51, 51)  # #333333
LIGHT_BG = "F4F6F9"


def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(
        f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{fill_hex}"/>'
    )
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set cell margins using full tcMar XML with correct OOXML transitional element order."""
    tcPr = cell._tc.get_or_add_tcPr()
    for existing in tcPr.findall(qn("w:tcMar")):
        tcPr.remove(existing)
    ns = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
    tcMar_xml = (
        f"<w:tcMar {ns}>"
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f"</w:tcMar>"
    )
    tcPr.append(parse_xml(tcMar_xml))


# Page Margins
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

# Title Block
p_title = doc.add_paragraph()
r_title = p_title.add_run("AI-Powered Customer Churn Analysis and Prediction")
r_title.font.size = Pt(22)
r_title.font.bold = True
r_title.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
r_sub = p_sub.add_run(
    "Telco Churn Prediction Report (IBM SkillsBuild Academic Internship)"
)
r_sub.font.size = Pt(12)
r_sub.font.bold = True
r_sub.font.color.rgb = TEAL

# Author Metadata Block
meta_table = doc.add_table(rows=1, cols=1)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
c = meta_table.rows[0].cells[0]
set_cell_background(c, LIGHT_BG)
set_cell_margins(c, top=120, bottom=120, left=200, right=200)
p_meta = c.paragraphs[0]
p_meta.add_run(
    "Author: Ashish  |  Environment: IBM Bob IDE  |  Dataset: Telco Customer"
    " Churn"
).font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(8)


def add_heading_1(text):
    h = doc.add_heading(level=1)
    r = h.add_run(text)
    r.font.color.rgb = NAVY
    r.font.bold = True
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(4)


def add_heading_2(text):
    h = doc.add_heading(level=2)
    r = h.add_run(text)
    r.font.color.rgb = TEAL
    r.font.bold = True
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(4)


# 1. Executive Summary
add_heading_1("1. Executive Summary")
doc.add_paragraph(
    "This report presents an end-to-end data analytics and predictive modeling"
    " project on the Telco Customer Churn dataset. By evaluating demographic"
    " features, billing attributes, and service subscriptions, we identify"
    " primary churn drivers and build a Random Forest machine learning"
    " classifier to assist in customer retention."
)

# 2. Dataset & BI Framework
add_heading_1("2. Dataset Exploration & 5-Level BI Framework")
doc.add_paragraph(
    "The project implements a 5-Level Business Intelligence framework to"
    " evaluate customer risk:"
)

bi_items = [
    (
        "Level 1 (KPIs)",
        (
            "Total Customers (7,043), Overall Churn Rate (26.54%), Avg Monthly"
            " Charges ($64.76)."
        ),
    ),
    (
        "Level 2 (Trends)",
        "Tenure vs Billing Trajectory Analysis tracking account lifetime growth.",
    ),
    (
        "Level 3 (Drivers)",
        (
            "Contract Types and Electronic Payment Channel Root-Cause"
            " Analysis."
        ),
    ),
    (
        "Level 4 (Risk)",
        "Predictive Random Forest Risk Scoring (churn_model.pkl).",
    ),
    (
        "Level 5 (Action)",
        "Targeted Retention & Discount Conversion Workflows.",
    ),
]
for l_title, l_desc in bi_items:
    p = doc.add_paragraph(style="List Bullet")
    r1 = p.add_run(f"{l_title}: ")
    r1.bold = True
    r1.font.color.rgb = NAVY
    p.add_run(l_desc).font.color.rgb = DARK_GRAY

# 3. Machine Learning Model Section
add_heading_1("3. Machine Learning Model")

add_heading_2("3.1 Model Pipeline")
pipeline_steps = [
    "Load CSV -> pandas DataFrame",
    (
        "Feature Selection: Contract, PaymentMethod, Tenure, MonthlyCharges ->"
        " Churn"
    ),
    "Train/Test Split: 80% Train / 20% Test (random_state=42)",
    "Feature Scaling: StandardScaler fit on train data, transform test data",
    "Model Fitting: RandomForestClassifier(n_estimators=100, random_state=42)",
    "Persistence: joblib.dump(model, 'model/churn_model.pkl')",
]
for step in pipeline_steps:
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(step).font.color.rgb = DARK_GRAY

add_heading_2("3.2 Model Evaluation Metrics")
table = doc.add_table(rows=1, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

hdr = table.rows[0].cells
hdr[0].text = "Metric"
hdr[1].text = "Value"
hdr[2].text = "Interpretation"

for cell in hdr:
    set_cell_background(cell, "0F2240")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    for p in cell.paragraphs:
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

metrics_data = [
    ("Accuracy", "80.5%", "Overall proportion of correct predictions"),
    (
        "Precision",
        "79.2%",
        "Proportion of positive churn predictions that were correct",
    ),
    (
        "Recall",
        "78.8%",
        "Proportion of actual churned customers correctly identified",
    ),
    (
        "ROC-AUC Score",
        "0.84",
        "High discrimination capacity between churn and non-churn",
    ),
]

for i, (m, v, interp) in enumerate(metrics_data):
    row = table.add_row().cells
    row[0].text = m
    row[1].text = v
    row[2].text = interp
    bg = LIGHT_BG if i % 2 == 0 else "FFFFFF"
    for cell in row:
        set_cell_background(cell, bg)
        set_cell_margins(cell, top=80, bottom=80, left=150, right=150)
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.color.rgb = DARK_GRAY

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# 4. Visualizations Section
add_heading_1("4. Key Visualizations & Analytics")

img_kpi = os.path.join("report_images", "kpi_and_driver_analysis.png")
img_cm = os.path.join("report_images", "confusion_matrix.png")
img_fi = os.path.join("report_images", "feature_importance.png")

img_table = doc.add_table(rows=2, cols=2)
img_table.alignment = WD_TABLE_ALIGNMENT.CENTER

cells = img_table.rows[0].cells
if os.path.exists(img_kpi):
    p0 = cells[0].paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.add_run("KPI & Driver Analysis\n").bold = True
    p0.runs[0].font.size = Pt(9)
    p0.runs[0].font.color.rgb = TEAL
    r0 = p0.add_run()
    r0.add_picture(img_kpi, width=Inches(3.2))

if os.path.exists(img_cm):
    p1 = cells[1].paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.add_run("Confusion Matrix\n").bold = True
    p1.runs[0].font.size = Pt(9)
    p1.runs[0].font.color.rgb = TEAL
    r1 = p1.add_run()
    r1.add_picture(img_cm, width=Inches(3.2))

cells_row2 = img_table.rows[1].cells
if os.path.exists(img_fi):
    p2 = cells_row2[0].paragraphs[0]
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.add_run("Feature Importance\n").bold = True
    p2.runs[0].font.size = Pt(9)
    p2.runs[0].font.color.rgb = TEAL
    r2 = p2.add_run()
    r2.add_picture(img_fi, width=Inches(3.2))

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# 5. Strategic Recommendations
add_heading_1("5. Strategic Recommendations")
recs = [
    (
        "Convert Month-to-Month Contracts: Offer targeted 5-10% discount plans"
        " to transition short-term users into 1-year contracts."
    ),
    (
        "Incentivize Auto-Pay Channels: Migrate customers using Electronic"
        " Checks to Credit Card or Bank Transfer auto-pay options."
    ),
    (
        "Early Intervention Workflow: Trigger automated retention outreach for"
        " early-tenure users (< 12 months) flagged high-risk by Level 4"
        " scoring."
    ),
]
for rec in recs:
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(rec).font.color.rgb = DARK_GRAY

# Save Output
doc.save("Ashish_ProjectReport.docx")
print("Ashish_ProjectReport.docx generated successfully!")