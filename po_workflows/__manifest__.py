{

    'name':'Purchase Order WorkFlows',
    'description' : 'PO WorkFlows',
    'author' : 'Hafeez Brothers',
    'license': 'LGPL-3',
    'version' : '1.0',
    'depends' : [
                   'base', 'product','purchase',
                ],
    'data' :[   
                
                'views/purchase_cus.xml',
                'security/hr_user_rights1.xml'
            ],
    'installable' : True,
    'price':25.00,
    'currency':'EUR', 
   

}
