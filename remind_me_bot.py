import discord
import asyncio
from datetime import datetime, timedelta
from discord.ext import commands
import pytz
import API_keys

TOKEN = API_keys.bot_api
CHANNEL_ID = API_keys.chat_api
TIMEZONE = "America/New_York"

intent = discord.Intents.default()
intent.messages = True
bot = commands.Bot(command_prefix="!", intents=intent)

# Set a reference date
START_DATE = datetime(2025, 5, 14)  # Change this to the desired starting date

# Reminders list
reminders = [
    {"time": (19, 00), "message": "Don't forget to update the log books!"},
    #{"date": "2025-05-12", "time": (7, 30), "message": "Seeds should be in today!"},  # Date-specific reminder
]

async def send_reminders():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Error: Could not find channel with ID {CHANNEL_ID}")
        return

    timezone = pytz.timezone(TIMEZONE)

    while not bot.is_closed():
        now = datetime.now(timezone)

        # Check regular reminders
        for reminder in reminders:
            if "date" in reminder:
                reminder_datetime = datetime.strptime(reminder["date"], "%Y-%m-%d")
                reminder_datetime = reminder_datetime.replace(
                    hour=reminder["time"][0],
                    minute=reminder["time"][1],
                    second=0,
                    microsecond=0
                ).astimezone(timezone)

                if now.date() == reminder_datetime.date() and now.hour == reminder_datetime.hour and now.minute == reminder_datetime.minute:
                    await channel.send(reminder["message"])
            else:
                if now.hour == reminder["time"][0] and now.minute == reminder["time"][1]:
                    await channel.send(reminder["message"])

        # Check daily counter reminder at 9 AM
        if now.hour == 23 and now.minute == 28:
            days_passed = (now.date() - START_DATE.date()).days
            message = f"Good morning! Its day {days_passed} of the grow!"
            await channel.send(message)

        await asyncio.sleep(60)  # Check every minute

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    bot.loop.create_task(send_reminders())

bot.run(TOKEN)