import json, random, os

class misc():

    def clientToken(self):
        return (os.environ['DISCORD_TOKEN'])

    def randomDice(self):
        return (random.randint(0,6))

    def randomCoin(self):

        flip = random.randint(0,1)
        if (flip == 0):
            return ('Heads')
        else:
            return ('Tails')

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
