import discord
import sqlite3
import os
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

# Définir le chemin du dossier "static"
static_folder = "static"

# Fonction pour sauvegarder un message en tant que fichier audio
current_file_path = None

def save_message(message):
    global current_file_path

    # Supprimer le fichier audio précédent s'il existe
    if current_file_path and os.path.exists(current_file_path):
        os.remove(current_file_path)

    # Générer le fichier audio et le sauvegarder
    tts = gTTS(message, lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    audio_folder = os.path.join(static_folder, "audio")
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    current_file_path = os.path.join(audio_folder, "message.mp3")
    with open(current_file_path, "wb") as audio_file:
        audio_file.write(audio_fp.read())

    return current_file_path

@bot.command()
@commands.check(isOwner)
async def coucou(ctx):
    await ctx.send("Coucou")

    # Génération de la synthèse vocale
    message = "Coucou"
    
    # Enregistrez le message comme un fichier audio
    file_path = save_message(message)

    # Informer que le fichier a été sauvegardé localement
    await ctx.send(f"Le fichier audio a été sauvegardé localement : `{file_path}`")
# Discord: !coucou

@bot.command()
@commands.check(isOwner)
async def serverInfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur {serverName} contient {numberOfPerson} personnes ! \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
    await ctx.send(message)

    # Enregistrez le message comme un fichier audio
    file_path = save_message(message)

    # Informer que le fichier a été sauvegardé localement
    await ctx.send(f"Le fichier audio a été sauvegardé localement : `{file_path}`")    
# Discord: !serverInfo

@bot.command()
@commands.check(isOwner)
async def say(ctx, *texte):
    # Envoyer le texte en tant que message texte dans le salon Discord
    await ctx.send(" ".join(texte))

    # Génération de la synthèse vocale
    message = " ".join(texte)
    
    # Enregistrez le message comme un fichier audio
    file_path = save_message(message)

    # Informer que le fichier a été sauvegardé localement
    await ctx.send(f"Le fichier audio a été sauvegardé localement : `{file_path}`")

@bot.command()
@commands.check(isOwner)
async def clear(ctx, nombre: int = 1):
    await ctx.channel.purge(limit=nombre + 1)
    await ctx.send(f"{nombre} messages effacés !")

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
    d_location = response

    requete = f"""
    SELECT SUM(nb_doses) AS somme_nb_doses
    FROM app_f_flux
    WHERE D_LOCATION = '{d_location}'
    AND strftime('%Y', D_DATE) = '2021'
    AND strftime('%W', D_DATE) = strftime('%W', 'now', 'localtime');
    """

    cursor.execute(requete)
    resultat = cursor.fetchone()
    somme_nb_doses = resultat[0] if resultat else None

    await ctx.send(f"Somme des doses dans la table de fait pour la clé 'D_LOCATION' **{d_location}** pour la semaine actuelle en 2021 : **{somme_nb_doses} doses**")
    await ctx.send("Voici le lien GitHub du projet 'Pharma Post': **https://github.com/Jerome-Reviron/Pharma_post**")

    # Génération de la synthèse vocale
    tts = gTTS(f"Somme des doses dans la table de fait pour la clé 'D_LOCATION' {d_location} : {somme_nb_doses} doses. Voici le lien GitHub du projet Pharma Post : https://github.com/Jerome-Reviron/Pharma_post", lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Enregistrez le message comme un fichier audio
    file_path = save_message(f"Somme des doses dans la table de fait pour la clé 'D_LOCATION' {d_location} : {somme_nb_doses} doses. Voici le lien GitHub du projet Pharma Post : https://github.com/Jerome-Reviron/Pharma_post")
    
    # Informer que le fichier a été sauvegardé localement
    await ctx.send(f"Le fichier audio a été sauvegardé localement : `{file_path}`")
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
    # Requète sql db_browser:
    # SELECT
    #     SUM(app_f_flux.nb_doses) AS somme_nb_doses
    # FROM
    #     app_f_flux
    # JOIN
    #     app_d_location ON app_f_flux.D_LOCATION = app_d_location.code_region_code_departement
    # WHERE
    #     app_d_location.libelle_departement = 'Puy-de-Dôme'
    #     AND strftime('%Y', app_f_flux.D_DATE) = '2021'
    #     AND strftime('%W', app_f_flux.D_DATE) = strftime('%W', 'now', 'localtime');

    # Exécution de la requête
    cursor.execute(requete)

    # Récupération du résultat
    resultat = cursor.fetchone()
    somme_nb_doses = resultat[0] if resultat else None

    # Définir le chemin du dossier "static/audio"
    static_audio_folder = os.path.join("static", "audio")
    if not os.path.exists(static_audio_folder):
        os.makedirs(static_audio_folder)

    # Génération de la synthèse vocale
    tts = gTTS(f"Somme des doses pour le département {libelle_departement} : {somme_nb_doses} doses. Voici le lien GitHub du projet Pharma Post : https://github.com/Jerome-Reviron/Pharma_post", lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Enregistrez le message comme un fichier audio dans le dossier "static/audio"
    file_path = os.path.join(static_audio_folder, "message.mp3")
    with open(file_path, "wb") as audio_file:
        audio_file.write(audio_fp.read())

    # Informer que le fichier a été sauvegardé localement
    await ctx.send(f"Le fichier audio a été sauvegardé localement : `{file_path}`")
# Discord: !le_bon_coin

# Commande Troisième
@bot.command()
@commands.check(isOwner)
async def en_terre_inconnue(ctx):
    # Répondre à l'utilisateur
    await ctx.send("Renseignez la région souhaitée !")

    # Attendre une réponse de l'utilisateur
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_response = await bot.wait_for('message', check=check, timeout=60)
    except TimeoutError:
        await ctx.send("Délai expiré. Réessayez plus tard.")
        return

    # Traiter la réponse de l'utilisateur
    await far_west(ctx, user_response.content)

async def far_west(ctx, libelle_region):
    # Récupération des code_region_code_departement depuis la table app_d_location
    cursor.execute(f"""
        SELECT code_region_code_departement
        FROM app_d_location
        WHERE libelle_region = '{libelle_region}';
    """)
    codes_region_code_departement = cursor.fetchall()

    if not codes_region_code_departement:
        await ctx.send("Région non trouvée.")
        return

    # Initialiser la somme des doses
    somme_nb_doses = 0

    # Exemple de requête pour obtenir la somme des doses avec D_LOCATION dynamique
    for code_region_code_departement in codes_region_code_departement:
        requete = f"""
        SELECT SUM(nb_doses) AS somme_nb_doses
        FROM app_f_flux
        WHERE D_LOCATION = '{code_region_code_departement[0]}'
        AND strftime('%Y', D_DATE) = '2021'
        AND strftime('%W', D_DATE) = strftime('%W', 'now', 'localtime');
        """
        # requète db_browser:
        # SELECT
        #     SUM(app_f_flux.nb_doses) AS somme_nb_doses
        # FROM
        #     app_f_flux
        # JOIN
        #     app_d_location ON app_f_flux.D_LOCATION = app_d_location.code_region_code_departement
        # WHERE
        #     app_d_location.libelle_region = 'ARA'
        #     AND strftime('%Y', app_f_flux.D_DATE) = '2021'
        #     AND strftime('%W', app_f_flux.D_DATE) = strftime('%W', 'now', 'localtime');

        cursor.execute(requete)

        # Récupération du résultat
        resultat = cursor.fetchone()
        somme_nb_doses += resultat[0] if resultat else 0

    # Définir le chemin du dossier "static/audio"
    static_audio_folder = os.path.join("static", "audio")
    if not os.path.exists(static_audio_folder):
        os.makedirs(static_audio_folder)

    # Génération de la synthèse vocale
    tts = gTTS(f"Somme des doses pour la région {libelle_region} : {somme_nb_doses} doses. Voici le lien GitHub du projet Pharma Post : https://github.com/Jerome-Reviron/Pharma_post", lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Enregistrez le message comme un fichier audio dans le dossier "static/audio"
    file_path = os.path.join(static_audio_folder, "message.mp3")
    with open(file_path, "wb") as audio_file:
        audio_file.write(audio_fp.read())

    # Informer que le fichier a été sauvegardé localement
    await ctx.send(f"Le fichier audio a été sauvegardé localement : `{file_path}`")
# Discord: !en_terre_inconnue

@bot.event
async def on_disconnect():
    conn.close()

bot.run(token)
