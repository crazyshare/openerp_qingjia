# -*- coding: utf-8 -*-
{
    'name': "qingjia",

    'summary': """请假功能测试模块""",

    'description': """
       请假功能测试模块
    """,

    'author': "上海善之农生物科技有限公司",
    'website': "http://www.caimaimai.com.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    #'depends': ['website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'application': True,    
}