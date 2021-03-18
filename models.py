# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Evenement(models.Model):
    _name = 'evenement_repas.evenement'
    _description = "evenement repas "

   # repasType = fields.Char(string="Type de repas", required=True)
    repasType = fields.Selection([ ('type1', 'Type 1'),('type2', 'Type 2'),],'Type', default='type1')
    description = fields.Text(string="Description",required=True)
    nbrPersonne = fields.Integer(string="Nombre Attendue des personnes",required=True)
    validate = fields.Boolean(string= "evenement valider ou non",required=True)


class Locaux(models.Model):
    _name = 'evenement_repas.locaux'
    _description = "locaux disponibles "

    localName = fields.Text(string="Locale Name",required=True)
    disponible = fields.Boolean(string= "Disponible",required=True)


class Participents(models.Model):
    _name = 'evenement_repas.participant'
    _description = "Evenement participants "

    firstName = fields.Text(string="Nom ",required=True)
    lastName = fields.Text(string="Prenom ",required=True)
    email = fields.Text(string="Email",required=True)
    phone = fields.Text(string="Phone ",required=True)
    ressources = fields.Text(string="Ressources ",required=True)
