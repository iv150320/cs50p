import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    f = sys.argv[2]
else:
    sys.exit("Invalid usage")

figlet.setFont(font=f)
s = input("Input: ")
print(figlet.renderText(s))
