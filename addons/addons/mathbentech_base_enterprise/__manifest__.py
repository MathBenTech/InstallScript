# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'MathBenTech base enterprise',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': 'INSTALL my base enterprise',
    'description': """
MathBenTechBase
===============

""",
    'depends': [
        # Custom MathBenTech
        'mathbentech_base',

        'hr_expense_associate_with_customer',
        'hr_expense_tip',

        # Odoo base
        'account',

        'board',

        'contacts',

        'crm',

        'portal',

        'payment',
        'payment_transfer',

        'project',

        'purchase',

        'hr',
        'hr_expense',
        'hr_org_chart',

        'website',
        'website_crm',

        'sale',
        'sale_management',
        'stock',

        # OCA
        'website_form_builder',
        'website_snippet_anchor',

        # Canada
        'l10n_ca',
    ],
    'data': [],
    'installable': True,
}