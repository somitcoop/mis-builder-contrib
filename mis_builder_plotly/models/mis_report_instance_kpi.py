from odoo import models, fields, api, _


class MisReportInstanceKpi(models.Model):
    _name = "mis.report.instance.kpi"

    mis_report_instance_id = fields.Many2one(
        'mis.report.instance',
        string="Report Instance",
        required=True
    )
    report_kpi_ids = fields.One2many(
        'mis.report.kpi',
        related="mis_report_instance_id.report_id.kpi_ids"
    )
    kpi_id = fields.Many2one(
        'mis.report.kpi',
        domain="[('id', 'in', report_kpi_ids)]",
        ondelete="cascade",
        required=True
    )

    kpi_style_id = fields.Many2one(
        'mis.report.plotly.style',
        string="KPI Style",
        store=True,
        compute='_compute_kpi_style_id',
        required=True
    )
    

    @api.depends('kpi_id')
    @api.onchange('kpi_id')
    def _compute_kpi_style_id(self):
        for record in self:
            if record.kpi_id:
                record.kpi_style_id = record.kpi_id.plotly_style_id
            else:
                record.kpi_style_id = False
