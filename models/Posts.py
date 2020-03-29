from pymongo import MongoClient


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.Users
        self.Posts = self.db.Posts

    def insert_post(self, data):
        self.Posts.insert({'username': data.username, 'content': data.content})
        return True

    def get_all_posts(self):
        all_posts = self.Posts.find()
        new_posts = []
        for post in all_posts:
            post['user'] = self.Users.find_one({'username': post['username']})
            new_posts.append(post)

        return new_posts
