from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os

# Create reports folder if not exists
os.makedirs(
    "reports",
    exist_ok=True
)

# Create PDF
pdf = SimpleDocTemplate(
    "reports/customer_churn_report.pdf"
)

styles = getSampleStyleSheet()

content = []

# Title
title = Paragraph(
    "Customer Churn Analytics Report",
    styles["Title"]
)

content.append(title)

content.append(
    Spacer(1, 12)
)

# KPI Section

content.append(
    Paragraph(
        "Total Customers: 7043",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "Churn Customers: 1869",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "Churn Rate: 26.54%",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "Revenue Lost: 2,862,926.90",
        styles["Normal"]
    )
)

content.append(
    Spacer(1, 12)
)

# Insights Section

content.append(
    Paragraph(
        "Key Business Insights",
        styles["Heading2"]
    )
)

content.append(
    Paragraph(
        "1. Month-to-Month customers show the highest churn.",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "2. Customers with higher monthly charges are more likely to churn.",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "3. New customers have a higher churn risk than loyal customers.",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "4. High-value customers should be prioritized for retention.",
        styles["Normal"]
    )
)

content.append(
    Spacer(1, 12)
)

# Retention Recommendations

content.append(
    Paragraph(
        "Retention Recommendations",
        styles["Heading2"]
    )
)

content.append(
    Paragraph(
        "- Offer annual contract discounts.",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "- Introduce loyalty reward programs.",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "- Reduce churn through targeted retention campaigns.",
        styles["Normal"]
    )
)

content.append(
    Paragraph(
        "- Focus on high-risk and high-value customers.",
        styles["Normal"]
    )
)

# Generate PDF
pdf.build(content)

print(
    "PDF Report Generated Successfully!"
)

print(
    "Saved At: reports/customer_churn_report.pdf"
)