from odoo import _, fields, models


class MisReport(models.Model):
    _inherit = "mis.report"

    # TODO: verify if it is neccessary
    plotly_style_id = fields.Many2one(
        string="Plotly Style",
        comodel_name="mis.report.plotly.style"
    )
