Welcome to the Tic-Tac-Toe AI Bot demonstration!

Step 1: Introduction
We start with a simple HTML page featuring a Tic-Tac-Toe game. The board consists of 9 cells arranged in a 3x3 grid. Players can choose between Human vs Human, Human vs AI, or AI vs AI modes, and select the difficulty level: Newbie, Moderate, or Impossible.

Step 2: Setting Up the Game
When the "New Game" button is clicked, the startNewGame function initializes the board, setting all cells to empty. It also sets the current player based on the selected shape (e.g., X or O). If the game mode is AI vs AI, the AI makes the first move.

Step 3: Handling Player Moves
For Human vs Human mode, players take turns clicking on empty cells. The handleCellClick function updates the cell with the current player's symbol and checks for a win or draw using the checkWin function.

Step 4: AI Moves and Difficulty Levels
In Human vs AI or AI vs AI modes, the AI makes moves based on the selected difficulty:

Newbie: The AI makes random moves using the getRandomMove function.
Moderate: The AI uses simple heuristics to block the opponent, also implemented with getRandomMove (can be improved).
Impossible: The AI uses the getImpossibleMove function, which employs the Minimax algorithm with Alpha-Beta Pruning to ensure optimal play.
Step 5: Minimax Algorithm
The getImpossibleMove function simulates all possible moves and their outcomes:

Initialization: It sets the initial best move and value.
Simulating Moves: For each empty cell, it temporarily places the AI's symbol and evaluates the board using the minimax function.
Undoing Moves: It then removes the symbol, checking if this move is better than previous ones.
Selecting the Best Move: It updates the best move based on the optimal evaluation.
Step 6: Minimax Evaluation
The minimax function recursively evaluates game states:

Terminal State Evaluation: It checks if the current board state is a win for either player or a draw.
Maximizing and Minimizing Scores: It simulates future moves, maximizing the AI's score and minimizing the opponent's score. Alpha-Beta Pruning skips unnecessary branches, optimizing the evaluation process.
Step 7: AI Move Execution
The aiMove function executes the AI's turn:

Move Selection: It selects a move based on the difficulty level.
Updating the Board: It updates the board and checks for a win or draw.
Switching Turns: It switches the player and, if in AI vs AI mode, calls itself again after a delay.
Step 8: Conclusion
With this setup, the AI plays optimally in "Impossible" mode, ensuring it never loses. Players can enjoy a challenging game against an unbeatable AI or watch two AIs battle it out.

Enjoy your game of Tic-Tac-Toe!
