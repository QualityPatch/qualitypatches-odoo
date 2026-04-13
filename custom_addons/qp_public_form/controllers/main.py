from odoo import http
from odoo.http import request


class QPPublicFormController(http.Controller):

    @http.route('/qp/public-form/submit', type='http', auth='public', website=True, csrf=True, methods=['POST'])
    def qp_public_form_submit(self, **post):
        def to_int(value):
            try:
                return int(value) if value not in (None, '', False) else 0
            except Exception:
                return 0

        values = {
            'x_studio_order_no': post.get('order_no', '').strip(),
            'x_studio_shift_incharge': post.get('shift_incharge', '').strip(),
            'x_studio_machine_no': to_int(post.get('machine_no')),
            'x_studio_good_pcs_1': to_int(post.get('good_pcs')),
            'x_studio_rejected_pcs': to_int(post.get('rejected_pcs')),
            'x_studio_no_of_cones': to_int(post.get('no_of_cones')),
            'x_studio_fabric_length': post.get('fabric_length', '').strip(),
            'x_studio_store_in_time': post.get('store_in_time') or False,
            'x_studio_store_out_time': post.get('store_out_time') or False,
            'x_studio_machine_setup_time': post.get('machine_setup_time', '').strip(),
            'x_studio_edit_time': post.get('edit_time', '').strip(),
        }

        request.env['x_tracking_qp_orders'].sudo().create(values)
        return request.redirect('/patch-entry-form?submitted=1')
