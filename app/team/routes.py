from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Pokemon

team = Blueprint('team', __name__, template_folder='team_templates')

@team.route('/capture/<int:pokemon_id>')
@login_required
def capturePokemon(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    if pokemon:

        current_user.capture(pokemon)

    return redirect(url_for('homePage'))

@team.route('/release/<int:pokemon_id>')
@login_required
def releasePokemon(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    if pokemon:
        current_user.release(pokemon)

    return redirect(url_for('homePage'))

