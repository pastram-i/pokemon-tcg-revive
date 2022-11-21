![Revive](https://images.pokemontcg.io/base1/89_hires.png)
# Pokémon TCG Revive
### Version 0.0.1
##### This is not intended to be a standalone/complete game. Instead, this hopes to serve as a TCG equivelant to [Pokémon Showdown](https://pokemonshowdown.com/).

## A 'revive' of [TCG ONE](https://tcgone.net/), with newer languages and sources.
##### Hopefully provides *future-proof*-ing, whatever that really means...
##### TCG ONE is NOT an abandoned project, but is falling behind on features, UI/UX, and expansions (imo).
##### I aim to create a larger community by creating a more 'up-to-date' version.

# Play
 _Web link to be provided here when available_

# Currently using
 - [Pokémon TCG API](https://pokemontcg.io/) Donate: [Patreon](https://www.patreon.com/pokemon_tcg_api) | [ko-fi](https://ko-fi.com/pokemontcg)
 - [TCG-SDK-Python](https://github.com/PokemonTCG/pokemon-tcg-sdk-python)
 - [FastAPI](https://fastapi.tiangolo.com/tutorial/encoder/?h=json)
 
### Hope to use (in the future)
 - [Cards CSS](https://github.com/simeydotme/pokemon-cards-css) Donate: [PayPal](https://www.paypal.com/paypalme/simey/1)
 - [Pack Simulator](https://github.com/Pepper0ni/TTS-PTCG-Pack-Simulator)

# To Run/Test
 - Add `settings.cfg` in `_main_game/database`
```
[POKEMONTCG.IO API]
key = ''

[TCG API]
key = ''
```
 - Populate with personal [api key](https://dev.pokemontcg.io/dashboard) from [pokemontcg.io](https://dev.pokemontcg.io/)
    - This is free. A team key may be used in the future
 - A FE database key will be used in the future
 - Run `poetry install` in the root folder
 - Run `poetry shell` in the root folder
 
 _To add run instructions for each piece_

 # Contributing
 - Fork it ( https://github.com/[my-github-username]/pokemon-tcg-revive/fork )
 - Create your feature branch (git checkout -b my-new-feature)
 - Commit your changes (git commit -am 'Add some feature')
 - Push to the branch (git push origin my-new-feature)
 - Create a new Pull Request

 See `docs/structure.md` for details on each file.
 See `docs/main.todo` for current work.

 # Donation
Goes directly to web and database hosting. Any overage just goes to future months of hosting.

 _To add when actually running_


# _**This service, project, and/or website is not produced, endorsed, supported, or affiliated with Nintendo or The Pokémon Company. All rights, information, processes, data,  characters, etc remain the property of The Pokémon Company.**_