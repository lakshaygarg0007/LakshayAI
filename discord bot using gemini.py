import discord
import os
import google.generativeai as genai


genai.configure(api_key=os.environ['GENAI_KEY'])
model = genai.GenerativeModel('gemini-pro')

class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.author == client.user:
      return
    if client.user.mentioned_in(message):
      channel = message.channel
      response = model.generate_content(message.content)
      await channel.send(response.text)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['DISCORD_SERVER_TOKEN'])
