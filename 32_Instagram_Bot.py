from instagrapi import Client

# Login
cl = Client()
cl.login("your_username", "your_password")

# Follow a user
username_to_follow = "some_user"
user_id = cl.user_id_from_username(username_to_follow)
cl.user_follow(user_id)

# Unfollow a user
cl.user_unfollow(user_id)
