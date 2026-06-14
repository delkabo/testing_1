

class UsersCanDo:
    def __init__(self):
    # def __init__(self, username=None, email=None, password_hash=None):
        # self.name = username
        # self.email = email
        # self.password_hash = password_hash
        self.users = []
        self.posts = []
        self.friendships = []

    def register_user(self, username, email, password_hash):
        user = {
            'id': len(self.users) + 1,
            'username': username,
            'email': email,
            'password_hash': password_hash,
            'joined_date': '2024-01-15',
            'is_active': True
        }
        self.users.append(user)
        return user

    def create_post(self, user_id, content):
        post = {
            'id': len(self.posts) + 1,
            'user_id': user_id,
            'content': content,
            'timestamp': '2024-01-15 14:30',
            'likes': 0,
            'comments': []
        }
        self.posts.append(post)
        return post

    def add_friend(self, user_id1, user_id2):
        friendship = {
            'user_id1': user_id1,
            'user_id2': user_id2,
            'since': '2024-01-15'
        }
        self.friendships.append(friendship)
        return friendship

    def like_post(self, post_id):
        for post in self.posts:
            if post['id'] == post_id:
                post['likes'] += 1
                return True
        return False

    def get_user_feed(self, user_id):
        # Получаем друзей пользователя
        friend_ids = []
        for f in self.friendships:
            if f['user_id1'] == user_id:
                friend_ids.append(f['user_id2'])
            elif f['user_id2'] == user_id:
                friend_ids.append(f['user_id1'])
        
        # Получаем посты друзей
        feed = []
        for post in self.posts:
            if post['user_id'] in friend_ids or post['user_id'] == user_id:
                feed.append(post)
        
        # Сортируем по времени (здесь просто возвращаем)
        return feed

# Использование
base_users = UsersCanDo()
print(base_users.register_user('ivan', 'ivan@mail.com', 'hash123'))
print(base_users.register_user('maria', 'maria@mail.com', 'hash456'))
print(base_users.add_friend(1, 2))
# base_users.create_post(1, 'Привет, мир!')
# base_users.get_user_feed(1)
# base_users.like_post(1)