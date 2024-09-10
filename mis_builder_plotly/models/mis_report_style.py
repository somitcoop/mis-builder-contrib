from odoo import _, fields, models


class MisReportPlotlyStyle(models.Model):
    _name = "mis.report.plotly.style"
    _description = "MIS Report Style for Plotly"

    _sql_constraints = [
        (
            "unique_name",
            "UNIQUE(name)",
            _("Style name field must be unique."),
        )
    ]

    _graph_type_selection = [
        ('scatter', 'Scatter'),
        ('bar', 'Bar'),
    ]

    name = fields.Char(string="Style name", required=True)
    graph_type = fields.Selection(
        selection=_graph_type_selection,
        string="Graph Type",
    )
    color = fields.Char(
        string="Chart color",
        help="Chart color in valid RGB code (from #000000 to #FFFFFF) or Plotly CSS color",
        default="aliceblue",
    )
    