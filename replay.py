import imp
import sys
sys.path.insert(0,'./replays')
from replays.replay import Replay

if __name__ == '__main__':
    
    replay = Replay()
    replay.start_replay()
