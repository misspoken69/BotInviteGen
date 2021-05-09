import colorama
from colorama import Fore, Back, Style
colorama.init()

intro = rf"""

{Fore.LIGHTRED_EX} +--^----------,--------,-----,--------^--------,
{Fore.YELLOW} | |||||||||   `--------'  Bot Invite Generator 0
{Fore.LIGHTRED_EX} `+---------------------------^-----------------|
{Fore.YELLOW}   `\_,---------,---------,---------------------'
{Fore.LIGHTRED_EX}     / XXXXXX /'|       /'
{Fore.YELLOW}    / XXXXXX /  `\    /'
{Fore.LIGHTRED_EX}   / XXXXXX /`-------'
{Fore.YELLOW}  / XXXXXX /  By Misspoken
{Fore.LIGHTRED_EX} / XXXXXX /
{Fore.YELLOW}(________(                
{Fore.LIGHTRED_EX}`------'                         

{Fore.RESET}"""
    
print(intro)

id = input("[>] Input Bot ID: ")

invgen = "[>] https://discord.com/oauth2/authorize?client_id=" + id + "&permissions=8&scope=bot"

print("[>] Bot invited generated!")
print(invgen)

input()
print()
