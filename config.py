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
        "account_name": "Account kalip",  # A custom name for the account (not important, just for logs)
        "Authorization": "Bearer 1724902775619vt81wZu89saLNxtegQDsJsF36RvmCH8V3AfSGqvJNZDsG95CjFjdiB0LaTfnBGq16642866145",  # To get the token, refer to the README.md file
        "UserAgent": "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36",  # Refer to the README.md file to obtain a user agent
        "Proxy": {        
  "http": "http://113.195.224.222:9999",
  "http": "http://149.129.226.9:8080",
  "http": "http://120.42.224.254:21212",
  "http": "http://154.202.107.204:3128",
  "http": "http://202.159.35.153:443",
  "http": "http://78.11.40.150:3128",
  "http": "http://87.249.212.26:4145",
  "http": "http://36.7.252.165:3256",
  "http": "http://45.235.123.45:999",
  "http": "http://23.231.34.48:80",
  "http": "http://154.236.179.229:1976",
  "http": "http://180.180.151.53:4145",
  "http": "http://200.43.231.16:4153",
  "http": "http://206.189.12.206:80",
  "http": "http://185.32.5.130:8090",
  "http": "http://184.181.217.201:4145",
  "http": "http://103.23.101.30:4145",
  "http": "http://188.132.203.106:8080",
  "http": "http://103.163.134.95:8090",
  "http": "http://84.241.8.234:8080",
  "http": "http://200.35.50.89:3028",
  "http": "http://51.195.200.115:31280",
  "http": "http://91.134.101.142:80",
  "http": "http://118.173.124.103:4145",
  "http": "http://102.38.17.193:8080",
  "http": "http://146.19.196.145:40234",
  "http": "http://81.94.255.13:8080",
  "http": "http://75.119.206.91:32524",
  "http": "http://192.252.211.197:14921",
  "http": "http://176.105.199.153:8010",
  "http": "http://161.34.40.112:3128",
  "http": "http://27.72.29.7:5678",
  "http": "http://185.189.112.133:3128",
  "http": "http://103.94.133.94:4153",
  "http": "http://79.110.52.252:3128",
  "http": "http://166.0.235.5:63408",
  "http": "http://91.241.130.127:8080",
  "http": "http://35.154.71.72:1080",
  "http": "http://18.228.198.164:80",
  "http": "http://45.90.104.150:9090",
  "http": "http://104.207.62.241:3128",
  "http": "http://45.178.133.60:999",
  "http": "http://206.189.130.107:8080",
  "http": "http://181.129.198.58:5678",
  "http": "http://38.127.179.16:55994",
  "http": "http://13.212.136.79:3128",
  "http": "http://196.204.24.254:8080",
  "http": "http://83.54.9.242:3128",
  "http": "http://200.52.148.10:999",
  "http": "http://119.47.90.230:1111",
  "http": "http://43.153.3.241:443",
  "http": "http://104.239.37.99:5751",
  "http": "http://72.195.34.59:4145",
  "http": "http://103.247.23.197:8080",
  "http": "http://206.1.161.25:9090",
  "http": "http://51.158.98.197:16379",
  "http": "http://213.74.223.77:4153",
  "http": "http://85.232.243.235:8080",
  "http": "http://143.42.191.48:80",
  "http": "http://45.128.133.193:1080",
  "http": "http://107.181.130.58:5679",
  "http": "http://217.69.126.119:5989",
  "http": "http://101.43.191.233:2080",
  "http": "http://110.77.135.70:4145",
  "http": "http://220.248.70.237:9002",
  "http": "http://188.136.162.30:4153",
  "http": "http://212.79.107.116:5678",
  "http": "http://3.71.239.218:80",
  "http": "http://109.92.138.250:5678",
  "http": "http://31.31.77.228:6969",
  "http": "http://50.231.172.74:80",
  "http": "http://104.248.59.38:80",
  "http": "http://93.177.67.178:80",
  "http": "http://162.240.72.139:2079",
  "http": "http://45.6.15.119:5678",
  "http": "http://217.69.126.126:5996",
  "http": "http://117.40.32.133:8080",
  "http": "http://50.205.202.249:3128",
  "http": "http://84.17.35.129:3128",
  "http": "http://159.8.114.37:8123",
  "http": "http://162.19.7.48:43327",
  "http": "http://217.251.109.178:8080",
  "http": "http://143.202.226.205:4145",
  "http": "http://103.47.93.237:1080",
  "http": "http://167.172.109.12:39533",
  "http": "http://45.170.102.89:999",
  "http": "http://23.137.248.197:80",
  "http": "http://51.83.116.2:32909",
  "http": "http://20.205.16.47:3128",
  "http": "http://190.110.99.189:999",
  "http": "http://45.179.71.90:3180",
  "http": "http://43.134.68.153:3128",
  "http": "http://109.201.14.82:8080",
  "http": "http://178.159.42.76:25820",
  "http": "http://206.189.186.59:8080",
  "http": "http://88.80.103.9:6888",
  "http": "http://197.248.249.147:5678",
  "http": "http://8.130.39.117:8899",
  "http": "http://58.246.58.150:9002",
  "http": "http://206.206.64.147:6108",
  "http": "http://103.182.213.65:8080",
  "http": "http://192.9.237.224:3128",
  "http": "http://175.139.201.193:4153",
  "http": "http://50.174.145.9:80",
  "http": "http://154.113.121.60:80",
  "http": "http://37.187.73.7:21052",
  "http": "http://156.239.49.75:3128",
  "http": "http://8.210.69.108:443",
  "http": "http://200.118.152.126:3128",
  "http": "http://103.120.133.141:5678",
  "http": "http://46.146.204.156:1080",
  "http": "http://13.37.73.214:3128",
  "http": "http://49.48.69.224:8080",
  },  # You can use proxies to avoid getting banned. Use {} for no proxy
        # Example of using a proxy:
        # "Proxy": {
        #   "https": "https://10.10.1.10:3128",
        #   "http": "http://user:pass@10.10.1.10:3128/"
        # },
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
    # {
    #     "account_name": "Account 2",  # A custom name for the account (not important, just for logs)
    #     "Authorization": "Bearer TOKEN_HERE",  # To get the token, refer to the README.md file
    #     "UserAgent": "Your UserAgent",  # Refer to the README.md file to obtain a user agent
    #     "Proxy": {},  # You can use proxies to avoid getting banned. Use {} for no proxy
    #     # Example of using a proxy:
    #     # "Proxy": {
    #     #   "https": "https://10.10.1.10:3128",
    #     #   "http": "http://user:pass@10.10.1.10:3128/"
    #     # },
    #     "config": {
    #         "auto_tap": True,  # Enable auto tap by setting it to True, or set it to False to disable
    #         "auto_free_tap_boost": True,  # Enable auto free tap boost by setting it to True, or set it to False to disable
    #         "auto_get_daily_cipher": True,  # Enable auto get daily cipher by setting it to True, or set it to False to disable
    #         "auto_get_daily_task": True,  # Enable auto get daily tasks by setting it to True, or set it to False to disable
    #         "auto_get_task": True,  # Enable auto get (Youtube/Twitter and ...) task to True, or set it to False to disable
    #         "auto_finish_mini_game": True,  # Enable auto finish mini game by setting it to True, or set it to False to disable
    #         "auto_playground_games": True,  # Enable auto playground games by setting it to True, or set it to False to disable
    #         # If you have over 5 accounts, disable the auto_playground_games feature or use a proxy for each account.
    #         "auto_upgrade": True,  # Enable auto-upgrade by setting it to True, or set it to False to disable
    #         "auto_upgrade_start": 2_000_000,  # Start buying upgrades when the balance is greater than this amount
    #         "auto_upgrade_min": 100_000,  # Stop buying upgrades when the balance is less than this amount
    #         # This feature will ignore the auto_upgrade_start and auto_upgrade_min.
    #         # By changing it to True, the bot will find the overall best card and then wait for the best card to be available (based on cooldown or price).
    #         # When the best card is available, the bot will buy it and then wait for the next best card to be available.
    #         # This feature will stop buying upgrades when the balance is less than the price of the best card.
    #         "wait_for_best_card": True,  # Recommended to keep it True for high-level accounts
    #         "enable_parallel_upgrades": True,  # Enable parallel card upgrades. This will buy cards in parallel if the best card is on cooldown. It should speed up the profit.
    #         "parallel_upgrades_max_price_per_hour": 1000,  # Cards with less than X coins per 1k will be bought
    #         "show_num_buy_options": 0,  # Number of card buy options to show in the logs, ranked by best value, 0 disables this.
    #         "max_promo_games_per_round": 3,  # Maximum number of promo games to play in a single round, 0 disables this.
    #     },
    #     # If you have enabled Telegram bot logging,
    #     # you can add your chat ID below to receive logs in your Telegram account.
    #     # You can obtain your chat ID by messaging @chatIDrobot.
    #     # Example: "telegram_chat_id": "12345678".
    #     # If you do not wish to use this feature for this account, leave it empty.
    #     # This feature is optional and is required to enable the telegramBotLogging feature below.
    #     "telegram_chat_id": "",  # String - you can get it from https://t.me/chatIDrobot
    # },
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
    "is_active": True,  # Set it to True if you want to use it, and make sure to fill out the below fields
    "bot_token": "7069215582:AAEXyTWTu4KdhblkgFhG5_IbbtTkZjSEbTo",  # HTTP API access token from https://t.me/BotFather ~ Start your bot after creating it
    # Configure the what you want to receive logs from the bot
    "messages": {
        "general_info": True,  # General information
        "account_info": True,  # Account information
        "http_errors": False,  # HTTP errors
        "other_errors": False,  # Other errors
        "daily_cipher": True,  # Daily cipher
        "daily_task": False,  # Daily task
        "upgrades": True,  # Upgrades
    },
}

ConfigFileVersion = 1
