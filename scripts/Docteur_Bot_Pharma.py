import discord
import sqlite3
from discord.ext import commands
from scripts.Config_Docteur_Token import token

intents = discord.Intents.all()

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

bot = commands.Bot(command_prefix="!", description="Docteur Bot Pharma", intents=intents)

@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou")
# Discord: !coucou

@bot.command()
async def serverInfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
    await ctx.send(message)
# Discord: !serverInfo

@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))
# Discord: !say Comment ca vas ?

@bot.command()
async def clear(ctx, nombre: int = 1):
    await ctx.channel.purge(limit=nombre + 1)
    await ctx.send(f"{nombre} messages effacés !")
# Discord: !clear

@bot.command() 
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")
# Discord: !ban @Mcgen47

@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")


@bot.command()
async def get_doses_sum(ctx):
    requete = """
    SELECT SUM(nb_doses) AS somme_nb_doses
    FROM app_f_flux
    WHERE D_LOCATION = '84-63'
    AND strftime('%Y', D_DATE) = '2021'
    AND strftime('%W', D_DATE) = strftime('%W', 'now', 'localtime');
    """

    cursor.execute(requete)

    resultat = cursor.fetchone()
    somme_nb_doses = resultat[0] if resultat else None

    await ctx.send(f"Somme des doses pour '84-63' en 2021 (semaine actuelle) : {somme_nb_doses}")

@bot.event
async def on_disconnect():
    conn.close()

bot.run(token)
