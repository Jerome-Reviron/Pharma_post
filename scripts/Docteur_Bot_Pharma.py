import discord
import sqlite3
import asyncio
from discord.ext import commands
from gtts import gTTS
from io import BytesIO
from scripts.Config_Docteur_Token import token, boss

intents = discord.Intents.all()

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

bot = commands.Bot(command_prefix="!", description="Docteur Bot Pharma", intents=intents)

@bot.event
async def on_ready():
    print("Ready !")

def isOwner(ctx):
	return ctx.message.author.id == boss

@bot.command()
@commands.check(isOwner)
async def private(ctx):
	await ctx.send("Cette commande peut seulement etre effectuées par le propriétaire du bot !")

@bot.command()
@commands.check(isOwner)
async def coucou(ctx):
    await ctx.send("Coucou")

    # Génération de la synthèse vocale
    tts = gTTS("Coucou", lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Envoi du message vocal
    await ctx.send(content="Voici le message vocal:", file=discord.File(audio_fp, filename="coucou.mp3"))
# Discord: !coucou

@bot.command()
@commands.check(isOwner)
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
@commands.check(isOwner)
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))
# Discord: !say Comment ca vas ?

@bot.command()
@commands.check(isOwner)
async def clear(ctx, nombre: int = 1):
    await ctx.channel.purge(limit=nombre + 1)
    await ctx.send(f"{nombre} messages effacés !")
# Discord: !clear

@bot.command()
@commands.check(isOwner)
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")
# Discord: !ban @Mcgen47

@bot.command()
@commands.check(isOwner)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")
# Discord: !kick @Mcgen47

# Commande principale
@bot.command()
@commands.check(isOwner)
async def quoi_de_neuf_docteur(ctx):
    # Répondre à l'utilisateur
    await ctx.send("Renseignez la clé 'D_LOCATION' de la table de fait !")

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

    # Requête pour obtenir la somme des doses avec D_LOCATION dynamique
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
    await ctx.send(f"Somme des doses pour la clé 'D_LOCATION' de la table de fait **{d_location}** pour la semaine actuelle en 2021 : **{somme_nb_doses} doses**")
    await ctx.send("Voici le lien GitHub du projet 'Pharma Post': **https://github.com/Jerome-Reviron/Pharma_post**")

    # Génération de la synthèse vocale
    tts = gTTS(f"Somme des doses pour la clé 'D_LOCATION' de la table de fait {d_location} : {somme_nb_doses} doses. Voici le lien GitHub du projet Pharma Post : https://github.com/Jerome-Reviron/Pharma_post", lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Envoi du message vocal
    await ctx.send(content="Voici le message vocal :", file=discord.File(audio_fp, filename="quoi_de_neuf_docteur.mp3"))

# Discord: !quoi_de_neuf_docteur

# Commande secondaire
@bot.command()
@commands.check(isOwner)
async def le_bon_coin(ctx):
    # Répondre à l'utilisateur
    await ctx.send("Renseignez le département souhaité !")

    # Attendre une réponse de l'utilisateur
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_response = await bot.wait_for('message', check=check, timeout=60)
    except TimeoutError:
        await ctx.send("Délai expiré. Réessayez plus tard.")
        return

    # Traiter la réponse de l'utilisateur
    await ma_maison(ctx, user_response.content)

async def ma_maison(ctx, libelle_departement):
    # Récupération du code_region_code_departement depuis la table app_d_location
    cursor.execute(f"""
        SELECT code_region_code_departement
        FROM app_d_location
        WHERE libelle_departement = '{libelle_departement}';
    """)
    code_region_code_departement = cursor.fetchone()

    if not code_region_code_departement:
        await ctx.send("Département non trouvé.")
        return

    # Exemple de requête pour obtenir la somme des doses avec D_LOCATION dynamique
    requete = f"""
    SELECT SUM(nb_doses) AS somme_nb_doses
    FROM app_f_flux
    WHERE D_LOCATION = '{code_region_code_departement[0]}'
    AND strftime('%Y', D_DATE) = '2021'
    AND strftime('%W', D_DATE) = strftime('%W', 'now', 'localtime');
    """

    # Exécution de la requête
    cursor.execute(requete)

    # Récupération du résultat
    resultat = cursor.fetchone()
    somme_nb_doses = resultat[0] if resultat else None

    # Affichage du résultat dans le chat Discord
    await ctx.send(f"Somme des doses pour le département **{libelle_departement}** pour la semaine actuelle en 2021 : **{somme_nb_doses} doses**")
    await ctx.send("Voici le lien GitHub du projet 'Pharma Post': **https://github.com/Jerome-Reviron/Pharma_post**")

    # Génération de la synthèse vocale
    tts = gTTS(f"Somme des doses pour le département {libelle_departement} : {somme_nb_doses} doses. Voici le lien GitHub du projet Pharma Post : https://github.com/Jerome-Reviron/Pharma_post", lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Envoi du message vocal
    await ctx.send(content="Voici le message vocal :", file=discord.File(audio_fp, filename="le_bon_coin.mp3"))
# Discord: !le_bon_coin

@bot.event
async def on_disconnect():
    conn.close()

bot.run(token)
