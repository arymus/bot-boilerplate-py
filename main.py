import discord # Import Discord.py for interacting with the Discord API
from discord.ext import commands # Import commands from Discord extensions to create bot commands

# These imports are built in to Python's standard library, which you get when you install Python
from dotenv import load_dotenv # Import load_dotenv so we can load environment variables
import os # Import os which allows us to access the system outside the program
import logging # Import logging to output messages about the program (errors, debug messages, etc.)

load_dotenv() # Load environment variables (this loads the TOKEN variable from .env, which we'll need later)
TOKEN = os.getenv("TOKEN") # Access the TOKEN environment variable from the system (change TOKEN to whatever your variable name is in .env)

"""
Logging has a function called FileHandler which allows you to create a file for it to log messages to.
Filename specifies the file which the logs will be written to, and this file will be created if it does not exist.
discord.log will be the file which logs are written to (the .log extension is made for computer-generated messages)

Mode specifies the permissions for the file. "w" stands for write, which allows us to actually be able to write the logs.
"""
handler = logging.FileHandler(filename="discord.log", mode="w") # Create a file for logging messages
intents = discord.Intents.default() # Default set of intents, contains all intents but only the defaults are set to True
intents.message_content = True # Gives the bot permission to read message content, which we need for registering commands

"""
commands.Bot() initializes an object that can register and respond to commands.
command_prefix defines the prefix to call commands. (can be any symbol, slash is just the most common)
intents are the permissions to recieve certain discord events, like member joins or messages.
"""
bot = commands.Bot(command_prefix="/", intents=intents) # Initialize a bot to recieve handle commands

"""
-- ABOUT @bot.event --
@bot.event is a decorator function.
Python decorator functions are functions that have another function passed to them.
They are useful for executing code before and after a function is called.
The Discord.py module provides us with a bot.event function, which takes the function we write and registers it as an event.

-- ABOUT async def on_ready() --
Async is a keyword that is short for asynchronous.
Async functions create coroutines, which allow code to stop and resume it's execution.
The decorator function (@bot.event) holds the function, and passes it to the Discord API to be ran on the on_ready event.
The await keyword stops coroutine execution. In this case, the coroutine is stopped until the on_ready event occurs.

-- ABOUT bot.tree.sync() --
All bots have something called a command tree.
A command tree is a list of commands which branch out into subcommands.
This helps organize commands by making them easier to find in the Discord API.
"""
@bot.event # Event decorator (a function that has another function passed to it)
async def on_ready(): # Asynchronous function that handles the on_ready event (which is when the bot has finished loading)
    await bot.tree.sync() # Sync all commands with the bot tree once the on_ready event is registered 
    print(f"{bot.user.name} up and running!") # Print a message when the bot is up and running

# Event decorator that passes the sayhello() function to the Discord API in the event that /sayhello is called
@bot.tree.command(name="sayhello", description="Say hello!")
async def sayhello(interaction): # Function to say hello to the user

    # Sends a message inside the response that mentions the user inside the hello message (await means this only happens when the command is called)
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

"""
Run the bot using the token, which allows it to access the Discord API.
Run the bot using the log_handler, which provides a file for logs to be written to.
Log only errors to the file (this option can be set to logging.DEBUG for debug messages)
"""
bot.run(TOKEN, log_handler=handler, log_level=logging.ERROR)