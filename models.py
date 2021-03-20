# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Evenement(models.Model):
    _name = 'evenement_repas.evenement'
    _description = "evenement repas "

    titre = fields.Text(string="Titre",required=True)
    repasType = fields.Selection([ ('type1', 'Déjeuner'),('type2', 'Dinnr'),],'Type', default='type1')
    description = fields.Text(string="Description",required=True)
    organisateur = fields.Selection([ ('etudiant', 'Etudiant'),('enseignant', 'Enseignant'),('club', 'Club')],'Type', default='etudiant')
    organisateur_id = fields.Many2one('res.users', ondelete='set null', string="organisateur_email")
    
    nbrPersonne = fields.Integer(string="Nombre Attendue des personnes",required=True)
    validate = fields.Boolean(string= "evenement valider ou non",required=True)

    ressources_ids = fields.Many2many('evenement_repas.ressource', string="Event ressources")



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

    evenement_id = fields.Many2one('evenement_repas.evenement', string="Evenement")
    ressource_ids = fields.Many2many('evenement_repas.ressource', string="Ressource")
    ressource_nom = fields.Text(string="Ressource",required=True)

class Ressources(models.Model):
    _name = 'evenement_repas.ressource'
    _description = "Evenement ressources "

    ressource_type = fields.Text(string="Type",required=True)

