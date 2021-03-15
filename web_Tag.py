import uvicorn
import requests
from fastapi import FastAPI, HTTPException, status
from Tag_db import AsyncMainGameTagDB, Game

TAG_DB = AsyncMainGameTagDB()
app = FastAPI(
   title='Sonic Tag Server',
   description='Implementation of a game of Tag server by Erick Rojas'
)


async def get_game(game_id: str) -> Game:
    """
    Get game from the Tag database, otherwise raise a 404
    :param game_id: the uuid in str of the game to retrieve
    """
    the_game = await TAG_DB.get_game(game_id)
    if the_game is None:
        raise HTTPException(status_code=404, detail=f'Game {game_id} not found.')
    return the_game


@app.get('/')
async def home():
    return {'message': 'Welcome to Sonic Tag!'}


@app.get('/game/create/{game_id}', status_code=status.HTTP_201_CREATED)
async def create_game():
    new_uuid, new_term_pass = await TAG_DB.add_game()
    return {'success': True, 'game_id': new_uuid, 'termination_password': new_term_pass}


@app.post('/game/{game_id}/start')
async def start_game(game_id: str):
    the_game = await get_game(game_id)
    the_game.run()

    return {'success': True}


@app.post('/game/{game_id}/terminate')
async def delete_game(game_id: str, password: str):
    the_game = await TAG_DB.del_game(game_id, password)
    if the_game is False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Game not found')
    return {'success': True, 'delete_id': game_id}


if __name__ == '__main__':
    # payload = {'game_id': game_id }
    uvicorn.run('web_Tag:app', port=8000, log_level='info')
    # r = requests.get('http://127.0.0.1:8000', payload)
