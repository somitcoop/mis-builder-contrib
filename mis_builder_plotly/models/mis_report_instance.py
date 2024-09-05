from odoo import models, fields, api, _
import plotly
import plotly.graph_objects as go
import logging

_logger = logging.getLogger(__name__)


class MisReportInstance(models.Model):
    _inherit = "mis.report.instance"


    def _compute_plotly_chart(self):
        for record in self:
            
            matrix_data = self.compute()
            _logger.debug("Preview data:\n" + str(matrix_data))

            computed_matrix = self.compute()
            periods_to_show = record.period_ids.filtered('use_in_plotly')

            if not periods_to_show:
                record.plotly_chart = plotly.offline.plot(
                    [{'x': [1, 2, 3], 'y': [2, 3, 4]}],
                    include_plotlyjs=False,
                    output_type='div'
                )
                continue
            x_labels = periods_to_show.mapped('name')
            # retrieving the 'x' periods: all the header cols that are present in the plotly_bar_periods
            x_raw = list(filter(
                lambda column: column.get('label') in x_labels,
                computed_matrix.get('header')[0].get('cols')
            ))
            x = list(map(lambda col: col.get('label'), x_raw))
            fig = go.Figure()

            # retrieving each 'y' bar for each variable (kpi)
            # TODO: usar record.plotly_kpi_ids para el for loop
            for kpi in record.report_id.kpi_ids.mapped('name'): # this loop will be split in two (Bar and Line) according to *Their own selected KPIs *
                current_row = list(filter(
                    lambda row: row.get('row_id')==kpi.name,
                    computed_matrix.get('body')
                ))[0]
                cells = list(filter(
                    lambda val: val.get('drilldown_arg').get('period_id') in periods_to_show.ids,
                    current_row.get('cells')
                ))
                y_values = list(map(lambda cell: cell.get('val') or 0, cells))

                #adding them to the plot
                # TODO: switch  kpi.plotly_style_id.type_graph == 'bar' ...'scatter'
                fig.add_trace(go.Bar(
                    name=kpi.name,
                    x=x,
                    y=y_values,
                ))
                fig.add_trace(go.Line(
                    name=kpi.name,
                    x=x,
                    y=y_values,
                ))

            fig.update_layout(barmode='relative', title_text='CashFlow') # TODO: cambiar el title al nombre del propio report instance

            _logger.debug("Preview x&y:\n" + str(x) + "\n" + str(y_values))
            _logger.debug("Preview fig:\n" + str(fig))
            record.plotly_chart = plotly.offline.plot(
                fig,
                include_plotlyjs=False,
                output_type='div'
            )

    show_plotly_chart = fields.Boolean(
        string="Add Chart preview",
        help="Shows the added possibility of previewing in a chart rather than in a table",
    )
    plotly_chart = fields.Text(
        string="Plotly Chart",
        compute=_compute_plotly_chart,
        store=False,
    )

    plotly_kpi_ids = fields.One2many(
        'mis.report.instance.kpi',
        inverse_name="mis_report_instance_id",
    )

    use_in_plotly_period_ids = fields.One2many(
        'mis.report.instance.period',
        compute="_compute_use_in_plotly_period_ids",
        store=False,
    )
    
    @api.depends("period_ids.use_in_plotly")
    def _compute_use_in_plotly_period_ids(self):
        for record in self:
            periods = record.period_ids.filtered('use_in_plotly')
            record.use_in_plotly_period_ids = periods

    def preview_plotly(self):
        # Basically a duplication of the original preview method
        self.ensure_one()
        view_id = self.env.ref("mis_builder_plotly." "mis_report_instance_result_view_plotly_form")
        return {
            "type": "ir.actions.act_window",
            "res_model": "mis.report.instance",
            "res_id": self.id,
            "view_mode": "form",
            "view_id": view_id.id,
            "target": "current",
            "context": self.env.context,
        }

    def action_plotly_add_all_kpis(self):
        """
        This action will add all the KPIs coming from the report_id
        Though if there are already KPI's the list this will simply add all the REST on the bottom
        """
        kpi_ids = self.report_id.kpi_ids

        for kpi in kpi_ids:
            self.env['mis.report.instance.kpi'].create({
                'mis_report_instance_id': self.id,
                'kpi_id': kpi.id,
                'kpi_style_id': kpi.plotly_style_id.id
            })

    def action_plotly_remove_all_kpis(self):
        self.mapped('plotly_kpi_ids').unlink()
