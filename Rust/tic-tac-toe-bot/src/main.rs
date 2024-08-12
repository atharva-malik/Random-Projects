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
    fn place(&mut self, row: usize, col: usize, player: Player) {
        self.cells[row][col] = match player {
            Player::X => Cell::X,
            Player::O => Cell::O,
        };
    }

    fn is_empty(&self, row: usize, col: usize) -> bool {
        self.cells[row][col] == Cell::Empty
    }

    fn check_win(&self, player: Player) -> bool {
        // Check rows, columns, and diagonals for a win
        for i in 0..3 {
            if self.cells[i][0] == player as Cell &&
               self.cells[i][1] == player as Cell &&
               self.cells[i][2] == player as Cell {
                return true;
            }
            if self.cells[0][i] == player as Cell &&
               self.cells[1][i] == player as Cell &&
               self.cells[2][i] == player as Cell {
                return true;
            }
        }
        if self.cells[0][0] == player as Cell &&
           self.cells[1][1] == player as Cell &&
           self.cells[2][2] == player as Cell {
            return true;
        }
        if self.cells[0][2] == player as Cell &&
           self.cells[1][1] == player as Cell &&
           self.cells[2][0] == player as Cell {
            return true;
        }
        false
    }

    fn is_full(&self) -> bool {
        self.cells.iter().flatten().all(|&cell| cell != Cell::Empty)
    }

    fn get_available_moves(&self) -> Vec<(usize, usize)> {
        let mut moves: Vec<(usize, usize)> = Vec::new();
        for i in 0..3 {
            for j in 0..3 {
                if self.cells[i][j] == Cell::Empty {
                    moves.push((i, j));
                }
            }
        }
        moves
    }
}   

fn minimax(board: &Board, depth: i32, is_maximizing: bool, alpha: i32, beta: i32) -> i32 {
    let player = if is_maximizing { Player::X } else { Player::O };

    if board.check_win(Player::X) {
        return 1;
    } else if board.check_win(Player::O) {
        return -1;
    } else if board.is_full() {
        return 0;
    }

    if is_maximizing {
        let mut best_val = std::i32::MIN;
        for move_ in board.get_available_moves() {
            let mut new_board = board.clone();
            new_board.place(move_.0, move_.1, Player::X);
            let val = minimax(&new_board, depth + 1, false, alpha, beta);
            best_val = max(best_val, val);
            alpha = max(alpha, val);
            if beta <= alpha {
                break;
            }
        }
        best_val
    } else {
        let mut best_val = std::i32::MAX;
        for move_ in board.get_available_moves() {
            let mut new_board = board.clone();
            new_board.place(move_.0, move_.1, Player::O);
            let val = minimax(&new_board, depth + 1, true, alpha, beta);
            best_val = min(best_val, val);
            beta = min(beta, val);
            if beta <= alpha {
                break;
            }
        }
        best_val
    }
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

