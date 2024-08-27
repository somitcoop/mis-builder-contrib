from odoo import _, fields, models


class MisReport(models.Model):
    _inherit = "mis.report"

    plotly_style_id = fields.Many2one(string="Plotly Style", comodel_name="mis.report.plotly.style")


class MisReportKpi(models.Model):
    _inherit = "mis.report.kpi"

    
    plotly_style_id = fields.Many2one(string="Plotly Style", comodel_name="mis.report.plotly.style")