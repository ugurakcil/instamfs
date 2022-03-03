import sys
import instaloader
L = instaloader.Instaloader()
L.login(sys.argv[1], sys.argv[2])
profile = instaloader.Profile.from_username(L.context, sys.argv[1])

followersIteration = profile.get_followers()
followers = list()

for follower in followersIteration:
    followers.append(follower.username)

followeesIteration = profile.get_followees()
followees = list()

for follow in followeesIteration:
    followees.append(follow.username)
    
print("mfs who don't follow back")
print("##################################")
for user in followees:
    if user not in followers:
        print(user)
