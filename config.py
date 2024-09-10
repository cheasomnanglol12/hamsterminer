# ---------------------------------------------#
# Configuration
# ---------------------------------------------#
# Recheck time in seconds to recheck all accounts (60 seconds = 1 minute and 0 means no recheck)
AccountsRecheckTime = 300

# Adds a random delay to the AccountsRecheckTime interval to make it more unpredictable and less detectable.
# Set it to 0 to disable the random delay.
# For example, if set to 120, the bot will introduce a random delay between 1 and 120 seconds each time it rechecks.
MaxRandomDelay = 120

# Accounts will be checked in the order they are listed
AccountList = [
    {
        "account_name": "cidnha",  # A custom name for the account (not important, just for logs)
        "Authorization": "Bearer 1725952799827CoiYE5NKNEDvedEVQhWdT88DouC0dicw08Q0HP95dMHqqwmFGpS9BvIb9wEFqmAl7149859105",  # Account 1 Bearer token
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Provided UserAgent
        "Proxy": {
            "https": "https://173.249.34.184:3128",  # Proxy for Account 1
        },
        "config": {
            "auto_tap": True,
            "auto_free_tap_boost": True,
            "auto_get_daily_cipher": True,
            "auto_get_daily_task": True,
            "auto_get_task": True,
            "auto_finish_mini_game": True,
            "auto_claim_daily_combo": True,
            "auto_daily_combo_enable": True,
            "auto_daily_combo_max_price": 5_000_000,
            "auto_playground_games": True,
            "auto_upgrade": True,
            "auto_upgrade_start": 2_000_000,
            "auto_upgrade_min": 100_000,
            "wait_for_best_card": True,
            "enable_parallel_upgrades": True,
            "parallel_upgrades_max_price_per_hour": 1000,
            "show_num_buy_options": 0,
            "max_promo_games_per_round": 3,
        },
        "telegram_chat_id": "7149859105",  # First Telegram chat ID for Account 1
    },
    {
        "account_name": "Account 2",  # Second account configuration
        "Authorization": "Bearer 172595298842289yMxIWMB3UE6AMouWE3123DDI7pQ7B456tBzFYEAFrZpsCiJCYD7ithjcIJb4Wi5001451526",  # Account 2 Bearer token
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Provided UserAgent
        "Proxy": {
            "https": "https://161.35.70.249:3128",  # Proxy for Account 2
        },
        "config": {
            "auto_tap": True,
            "auto_free_tap_boost": True,
            "auto_get_daily_cipher": True,
            "auto_get_daily_task": True,
            "auto_get_task": True,
            "auto_finish_mini_game": True,
            "auto_claim_daily_combo": True,
            "auto_daily_combo_enable": True,
            "auto_daily_combo_max_price": 5_000_000,
            "auto_playground_games": True,
            "auto_upgrade": True,
            "auto_upgrade_start": 2_000_000,
            "auto_upgrade_min": 100_000,
            "wait_for_best_card": True,
            "enable_parallel_upgrades": True,
            "parallel_upgrades_max_price_per_hour": 1000,
            "show_num_buy_options": 0,
            "max_promo_games_per_round": 3,
        },
        "telegram_chat_id": "1439771387",  # Second Telegram chat ID for Account 2
    },
    {
        "account_name": "Account 3",  # Third account configuration
        "Authorization": "Bearer 1725953159405kGu1IiqUc60wj7AQUfFoG5umoUBBJYp4knlMJMkgMDP5vVlUFaBOncnR2ZBW0Anj5129273722",  # Account 3 Bearer token
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Provided UserAgent
        "Proxy": {
            "https": "https://178.250.88.254:80",  # Proxy for Account 3
        },
        "config": {
            "auto_tap": True,
            "auto_free_tap_boost": True,
            "auto_get_daily_cipher": True,
            "auto_get_daily_task": True,
            "auto_get_task": True,
            "auto_finish_mini_game": True,
            "auto_claim_daily_combo": True,
            "auto_daily_combo_enable": True,
            "auto_daily_combo_max_price": 5_000_000,
            "auto_playground_games": True,
            "auto_upgrade": True,
            "auto_upgrade_start": 2_000_000,
            "auto_upgrade_min": 100_000,
            "wait_for_best_card": True,
            "enable_parallel_upgrades": True,
            "parallel_upgrades_max_price_per_hour": 1000,
            "show_num_buy_options": 0,
            "max_promo_games_per_round": 3,
        },
        "telegram_chat_id": "1439771387",  # First Telegram chat ID for Account 3 (you can change this if needed)
    },
]

# ---------------------------------------------#
# Telegram Logging
# By enabling this feature, you will receive logs in your Telegram account.
# To use this feature, you need to create a bot and obtain the token from @BotFather.
# Note: Only important logs are sent to Telegram, feel free to include more logs as needed.
# You can also use this feature to receive logs from a bot running on a server.
# If you don't want to use this feature, set "is_active" to False and leave "bot_token" and "uid" fields empty.
# This feature is optional, and you can disable it by setting "is_active" to False.
telegramBotLogging = {
    "is_active": True,  # Set to True to activate Telegram logging
    "bot_token": "7069215582:AAEXyTWTu4KdhblkgFhG5_IbbtTkZjSEbTo",  # Provided bot token
    # Configure the what you want to receive logs from the bot
    "messages": {
        "general_info": True,
        "account_info": True,
        "http_errors": False,
        "other_errors": False,
        "daily_cipher": True,
        "daily_task": False,
        "upgrades": True,
    },
}

ConfigFileVersion = 1
