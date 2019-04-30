# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    ticket_id = fields.Many2one(
        string="Ticket",
        comodel_name="helpdesk.ticket")

    # TODO: Heredar funcion de creacion de devolucion

    def _create_returns(self):
        res = super(
            StockReturnPicking, self)._create_returns()

        ticket = self.ticket_id.id

        stock_picking = self.env['stock.picking']
        picking_return = stock_picking.browse(res[0])
        picking_return.write({'ticket_id': ticket})
        return res[0], res[1]
