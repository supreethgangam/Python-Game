import imp
import sys
sys.path.insert(0,'./src')
from src.logic import Logic

# Driver code
if __name__ == '__main__':
    
    game = Logic()
    game.start_game()

 