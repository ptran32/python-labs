import click
import requests

pokemon_type = [
    'physical',
    'fighting', 
    'flying', 
    'poison', 
    'ground', 
    'rock', 
    'bug', 
    'ghost', 
    'steel', 
    'fire', 
    'water', 
    'grass', 
    'electric', 
    'psychic', 
    'ice', 
    'dragon', 
    'dark']


def get_all(limit):
    """ Get a range of pokemon and filter by type """
    pokemon_list = []

    r = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset=1.")
    data = r.json()

    # Get pokemon names and append it to the list
    for pokemon in data['results']:
        pokemon_list.append(pokemon['name'])
    
    print("I catch the pokemons below:")
    for position, pokemon in enumerate(pokemon_list):
        print(position, '-', pokemon.title())


def filter_by_type(type):
    """ Get all pokemons of the same type """
    pokemon_list = []

    r = requests.get(f"https://pokeapi.co/api/v2/type/{type}")
    data = r.json()

    for pokemon in data['pokemon']:
        pokemon_list.append(pokemon['pokemon']['name'])

    print(f"All pokemons of type {type}: \n")
    for pokemon in pokemon_list:
        print(pokemon.title())


@click.command()
@click.option('--limit', help='Limit the pokemon list', type=int)
@click.option('--type', type=click.Choice(pokemon_type), help='Filter pokemon by type')

def main(limit, type):
    click.echo("Start Pokemon Catcher...\n")
    if limit:
        get_all(limit)
    if type:
        filter_by_type(type)

if __name__ == '__main__':
    main()