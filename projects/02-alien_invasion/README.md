**Alien Invasion Game with Pygame**

In Alien Invasion, the player control a ship that appears at the bottom of the center.
The player can move right and left using the arrow keys and shoot bullets using the spacebar.

When the game begins, a fleet of aliens fills the sky and move across and down the screen.
The player shoots and destroys the aliens.
If the player shoots all the alien, a new fleet appears that move faster than the previous one.

If any alien hits the ship or reach the bottom of the screen, the player looses a ship.
If player looses 3 ships, he looses.

**Requirements**

- python >= 3.8
- Poetry installed on your laptop ( [https://github.com/python-poetry/poetry](https://github.com/python-poetry/poetry) )


**Run app**

*Create a new virtual environment*

```
poetry shell
```

*Install project dependencies*

```
poetry install
```

*Start the application*
inside alien_invasion folder, run:

```
python alien_invasion.py
```

The game should start in a new window.
