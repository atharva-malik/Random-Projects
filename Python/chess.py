import chess
import chess.engine
import chess.svg


def display_board(board):
    symbol_dict = {
        'P': '♙',
        'R': '♖',
        'N': '♘',
        'B': '♗',
        'Q': '♕',
        'K': '♔',
        'p': '♟',
        'r': '♜',
        'n': '♞',
        'b': '♝',
        'q': '♛',
        'k': '♚'
    }

    print("\n  a b c d e f g h")
    print(" +-+-+-+-+-+-+-+-+")
    for i in range(8):
        row = 8 - i
        line = str(row) + "|"
        for j in range(8):
            piece = board.piece_at(8 * i + j)
            if piece:
                line += symbol_dict[piece.symbol().upper()] + "|"
            else:
                line += " |"
        print(line)
        print(" +-+-+-+-+-+-+-+-+")
    print("  a b c d e f g h\n")


board = chess.Board()
while not board.is_game_over():
    display_board(board)
    if board.turn:
        print("White's turn")
    else:
        print("Black's turn")
    move = input("Enter move: ")
    if move == 'quit':
        break
    try:
        board.push_uci(move)
    except:
        print("Invalid move.")

if board.is_checkmate():
    winner = "Black" if board.turn else "White"
    print(winner + " wins by checkmate.")
elif board.is_stalemate():
    print("Stalemate.")
elif board.is_insufficient_material():
    print("Insufficient material.")
elif board.is_seventyfive_moves():
    print("75 moves rule.")
elif board.is_fivefold_repetition():
    print("5-fold repetition.")
