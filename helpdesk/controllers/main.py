from odoo.http import request, route, Controller
from odoo import http


class HelpdeskController(Controller):

    @route('/new_helpdesk_ticket', auth='public')
    def new_helpdesk_ticket(self, **kw):
        return http.request.render('helpdesk.new_helpdesk_ticket', {})

    @route('/new_helpdesk_ticket_done', auth='public')
    def new_helpdesk_ticket_done(self, **post):
        partner_email = post.get('partner_email')
        ticket_subjet = post.get('ticket_subjet')
        ticket_detail = post.get('ticket_detail')

        partners = request.env['res.partner'].sudo().search(
            [('email', '=', partner_email)])

        request.env['helpdesk.ticket'].sudo().create(
            {'name': ticket_subjet,
             'description': ticket_detail,
             'partner_id': partners.id,
             'project_task_id': 1})

        partner_email_done = partners and 'Partner encontrado' or \
            'Partner no encontrado'

        return http.request.render('helpdesk.new_helpdesk_ticket_done',
                                   {'partner_email_done': partner_email_done})
