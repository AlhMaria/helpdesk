# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_ids = fields.One2many(
        string="Project id",
        comodel_name="project.project",
        inverse_name="sale_order_id"
    )

    def _prepare_project_vals(self):
        self.ensure_one()
        name = u" %s - %s - %s" % (
            self.partner_id.name,
            date.today().year,
            self.name)

        return {
            'user_id': self.user_id.id,
            'name': name,
            'partner_id': self.partner_id.id,
        }

    @api.multi
    def action_create_project(self):
        project_obj = self.env['project.project']
        for order in self:
            if order.project_ids:
                raise Warning((
                    'There is a project already related with this sale order.'
                ))
            vals = order._prepare_project_vals()
            project = project_obj.create(vals)
            order.write({
                'project_ids': [(6, 0, [project.id])]
            })
            return True

    @api.multi
    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        self.action_create_project()

    # @api.multi
    # def action_create_project(self):
    #     project_obj = self.env['project.project']
    #     for order in self:
    #         if order.project_ids:
    #             raise Warning((
    #                 'There is a project already related with this sale order'
    #             ))
    #         vals = order._prepare_project_vals()
    #         project = project_obj.create(vals)
    #         order.write({
    #             'project_ids': [(6, 0, [project.id])]
    #         })
    #         return {
    #             'name': 'Project Form',
    #             'view_type': 'form',
    #             'view_mode': 'form',
    #             'res_model': 'project.project',
    #             'res_id': project.id,
    #             'type': 'ir.actions.act_window',
    #         }
