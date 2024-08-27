from odoo import models, fields, api, _


class MisReportInstancePeriod(models.Model):
    _inherit = "mis.report.instance.period"


    use_in_plotly = fields.Boolean(
        string="Use in Plotly",
        default=True,
    )