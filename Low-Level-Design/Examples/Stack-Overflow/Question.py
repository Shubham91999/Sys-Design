from typing import List
from datetime import datetime
from Vote import Vote
from Votable import Votable
from Tag import Tag
from Comment import Comment
from Commentable import Commentable

class Question(Votable, Commentable):
    def __init__(self, author, title, content, tag_names):
        self.id = id(self)
        self.author = author
        self.title = title
        self.content = content
        self.creation_date = datetime.now()
        self.answers = []
        self.tags = [Tag(name) for name in tag_names]
        self.votes = []
        self.comments = []
        

