from odoo import _, fields, models


class MisReportPlotlyStyle(models.Model):
    _name = "mis.report.plotly.style"
    _description = "MIS Report Style for Plotly"

    _type_graph_selection = [
        ('scatter', 'Scatter'),
        ('bar', 'Bar'),
    ]


    name = fields.Char(string="Style name", required=True)

    # type
    type_graph_inherit = fields.Boolean(default=True, required=True)
    type_graph = fields.Selection(
        selection=_type_graph_selection,
        string="Graph Type",
    )

    # color
    color_inherit = fields.Boolean(default=True)
    color = fields.Char(
        string="Chart color",
        help="Chart color in valid RGB code (from #000000 to #FFFFFF)",
        default="#000000",
    )
    