from models.novel import NovelInfo, NovelChapter, NovelChapterDetail
from ext import db
from app import app
import enum

class NovelState(enum.Enum):
    start = 0
    middle = 1
    end = 2

def get_state(state = None):
    if state == NovelState.start or state == NovelState.middle:
        return "连载"
    elif state == NovelState.end:
        return "完结"
    else:
        return None

if __name__ == '__main__':

    print(get_state(NovelState.end))