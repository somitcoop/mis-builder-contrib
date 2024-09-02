# Copyright 2024-SomItCoop SCCL(<https://gitlab.com/somitcoop>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "MIS Builder Plotly",
    "version": "16.0.0.0.1",
    "depends": [
        "mis_builder",
        "web_widget_plotly_chart",
    ],
    "author": """
        Som It Cooperatiu SCCL,
        Odoo Community Association (OCA)
    """,
    "category": "Auth",
    "website": "https://gitlab.com/somitcoop",
    "license": "AGPL-3",
    "summary": """
    """,
    "data": [
        "security/ir.model.access.csv",
        "views/mis_report_plotly.xml",
        "views/mis_report_instance.xml",
        "views/mis_report_instance_kpi.xml",
        "views/mis_report_instance_period.xml",
        "views/mis_report_style.xml",
        "views/mis_report.xml",
    ],
    "application": False,
    "installable": True,
}
