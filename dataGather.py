from github import Github
from githubApp.models import gitUser, link

def loginUser(user):
    print(user.get_user().name)
    repos = user.get_user().get_repos()
    currentUser = user.get_user()
    return currentUser


def getFollowers(username, login):
    user = login.get_user(username)
    followers = user.get_followers()
    #gitUser.objects.create(name = user.login, weight = user.followers)
    #gitUser.objects.create(name = user.login, weight = user.followers)
    #Find links between nodes
    for follower in followers:
        follower = follower.login
        linkedTo = gitUser.objects.filter(name = follower)
        for user in linkedTo:
            print(user.name)
            print(username)
            link.objects.create(source= username, target = user.name)

    #creating user in database

    #save username in database
    #for follower in user.get_user().get_followers():

        #search to see if follower id in database
        #if so make link

#def makeLinks():

#def getLinks(currentUser, userNames)
##{

#}
