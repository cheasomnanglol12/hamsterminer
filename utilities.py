# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
import base64


# Sort upgrades by best profit per hour (profitPerHourDelta / price)
# You can change this to sort by price, profitPerHourDelta, level, etc.
def SortUpgrades(upgrades, max_budget):
    upgrades = [item for item in upgrades if item["price"] <= max_budget]
    upgrades.sort(key=lambda x: x["price"] / x["profitPerHourDelta"])
    return upgrades


def CalculateCardProfitCoefficient(card):
    return card["price"] / card["profitPerHourDelta"]


def FindBestCardWithLowerCoefficient(upgrades, max_coefficient):
    cards = SortUpgrades(upgrades, 999_999_999_999_999)
    for card in cards:
        card_coeff = CalculateCardProfitCoefficient(card)
        if card_coeff <= max_coefficient and "cooldownSeconds" in card and card["cooldownSeconds"] == 0:
            return card
    return None


# Convert number to string with k, m, b, t to make it more readable
def number_to_string(num):
    if num < 1000:
        return str(num)
    elif num < 1000000:
        return str(round(num / 1000, 2)) + "k"
    elif num < 1000000000:
        return str(round(num / 1000000, 2)) + "m"
    elif num < 1000000000000:
        return str(round(num / 1000000000, 2)) + "b"
    else:
        return str(round(num / 1000000000000, 2)) + "t"


def DailyCipherDecode(cipher):
    cipher = cipher[:3] + cipher[4:]
    cipher = cipher.encode("ascii")
    cipher = base64.b64decode(cipher)
    cipher = cipher.decode("ascii")
    return cipher


def TextToMorseCode(text):
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-",
        "@": ".--.-.",
    }
    text = text.upper()
    morse = ""
    for char in text:
        if char in morse_code:
            morse += morse_code[char] + " "
    return morse
