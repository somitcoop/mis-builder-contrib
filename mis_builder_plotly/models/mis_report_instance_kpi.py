from odoo import models, fields, api, _


class MisReportInstanceKpi(models.Model):
    _name = "mis.report.instance.kpi"


    mis_report_instance_id = fields.Many2one(
        'mis.report.instance',
        string="Report Instance",
    )
    kpi_id = fields.Many2one(
        'mis.report.kpi',
        domain=[('id', 'in', 'mis_report_instance_id.report_id.kpi_ids')],
        ondelete="cascade",
    )