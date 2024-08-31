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
        "account_name": "Account kalip",  # A custom name for the account (not important, just for logs)
        "Authorization": "Bearer 1724902775619vt81wZu89saLNxtegQDsJsF36RvmCH8V3AfSGqvJNZDsG95CjFjdiB0LaTfnBGq16642866145",  # To get the token, refer to the README.md file
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Refer to the README.md file to obtain a user agent
        "Proxy": {
            "http": "http://103.144.192.157:8080",
            "http": "http://104.237.240.2:3128",
            "http": "http://105.112.191.250:8080",
            "http": "http://109.167.206.121:8080",
            "http": "http://110.232.74.55:8080",
            "http": "http://111.118.128.123:41344",
            "http": "http://112.78.141.214:8080",
            "http": "http://116.58.232.230:8080",
            "http": "http://118.107.44.181:8080",
            "http": "http://119.82.253.210:8080"
        },
        "config": {
            "auto_tap": True,  # Enable auto tap by setting it to True, or set it to False to disable
            "auto_free_tap_boost": True,  # Enable auto free tap boost by setting it to True, or set it to False to disable
            "auto_get_daily_cipher": True,  # Enable auto get daily cipher by setting it to True, or set it to False to disable
            "auto_get_daily_task": True,  # Enable auto get daily tasks by setting it to True, or set it to False to disable
            "auto_get_task": True,  # Enable auto get (Youtube/Twitter and ...) task to True, or set it to False to disable
            "auto_finish_mini_game": True,  # Enable auto finish mini game by setting it to True, or set it to False to disable
            "auto_playground_games": True,  # Enable auto playground games by setting it to True, or set it to False to disable
            # If you have over 5 accounts, disable the auto_playground_games feature or use a proxy for each account.
            "auto_upgrade": True,  # Enable auto-upgrade by setting it to True, or set it to False to disable
            "auto_upgrade_start": 2_000_000,  # Start buying upgrades when the balance is greater than this amount
            "auto_upgrade_min": 100_000,  # Stop buying upgrades when the balance is less than this amount
            # This feature will ignore the auto_upgrade_start and auto_upgrade_min.
            # By changing it to True, the bot will find the overall best card and then wait for the best card to be available (based on cooldown or price).
            # When the best card is available, the bot will buy it and then wait for the next best card to be available.
            # This feature will stop buying upgrades when the balance is less than the price of the best card.
            "wait_for_best_card": True,  # Recommended to keep it True for high-level accounts
            "enable_parallel_upgrades": True,  # Enable parallel card upgrades. This will buy cards in parallel if the best card is on cooldown. It should speed up the profit.
            "parallel_upgrades_max_price_per_hour": 1000,  # Cards with less than X coins per 1k will be bought
            "show_num_buy_options": 0,  # Number of card buy options to show in the logs, ranked by best value, 0 disables this.
            "max_promo_games_per_round": 3,  # Maximum number of promo games to play in a single round, 0 disables this.
        },
        # If you have enabled Telegram bot logging,
        # you can add your chat ID below to receive logs in your Telegram account.
        # You can obtain your chat ID by messaging @chatIDrobot.
        # Example: "telegram_chat_id": "12345678".
        # If you do not wish to use this feature for this account, leave it empty.
        # This feature is optional and is required to enable the telegramBotLogging feature below.
        "telegram_chat_id": "1439771387",  # String - you can get it from https://t.me/chatIDrobot
    },
    {
        "account_name": "Account kalip2",  # A custom name for the account (not important, just for logs)
        "Authorization": "Bearer 1725016141007gWBMv81HJwTYWRnClBPvHB3ZwBooOGyb5O0WL8YOPZ2HiD6ok4bYFnSzC21tGngX6896218626",  # To get the token, refer to the README.md file
        "UserAgent": "Mozilla/5.0 (Linux; Android 11; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Refer to the README.md file to obtain a user agent
        "Proxy": {
            "http": "http://103.144.192.157:8080",
            "http": "http://104.237.240.2:3128",
            "http": "http://105.112.191.250:8080",
            "http": "http://109.167.206.121:8080",
            "http": "http://110.232.74.55:8080",
            "http": "http://111.118.128.123:41344",
            "http": "http://112.78.141.214:8080",
            "http": "http://116.58.232.230:8080",
            "http": "http://118.107.44.181:8080",
            "http": "http://119.82.253.210:8080"
        },
        "config": {
            "auto_tap": True,  # Enable auto tap by setting it to True, or set it to False to disable
            "auto_free_tap_boost": True,  # Enable auto free tap boost by setting it to True, or set it to False to disable
            "auto_get_daily_cipher": True,  # Enable auto get daily cipher by setting it to True, or set it to False to disable
            "auto_get_daily_task": True,  # Enable auto get daily tasks by setting it to True, or set it to False to disable
            "auto_get_task": True,  # Enable auto get (Youtube/Twitter and ...) task to True, or set it to False to disable
            "auto_finish_mini_game": True,  # Enable auto finish mini game by setting it to True, or set it to False to disable
            "auto_playground_games": True,  # Enable auto playground games by setting it to True, or set it to False to disable
            # If you have over 5 accounts, disable the auto_playground_games feature or use a proxy for each account.
            "auto_upgrade": True,  # Enable auto-upgrade by setting it to True, or set it to False to disable
            "auto_upgrade_start": 2_000_000,  # Start buying upgrades when the balance is greater than this amount
            "auto_upgrade_min": 100_000,  # Stop buying upgrades when the balance is less than this amount
            # This feature will ignore the auto_upgrade_start and auto_upgrade_min.
            # By changing it to True, the bot will find the overall best card and then wait for the best card to be available (based on cooldown or price).
            # When the best card is available, the bot will buy it and then wait for the next best card to be available.
            # This feature will stop buying upgrades when the balance is less than the price of the best card.
            "wait_for_best_card": True,  # Recommended to keep it True for high-level accounts
            "enable_parallel_upgrades": True,  # Enable parallel card upgrades. This will buy cards in parallel if the best card is on cooldown. It should speed up the profit.
            "parallel_upgrades_max_price_per_hour": 1000,  # Cards with less than X coins per 1k will be bought
            "show_num_buy_options": 0,  # Number of card buy options to show in the logs, ranked by best value, 0 disables this.
            "max_promo_games_per_round": 3,  # Maximum number of promo games to play in a single round, 0 disables this.
        },
        # If you have enabled Telegram bot logging,
        # you can add your chat ID below to receive logs in your Telegram account.
        # You can obtain your chat ID by messaging @chatIDrobot.
        # Example: "telegram_chat_id": "12345678".
        # If you do not wish to use this feature for this account, leave it empty.
        # This feature is optional and is required to enable the telegramBotLogging feature below.
        "telegram_chat_id": "12345678",  # String - you can get it from https://t.me/chatIDrobot
    }
]
