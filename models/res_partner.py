# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    vehicle_ids = fields.One2many(
        "my.company.vehicle",
        "partner_id",
        string="Vehicles",
    )
    vehicle_count = fields.Integer(
        "Vehicles Count",
        compute="_compute_vehicle_count",
        store=True,
    )

    # COMPUTED FIELDS
    @api.depends("vehicle_ids")
    def _compute_vehicle_count(self):
        for rec in self:
            rec.vehicle_count = len(rec.vehicle_ids)
