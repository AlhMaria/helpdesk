# Copyright 2019 Daniel Cano, Adrián Cruz, María Alhambra
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk Time",
    "summary": "Module to Support Teams",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Daniel Cano Lozoya,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "data": [
        "views/helpdesk_ticket_view.xml",
        "views/product_product_view.xml",
        "views/sale_order_view.xml"
    ],
    "application": True,
    "installable": True,
    "depends": ["helpdesk", "project", "base", "hr_timesheet",
                "product", "sale"],
}
