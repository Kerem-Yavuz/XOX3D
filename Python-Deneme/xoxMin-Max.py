import random

# Oyun tahtası (tek bir liste)
board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        print('-' * 5)

def is_winner(player):
    # Satır, sütun ve çapraz kontrolü
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Satırlar
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Sütunlar
        [0, 4, 8], [2, 4, 6]              # Çaprazlar
    ]
    return any(all(board[pos] == player for pos in line) for line in win_positions)

def is_full():
    return all(cell != ' ' for cell in board)

def minimax(is_maximizing):
    if is_winner('O'):
        return 1
    if is_winner('X'):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def find_best_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Oyun döngüsü
print("XOX Oyunu! X oyuncusu sizsiniz, O yapay zeka.")
while True:
    print_board()

    # Kullanıcı hamlesi
    user_move = input("Hamlenizi girin (0-8): ")
    try:
        move = int(user_move)
        if board[move] != ' ':
            print("Geçersiz hamle. Tekrar deneyin.")
            continue
        board[move] = 'X'
    except (ValueError, IndexError):
        print("Geçersiz giriş. Lütfen 0-8 arasında bir sayı girin.")
        continue

    # Kazanma kontrolü
    if is_winner('X'):
        print_board()
        print("Tebrikler! X kazandı!")
        break
    if is_full():
        print_board()
        print("Beraberlik!")
        break

    # Yapay zeka hamlesi
    print("Yapay zeka düşünüyor...")
    move = find_best_move()
    if move is not None:
        board[move] = 'O'

    # Kazanma kontrolü
    if is_winner('O'):
        print_board()
        print("Yapay zeka (O) kazandı!")
        break
    if is_full():
        print_board()
        print("Beraberlik!")
        break
