# ---------------------------------------------#
# Configuration
# ---------------------------------------------#
# Recheck time in seconds to check all accounts again (60 seconds = 1 minute and 0 means no recheck)
AccountsRecheckTime = 300

# Adds a random delay to the AccountsRecheckTime interval to make it more unpredictable and less detectable.
# Set it to 0 to disable the random delay.
# For example, if set to 120, the bot will introduce a random delay between 1 and 120 seconds each time it rechecks.
MaxRandomDelay = 120

# Accounts will be checked in the order they are listed
AccountList = [
    {
        "account_name": "cidnha",  # A custom name for the account (not important, just for logs)
        "Authorization": "Bearer 1725952799827CoiYE5NKNEDvedEVQhWdT88DouC0dicw08Q0HP95dMHqqwmFGpS9BvIb9wEFqmAl7149859105",  # To get the token, refer to the README.md file
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Refer to the README.md file to obtain a user agent
        "Proxy": {           
            "http": "http://113.195.224.222:9999"
        },
        "config": {
            "auto_tap": True,
            "auto_free_tap_boost": True,
            "auto_get_daily_cipher": True,
            "auto_get_daily_task": True,
            "auto_get_task": True,
            "auto_finish_mini_game": True,
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
        "telegram_chat_id": "1439771387",
    },
    {
        "account_name": "heng os zin",
        "Authorization": "Bearer 172595298842289yMxIWMB3UE6AMouWE3123DDI7pQ7B456tBzFYEAFrZpsCiJCYD7ithjcIJb4Wi5001451526",
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",
        "Proxy": {
            "http": "http://149.129.226.9:8080"
        },
        "config": {
            "auto_tap": True,
            "auto_free_tap_boost": True,
            "auto_get_daily_cipher": True,
            "auto_get_daily_task": True,
            "auto_get_task": True,
            "auto_finish_mini_game": True,
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
        "telegram_chat_id": "1439771387",
    },
    {
        "account_name": "mine",
        "Authorization": "Bearer 1725953159405kGu1IiqUc60wj7AQUfFoG5umoUBBJYp4knlMJMkgMDP5vVlUFaBOncnR2ZBW0Anj5129273722",
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",
        "Proxy": {
            "http": "http://120.42.224.254:21212"
        },
        "config": {
            "auto_tap": True,
            "auto_free_tap_boost": True,
            "auto_get_daily_cipher": True,
            "auto_get_daily_task": True,
            "auto_get_task": True,
            "auto_finish_mini_game": True,
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
        "telegram_chat_id": "1439771387",
    }
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
    "is_active": True,
    "bot_token": "7069215582:AAEXyTWTu4KdhblkgFhG5_IbbtTkZjSEbTo",
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
