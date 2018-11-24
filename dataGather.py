from github import Github
from githubApp/models.py import gitUser, link

def loginUser(user):
    repos = user.get_user().get_repos()
    for follower in user.get_user().get_followers():
        print(follower.login)
    return user.get_user()


def getFollowers(user, login):
{

    if(user == None)
    {
        return None
    }
    user = login.get_user(user)
    #creating user in database
    gitUser.objects.create(name = user.login, weight = user.followers)
    #save username in database
    for follower in user.get_user().get_followers():
        #search to see if follower id in database
        #if so make link
}


def makeLinks():
{

}
#def getLinks(currentUser, userNames)
##{

#}
