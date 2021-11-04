# import the appJar library
from appJar import gui
app = gui("Username Manager", "500x550")
app.setStretch("column")
app.setSticky("nesw")

#load usernames
usernamesTxt = "usernames.txt"
usernames = []
with open(usernamesTxt) as openFile:
    for line in openFile:
        usernames.append(line.split()[0])

def removeUser(user):
    if user in usernames:
        usernames.remove(user)
        app.openScrollPane("users")
        app.removeButton(user)
        app.stopScrollPane()

#widget functions
def addClick(user):
    #add name to array if it doesnt exist
    if user not in usernames:
        usernames.append(user)
        app.setEntry("username", "")
        app.openScrollPane("users")
        app.addButton(user, removeUser)
        app.stopScrollPane()


def saveUsers():
    f = open(usernamesTxt, "w")
    f.write("\n".join(sorted(usernames, key=str.lower)))
    f.close()

def enterPress():
    addClick(app.getEntry("username"))


#create widgets
app.addLabel("title", "Username Manager",colspan=3 )
row = app.getRow()
app.addEntry("username", row,0)
app.enableEnter(enterPress)
app.addButton("Save", saveUsers, row,1)
#scroll frame
app.startScrollPane("users", colspan=3)
app.setScrollPaneHeight("users",500)
for user in usernames:
    app.addButton(user, removeUser)

# scuffed way of setting length of buttons
app.addButton("---------------------------------------------------------------------------------------------------",removeUser)
app.stopScrollPane()


#configure widgets

#run app
app.go()