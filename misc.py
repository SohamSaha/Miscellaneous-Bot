import json, random, os
import requests, base64
import constants
from datetime import date, time, datetime
from github import Github

g = Github(os.environ['GITHUB_TOKEN'])

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
        
        url = constants.CALLOUT_FILE_URL
        req = requests.get(url)
    
        req = req.json()
                        
        repo = g.get_repo(constants.REPOSITORY_NAME)
        contents = repo.get_contents('quotes.json')
        repo.create_file('test.json', 'test', contents.decoded_content)
            


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

# myobject = misc()
# myobject.githubWrite('Test1','hello')