
#IMPORTING PACKAGES

from datetime import timedelta
import discord
from discord import message
from discord import embeds
from discord import colour
from discord.ext import commands
from discord.ext.commands.core import guild_only
from discord.role import Role 
import asyncio
import random
from dotenv import load_dotenv
import os

client = commands.Bot(command_prefix='$', help_command=None)
allowed_roles = ["TRL Executives", "TRL Directors", "admin"]
allowed_roles_2 = ["TRL Team Captains", "TRL Executives", "TRL Directors"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="The Revival League"))

#ABOUT COMMAND

@client.command()
async def about(ctx):
    embed=discord.Embed(title="__Generational Esports Incentive__", description="**Generational Esports Incentive is an initiative under the headship of The Revival League with a premise of bridging the gap between the Competitive Scene and the nostalgic tournament phenomena. Generational Esports Incentive aims to shape the history of Forward Assault Esports and create additional possibilities for involvement and advancement within our competitive community. Generational Esports Incentive is dedicated to providing the best exciting experiences to our Community.\n\nOur Official Website:\nhttps://www.therevivalleague.com/\n\nJoin up our Socials to stay connected with The Revival League**\n <:Twitter:923911089094295583> [Follow us here on twitter!](https://twitter.com/LeagueRevival)\n <:Youtube_playbutton:923910622461186098> [Subscribe to get notified about uploads!](https://youtube.com/TheRevivalLeague)\n <:disc:923910935347875861> [Join the discord!](https://discord.gg/trl)\n <:Instagram:923910361776783442> [Follow us on instagram!](https://instagram.com/the.revivalleague)", colour = discord.Color.from_rgb(191, 64, 191))
    embed.set_image(url="https://media.discordapp.net/attachments/899659923770707998/906152518566969374/PicsArt_11-05-05.06.25.jpg")
    await ctx.send(embed=embed)

