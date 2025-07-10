# Discord.py Boilerplate Code + Tutorial
## Table of contents
1. [Prerequisites](#prerequisites)
2. [Creating a Bot](#creating-a-bot)
3. [General Information](#general-information)
4. [Bot Account Creation](#bot-account-creation)
    - [General Information Page](#about-the-general-information-page)
    - [Generating a Token](#generating-a-token)
    - [Inviting Your Bot](#inviting-your-bot)

5. [Creating the Code Environment](#creating-the-code-enviroment)


## Prerequisites
- Python installed and above v3.12 (install [here](https://www.python.org/downloads/)!)

## Creating a Bot
In order to have a working Discord bot, you need to create the bot's actual user. Here is a step by step tutorial on how to create your bot and invite it to your server!

### General Information
Discord bots base around the use of events to trigger reactions.
For example, if a user sends a message, the bot can get that event and perform a reaction to it.

However, Discord bots cannot recieve every single event that happens in a server, or else they might overload.
Imagine if you were a bot! Would you like to:
- Track whenever someone joins the server
- Read every message that's sent
- Check the username and bio of every user
- Check what activity each member is doing
- Track whenever a user reacts to a message
- And way, way more

You'd explode right?! Therefore, we select specific events that our bot can respond to. The permissions to respond to these events are called **intents**.

### Bot Account Creation
1. Head to [this link](https://discord.com/developers/applications) to create a new bot.
2. Hit the blue button that says "New Application" at the top right corner.
3. Enter a name and agree to the [Discord Developer TOS](https://support-dev.discord.com/hc/en-us/articles/8562894815383-Discord-Developer-Terms-of-Service) and [Developer Policy](https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy).

Congratulations! You now have a bot user. You can give it a description, a profile picture and some tags.

### About the General Information page
- Name is the display name of your bot. You can configure the bot's actual Discord username (and banner) in the **Bot** section of the dashboard on the left of the page.
- App icon is the profile picture of your bot. If you do not assign it one, it takes a default profile picture, like any other Discord account.
- Description is the About Me of your bot. It is displayed on their Discord page, like any other user's About Me.
- Application ID is your bot's Discord ID. Every Discord user has a unique ID, and your bot is no different.
- Public key is like a password for your bot and the Discord API to communicate. The public key is used to verify that HTTP [requests and responses](https://en.wikipedia.org/wiki/Request%E2%80%93response) are coming from Discord and have not been tampered with by a third party.

### Generating a token
Your bot token is what your bot relies on to connect to the Discord API. It is the most important component of your bot.
It is extremely important that no one ever knows your bot token besides yourself. If someone gets ahold of your bot token, they can do malicious things with your bot and abuse its permissions in servers it is part of. If your bot token has been compromised, immediately generate a new one.

1. Go to the **Bot** section of the dashboard on the left side of the screen
2. Find the **Token** section
3. Hit the **Reset Token** button.
4. Immediately copy your token. 
5. Store your token somewhere safe (like an .env file in your project directory)

### Inviting Your Bot
Now that you have a bot account, it's time to invite it to your server!

1. Go to the **OAuth2** page on the dashboard, located on the left side of the screen.
2. Find the section that says **OAuth2 URL Generator** and select the bot option.
3. Scroll down to the **Bot Permissions** section and pick what permissions your bot needs to execute to do its job.
4. Scroll down to the **Generated URL**, and copy-and-paste it into your browser! Remember that you need special permissions to add a bot into any server.

Your bot is now added to your server! Now that we have a bot to code for, we can beging the code.

## Creating the Code Enviroment
### Project Directory

Create your project directory (<folder-name> is the name of your project)
```
mkdir <folder-name>`
`cd <folder-name>`
```
### Main Files
**FOR WINDOWS** 
```
# The 'echo' command outputs strings, so echo "" would output nothing since it is an empty string. Try running `echo Hello, World!" in your terminal!
# The > operator just means to write some output to a file.
# Since echo outputs strings, we're outputting "" to main.py, .env, and requirements.txt to create empty files. If you write to a nonexistent file, it's made for you!

echo "" > main.py # Python file, holds our code
echo "" > .env # .env file, stores environment variables (variables outside of our program that can be accessed by the system)
echo "" > .gitignore # Optional if you're sharing code on GitHub or any other Git-hosting service (Codeberg, Bitbucket, GitLab, etc.)
```

**FOR LINUX/MACOS**
```
touch main.py .env .gitignore # Touch creates files, and can create multiple files when multiple arguments are passed to it!
```
### Virtual Environment
Python has virtual environments, usually named venv, env, or virtualenv. These virtual environments hold all the dependencies we need to run our bot's code!

`python -m venv venv # Creates a virtual environment named venv`

**FOR WINDOWS**
`venv\Scripts\activate # Runs the activation script inside the venv`

**FOR LINUX/MACOS**
`source venv/bin/activate # Runs the activation script inside the venv`

You can exit the virtual environment by simply writing `deactivate` in the terminal.

5. Installing dependencies
Now that you're in a virtual environment, you have access to pip, Python's package manager which we can use to install our dependencies!
`pip install discord.py dotenv # Installs Discord.py to interact with the Discord API, and dotenv for accessing environment variables`

6. Writing requirements.txt
In order for other people to run your code, you need a requirements.txt so people can install the dependencies you used.
```
# `pip freeze` outputs all your dependencies, so we write those dependencies to requirements.txt (which is made for us if it doesn't already exist)
pip freeze > requirements.txt
```

Our code environment is finally set up! Now we can start writing the real code.

## Writing the code
Inside .env, write `TOKEN=<your-token>` (replace <your-token> with your [bot token](#generating-a-token) you generated earlier)
Navigate to our [Python file](main.py) to see the code for our robot.
If you want to install dependencies from a project, enter a [virtual environment](#virtual-environment) and run `pip install -r requirements.txt`