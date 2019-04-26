# Copyright 2019 Maria, Daniel, Adrian
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields

class HelpdeskActions(models.Model):
    _name = 'helpdesk.actions'
    _description = 'Helpdesk Action'

    name = fields.Char()
    actions_id = fields.Many2one('helpdesk.ticket', string="Actions")
