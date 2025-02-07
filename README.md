# Tic-Tac-Toe with AI (Alpha-Beta Pruning)

This is a **Tic-Tac-Toe** game built using Python and **Tkinter** for the GUI. The AI opponent uses the **Alpha-Beta Pruning** optimization of the **Minimax** algorithm to decide the best moves.

## Features  
- **Customizable board size**: The user can choose the board size before starting the game.  
- **AI Difficulty levels**:  
  - **Easy:** AI searches with limited depth.  
  - **Hard:** AI searches deeper for stronger gameplay.  
- **Graphical User Interface (GUI):** The game uses **Tkinter** for an interactive interface.  
- **AI Move Calculation**: The AI evaluates moves using:
  - **Minimax Algorithm**: A decision rule for choosing the optimal move.  
  - **Alpha-Beta Pruning**: Optimizes the Minimax search by cutting unnecessary branches.  
  - **Board Evaluation Function**: Scores board states based on potential wins or threats.

## How the AI Works  
1. The AI finds the best move by calling `best_move()`, which iterates over all possible moves.  
2. The `alpha_beta_minimax()` function explores game states recursively:  
   - **Maximizing player (AI)** tries to **maximize** the score.  
   - **Minimizing player (human)** tries to **minimize** the score.  
3. **Alpha-Beta Pruning** is used to eliminate unnecessary branches and speed up the decision process.  
4. When a terminal state (**win, loss, or draw**) is reached, a score is returned.  

## Screenshots

### 1. Choosing Board Size  
<img src="https://github.com/ShadiBaramaki/Tic-Tac-Toe-AI/blob/main/Gui%20pictures/Screenshot%202025-02-07%20172244.png" width="300">

### 2. Selecting Difficulty Level  
<img src="https://github.com/ShadiBaramaki/Tic-Tac-Toe-AI/blob/main/Gui%20pictures/Screenshot%202025-02-07%20172313.png" width="300">

### 3. Empty Game Board created 
<img src="https://github.com/ShadiBaramaki/Tic-Tac-Toe-AI/blob/main/Gui%20pictures/Screenshot%202025-02-07%20172322.png" width="300">

### 4. Gameplay in Progress  
<img src="https://github.com/ShadiBaramaki/Tic-Tac-Toe-AI/blob/main/Gui%20pictures/Screenshot%202025-02-07%20172351.png" width="300">

### 5. AI Wins the Game  
<img src="https://github.com/ShadiBaramaki/Tic-Tac-Toe-AI/blob/main/Gui%20pictures/Screenshot%202025-02-07%20172403.png" width="300">

## Requirements  
- **Python 3.x**  
- **Tkinter** (included in standard Python distributions)  

## How to Run  
1. Run the script in a Python environment:  
   ```bash
   python tic_tac_toe.py
