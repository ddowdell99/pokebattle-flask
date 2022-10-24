from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    team_id = db.relationship('Team', backref='team', lazy=True)

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def get_id(self):
        return (self.user_id)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()



class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __init__(self, team_id, user_id):
        self.team_id = team_id
        self.user_id = user_id


class TeamPokemonJoin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.pokemon_id'))

    def __init__(self, team_id, pokemon_id):
        self.team_id = team_id
        self.pokemon_id = pokemon_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Pokemon(db.Model):
    pokemon_id = db.Column(db.Integer, primary_key=True)
    pokemon_img = db.Column(db.String)
    name = db.Column(db.String(100), nullable=False, unique=True)
    ability = db.Column(db.String(50), nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)

    def __init__(self, pokemon_id, pokemon_img, name, ability, attack, hp, defense):
        self.pokemon_id = pokemon_id
        self.pokemon_img = pokemon_img
        self.name = name
        self.ability = ability
        self.attack = attack
        self.hp = hp
        self.defense = defense

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    
