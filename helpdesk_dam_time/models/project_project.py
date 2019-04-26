# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Project(models.Model):
    _inherit = 'project.project'

    ticket_ids = fields.One2many(
        string="HelpDesk Ticket",
        comodel_name="helpdesk.ticket",
        inverse_name="project_id"
    )

    sale_order_id = fields.Many2one(
        comodel_name="sale_order")
