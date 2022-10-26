from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Pokemon, User, teamTable
from sqlalchemy import select

team = Blueprint('team', __name__, template_folder='team_templates')

@team.route('/capture/<int:pokemon_id>')
def capturePokemon(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    if pokemon:

        current_user.capture(pokemon)

    return redirect(url_for('team.viewCurrentTeam'))

@team.route('/release/<int:pokemon_id>')
def releasePokemon(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    if pokemon:
        current_user.release(pokemon)

    return redirect(url_for('team.viewCurrentTeam'))

@team.route('/teams')
def viewTeams():
    users = User.query.all()
    for u in users:
        if Pokemon.query.join(teamTable).join(User).filter(teamTable.c.user_id == u.user_id).all():
            viewTeams = Pokemon.query.join(teamTable).join(User).filter(teamTable.c.user_id == u.user_id).all()
            print(viewTeams)
    return render_template('other_teams.html', viewTeams=viewTeams)

@team.route('/current_team')
def viewCurrentTeam():
    viewTeam = Pokemon.query.join(teamTable).join(User).filter(teamTable.c.user_id == current_user.user_id)
    print(viewTeam)
    return render_template('team.html',viewTeam=viewTeam)