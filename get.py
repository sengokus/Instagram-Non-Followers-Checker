import instaloader as il

class Instaloader:
    def __init__(self):
        self.session = il.Instaloader()
        self.session.login('username', 'password')

    def get_profile(self):
        profile = self.session.get_profile()
        return profile

    def get_followers(self):
        followers = self.session.get_followers()
        return followers

    def get_following(self):
        following = self.session.get_following()
        return following

    def get_non_followers(self):
        followers = self.get_followers()
        following = self.get_following()
        non_followers = list(set(following) - set(followers))
        return non_followers

api = Instaloader()
non_followers = api.get_non_followers()
print(non_followers)