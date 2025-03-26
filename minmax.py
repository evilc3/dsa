'''
consider a state
board 
 _O_|___|_X_
 _X_|___|_X_
    | O | O
    
1 -> 4 -> 7  +3
2 -> 5 -> 8  +3
3 -> 6 -> 9  +3

1. start pos with 1 with 9
2. Base Case 
    1. player wins: -10
    2. you win: +10
    3. tie : 0

'''

current_board = ["O", 2, "X", "X", 5, "X", 7, "O", "O"]
human_player = "O"
ai_player = "X"

eval_func = {human_player: min, ai_player: max}

def get_available_actions(board):
    return [i for i in board if  i not in ["O", "X"]]


def is_terminal(board):
    
    ###check for all winning combinations.
    
    #OOO or XXX
    for i in range(0, 9, 3):
        
        if board[i]==board[i+1]==board[i+2]:
            # print('in here')
            if board[i] == human_player: 
                return -10 ### ai loose
            return 10 ### ai wins
    
    ###vertical check 
    for i in range(3):
        
        if board[i] == board[i+3] == board[i+6]:
            # print('in here v')
            if board[i] == human_player: 
                return -10 ### ai loose
            return 10 ### ai wins
        
    ### vertical 
    if board[0] == board[4] == board[8]:
        # print('in here v1')
        if board[0] == human_player: 
                return -10 ### ai loose
        return 10 ### ai wins

    ###vertical 
    if board[2] == board[4] == board[6]:
        
        # print(board)
        
        # print('in here v2')
        if board[2] == human_player: 
                return -10 ### ai loose
        return 10 ### ai wins
    

def minmax(board, current_player):
    
    val = is_terminal(board)
    
    # print('is terminal val', val)
    
    if val: return val

    possiable_actions = get_available_actions(board)
    
    # print('current player: ', current_player)
    # print(possiable_actions)
    # print(board)
    
    if possiable_actions == []: return 0 #tie case
    
    # score = float('inf') if current_board == human_player else float('-inf')
    score = 100 if current_player == human_player else -100
    
    for action in possiable_actions:
        
        new_player = human_player if current_player == ai_player else ai_player
        board[action-1] = current_player
        
        val = minmax(board, new_player)
        
        board[action-1] = action
        
        score = eval_func[current_player](score, val)
     
    return score

def get_best_step(board, current_player):
    
    possiable_actions = get_available_actions(board)

    if possiable_actions == []: {}
    
    result = {}
    
    for action in possiable_actions:
        
        board[action-1] = current_player
        new_player = human_player if current_player == ai_player else ai_player
        result[action] = minmax(board=board, current_player=new_player)
        board[action-1] = action
    
    return result        

def print_board(board):
    
    for i in range(9):
        
        if i in [3,6]: print('\n')
        
        print(board[i],'|',end="")
    
    print()


if __name__ == '__main__':
    
    # print(minmax(board = current_board, current_player=ai_player))
    # print(get_best_step(board=current_board, current_player=ai_player))
    
    # current_board = ["O", 2, "X", "X", 5, "X", 7, "O", 9]
    '''
    X |O |3 |

    X |O |O |

    O |X |X |
    '''
        
    current_board = ["X", "O", 3, "X", "O", "O", "O", "X", 9]
    
    print(get_best_step(board=current_board, current_player=ai_player))
    
    
    # exit() d
    current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print('\n\n\n')
    
    while True:
        
        print('Current Board')
        
        print_board(board=current_board)
        
        val = is_terminal(current_board)
        
        if val == -10:
            print('HUMAN WINS')
            break
        
        if val == 10:
            print('AI WINS')
            break
        
        if get_available_actions(current_board) == []: 
            print("TIE")
            break
        
        
        human_pos = int(input("Pick a position on board : (1-9) ", ))
        
        current_board[human_pos-1] = human_player
        
        ###get bot output
        results = get_best_step(board=current_board, current_player=ai_player)
        
        print('AI CHOICES:', results)
        
        best_score = -1000
        best_move = -1000
        for i in results:
            if results[i] >  best_score:
                best_score = results[i]
                best_move = i

        if best_move != -1000:
            current_board[best_move-1] = ai_player
        
        
        print('--------')