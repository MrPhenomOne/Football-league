def createLeague(): #creates a list with all teams
    file = open('Russian teams.txt', 'r')
    teams = []
    for line in file:
        team = line.split()
        teams.append(team)
    file.close()
    return teams

def getTeam(choice, teams): #this function gets a team that user inputs
    result = ' '
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
    if checkforteam: #if True, it will return the team. If False, returns an error message
        search = result + '. Games: ' + str(games) + ', wins: ' + str(wins) + ', draws: ' + str(draws) + ', loses: ' + str(loses)
        return search
    else:
        nope = 'No such a team'
        return nope

def getWinner(teams): #returns a leader
    winner = ' '
    result = 0
    losses = 100
    for team in teams:
        points = int(team[2])*3 + int(team[3])
        lose = int(team[4])#counting all points
        if points > result: #find a team with maximum points
            result = points
            winner = team[0]
            losses = lose
        elif points == result: #equal? count the loses
            if lose < losses:
                winner = team[0]
    line = "Leader is " + winner + ", they score " + str(result) + " points"
    return line

def updateScore(home, goal1, away, goal2, teams):
    f = open('Russian teams.txt', 'w') #update the table
    for team in teams:
        komanda = team[0]
        matches = int(team[1])
        wins = int(team[2])
        draws = int(team[3])
        loses = int(team[4])
        if home == komanda:#if home team is found
            matches += 1        
            if goal1 > goal2:
                wins += 1
            elif goal1 == goal2:
                draws += 1
            else:
                loses += 1
        elif away == komanda: #if away team is found
            matches += 1
            if goal1 < goal2:
                wins += 1
            elif goal1 == goal2:
                draws += 1
            else:
                loses += 1
        newline = komanda+ ' '+ str(matches) + ' ' +str(wins)+ ' '+ str(draws) + ' '+ str(loses)+ '\n'
        f.write(newline) #rewrite the text file to update the results
    f.close()
    message = 'Saved!'
    return message
        

#main program
teams = createLeague()

#menu
loop = 1 #variable that makes 'while' working until user wants to close the program
while loop == 1:
    print('0. Exit')
    print('1. Find a team')
    print('2. Get a leader')
    print('3. Update the results')
    x = input("It's up to you. ")
    if x == '1':
        choice = input('Enter a team: ')
        print(getTeam(choice, teams))
    elif x == '2':
        print(getWinner(teams))
    elif x == '3':
        home = input('Home team: ')
        goal1 = int(input('Goals scored by home: '))
        away = input('Away team: ')
        goal2 = int(input('Goals score by away team: '))
        print(updateScore(home, goal1, away, goal2, teams))
    elif x == '0':
        print('Goodbye!')
        loop = 0
    else:
        print('Wrong!')

