{

    'name':'Purchase Order WorkFlows (Single Level)',
    'description' : 'PO WorkFlows',
    'author' : 'Hafeez Brothers',
    
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
