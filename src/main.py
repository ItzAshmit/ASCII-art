print("hello! here you can type to make your letters look nice. type stop when you are done. HAVE FUN")


RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


art = {
    "A": f"    {MAGENTA}/\\     {RESET}\n   {MAGENTA}/  \\    {RESET}\n  {MAGENTA}/----\\   {RESET}\n {MAGENTA}/      \\  {RESET}\n{MAGENTA}/        \\ {RESET}",
    "B": f"{RED}|-----\\    {RESET}\n{RED}|     |    {RESET}\n{RED}|-----/    {RESET}\n{RED}|     \\    {RESET}\n{RED}|_____/     {RESET}",
    "C": f"{CYAN}  ______ {RESET}\n{CYAN} /      \\ {RESET}\n{CYAN}|        {RESET}\n{CYAN} \\______/{RESET}\n{CYAN}         {RESET}",
    "D": f"{BLUE}|-----\\    {RESET}\n{BLUE}|      \\   {RESET}\n{BLUE}|       |  {RESET}\n{BLUE}|      /   {RESET}\n{BLUE}|_____/    {RESET}",
    "E": f"{YELLOW}|-------\n|        \n|------- \n|        \n|------- ",
    "F": f"{MAGENTA}|-------\n|        \n|------- \n|        \n|        ",
    "G": f"{CYAN}  ______  \n /      \\ \n|        | \n|   ___/  \n \\_____/  ",  
    "H": f"{GREEN}|     |  \n|     |  \n|-----|  \n|     |  \n|     |  ",
    "I": f"{YELLOW}  |   \n  |   \n  |   \n  |   \n  |   ",
    "J": f"{CYAN}    |   \n    |   \n    |   \n|   |   \n \\__/   {RESET}",
    "K": f"{BLUE}|    / \n|   /  \n|--/   \n|   \\  \n|    \\ ",
    "L": f"{MAGENTA}|        \n|        \n|        \n|        \n|_______ ",
    "M": f"{RED}|     |   \n|\\   /|   \n| \\ / |   \n|  |  |   \n|     |   ", 
    "N": f"{CYAN}|     |   \n|\\    |   \n| \\   |   \n|  \\  |   \n|   \\_|   ",
    "O": f"{YELLOW}  ____  \n /    \\ \n|      |\n \\____/ \n        {RESET}",
    "P": f"{BLUE}|-----\\   \n|     |   \n|-----/   \n|         \n|         ",
    "Q": f"{RED}  ____  \n /    \\ \n|      |\n \\____/ \n     \\__{RESET}",
    "R": f"{CYAN}|-----\\   \n|     |   \n|-----/   \n|    \\    \n|     \\   ",    "S": f"{MAGENTA}  ____   \n /       \n  ---    \n     __/ \n ____/   {RESET}",
    "T": f"{GREEN}|------- \n   |     \n   |     \n   |     \n   |     ",
    "U": f"{YELLOW}|     |   \n|     |   \n|     |   \n|     |   \n \\____/   ",
    "V": f"{RED}|     |   \n|     |   \n \\   /    \n  \\_/     \n          ",
    "W": f"{MAGENTA}|     |     | \n|     |     | \n|     |     |\n|     |     |\n \\___/-/____/    ",
    "X": f"{CYAN}|     |   \n \\   /    \n  \\_/     \n  /\\      \n /  \\     ",
    "Y": f"{BLUE}|     |   \n \\   /    \n  \\_/     \n    |     \n    |     ",
    "Z": f"{YELLOW}|-------  \n     /    \n    /     \n   /      \n  |_______",

    "0": f"{CYAN}  ____  \n /    \\ \n|      |\n|      |\n \\____/ {RESET}",
    "1": f"{MAGENTA}   |    \n   |    \n   |    \n   |    \n   |    ",
    "2": f"{GREEN}  ____  \n /    \\ \n     /  \n  ---    \n |______ ",
    "3": f"{RED}  ____  \n /    \\ \n     /  \n  ---    \n \\____/  ",
    "4": f"{YELLOW}|     |  \n|     |  \n|-----|  \n      |  \n      |  ",
    "5": f"{CYAN} |______ \n|        \n|-----   \n     --- \n  ____/  ",
    "6": f"{MAGENTA}  ____  \n /      \n|______ \n|     | \n \\____/  ",
    "7": f"{BLUE} _______ \n     /   \n    /    \n   /     \n  /      ",
    "8": f"{GREEN}  ____  \n /    \\ \n|----|  \n \\____/ \n        ",
    "9": f"{RED}  ____  \n /    \\ \n|    |  \n \\___/  \n     /\n    /\n   /",
}

while True:
    y = input("").upper()
    if y == "STOP":
        break
    result = []
    for k in y:
        if k in art:
            result.append(art[k])
    print("\n".join(result))


