# -*- coding: utf-8 -*-

from odoo import fields, models

FUEL_TYPE = [("gasoline", "Gasoline"), ("diesel", "Diesel"), ("electric", "Electric")]
MONTHS_TO_SERVICE = 6


class Vehicle(models.Model):
    _name = "my.company.vehicle"
    _description = "Vehicle"

    name = fields.Char(string="Name", required=True)
    license_plate = fields.Char(string="License Plate", required=True)
    fuel_type = fields.Selection(
        FUEL_TYPE,
        string="Fuel Type",
        required=True,
        default="gasoline",
    )
    partner_id = fields.Many2one("res.partner", string="Vehicle Owner")
    mileage = fields.Float(string="Mileage")
    last_service_date = fields.Date(
        string="Last Service Date",
        default=fields.Date.today,
    )
