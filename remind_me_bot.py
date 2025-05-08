import discord
import asyncio
from datetime import datetime, timedelta
from discord.ext import commands
import pytz
import API_keys

# Replace with your bot's token
TOKEN = API_keys.BOTKEY
# Replace with the target channel ID
CHANNEL_ID = API_keys.CHANNEL_ID
# Replace with the timezone of the reminder
TIMEZONE = "America/New_York"

intent = discord.Intents.default()
intent.messages = True
bot = commands.Bot(command_prefix="!", intents=intent)

reminders = [
    {"time": (19, 00), "message": "Dont Forget to update the log books!"},  # Hour, Minute, Message
#    {"time": (10, 0), "message": "Reminder 2: Water the plants."},
#    {"time": (18, 60), "message": "Reminder 3: Check your emails."},
    {"date": "2025-05-12", "time": (7,30 ), "message": "Seeds should be in today!"},  # Example of a date-specific reminder
]


async def send_reminders():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Error: Could not find channel with ID {CHANNEL_ID}")
        return

    timezone = pytz.timezone(TIMEZONE)  # Define timezone once

    while not bot.is_closed():
        now = datetime.now(timezone)  # Get datetime object with timezone information

        for reminder in reminders:
            if "date" in reminder:
                try:
                    reminder_date_str = reminder["date"]
                    reminder_datetime = datetime.strptime(reminder_date_str, "%Y-%m-%d")
                    reminder_datetime = reminder_datetime.replace(
                        hour=reminder["time"][0],
                        minute=reminder["time"][1],
                        second=0,
                        microsecond=0
                    ).astimezone(timezone) # Add timezone

                    if now.date() == reminder_datetime.date() and now.hour == reminder_datetime.hour and now.minute == reminder_datetime.minute:
                        await channel.send(reminder["message"])

                except (ValueError, KeyError) as e:
                    print(f"Error processing date-specific reminder: {e}")
            else:
                try:
                    if now.hour == reminder["time"][0] and now.minute == reminder["time"][1]:
                        await channel.send(reminder["message"])
                except discord.errors.Forbidden:
                    print(f"Error: Bot does not have permission to send messages in channel {CHANNEL_ID}")
                except (ValueError, KeyError) as e:
                    print(f"Error processing time-based reminder: {e}")

        await asyncio.sleep(15)#Check every minute


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    bot.loop.create_task(send_reminders())


bot.run(TOKEN)