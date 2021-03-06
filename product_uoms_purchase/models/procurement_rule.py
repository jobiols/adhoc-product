##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    @api.multi
    def _prepare_purchase_order_line(
            self, product_id, product_qty, product_uom, values, po, supplier):

        """ We modify this method to set the uom select for purchase in the
        UOMs of the product, by de onchange selected the correctly
        of the line product to avoid an error then when validate in the
         creation of the purchase line.
        """
        res = super()._prepare_purchase_order_line(
            product_id=product_id, product_qty=product_qty,
            product_uom=product_uom, values=values, po=po, supplier=supplier)

        product = self.env['purchase.order.line'].new(res)
        product.onchange_product_id()
        res['product_uom'] = product.product_uom.id
        return res
