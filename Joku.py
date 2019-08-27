import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio
import logging
import random
import discord.emoji
import discord.user
import discord.activity
import discord.member
import socketserver
import discord.channel
from discord import Member
from discord import Emoji
from discord.ext.commands import has_permissions, MissingPermissions, MissingAnyRole, MissingRole, has_any_role, has_role
import re
import datetime
import io

client = commands.Bot(command_prefix='"')
TOKEN = 'NjAxNTQwMTg1MTUwMTkzNjY4.XTDzig.3P-4ju9EnRWtdGenOCXnF1UNe2A'

#Wiadomość powitalna na konsoli

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Piszę bota do discorda"))
    print('Bot jest gotowy!')

@client.event
async def on_member_join(member):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        description=f"Witaj <@{member.id}> na serwerze **Sowie Imperium!** \n \n Zapoznaj się z zasadami \n Znajdziesz je na kanale <#573893391746596874> \n \n **Życzymy miłej zabawy!**"
    )

    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text=f'{member.guild}', icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    role = discord.utils.get(member.guild.roles, name='Członek')

    channel = client.get_channel(id=600337781654552577)
    await channel.send(embed=embed)
    await member.add_roles(role)

@client.event
async def on_member_remove(member):

    embed = discord.Embed(
        colour=discord.Colour.blue(),
        description=f"Użytkownik <@{member.id}> Opuścił nas! \n \n Co za gościu!"
    )

    embed.set_thumbnail(url=f'{member.avatar_url}')
    embed.set_author(name=f'{member.name}', icon_url=f'{member.avatar_url}')
    embed.set_footer(text=f'{member.guild}', icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=600337940924858413)
    await channel.send(embed=embed)

#Błąd po wpisaniu źle komendy

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**Chyba wpisałeś coś źle...**')

#Ciekawostka o RadweiNie

@client.command(aliases=['RadweiN', 'RADWEIN', 'Radwein', 'radweiN', 'RadwaiN', 'radwain', 'RADWAIN'])
async def radwein(ctx):
    responses = ['**HEIL**',
                 '**Był Nadzorcą na ULNCMC, ciekawe co spowodowowało że już nie jest...**',
                 '**RadweiN kiedy doki doki?**',
                 '****']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

