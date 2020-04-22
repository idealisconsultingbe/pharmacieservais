# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Minimum of Quantity in shop",
    "author" : "Softhealer Technologies",
    "support": "support@softhealer.com",
    "website": "https://www.softhealer.com",
    "category": "Website",
    "summary": """
product minimum quantity odoo, set minimum quantity module, product min qty number app, goods minimum quantity odoo
    """,
    "description": """
    Are you planning to define the Minimum of quantities to the products which you are selling on your store build up with website? A minimum order quantity is often seen as a necessary evil in wholesaling, retailing, and manufacturing. You can set easily minimum of quantity No. using this module.Suppose you want to set minimum of quantity is 5, it will default value of product in shop. If customer put manual quantity (manually = 3)of product so it will automatically take minimum No of quantity(minimum = 5). Customer can decrease quantity of product relative to default quantity(default is 5) in shop or cart. If customer click button "Add to Cart" in shop, product quantity automatically set default quantity.
    product minimum quantity odoo, set minimum quantity module, product min qty number app, goods minimum quantity odoo
	""",
    "version":"13.0.1",
    "depends" : ['sale_management', 'account', 'web', 'website', 'website_sale'],
    "data" : [  
            'views/sh_product_view.xml',
            'views/assets.xml',
            'views/sh_shop_template.xml',
            ],
    
    "images": ['static/description/background.png'],
    "auto_install":False,
    "application" : True,
    "installable" : True,
    "price"       : 25,
    "currency"    : 'EUR',
}
