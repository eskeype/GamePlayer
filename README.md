# GamePlayer

This project was made in collaboration with [pijel](https://github.com/pijel).

This repository stores currently contains a platform where users can have AI's play Tic Tac Toe (AKA Noughts and Crosses) against eachother

Currently this platform contains two different AI Game Players - a perfect Tic Tac Toe player (which can only win or tie), and a MENACE game player, which uses a simple reinforcement learning algorithm to learn the game of tic tac toe.

For a demonstration of how the Matchbox engine's capacity to learn Tic Tac Toe, run matchbox_demo.py (located in src) using Python 2.7 (will be updated soon)

The intent of this platform is to have it be a convenient way for people to train and test out AI's for simple two player games like Tic Tac Toe, and other games in the future as well.

This project was written in Python 2.7, but it will soon be ported to Python 3.x



# Specific intended changes for GamePlayer (Ordered by priority)

- Include driver scripts for training, validation (without training), and spectating particular games - IN PROGRESS

- Include documentation & tests

- Have Game's do input validation

- A demo for the Perfect Player

- Support getting basic analytics on training speed

- Update to Python 3.x


# Longterm additions

- More AI type algorithms (Q learning, minimax, monte carlo)

- More games (Complicated games like Chess & Connect 4, along with simple solved games, like Nim, Hexapawn, etc.)

- Potentially create a UI that can display the games in a neat manner
