<div align="center">

# PyPI Stats Telegram Bot

A simple Telegram bot that fetches and displays download statistics for PyPI packages using BigQuery.

</div>

## Features

- **Retrieve Download Stats:** Get the total number of downloads for any PyPI package.
- **User-Friendly Interface:** Interact with the bot using simple commands and inline buttons.

## How It Works

1. **Send Package Name:** Start the bot and send the name of a PyPI package.
2. **Fetch Stats:** The bot queries BigQuery for the package's total download count.
3. **Receive Stats:** Get the download stats directly in your chat.

## Getting Started

To set up the bot on your own, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/superhexa/PypiStats.git
   cd PypiStats
   ```

2. **Install Dependencies:**
   Make sure you have Python 3.7+ installed. Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Bot:**
   - Edit the `config.py` file with your Telegram bot token and BigQuery credentials:
     ```python
     TOKEN = '' # Your Telegram bot token
     PROJECT_ID = '' # Your Google Cloud Project ID (the project where BigQuery is set up)
     KEYS_JSON = '' # Path to your Google Cloud service account credentials JSON file
     ```

4. **Run the Bot:**
   ```bash
   python bot.py
   ```

5. **Interact with the Bot:**
   Start a chat with your bot on Telegram and send the name of a PyPI package to get its download stats.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
