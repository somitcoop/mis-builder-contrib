from odoo import _, fields, models


class MisReportKpi(models.Model):
    _inherit = "mis.report.kpi"
    
    use_in_plotly = fields.Boolean(
        string="Use in Plotly",
        help="This will make this KPI available for the Report Instance in the Plotly Tab",
    )
    default_plotly_style_id = fields.Many2one(
        string="Default Plotly Style",
        comodel_name="mis.report.plotly.style"
    )
