from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Team, TeamPokemonJoin, Pokemon

team = Blueprint('team', __name__, template_folder='team_templates')

@team.route('/team/create', methods=['GET', 'POST'])
def createTeam():
    return render_template