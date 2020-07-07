from odoo import api, fields, models


class tech_product(models.Model):
    _inherit = "product.template"

    state = fields.Selection([
        ('scratch', 'Brouillion'),
        ('qualifid', 'Qualifié'),
        ('valide', 'Validé'),
        ], setting='State', readonly=True, default='scratch')
    sale_noo = fields.Char('conso')
    type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service'),
        ('product', 'Article stockable')], string='Product Type', default='product', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')

    type_catégorie = fields.Selection([
        ('production', 'Production'),
        ('out_of_production', 'Hors production')], string='Type catégorie', default='production')

    def action_qualifie(self):
        for rec in self:
            rec.state = 'qualifid'
    
    def action_validate(self):
        for rec in self:
            rec.state = 'valide'


class type_category(models.Model):
    _inherit = "product.category"

    type_catégorie = fields.Selection([
        ('production', 'Production'),
        ('out_of_production', 'Hors production')], string='Type catégorie', default='production')

