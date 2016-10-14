from tkinter import *

def createLeague(): #creates a list with all teams
    file = open('Russian teams.txt', 'r')
    teams = []
    for line in file:
        team = line.split()
        teams.append(team)
    file.close()
    return teams

def getTeam(choice): #this function gets a team that user inputs
    result = ' '
    teams = createLeague()
    checkforteam = False 
    for line in teams:
        team = line[0] 
        if choice == team: #check for input team in all lines
            result = team               
            games = line[1]
            wins = line[2]     #assign all statistics to the variables with
            draws = line[3]    #appropriate names
            loses = line[4]
            checkforteam = True
    if checkforteam: #if it is True, it will return the team. If False, returns an error message
        search = result + '. Games: ' + str(games) + ', wins: ' + str(wins) + ', draws: ' + str(draws) + ', loses: ' + str(loses)
        return search
    else:
        no = 'No such a team'
        return no

def clickTeam():
    search.set(getTeam(choice.get()))

def getWinner():#returns a leader
    teams = createLeague()
    winner = ' '
    result = 0
    loses = 100
    for team in teams:
        points = int(team[2])*3 + int(team[3])
        lose = int(team[4])#counting all points
        if points > result: #find a team with maximum points
            result = points
            winner = team[0]
            loses = lose
        elif points == result: #equal? count the loses
            if lose < loses:
                winner = team[0]
    line = "Leader is " + winner + ", they score " + str(result) + " points"
    return line

def updateScore(home, goal1, away, goal2):#update the table
    teams = createLeague()
    f = open('Russian teams.txt', 'w')
    for team in teams:
        komanda = team[0]
        matches = int(team[1])
        wins = int(team[2])
        draws = int(team[3])
        loses = int(team[4])
        if home == komanda: #if home team is found
            if goal1 > goal2:
                matches += 1
                wins += 1
            elif goal1 == goal2:
                matches += 1
                draws += 1
            else:
                matches += 1
                loses += 1
        elif away == komanda: #if away team is found
            if goal1 < goal2:
                matches += 1
                wins += 1
            elif goal1 == goal2:
                matches += 1
                draws += 1
            else:
                matches += 1
                loses += 1

        newline = komanda+ ' '+ str(matches) + ' ' +str(wins)+ ' '+ str(draws) + ' '+ str(loses)+ '\n'
        f.write(newline) #rewrite the text file to update the results
    f.close()
    message = 'Saved!'
    return message

def clickTable():
    message.set(updateScore(home.get(), goal1.get(), away.get(), goal2.get()))    

#menu
loop = 1 #variable that makes 'while' working until user wants to close the program
while loop == 1:
    print('0. Exit')
    print('1. Find a team')
    print('2. Get a leader')
    print('3. Update the results')
    x = input("It's up to you. ")
    if x == '1':
        root = Tk()
        root.title("Find a team")
        root.geometry("300x150")

        Label(root, text = "Team: ").grid(row = 0, column = 0)
        choice = StringVar()
        Entry(root, textvariable = choice).grid(row = 0, column = 1)

        Label(root, text = "Result: ").grid(row = 2, column = 0)
        search = StringVar()
        Label(root, textvariable = search).grid(row = 2, column = 1)

        button = Button(root, text = "Search", command = clickTeam)
        button.grid(row = 6, column = 1, columnspan = 2)

        root.mainloop()
    elif x == '2':
        print(getWinner())
    elif x == '3':
        root = Tk()
        root.title("Update score")
        root.geometry("500x200")

        Label(root, text = "Home team: ").grid(row = 0, column = 0)
        home = StringVar()
        Entry(root, textvariable = home).grid(row = 0, column = 2)

        Label(root, text = "Home goals: ").grid(row = 2, column = 0)
        goal1 = IntVar()
        Entry(root, textvariable = goal1).grid(row = 2, column = 2)

        Label(root, text = "Away team: ").grid(row = 0, column = 6)
        away = StringVar()
        Entry(root, textvariable = away).grid(row = 0, column = 8)

        Label(root, text = "Away goals: ").grid(row = 2, column = 6)
        goal2 = IntVar()
        Entry(root, textvariable = goal2).grid(row = 2, column = 8)

        Label(root, text = "").grid(row = 10, column = 5)
        message = StringVar()
        Label(root, textvariable = message).grid(row = 10, column = 5)

        button = Button(root, text = "Update", command = clickTable)
        button.grid(row = 9, column = 3, columnspan = 3)

        root.mainloop()
    elif x == '0':
        print('Goodbye!')
        loop = 0
    else:
        print('Wrong!')
