from odoo import models, fields, api, _


class MisReportInstanceKpi(models.Model):
    _name = "mis.report.instance.kpi"

    _sql_constraints = [
        (
            "unique_kpi_report_instance_combination",
            "UNIQUE(mis_report_instance_id,kpi_id)",
            _("Kpi must be unique per Report instance"),
        )
    ]


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
        related="kpi_id.plotly_style_id"
    )