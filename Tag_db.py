from uuid import uuid4
from typing import Tuple, Dict
from Tag.MainGameTag import Game
import asyncio


class AsyncMainGameTagDB(object):
    def __init__(self):
        self._current_games: Dict[str, Game] = {}
        self._termination_passwords: Dict[str, str] = {}
        self._QUERY_TIME: float = 0.05

    async def add_game(self) -> Tuple[str, str]:
        await asyncio.sleep(self._QUERY_TIME)
        game_uuid = str(uuid4())
        game_term_password = str(uuid4())
        self._current_games[game_uuid] = Game()
        self._termination_passwords[game_uuid] = game_term_password
        return game_uuid, game_term_password

    async def get_game(self, game_id: str):
        await asyncio.sleep(self._QUERY_TIME)
        return self._current_games.get(game_id)

    async def del_game(self, game_id: str, term_pass: str) -> bool:
        try:
            await asyncio.sleep(self._QUERY_TIME)  # simulate query time
            if self._termination_passwords[game_id] == term_pass:
                del self._current_games[game_id]
                return True
            else:
                return False
        except KeyError:
            return False
