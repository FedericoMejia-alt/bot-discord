import discord
from bot_logic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("$Hi!")
        
    elif message.content.startswith('p-2'):
        await message.channel.send("SISYPHUS PRIME")
        
    elif message.content.startswith('7-4'):
        await message.channel.send("BENJAMIN")
        
    elif message.content.startswith('p-1'):
        await message.channel.send("MINOS PRIME")
        
    elif message.content.startswith('ERES TONTO V1'):
        await message.channel.send("nuh uh +parry +disrespect")
        
    elif message.content.startswith('vas a ayudar a v2?'):
        await message.channel.send("RECONSTRUCT WHAT??? THERES NOTHING LEFT!!!")
        
    elif message.content.startswith('something wicked this ways come'):
        await message.channel.send("Kys")
        
    elif message.content.startswith('kys'):
        await message.channel.send("nuh uh +chargeback +parry +fist full of dollar")
        
    elif message.content.startswith('haz una contrasena'):
        await message.channel.send(gen_pass(10))
        
    elif message.content.startswith('vente pal p-2'):
        await message.channel.send("esta vez si hay una fiesta o me van a golpear de nuevo?")
        
    elif message.content.startswith('bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
        
      


client.run("nuh uh")