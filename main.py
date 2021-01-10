import discord, random
from decouple import config
from googlesearch import search

client = discord.Client()
salutations = ['Bom dia', 'olá', 'ola', 'eae', 'Eae', 'EAE', 'bom dia', 'Boa tarde', 'boa tarde', 'boa noite', 'Boa noite', 'Oi']
salutations_response = ['Bom dia!', 'Olá!', 'Oi!', 'kk iae corno']


@client.event
async def on_ready():
    print('Logado como %s' %(client.user))

@client.event
async def on_message(message):
    if message.author == client.user: return
    
    if message.content.startswith('$olá'):
        await message.channel.send('Olá %s' %(message.author.mention))
    
    if any(salutation in message.content for salutation in salutations):
        await message.channel.send(random.choice(salutations_response))

    if message.content.startswith('$responda'):
        question = message.content.split('$responda ', 1)[1]
        response = search('"%s"' %(question), stop=1)
        for i in response:
            await message.channel.send('%s' %(i))

    if message.content.startswith('$youtube'):
        question = message.content.split('$youtube ', 1)[1]
        response = search('"%s" youtube' %(question), stop=1)
        for i in response:
            await message.channel.send('%s' %(i))

if __name__ == "__main__":
    client.run(config('TOKEN'))