# MudaeBot

This project is a discord bot that will automatically claim Pokémon on the Discord Mudae game.

## Installation

```bash
    git clone git@github.com:GuillaumeLarue/MudaeBot.git
    cd MudaeBot
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt  
```

## Use

Change your discord IDs in the Dockerfile and run the bot with:

```bash
    docker compose up -d --build
```

To stop the bot you have to run

```bash
    docker compose down
```

## Author

- Guillaume Larue