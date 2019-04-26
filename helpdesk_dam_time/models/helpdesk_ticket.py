# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    #
    # @api.multi
    # def _get_domain(self):
    #     # domain = []
    #
    #     domain = [('project_id', '=', self.project_id.id)]
    #     # if self.project_id:
    #
    #     return domain
    @api.onchange('project_id')
    def apply_domain_task(self):
        if self.project_id:
            return {
                'domain': {
                    'project_task_id': [
                        ('project_id',
                            '=', self.project_id.id)]}
                }
        return {'domain': {'project_task_id': []}}

    @api.multi
    @api.onchange("project_task_id")
    def _onchange_field(self):
        self.project_id = self.project_task_id.project_id.id

    @api.multi
    @api.onchange("partner_id")
    # !!!!!!!!!!!!!!!!!!! No funciona correctamente se puede
    # elegir una tarea, cuyo proyecto no es del cliente selecionado
    def _onchange_partner_project(self):
        if self.partner_id:
            self.project_task_id = False
            return{
                'domain': {'project_id': [
                    ('partner_id', '=', self.partner_id.id)]}
            }
        return {'domain': {'project_id': [], 'project_task_id': []}}

    project_id = fields.Many2one(
        comodel_name="project.project"
    )
    project_task_id = fields.Many2one(
        comodel_name='project.task',
        required=True
    )
    planned_hours = fields.Float(
        string='Planned Hours',
        related='project_task_id.planned_hours')
    effective_hours = fields.Float(
        string='Effective Hours',
        related='project_task_id.effective_hours')
    hr_timesheet = fields.One2many(
        string='Effective Hours',
        related='project_task_id.timesheet_ids')
