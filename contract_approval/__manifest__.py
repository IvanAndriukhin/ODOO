{
    'name': 'Contract: Approval',
    'version': '1.0.1',
    'category': '',
    'depends': ['base', 'contract', 'document_flow', 'report_docx'],
    'description': """
    """,
    'author': '',
    'support': '',
    'installable': True,
    'auto_install': True,
    'images': ['static/description/icon.png'],
    'assets': {
        'web.assets_backend': [
        ]
    },
    'data': [
        'security/contract_approval_security.xml',
        'security/ir.model.access.csv',
        'views/contract_contract_views.xml',
        'views/contract_type_views.xml',
        'views/contract_access_views.xml',
        'views/document_flow_process_template_views.xml',
        'report/report.xml'
    ],
    'demo': [
    ],
    'license': 'LGPL-3'
}
