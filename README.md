# Discord Reminder Bot

This Python bot sends reminders to a Discord channel at specified times or dates

## Prerequisites

* **Python 3.7 or higher:**  Make sure you have a compatible Python version installed.
* **Discord.py Library:** The bot relies on the `discord.py` library.
* **pytz Library:** Used for timezone handling.

## Installation

1. **Create a Python environment (recommended):** This helps isolate dependencies. You can use
`venv` or `conda`.

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate  # On Windows
   ```

2. **Install dependencies:**

   ```bash
   pip install discord.py pytz
   ```

3. **Create `API_keys.py`:**

   Create a file named `API_keys.py` in the same directory as your bot script and store your bot
token and channel ID there.  **Do not commit this file to version control (e.g., Git) as it
contains sensitive information.**

   Example `API_keys.py`:

   ```python
   BOTKEY = "YOUR_BOT_TOKEN"
   CHANNEL_ID = 123456789012345678
   ```

   * Replace `"YOUR_BOT_TOKEN"` with your Discord bot token.
   * Replace `123456789012345678` with the ID of the Discord channel you want the bot to send
reminders to.  To get the channel ID, enable Developer Mode in Discord (User Settings ->
Advanced) and then right-click the channel and select "Copy ID".

## Configuration

The bot is configured through the `API_keys.py` file and the `reinders` list within the main
Python script.

* **`API_keys.py`:**  Defines the bot token and target channel ID.
* **`reinders` list:**  This list contains the reminder schedules.  Each reminder can be either
time-based or date-specific.

**Reminder Formats:**

* **Time-based Reminders:**

  ```python
  {"time": (hour, minute), "message": "Reminder message"}
  ```

  Example:

  ```python
  {"time": (19, 00), "message": "Dont Forget to update the log books!"}
  ```

* **Date-Specific Reminders:**

  ```python
  {"date": "YYYY-MM-DD", "time": (hour, minute), "message": "Reminder message"}
  ```

  Example:

  ```python
  {"date": "2025-05-12", "time": (7, 30), "message": "Seeds should be in today!"}
  ```

  * The `date` key must be in the format "YYYY-MM-DD".

**Timezone:**

* By default, the bot uses the server's timezone. If you need to change this, you need to adjust
the timezone settings within the script (advanced users only).

## Running the Bot

1. **Navigate to the bot's directory:** Open a terminal or command prompt and change the current
directory to the folder containing the bot script (e.g., `discord_reminder_bot`).

2. **Run the script:**

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of your Python file (e.g.,
`reminder_bot.py`).

## Important Considerations

* **Security:**  Keep your bot token secure. Do not share it publicly or commit it to version
control.
* **Rate Limiting:** Discord has rate limits. Avoid sending too many messages too quickly to
avoid getting your bot temporarily banned.
* **Error Handling:** The bot includes basic error handling, but you might want to add more
robust error handling and logging for production environments.
* **Permissions:**  Ensure your bot has the necessary permissions in the Discord channel (e.g.,
"Send Messages").
* **Maintenance:** Regularly review the bot's logs and update the reminder schedules as needed.
* **Timezone Awareness:** Ensure the timezone of the bot aligns with the intended recipients of
the reminders to avoid confusion.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open
an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
