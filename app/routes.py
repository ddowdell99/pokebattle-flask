from app import app
from flask import render_template, request, redirect, url_for
import requests as r

from app.forms import GrabPokemon, AddToTeam
from app.models import Pokemon

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
                    try:
                        ability2 = poke_data['abilities'][1]['ability']['name'].title()
                        pokemonInfo['ability2'] = ability2
                    except:
                        pass
                    base_exp = poke_data['base_experience']
                    pokemonInfo['base_exp'] = base_exp 
                    normal_img = poke_data['sprites']['front_default']
                    pokemonInfo['default_img'] = normal_img
                    front_shiny = poke_data['sprites']['front_shiny']
                    pokemonInfo['front_shiny'] = front_shiny
                    attack_stat = poke_data['stats'][1]['base_stat']
                    pokemonInfo['attack_stat'] = attack_stat
                    hp_stat = poke_data['stats'][0]['base_stat']
                    pokemonInfo['hp_stat'] = hp_stat
                    defense_stat = poke_data['stats'][2]['base_stat']
                    pokemonInfo['defense_stat'] = defense_stat

                    pokemon_id = pokemonInfo['id']
                    pokemon_img = pokemonInfo['default_img']
                    name = pokemonInfo['name']
                    ability = pokemonInfo['ability']
                    attack = pokemonInfo['attack_stat']
                    hp = pokemonInfo['hp_stat']
                    defense = pokemonInfo['defense_stat']

                    potential_new_pokemon = Pokemon.query.filter_by(pokemon_id=pokemon_id).first()

                    if potential_new_pokemon:
                        return redirect(url_for('pokemonCard')) 

                    else:
                        pokemon = Pokemon(pokemon_id, pokemon_img, name, ability, attack, hp, defense)
                        pokemon.saveToDB()
                        return redirect(url_for('pokemonCard')) 

    return render_template('index.html', form=form)

@app.route('/PokemonCard')
def pokemonCard():
    addToTeamForm = AddToTeam()
    # print('Add to team')

    # if request.method == 'POST':
    #     print('get happened')
    #     if addToTeamForm.validate():

    #         pokemon_id = pokemonInfo.id.data
    #         pokemon_img = pokemonInfo.front_shiny.data
    #         name = pokemonInfo.name.data
    #         ability = pokemonInfo.ability.data
    #         attack = pokemonInfo.attack_stat.data
    #         hp = pokemonInfo.hp_stat.data
    #         defense = pokemonInfo.defense_stat.data
            
    #         pokemon = Pokemon(pokemon_id, pokemon_img, name, ability, attack, hp, defense)

    #         pokemon.saveToDB()

            



    return render_template('pokemon_card.html', pokemonInfo=pokemonInfo, addToTeamForm=addToTeamForm)


