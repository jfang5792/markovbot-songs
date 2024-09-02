"""A Markov chain generator that can respond with song excerpts."""
import os
import discord
import sys
from random import choice


def open_and_read_file(filenames):
    """Take list of files. Open them, read them, and return one long string."""

    body = ''
    for filename in filenames:
        text_file = open(filename)
        body = body + text_file.read()
        text_file.close()

    return body


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}

    words = text_string.split()
    # words.append(None)
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Take dictionary of Markov chains; return random text."""

    keys = list(chains.keys())
    key = choice(keys)

    words = [key[0], key[1]]
    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text).

        word = choice(chains[key])
        words.append(word)
        key = (key[1], word)

    return ' '.join(words)


# Get the filenames from the user through a command line prompt, ex:
# python markov.py cherry.txt
# python markov.py the-one.txt
# python markov.py tears-ricochet.txt
filenames = sys.argv[1:]

if not filenames:
    print("Please provide a filename on the command line! Ex. python3 markov.py cherry.txt")
    exit(1)

# Open the files and turn them into one long string
text = open_and_read_file(filenames)

# Get Markov chain
chains = make_chains(text)
response = make_text(chains)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('gimme song lyrics from it ends with us soundtrack'):
        await message.channel.send(make_text(chains))

#client.run('')
client.run(os.environ['DISCORD_TOKEN'])
