from app import app
from flask import render_template, request, redirect, url_for
import requests as r

from app.forms import GrabPokemon, AddToTeam

pokemonInfo = {}

@app.route('/', methods=["GET", "POST"])
def homePage():
    form = GrabPokemon()
    if request.method == 'POST':
        if form.validate():
            pokemon = form.pokemon.data
            poke_data = {}
            response = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            if response.ok:
                data = response.json()
                poke_data = data
                for entry in poke_data:
                    id = poke_data['id']
                    pokemonInfo['id'] = id                     
                    name = poke_data['name'].title()
                    pokemonInfo['name'] = name 
                    ability = poke_data['abilities'][0]['ability']['name'].title()
                    pokemonInfo['ability'] = ability 
                    ability2 = poke_data['abilities'][1]['ability']['name'].title()
                    pokemonInfo['ability2'] = ability2 
                    base_exp = poke_data['base_experience']
                    pokemonInfo['base_exp'] = base_exp 
                    front_shiny = poke_data['sprites']['front_shiny']
                    pokemonInfo['front_shiny'] = front_shiny
                    attack_stat = poke_data['stats'][1]['base_stat']
                    pokemonInfo['attack_stat'] = attack_stat
                    hp_stat = poke_data['stats'][0]['base_stat']
                    pokemonInfo['hp_stat'] = hp_stat
                    defense_stat = poke_data['stats'][2]['base_stat']
                    pokemonInfo['defense_stat'] = defense_stat
                    return redirect(url_for('pokemonCard'))                  



                    



    return render_template('index.html', form=form)

@app.route('/PokemonCard')
def pokemonCard():
    addToTeamForm = AddToTeam()

    if request.method == 'POST':
        if addToTeamForm.validate():

            pokemon_id = pokemonInfo.id.data
            pokemon_img = pokemonInfo.front_shiny.data
            name = pokemonInfo.name.data
            ability = pokemonInfo.ability.data
            attack = pokemonInfo.attack_stat.data
            hp = pokemonInfo.hp_stat.data
            defense = pokemonInfo.defense_stat.data
            
            pokemon = Pokemon(pokemon_id, pokemon_img, name, ability, attack, hp, defense)

            pokemon.saveToDB()

            



    return render_template('pokemon_card.html', pokemonInfo=pokemonInfo, addToTeamForm=addToTeamForm)


