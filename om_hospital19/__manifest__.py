# -*- coding: utf-8 -*-
{
    'name': 'OM_hospital',
    'version': '19.0.1.0.0',
    'summary': 'Hospital Management System',
    'sequence': -100,
    'description': """Hospital Management System for Odoo 19""",
    'category': 'Hospital',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'hr',
        'sale',
        'mail',
        # 'report_xlsx',  # ✅ Removed - not available in system
        'stock',
        'product',
        'hr_payroll',
    ],
    'data': [
        # seurity
        'security/res_groups.xml',  # 1st
        'security/ir.model.access.csv',
        'security/ir_rule.xml',  # 2st

        # report
        # 'report/patient_details_template.xml',
        # 'report/salary_Letter_template.xml',
        # 'report/patient_card.xml',
        # 'report/appointment_report_details.xml',
        # 'report/report_action_view.xml',
        # 'report/action_salary_Letter.xml',
        # 'report/Emplyeereport_view.xml',
        # 'report/purchase_report.xml',

        # data
        'data/data.xml',

        # wizard
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        'wizard/all_patient_report_view.xml',

        # views
        'views/hospital_patient.xml',
        'views/hospital_doctor.xml',
        'views/hospital_appointment.xml',
        'views/tesing_orm_view.xml',
        'views/kids_view.xml',
        'views/hrpayslip_view.xml',
        'views/patient_gender_view.xml',
        'views/partner.xml',
        'views/res_partner.xml',
        # 'views/purchase_order_view.xml',
        'views/menu.xml',
        'views/sale_order.xml',

    ],
    'assets': {
        'web.assets_backend': [
            # 'om_hospital19/static/src/css/ribbon_animation.css',
            'om_hospital19/static/src/css/ribbon_blink.css',
        ],
    },
    'demo': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
