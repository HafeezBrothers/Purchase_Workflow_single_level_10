from odoo import api, fields, models



_STATES = [
    ('draft', 'Draft'),
    ('to_approve', 'To Approve'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('done', 'Done')
]

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"   
     
    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('approval1','Approved'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
        ], string='Status', readonly=True, index=True, copy=False, default='draft', track_visibility='onchange')
     
   
     
    @api.multi
    def approv1(self):
        self.button_confirm()
         
