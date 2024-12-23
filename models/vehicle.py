# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

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
    needs_service = fields.Boolean(
        string="Needs Service",
        compute="_compute_needs_service",
        store=True,
    )

    @api.model
    def _validate_license_plate(self, license_plate):
        if self.search_count([("license_plate", "=", license_plate)]) > 0:
            raise ValidationError(_("License Plate already exists"))

    # COMPUTED FIELDS
    @api.depends("mileage", "last_service_date")
    def _compute_needs_service(self):
        """Computes if the vehicle needs service according to the mileage
        or the last service date."""
        for vehicle in self:
            vehicle.needs_service = (
                vehicle.mileage > 20000
                or (fields.Date.today() - vehicle.last_service_date).days
                > MONTHS_TO_SERVICE * 30
            )

    @api.onchange("fuel_type")
    def _onchange_fuel_type(self):
        for vehicle in self:
            if vehicle.fuel_type == "electric":
                vehicle.mileage = 0

    # ACTIONS
    def action_schedule_service(self):
        """Show a popup to schedule the service."""

    # OVERRIDES
    @api.model_create_multi
    def create(self, vals):
        license_plates = list(map(lambda x: x.get("license_plate").upper(), vals))
        if len(set(license_plates)) != len(license_plates):
            raise ValidationError(_("License Plate must be unique"))
        for val in vals:
            # Save the license plate in uppercase
            val["license_plate"] = val.get("license_plate").upper()
            self._validate_license_plate(val["license_plate"])

        return super().create(vals)
