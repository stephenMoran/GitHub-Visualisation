from github import Github
from githubApp.models import gitUser, link

def loginUser(user):
    print(user.get_user().name)
    repos = user.get_user().get_repos()

    for follower in user.get_user().get_followers():
        print(follower.login)
    currentUser = user.get_user()
    return currentUser


def getFollowers(user, login):
    user = login.get_user(user)
    followers = user.get_user().get_followers()
    user = login.get_user(user)
    #creating user in database
    gitUser.objects.create(name = user.login, weight = user.followers)
    #save username in database
    #for follower in user.get_user().get_followers():

        #search to see if follower id in database
        #if so make link

#def makeLinks():

#def getLinks(currentUser, userNames)
##{

#}
