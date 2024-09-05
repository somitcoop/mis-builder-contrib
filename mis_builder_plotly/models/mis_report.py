from odoo import _, fields, models


class MisReport(models.Model):
    _inherit = "mis.report"

    plotly_style_id = fields.Many2one(
        string="Plotly Style",
        comodel_name="mis.report.plotly.style"
    )


class MisReportKpi(models.Model):
    _inherit = "mis.report.kpi"
    
    use_in_plotly = fields.Boolean(
        string="Use in Plotly",
        help="This will make this KPI available for the Report Instance in the Plotly Tab",
    )
    plotly_style_id = fields.Many2one(
        string="Plotly Style",
        comodel_name="mis.report.plotly.style"
    )