# bot

A bot made for devs to interact with the bladelist api

## Installation Instructions

```bash
# Your global Python installation needs to have poetry
pip install poetry

# Clone the repo
git clone https://github.com/bladelist/bot

# Change directories into the project
cd bot

# If you're not a developer just install required dependencies like this
poetry install

# Activate the Pipenv shell (aka tell your terminal/whatever to use dependencies from the env in this project)
poetry shell

# Before we run the bot we need to create .env file where all secret keys will be (tokens etc)

# Create it inside the bot directory
touch bot/.env

# Edit it and change the keys to your values (see section below for sample layout)
nano bot/.env
```

Sample layout of .env file

```bash
BOT_TOKEN=your_bot_token_here
```

BOT_TOKEN the most important one. You can get one by creating a Discord bot

Once everything is ready
Run the bot!

```bash
# You need to be in the root of bot directory
# Once you are in bot/

# Run the bot
python bot```
