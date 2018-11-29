# GitHub-Visualisation
This is a webapp that shows a graph of users that are connected. These connections are based on users following eachother. The weight of each node in the graph is dependant on how well the node is connected to other elements of the graph. This webapp is built using the Django web framework along with D3.js for the graph visualisation and the CSS framework Bootstrap for styling. Graph information is stored in a SQLite database.

## Usage
* Log in using your GitHub credentials
* Graph is displayed of current connected users
* Use the input box to add a new user to the graph 
* If the user is following any of the current members in the graph or is followed by any then it is added to the database. 
* A link is then created between the two users and stored in the databse
* The graph is rerendered using links from the database

## Installation instructions and requirements
  
  
  ### Installation
  1. Clone git repository
  2. Navigate into project folder
  3. Install required libraries(see requirements)
  4. set-up database
      '''
      **python manage.py makemigrations**
      '''
      '''
      **python mange.py migrate**
      '''
  5. run server 
      '''
      **python manage.py runserver**
      '''
  ### Requirements
   '''
   pip install Django 
   '''
   '''
   pip install PyGithub
   '''
   '''
   pip install --upgrade django-crispy-forms
   '''

## Screenshot of system
![](https://github.com/stephenMoran/GitHub-Visualisation/blob/master/systemScreenshot.PNG)
