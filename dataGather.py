from github import Github
from githubApp.models import gitUser, link

#API to gather data from github and update the datbase

#Log a user into the system
def loginUser(user):
    repos = user.get_user().get_repos()
    currentUser = user.get_user()
    return currentUser


#function to gather followers and create links between users. Results are stored in the database
def getFollowers(username, login):
    user = login.get_user(username)
    followers = user.get_followers()
    following = user.get_following()

    #Find links between nodes - followers
    gitUser.objects.create(name = user.login)
    for follower in followers:
        followerLogin = follower.login
        linkedTo = gitUser.objects.filter(name = followerLogin)

        for user in linkedTo:
            link.objects.create(source= username, target = user.name)

    #If youre following anyone in the database
    for followed in following:
        followedLogin = followed.login
        print(followedLogin + " followed by :" + username)
        linkedTo = gitUser.objects.filter(name = followedLogin)
        print(linkedTo)
        for member in linkedTo:
            link.objects.create(source= username, target = member.name)
