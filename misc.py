import json, random, os
import constants
from datetime import date, time, datetime
from github import Github

g = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'])


class misc():

    def randomDice(self):
        number = random.randint(0,6)
        return (str(number))

    def randomCoin(self):

        flip = random.randint(0,1)
        if (flip == 0):
            return ('Heads')
        else:
            return ('Tails')

    def quitter(self):
        d = date.today()
        e = date(year=constants.QUITTER_YEAR, month=constants.QUITTER_MONTH, day=constants.QUITTER_DAY)
        delta = d-e
        return (delta.days)
    
    def githubWrite(self, user, callout):
                      
        repo = g.get_repo(constants.REPOSITORY_NAME)
        contents = repo.get_contents('callouts.json')
        testContent = contents.decoded_content.decode('utf8')
        data = json.loads(testContent)
        count = 1

        if (user in data):
            calloutLength = len(data[user][0])
            data['temp']=[{}]
            if (calloutLength == 6):
                while (count != 6): 
                    for users in data[user]:
                        data['temp'][0][str(count)] = users[str(count + 1)]
                        count+=1
                data['temp'][0][str(calloutLength)] = callout
                data[user]=data.pop('temp')
                result = json.dumps(data)
            else:
                data.pop('temp')
                data[user][0][str(len(data[user][0])+1)] = str(callout)
                result = json.dumps(data)
            repo.update_file(contents.path, 'Updated with new content', result, contents.sha)
        elif (user not in data):
            data[user]=[{}]
            data[user][0]['1']= str(callout)
            result = json.dumps(data)            
            repo.update_file(contents.path, 'Updated with new user', result, contents.sha)
            

    def calloutAll(self, user):

        callOutList = []
        repo = g.get_repo(constants.REPOSITORY_NAME)
        contents = repo.get_contents('callouts.json')
        testContent = contents.decoded_content.decode('utf8')
        data = json.loads(testContent)

        if (user in data):
            count = len(data[user][0]) - 1
            while (count != -1):
                callOutList.append(data[user][0][str(count)])
                count -= 1
            return(callOutList)
        elif (user not in data):
            return ('This user has not been called out yet')

    def puns(self):

        file = open('puns.json') 
        with file as f:
            data = json.load(f)
        file.close()
        
        number = random.randint(1,len(data['Puns'][0]))
        for item in data['Puns']:
            return (str(item[str(number)]))

    def londaQuotes(self):
        file = open('quotes.json') 
        with file as f:
            data = json.load(f)
        file.close()

        number = random.randint(1,len(data['Linda']))

        for references in data['Linda']:
            if (references['id'] == str(number)):
                if (references['type'] == 'string'):
                    return ('String', references['content'])
                elif (references['type'] == 'picture'):
                    return ('Picture', references['content'])