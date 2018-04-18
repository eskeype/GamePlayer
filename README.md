ddd# GamePlayer

This project was made in collaboration with [pijel](https://github.com/pijel).

This repository stores currently contains a platform where users can have AI's play Tic Tac Toe (AKA Noughts and Crosses) against eachother

Currently this platform contains two different AI Game Players - a perfect Tic Tac Toe player (which can only win or tie), and a MENACE game player, which uses a simple reinforcement learning algorithm to learn the game of tic tac toe.

The intent of this platform is to have it be a convenient way for people to train and test out AI's for simple two player games like Tic Tac Toe, and other games in the future as well.

# Specific intended changes for GamePlayer (Ordered by priority)

- Redo design for PerfectGamePlayer. It should be possible to store the game tree for a particular game.

- Include driver scripts for training, validation (without training), and spectating particular games

- Users should be able to use these with whatever game player they choose, in accordance with the Open/closed principle

- Shouldn't be limited to TicTacToe. Game details should be configurable. Perhaps let game details be a singleton object used by the match object

- Also, the selection of functions that I use for TicTacToe isn't very well organized. We should come up with a cleaner interface

# Longterm additions

- More AI type algorithms (Q learning, minimax, monte carlo)

- More games (Complicated games like Chess & Connect 4, along with simple solved games, like Nim, Hexapawn, etc.)

- Potentially create a UI that can display the games in a neat manner