@client.command(aliases=['NANI', 'Nani'])
async def nani(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('**NANIII!**')

@client.command()
async def magia1(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('Jak sie nie da patrz ! \n :) \n XD')

@client.command()
async def magia2(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(':)')

@client.command()
async def magia3(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('Ale dzban :)')

#Komenda na gifa z porno


@client.command(aliases=['Porno', 'PORNO'])
@commands.has_role("18+")
async def porno(ctx):
    responses = ['https://imgur.com/MgCc4H9',
                 'https://imgur.com/LMz79Kv',
                 'https://imgur.com/AhC4yD2',
                 'https://imgur.com/aExF7sR',
                 'https://imgur.com/NHUZaCD']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'**Proszę **\n {random.choice(responses)} ')

#Komenda na biust

@client.command(aliases=['Cycki', 'CYCKI'])
@commands.has_role("18+")
async def cycki(ctx):
    responses = ['https://imgur.com/r7TjnBJ',
                 'https://imgur.com/aaey49a',
                 'https://imgur.com/Ufp2zsi',
                 'https://imgur.com/KGtYLlF']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'**Proszę **\n {random.choice(responses)} ')

#Komenda na ciekawostkę o przemo

@client.command(aliases=['Przemo', 'PRZEMO', 'PrzemoSówka', 'PrzemoSowka', 'PRZEMOSOWKA', 'PrzemoSOWKA', 'PRZEMOSowka', 'PRZEMOSówka'])
async def przemo(ctx):
    responses = ['**Wielmożny car naszego potężnego imperium** 😃',
                 '**Te, bo bana wyrwiesz ** ',
                 '**A dajcie mu spokój** 😃',
                 '**To ten car, nie ? ** 😃']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

#Ciekawostka o El Wariato

@client.command(aliases=['Wariat', 'WARIAT'])
async def wariat(ctx):
    responses = ['**Holandia na zawsze, w jego sercu!** 😃',
                 '**Ale bym se zapalił...** 😃',
                 '**To ten dzban!** 😃',
                 '**Jest adminem ale i tak musi mieć pozwolenie przema**',
                 '**Masz się go bać** 😃']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

#Ciekawostka o yaroo

@client.command(aliases=['YAROO', 'Yaroo'])
async def yaroo(ctx):
    responses = ['**Jotaro, Kisama De!** 😃']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

#Ciekawostka o Pandzie

@client.command(aliases=['PANDA', 'Panda'])
async def panda(ctx):
    responses = ['**Pandy od zawsze były przyjazne sowom... Nie?** 😃',
                 '**Ulubione emotki większości serwa** 😃',
                 '**Zawarły unię personalną z naszym imperium** 😃']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

#Ciekawostka o mudzie

@client.command(aliases=['MUDA', 'Muda'])
async def muda(ctx):
    responses = ['https://tenor.com/view/dio-brando-muda-jjba-jojo-gif-5464738',
                 'https://tenor.com/view/jojo-mudamuda-nope-gif-7665433',
                 'https://tenor.com/view/muda-dio-jojo-gif-12657925']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')


#Ciekawostka o kp

@client.command(aliases=['KP', 'Kp', 'K.P', 'k.p', 'K.p'])
async def kp(ctx):
    responses = ['Jak długo na Wawelu,\n Zygmunta bije dzwon,\n Tak długo nasza Wisła,\n Zwyciężać będzie wciąż.\n \n Zwycięży orzeł biały, zwycięży polski ród\n Zwycięży nasza Wisła, bo to Krakowski klub ']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

#Ciekawostka o goku

@client.command()
async def goku(ctx):
    responses = ['**Kamehame... HAA**',
                 '**Dajcie mi swoją energię!!**',
                 '**FRIEZAAAA!**']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

#Ciekawostka o Dachim

@client.command(aliases=['Dachi', 'DACHI'])
async def dachi(ctx):
    responses = ['**Jego się obawiaj!**',
                 '**Buuu**',
                 '**Kurier go nawiedza!**',
                 '**Ponoć uczy się od RadweiNa programowania w Javie i Pythonie**']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

#Ciekawostka o Cicho

@client.command(aliases=['Cicho', 'CICHO'])
async def cicho(ctx):
    responses = ['**Pal gumsona!**',
                 '**Zawżyj się typie!**',
                 '**Pal wrota!**']
    await ctx.channel.purge(limit=1)
    await ctx.send(f'{random.choice(responses)}')

@client.command(aliases=['Penis', 'PENIS'])
async def penis(ctx):
    responses = ['**8=D**',
                 '**8==D**',
                 '**8===D**',
                 '**8====D**',
                 '**8=====D**',
                 '**8======D**',
                 '**8=======D**',
                 '**8========D**',
                 '**8=========D**',
                 '**8==========D**',
                 '**8===========D**',
                 '**8============D**']

    embed = discord.Embed(
        colour=discord.Colour.green()
    )
    embed.add_field(name=f'Maszyna rozmiaru...', value=f'Rozmiar penisa <@{ctx.author.id}> : \n {random.choice(responses)}')

    await ctx.send(embed=embed)

#Czyszczenie chatu

@client.command(aliases=['HAKAI', 'Hakai', 'HakaI'])
@commands.has_role("Moderatorzy")
async def hakai(ctx, amount: int):
    if amount==0:
        await ctx.send('Ile ty masz IQ')
    else:
        await ctx.send('**HAKAI!**')
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=amount +2)
        await ctx.send(f'**Wykonano... **')

@hakai.error
async def hakai_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.purge(limit=1)
        await ctx.send('**Podaj liczbę wiadomości którą mam zniszczyć!**')

@client.command()
@has_role("Admin")
async def warn(ctx, member: discord.Member, *, reason):
    embed = discord.Embed(
        colour=discord.Colour.orange(),
        description=f"Użytkownik <@{member.id}> został zwarnowany \n \n  **Powód:** {reason} \n \n **Przez:** <@{ctx.author.id}>")
    embed2 = discord.Embed(
        colour=discord.Colour.orange(),
        description=f"<@{member.id}> zostałeś zwarnowany \n \n  **Powód:** {reason} \n \n **Przez:** <@{ctx.author.id}>")
    await ctx.send(embed=embed)
    await member.send(embed=embed2)

@client.command()
@has_role("Admin")
async def pochwal(ctx, member: discord.Member, *, reason):
    embed = discord.Embed(
        colour=discord.Colour.orange(),
        description=f"Użytkownik <@{member.id}> został pochwalony \n \n  **Powód:** {reason} \n \n **Przez:** <@{ctx.author.id}>")
    await ctx.send(embed=embed)

@client.command()
@has_role("Boska Moc")
async def dajrole(ctx, member: discord.Member, *,  words):
    role = discord.utils.get(member.guild.roles, name=f"{words}")
    await ctx.send("Spoko, pajacu!")
    await member.add_roles(role)

@client.command()
@has_role("Admin")
async def statusbota(ctx, *, words):
    embed = discord.Embed(
        colour=discord.Colour.orange(),
        description=f"**Gra w:** {words}"
    )
    embed.set_author(name="Ustawiono status:")
    await client.change_presence(activity=discord.Game(words))
    await ctx.send(embed=embed)


"""

@client.command()
@has_role("Admin")
async def troll(ctx):
    while True:
        id = int(input("Na jakim kanale mam trollować?  "))
        channel2 = client.get_channel(id)
        command = input("Troll to będzie komenda, czy wiadomosc?  ")
        check = input("Wpisz wiadomość:  ")
        if command=="k" or "K" and check=="h":
            await channel2.send("**Podaj liczbę wiadomości którą mam zniszczyć!**")
        if command=="k" or "K" and check=="ha":
            amount = int(input("Ile mam usunac wiadomości? "))
            await channel2.send("**HAKAI!**")
            await asyncio.sleep(1)
            await channel2.channel.purge(limit=amount)
            await channel2.send("**Wykonano...**")
        if command=="k" or "K" and check=="p":
            await channel2.send("**Gdybyś miał...**")
        if command=="w" or "W":
            await channel2.send(check)

"""

client.run(TOKEN)