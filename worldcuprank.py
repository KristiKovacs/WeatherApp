from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage =  'https://www.infoplease.com/people/soccer-players/all-time-world-cup-ranking-table'
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

table = soup.find('table', attrs={'class': 'sgmltable'})
results = table.find_all('tr')
print('Number of results:', len(results))

rows = []
rows.append(['Rank', 'Team', 'Matches Played', 'Wins', 'Draws', 'Losses', 'Goals For', 'Goals Against'])
print(rows)

# looped over results from the url in the table
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue

    # wrote columns to the variables
    rank = data[0].getText()
    team = data[1].getText()
    matches = data[2].getText()
    win = data[3].getText()
    draw = data[4].getText()
    loss = data[5].getText()
    goalsfor = data[6].getText()
    goalsagainst = data[7].getText()


    print('Rank:', rank)
    print('Team:', team)
    print('Matches Played:', matches)
    print('Wins:', win)
    print('Draws:', draw)
    print('Losses:', loss)
    print('Goals for:', goalsfor)
    print('Goals against:', goalsagainst)

    rows.append([rank, team, matches, win, draw, loss, goalsfor, goalsagainst])
print(rows)

with open('worldcupranking.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
