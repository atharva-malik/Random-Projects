use std::cmp::max;
use std::cmp::min;

#[derive(Clone, Copy, PartialEq)]
enum Player {
    X,
    O,
}

#[derive(Clone, Copy, PartialEq)]
enum Cell {
    Empty,
    X,
    O,
}

#[derive(Clone, Copy, PartialEq)]
enum GameState {
    Playing,
    XWin,
    OWin,
    Draw,
}

struct Board {
    cells: [[Cell; 3]; 3],
}

impl Board {
    fn new() -> Self {
        Board {
            cells: [[Cell::Empty; 3]; 3],
        }
    }

    // ... other board functions like placing, checking win, checking draw, etc.
}

fn minimax(board: &Board, depth: i32, is_maximizing: bool, alpha: i32, beta: i32) -> i32 {
    // ... implementation of minimax algorithm with alpha-beta pruning
}

fn main() {
    let mut board = Board::new();
    let mut current_player = Player::X;

    loop {
        board.print(); // Implement a print function for the board

        if current_player == Player::X {
            // Get human player's move
        } else {
            // AI's turn
            let best_move = find_best_move(&board, Player::O);
            board.place(best_move.0, best_move.1, Player::O);
        }

        if board.check_win(Player::X) {
            println!("X wins!");
            break;
        } else if board.check_win(Player::O) {
            println!("O wins!");
            break;
        } else if board.is_full() {
            println!("Draw!");
            break;
        }

        current_player = match current_player {
            Player::X => Player::O,
            Player::O => Player::X,
        };
    }
}

