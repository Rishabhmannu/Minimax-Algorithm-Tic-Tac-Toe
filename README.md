# Tic Tac Toe with Minimax Algorithm - C++ and Python Implementations

Two implementations of the classic Tic Tac Toe game featuring the minimax algorithm:
1. **C++ Version**: Console-based implementation with basic AI
2. **Python Version**: GUI-based implementation with enhanced AI and optimizations

## Key Features

### C++ Implementation
- 🖥️ **Console-based interface**
- ⚡ **Basic minimax algorithm** implementation
- 🔢 **1-9 grid input system**
- 🏆 **Win/draw detection** with game state validation
- 🔄 **Turn-based gameplay** with computer opponent
- 📟 **Text-based visualizations** of game board
- 🔄 **Replayability** without restarting program

### Python Implementation
- 🎨 **Modern GUI** using Tkinter
- 🤖 **Enhanced AI** with alpha-beta pruning
- ⚡ **Performance optimizations** for faster decision making
- 🖱️ **Interactive click-based interface**
- 📊 **Real-time game status updates**
- 🔄 **Auto-reset functionality** after game completion
- 🏆 **Advanced win detection** system
- 🎮 **Player choice** to start first or second
- 💾 **State preservation** during gameplay

## Algorithms & Optimizations

### Core Algorithm
- **Minimax Algorithm** (Both Versions):
  - Decision-making algorithm for perfect gameplay
  - Recursive tree traversal for move evaluation
  - Score-based position evaluation (-10 to +10 system)

### Python-specific Optimizations
- **Alpha-Beta Pruning**:
  - Reduces search space by 30-50%
  - Dramatically improves AI response time
  - Enables deeper tree exploration
- **Memoization Patterns**:
  - Board state caching for faster evaluations
  - Efficient move prioritization
- **Object-Oriented Design**:
  - Clean separation of game logic and GUI
  - Modular components for easy maintenance

## Dependencies

### C++ Version
- **Compiler**: Any C++11 compatible compiler (g++ recommended)
- **Build Tools**: Make (optional)
- **Libraries**: Standard Library only

### Python Version
- **Python 3.6+** (Tested on 3.8+)
- **Tkinter** (Standard Python GUI library)
- **No external dependencies**

## How to Run

### C++ Version
1. Compile the program:
   ```bash
   g++ -std=c++11 -o tic_tac_toe tic_tac_toe.cpp

Run the executable:

```bash
./tic_tac_toe
```
Follow on-screen instructions (1-9 grid system)

### Python Version
Ensure Python 3 is installed

Run the script:

```bash
python3 tic_tac_toe_gui.py
```
Use mouse to click cells (1-9 grid pattern)

### Implementation Comparison

| Feature                | C++ Version         | Python Version      |
|------------------------|---------------------|---------------------|
| **Interface**          | Console             | Graphical (Tkinter) |
| **AI Algorithm**       | Basic Minimax       | Minimax + α-β Pruning |
| **Move Evaluation**    | ~500ms/move         | ~100ms/move         |
| **Input Method**       | Numeric Input       | Mouse Click         |
| **Code Structure**     | Procedural          | Object-Oriented     |
| **Dependencies**       | None                | Built-in Libraries  |
| **Visual Presentation**| Basic ASCII         | Modern GUI          |
| **Learning Focus**     | Algorithm Basics    | GUI Integration     |


License
MIT License (Add separate LICENSE file)

Developed with ❤️ by Rishabhmannu
Part of my AI Algorithm Exploration Series

