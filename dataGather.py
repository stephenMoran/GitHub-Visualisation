from github import Github
from githubApp.models import gitUser, link

def loginUser(user):
    repos = user.get_user().get_repos()
    currentUser = user.get_user()
    return currentUser


def getFollowers(username, login):
    user = login.get_user(username)
    followers = user.get_followers()
    following = user.get_following()
    #Find links between nodes - followers
    for follower in followers:
        followerLogin = follower.login
        linkedTo = gitUser.objects.filter(name = followerLogin)
        print("hello1")
        for user in linkedTo:
            link.objects.create(source= username, target = user.name)

    #If youre following anyone in the database
    for followed in following:
        followedLogin = followed.login
        print(followedLogin + " followed by :" + username)
        linkedTo = gitUser.objects.filter(name = followedLogin)
        print(linkedTo)
        for user in linkedTo:
            link.objects.create(source= username, target = user.name)
    #only add if part of graph

    gitUser.objects.create(name = user.login, weight = user.followers)


#    for member in gitUser.objects.all():
#        memberAccount = login.get_user(member.name)
#        memberFollows = memberAccount.get_followers()
#        for follower in memberFollows:
#            print(member.name + "fllowed by " + follower.name)
#            if follower.login == user.login:
#                print("bye Bye")
##               hasConnection = True
#                link.objects.create(source= memberAccount.login, target = user.name)
#
