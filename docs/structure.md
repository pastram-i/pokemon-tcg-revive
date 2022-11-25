# _api - Provides calls from FE to DB
 - main.py - Main API code (fastapi)

# _database - Provides database instance
 - card_search.py - makes pokemontcg.io api call, syncs to db

# _frontend - Provides frontend web application

# _main_game - Provides main game code
## app - Main game
 - main.py - Run game code/start server
 - battle.py - Battle processes/steps
 - board.py - Board objects for current battle
### helpers - Functions for gameplay
 - abilities.py - Functions for cards to use during battles
 - mechanics.py - Status effects and processes
## db - API calls to DB
 - abilities.py - Calls abilities table
 - player.py - Calls player table