class User:
    # pass  # Use pass to let Python know that we want to end the class/function with a blank body

    def __init__(self, user_id, username):  # Constructor
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"

# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"

user_1 = User("001", "angela")
user_2 = User("002", "jack")

print(user_1.username)
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)