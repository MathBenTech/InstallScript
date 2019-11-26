# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'MathBenTechBase',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': 'INSTALL my base',
    'description': """
MathBenTechBase
===============

""",
    'depends': [
        # Custom MathBenTech
        'hr_expense_associate_with_customer',
        'hr_expense_tip',

        # Odoo base
        'account',

        'board',

        'crm',

        'portal',

        'payment',
        'payment_transfer',

        'project',

        'purchase',

        'hr',
        'hr_attendance',
        'hr_expense',
        'hr_payroll',

        'website',
        'website_crm',

        'sale',
        'stock',

        # OCA
        'web_responsive',
        'website_form_builder',
        'website_odoo_debranding',
        'website_snippet_anchor',

        # OCA server-brand
        'disable_odoo_online',
        'remove_odoo_enterprise',

        # OCA website
        'website_odoo_debranding',
        'website_no_crawler',

        # Canada
        'l10n_ca',
    ],
    'data': [],
    'installable': True,
}
