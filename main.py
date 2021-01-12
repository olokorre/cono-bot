import discord, random
from decouple import config
from googlesearch import search

client = discord.Client()
salutations = ['Bom dia', 'olá', 'ola', 'eae', 'Eae', 'EAE', 'bom dia', 'Boa tarde', 'boa tarde', 'boa noite', 'Boa noite', 'Oi']
salutations_response = ['Olá!', 'Oi!', 'kk iae corno', 'Oi bb :kissing_heart:']


@client.event
async def on_ready():
    print('Logado como %s' %(client.user))

@client.event
async def on_message(message):
    if message.author == client.user: return
    
    if message.content.startswith('~test'):
        await message.channel.send('Olá %s' %(message.author.mention))
    
    if any(salutation in message.content for salutation in salutations):
        await message.channel.send(random.choice(salutations_response))

    if message.content.startswith('~answer'):
        question = message.content.split('~answer ', 1)[1]
        response = search('"%s"' %(question), stop=1)
        for i in response:
            await message.channel.send('%s' %(i))

    if message.content.startswith('~youtube'):
        question = message.content.split('~youtube ', 1)[1]
        response = search('"%s" youtube' %(question), stop=1)
        for i in response:
            await message.channel.send('%s' %(i))

    if message.content.startswith('~commands'):
        await message.channel.send('`~test` = _Não faz nada muito especial..._\n`~answer [texto]` = Responde a qualquer pergunta!\n`~youtube [texto]` = Pesquisa no youtube... uau!\n`~about` = Mostra informações about mim.\n`~commands` = Mostra essa tela...')

    if message.content.startswith('~say'):
        say = message.content.split('~say ', 1)[1]
        await message.delete()
        await message.channel.send('%s' %say)

    if message.content.startswith('~about'):
        await message.channel.send('Versão: Dev\nMeu criador: olokorre#0738\nDesenvolvido em Python\nCódigo fonte: https://github.com/olokorre/cono-bot')


if __name__ == "__main__":
    client.run(config('TOKEN'))