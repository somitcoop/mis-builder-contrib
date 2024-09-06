from odoo import _, fields, models


class MisReportPlotlyStyle(models.Model):
    _name = "mis.report.plotly.style"
    _description = "MIS Report Style for Plotly"

    _graph_type_selection = [
        ('scatter', 'Scatter'),
        ('bar', 'Bar'),
    ]


    name = fields.Char(string="Style name", required=True)
    
    # TODO: verify if it is neccessary
    graph_type_inherit = fields.Boolean(default=True, required=True)


    graph_type = fields.Selection(
        selection=_graph_type_selection,
        string="Graph Type",
    )
    

    # TODO: verify if it is neccessary
    color_inherit = fields.Boolean(default=True)


    # TODO: we need to implement a way for this
    color = fields.Char(
        string="Chart color",
        help="Chart color in valid RGB code (from #000000 to #FFFFFF) or Plotly CSS color",
        default="aliceblue",
    )
    