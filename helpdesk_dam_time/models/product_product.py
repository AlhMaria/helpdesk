# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.template'

    detours_included = fields.Boolean(string="Detours included")
    payment_type = fields.Selection(
        [('prepaid', 'Prepaid'), ('postpaid', 'Postpaid')],
        string='Payment Type')
