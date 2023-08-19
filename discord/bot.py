import discord
from discord_functions import *

TOKEN= 'MTE0MTQ2ODgzNjU1ODc5ODg0OA.GhXtUo.ycug9c6LKf0sh46RLukDQy71ljnkGeFMfTe5ME'
target_channel_premium='💪premium-chat'
target_channel_trial='trial-chat'
target_role_premium='NinjaTrader Premium'
target_role_trial='Trial'


def run_discord_bot():
    global TOKEN
    global target_channel_premium
    global target_role_premium
    
    intents=discord.Intents.default()
    intents.message_content=True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author==client.user:
            return
        
        #username = str(message.author)
        #id= str(message.author.id)
        user_message = str(message.content)
        channel = str(message.channel)
        roles=None
        author_roles = get_author_roles(message.author)
        if author_roles:
            roles = [role.name for role in author_roles]

        channel=channel.strip()
        if channel==target_channel_premium and roles:
            if target_role_premium in roles:
                u_id=None
                if len(user_message)>0 and user_message[0]=='?':
                    u_id=user_message[1:]
                    u_id=u_id.strip()
                await send_message(message,user_message,u_id,isTrial=False)
        elif channel==target_channel_trial and roles:
            if target_role_trial in roles:
                u_id=None
                if len(user_message)>0 and user_message[0]=='?':
                    u_id=user_message[1:]
                    u_id=u_id.strip()
                await send_message(message,user_message,u_id,isTrial=True)
    
    @client.event
    async def on_member_update(before, after):
        removed_roles = [role.name for role in before.roles if role not in after.roles]

        if target_role_premium in removed_roles:
            await set_item_invalid(after=after)
            #print('NinjaTrader Premium subscription removed')
            #print(f'{after.id} quit the role ' + target_role_premium)

    client.run(TOKEN)
    #loop = asyncio.get_event_loop()
    #loop.create_task(check_data_file())
    #loop.run_until_complete(client.start(TOKEN))