#HELP COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def help(ctx, cmd_name=None):
    if cmd_name is None:
        embed = discord.Embed(title="Enter the name of the command you require help with!", description="Following is a list of commands available:", colour=discord.Color.from_rgb(255,255,0))
        embed.add_field(name="about",value="$help about", inline=True)
        embed.add_field(name="purge",value="$help purge", inline=True)
        embed.add_field(name="announce",value="$help announce", inline=True)
        embed.add_field(name="ban",value="$help ban", inline=True)
        embed.add_field(name="unban",value="$help unban", inline=True)
        embed.add_field(name="mute",value="$help mute", inline=True)
        embed.add_field(name="unmute",value="$help unmute", inline=True)
        embed.add_field(name="kick",value="$help kick", inline=True)
        embed.add_field(name="dmuser",value="$help dmuser", inline=True)
        embed.add_field(name="give",value="$help give", inline=True)
        embed.add_field(name="remove",value="$help remove", inline=True)
        embed.add_field(name="flip",value="$help flip", inline=True)
        embed.add_field(name="register",value="$help register", inline=True)
        embed.add_field(name="edit",value="$help editroster", inline=True)
        await ctx.send(embed=embed)
    elif cmd_name == "about":
        embed = discord.Embed(title="$about", description="Sends an embed message containing some basic information about the tournament.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "purge":
        embed = discord.Embed(title="$purge number_of_messages", description="Deletes given number of messages.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "announce":
        embed = discord.Embed(title="$announce channel_name \"title\" \"content\" image_link", description="Announces the given content in the form of an embed.(**Keep in mind the double quotes while running the command!**)", colour=discord.Color.from_rgb(191, 64, 191))
        embed.set_image(url="https://media.discordapp.net/attachments/922764823350087710/927092093350993980/unknown.png")
        await ctx.send(embed=embed)
    elif cmd_name == "ban":
        embed = discord.Embed(title="$ban username reason", description="Bans a user from the server.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "unban":
        embed = discord.Embed(title="$unban username", description="Unbans a banned user.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "mute":
        embed = discord.Embed(title="$mute username reason", description="Mutes a user.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "unmute":
        embed = discord.Embed(title="$unmute username", description="Unmutes a muted user.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "kick":
        embed = discord.Embed(title="$kick username reason", description="Kicks a user from the server.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "dmuser":
        embed = discord.Embed(title="$dmuser user_id OR user \"title\" \"content\" image_link", description="Direct messages the given content to the specified user in the form of an embed.(**Keep in mind the double quotes while running the command!**)", colour=discord.Color.from_rgb(191, 64, 191))
        embed.set_image(url="https://media.discordapp.net/attachments/922764823350087710/924225706920132698/unknown.png")
        await ctx.send(embed=embed)
    elif cmd_name == "give":
        embed = discord.Embed(title="$give username role_name", description="Assigns specified role to specified user.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "remove":
        embed = discord.Embed(title="$remove username role_name", description="Removes specified role from specified user.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "flip":
        embed = discord.Embed(title="$flip", description="Flips a coin.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "register":
        embed = discord.Embed(title="$register", description="Register a team.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    elif cmd_name == "editroster":
        embed = discord.Embed(title="$edit", description="Edits an existing team.", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid argument.")


#PURGE COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


#ANNOUNCE COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def announce(ctx, channel: discord.TextChannel, title, desc=None, image=None):
    if desc is None:
        embed = discord.Embed(title=title, description=" ",color=discord.Color.from_rgb(255,255,0))
    else:
        embed = discord.Embed(title=title, description=desc,color=discord.Color.from_rgb(255,255,0))
    if image is None:
        pass
    else:
        embed.set_image(url=image)
    await ctx.send(embed=embed)
    await ctx.send(f"**Are you sure you want to announce this embed in {channel}**\n**Type** ``Y`` **to send and** ``N`` **to quit task**")
    def isCorrect(m):
      return m.author == ctx.author
    try:
        userInput = await client.wait_for('message',check=isCorrect, timeout=30)
        userInputStr = str(userInput.content)
    except asyncio.TimeoutError:
        embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)
    try:
        if userInputStr == "Y":
            announceMsg = True
        elif userInputStr == "N":
            announceMsg = False
        else:
         embedii = discord.Embed(title=f"Recieved invalid response from {ctx.author}", colour=discord.Color.from_rgb(255, 0, 0))
         await ctx.send(embed=embedii)
    except:
        print("Exception ignored.")
    if announceMsg:
        await channel.send(embed=embed)
        embedii = discord.Embed(title=f":white_check_mark: Successfully announced in {channel}", colour=discord.Color.from_rgb(0, 255, 1))
        await ctx.send(embed=embedii)
    else:
        embedii = discord.Embed(title="Task aborted", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)

#BAN COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def ban(ctx, member : discord.Member, *, reason=None):
    if ctx.author == member:
        await ctx.send("Bruh :skull:")
    else:
        await member.ban(reason = reason)
        e = discord.Embed(title="Banned!", description="Banned user " + str(member) + "\nReason: " + str(reason), colour=discord.Colour.from_rgb(255, 51, 51))
        await ctx.send(embed=e)

#UNBAN COMMAND

@client.command()
@guild_only()
@commands.has_any_role(*allowed_roles)
async def unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    e = discord.Embed(title="Unbanned!", description="Unbanned user: " + str(user), colour=discord.Colour.from_rgb(0, 255, 1))
    await ctx.send(embed=e)

#MUTE COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def mute(ctx, member: discord.Member, *,reason=None):
    if ctx.author == member:
        await ctx.send("Bruh :skull:")
    else:
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.add_roles(role)
        e = discord.Embed(title="Muted!", description="Muted user: " + str(member) + "\nReason: " + str(reason), colour=discord.Colour.from_rgb(255,255,0))
        await ctx.send(embed=e)

#UNMUTE COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name='Muted')
    await member.remove_roles(role)
    e = discord.Embed(title="Unmuted!", description="Unmuted user: " + str(member), colour=discord.Colour.from_rgb(255,255,0))
    await ctx.send(embed=e)

#KICK COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def kick(ctx, member : discord.Member, *, reason=None):
    if ctx.author == member:
        await ctx.send("Bruh :skull:")
    else:
        await member.kick(reason = reason)
        e = discord.Embed(title="Kicked!", description="Kicked user " + str(member) + "\nReason: " + str(reason), colour=discord.Colour.from_rgb(255,255,0))
        await ctx.send(embed=e)


#DM USER COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def dmuser(ctx, user: discord.Member, title, desc=None, image=None):
    user=user
    embed = discord.Embed(title=title, description=desc, colour=discord.Color.from_rgb(255,255,0))
    if desc is None:
        embed = discord.Embed(title=title, description=" ", colour=discord.Color.from_rgb(255,255,0))
    else:
        embed = embed = discord.Embed(title=title, description=desc, colour=discord.Color.from_rgb(255,255,0))
    if image is None:
        pass
    else:
        embed.set_image(url=f"{image}")
    await ctx.send(embed=embed)
    await ctx.send(f"**Are you sure you want to send this embed to {user}**\n**Type** ``Y`` **to send and** ``N`` **to quit task**")
    def isCorrect(m):
      return m.author == ctx.author
    try:
        userInput = await client.wait_for('message',check=isCorrect, timeout=30)
        userInputStr = str(userInput.content)
    except asyncio.TimeoutError:
        embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)
    try:
        if userInputStr == "Y":
            sendDm = True
        elif userInputStr == "N":
            sendDm = False
        else:
         embedii = discord.Embed(title=f"Recieved invalid response from {ctx.author}", colour=discord.Color.from_rgb(255, 0, 0))
         await ctx.send(embed=embedii)
    except:
        print("Exception ignored.")
    try:
        if sendDm:
            await user.send(embed=embed)
            embedii = discord.Embed(title=f":white_check_mark: Successfully dm'ed user {user}", colour=discord.Color.from_rgb(0, 255, 1))
            await ctx.send(embed=embedii)
        else:
            embedii = discord.Embed(title="Task aborted", colour=discord.Color.from_rgb(255, 0, 0))
            await ctx.send(embed=embedii)
    except discord.HTTPException:
        embedii = discord.Embed(title="Failed to DM user", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)

#ADD ROLES COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def give(ctx, member: discord.Member, *,role: discord.Role):
    await member.add_roles(role)
    e = discord.Embed(title="Assigned Role", description=f"Assigned **{role}** to {member}", colour=discord.Color.from_rgb(255,255,0))
    await ctx.send(embed=e)

#REMOVE ROLES COMMAND

@client.command()
@commands.has_any_role(*allowed_roles)
async def remove(ctx, member: discord.Member, *,role: discord.Role):
    await member.remove_roles(role)
    e = discord.Embed(title="Role removed", description=f"Removed **{role}** from {member}", colour=discord.Color.from_rgb(255,255,0))
    await ctx.send(embed=e)

#COIN FLIP

@client.command()
@commands.has_any_role(*allowed_roles)
async def flip(ctx):
    results = ["heads", "tails"]
    if random.choice(results) == "heads":
        embed = discord.Embed(title=f"**{ctx.author}** flipped **Heads**.", colour=discord.Color.from_rgb(255,255,0))
        embed.set_image(url="https://cdn.discordapp.com/attachments/723228136044757064/927936722950578256/trl.png")
    else:
        embed = discord.Embed(title=f"**{ctx.author}** flipped **Tails**.", colour=discord.Color.from_rgb(255,255,0))
        embed.set_image(url="https://media.discordapp.net/attachments/899659923770707998/900633998412353536/Generational_Esports_Incentive_Logo.png?width=670&height=670")
    await ctx.send(embed=embed)

#REGISTER COMMAND

@client.command()
async def register(ctx):
    initial_embed = discord.Embed(title="**__The Revival League: Register Team__**", description="**The Revival League allows teams to register through their special bot system. This has been implemented to provide teams with the facility of comfort and convenience. Kindly stay professional and use the command only when registering your respective team. Misuse of the command may result in rejection of your team's participation in the tournament and further consequences as decided per management.\nIf you want to continue creating a Team please respond with ``Y``, to abort please respond with ``N``.**", colour=discord.Color.from_rgb(255,255,0))
    await ctx.send(embed=initial_embed)
    def isCorrect(m):
      return m.author == ctx.author
    try:
        userInput = await client.wait_for('message',check=isCorrect, timeout=30)
        userInputStr = str(userInput.content)
    except asyncio.TimeoutError:
        embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)
    try:
        if userInputStr == "Y":
            registerConfirm=True
        elif userInputStr == "N":
            registerConfirm=False
        else:
         embedii = discord.Embed(title=f"Recieved invalid response from {ctx.author}", colour=discord.Color.from_rgb(255, 0, 0))
         await ctx.send(embed=embedii)
    except:
        print("Exception ignored.")
    if registerConfirm:
        embed_team = discord.Embed(title="**__The Revival League: Registration Format__**", description="**__Team Name:\nTeam Representative:\nRegion:__**\n\n**__Main 5__**\n-\n-\n-\n-\n-\n\n**__Substitutes__**\n-\n-\n-\n\n*Attach the **image link** for the logo of your team along **in the same message**.*", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=embed_team)
    else:
        embedii = discord.Embed(title="Task aborted", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)
        return
    try:
        userInputx = await client.wait_for('message',check=isCorrect, timeout=90)
        registration = str(userInputx.content)
    except asyncio.TimeoutError:
        embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)
    x = registration.split("https")
    link = f"https{x[1]}"
    embed_team_final = discord.Embed(title="The Revival League", description=f"{x[0]}", colour=discord.Color.from_rgb(255, 255, 0))
    embed_team_final.set_image(url=link)
    await ctx.send(embed=embed_team_final)
    await ctx.send(f"**Are you sure you want to register your team:**\nType ``Y`` for yes and ``N`` for no.")
    try:
        userInput2x = await client.wait_for('message',check=isCorrect, timeout=90)
        registrationConfirm = str(userInput2x.content)
    except asyncio.TimeoutError:
        embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)
    if registrationConfirm == "Y":
        confirm = True
    elif registrationConfirm == "N":
        confirm = False
    else:
        embedii = discord.Embed(title=f"Recieved invalid response from {ctx.author}", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)
    if confirm:
        channel = client.get_channel(723117337233850418)
        embedii = discord.Embed(title=f":white_check_mark: Registered successfully.", colour=discord.Color.from_rgb(0, 255, 1))
        await ctx.send(embed=embedii)
        embed_team_final.set_footer(text=f"Registered by {ctx.author}", icon_url=ctx.author.avatar_url)
        await channel.send(embed=embed_team_final)
    else:
        embedii = discord.Embed(title="Task aborted", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embedii)

@client.command()
@commands.has_any_role(*allowed_roles_2)
async def editroster(ctx):
    if ctx.channel.id == 716989978806059078:
        channel_To_Send = client.get_channel(783563511821238283)#SEND FINAL EDITED ROSTER IN THIS CHANNEL
        initial_embed = discord.Embed(title="**__The Revival League: Edit Roster__**", description="**The Revival League allows teams to edit teams through their special bot system. This has been implemented to provide teams with the facility of comfort and convenience. Kindly stay professional and use the command only when editing your respective team. Misuse of the command may result in rejection of your team's participation in the tournament and further consequences as decided per management.\nIf you want to continue editing a Team please respond with ``Y``, to abort please respond with ``N``.**", colour=discord.Color.from_rgb(255,255,0))
        await ctx.send(embed=initial_embed)
        def isCorrect(m):
            return m.author == ctx.author
        try:
            userInput = await client.wait_for('message',check=isCorrect, timeout=30)
            userInputStr = str(userInput.content)
        except asyncio.TimeoutError:
            embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
            await ctx.send(embed=embedii)
        if userInputStr == "Y":
            editRoster = True
        elif userInputStr == "N":
            editRoster = False
        else:
            embedii = discord.Embed(title=f"Recieved invalid response from {ctx.author}", colour=discord.Color.from_rgb(255, 0, 0))
            await ctx.send(embed=embedii)
        if editRoster:
            embed = discord.Embed(title="Send your updated roster along with an **image link** of the Team Logo.", colour=discord.Color.from_rgb(255,255,0))
            await ctx.send(embed=embed)
            try:
                userInput2 = await client.wait_for('message',check=isCorrect, timeout=90)
                updatedRoster = str(userInput2.content)
            except asyncio.TimeoutError:
                embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embedii)
            x = updatedRoster.split("https")
            link = f"https{x[1]}"
            embed_team_change = discord.Embed(title="The Revival League", description=f"{x[0]}", colour=discord.Color.from_rgb(255, 255, 0))
            embed_team_change.set_image(url=link)
            await ctx.send(embed=embed_team_change)
            await ctx.send(f"**Are you sure you want to edit your team?**\nType ``Y`` for yes and ``N`` for no.")
            try:
                userInput3 = await client.wait_for('message',check=isCorrect, timeout=30)
                editConfirm = str(userInput3.content)
            except asyncio.TimeoutError:
                embedii = discord.Embed(title=f"Time limit exceeded!", colour=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embedii)
            if editConfirm == "Y":
                embed_team_change.set_footer(text=f"Edited by {ctx.author}", icon_url=ctx.author.avatar_url)
                await channel_To_Send.send(embed=embed_team_change)
                embedii = discord.Embed(title=f":white_check_mark: Updated successfully.", colour=discord.Color.from_rgb(0, 255, 1))
                await ctx.send(embed=embedii)
            elif editConfirm == "N":
                embedii = discord.Embed(title="Task aborted", colour=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embedii)
            else:
                embedii = discord.Embed(title=f"Recieved invalid response from {ctx.author}", colour=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embedii)
        else:
            embedii = discord.Embed(title="Task aborted", colour=discord.Color.from_rgb(255, 0, 0))
            await ctx.send(embed=embedii)
    else:
        await ctx.send("This action cannot be performed in this channel!")
   

#IGNORES MESSEGES SENT BY BOT 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

#CLIENT RUN AND BOT TOKEN
client.run("token here")