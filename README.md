# Type-racer-bot
**Botting type racer by web scraping. A project I completed on 13th July, 2021.**

# Requirements:

[Chromedriver](https://chromedriver.chromium.org/)

**Python:**
```python
from selenium import webdriver
import time 
import pyautogui
```

# Project Details:

**Game url:** https://play.typeracer.com/

# How the game works:
This is a speed typing game where you face-off against other players to check who is the fastest typer.

# Project Details:
I wanted to have fun and try to refine my web scraping skills and thought "What better way than through a game!"

**Process:**
- The bot opens a new chrome window, then it sends a get request to the typeracer website.
- Once the website loads, after a small delay (to ensure everything loads), the bot clicks on the "Enter a typing race" button.
- Once inside the game, it goes through the html code of the site and using some simple filtering I procured the required text.
- Now, the bot just types all the text (again, with a small delay).

**Problems faced:**
- Since the bot was too fast I had to add some delay in a lot of places to ensure the bot runs smoothly. 

**After project thoughts:**
- The bot is almost perfect, as it can complete the race everytime with a very high score, but it cannot clear the captcha at the end of the race.
- The bot waits for a fixed time every race so that it types once the race starts and not before. This is an issue as the races can start within any time between 9 and 12 seconds, which causes the bot to, sometimes, not perform optimally (as the word per minute reduces the longer it stays idle).
