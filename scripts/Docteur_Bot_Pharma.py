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

# Commande principale
@bot.command()
async def quoi_de_neuf_docteur(ctx):
    # Répondre à l'utilisateur
    await ctx.send("Voulez-vous connaître une donnée?")

    # Attendre une réponse de l'utilisateur
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_response = await bot.wait_for('message', check=check, timeout=60)
    except TimeoutError:
        await ctx.send("Délai expiré. Réessayez plus tard.")
        return

    # Traiter la réponse de l'utilisateur
    await voici_la_piqure(ctx, user_response.content)

# Fonction pour traiter la réponse de l'utilisateur
async def voici_la_piqure(ctx, response):
    # Supposons que la réponse soit le paramètre pour D_LOCATION
    d_location = response

    # Exemple de requête pour obtenir la somme des doses avec D_LOCATION dynamique
    requete = f"""
    SELECT SUM(nb_doses) AS somme_nb_doses
    FROM app_f_flux
    WHERE D_LOCATION = '{d_location}'
    AND strftime('%Y', D_DATE) = '2021'
    AND strftime('%W', D_DATE) = strftime('%W', 'now', 'localtime');
    """

    # Exécution de la requête
    cursor.execute(requete)

    # Récupération du résultat
    resultat = cursor.fetchone()
    somme_nb_doses = resultat[0] if resultat else None

    # Affichage du résultat dans le chat Discord
    await ctx.send(f"Somme des doses pour '{d_location}' en 2021 (semaine actuelle) : {somme_nb_doses}")

# Discord: !quoi_de_neuf_docteur

@bot.event
async def on_disconnect():
    conn.close()

bot.run(token)
