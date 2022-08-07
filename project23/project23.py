import os

cookies = 0
clicks_total = 1
CLICK = 2
GRANDPA = 4
FARM = 8
INDUSTRY = 12
dic_clicks_boost = {"1":[CLICK, 50], "2":[GRANDPA, 70], "3":[FARM, 90], "4":[INDUSTRY, 130],}
name_boosts = ["Clicks", "Grandpa", "Farm", "Industry"]

def draw_consol(last_buy):
    os.system("cls||clear")
    print(f"{'COOKIE CLICKER':-^55}")
    print(f"{'[Press 1]Click -50 Cookies - Clicks = 2 clicks':>60}")
    print(f"{'[Press 2]Grandpa - 70 Cookies - Clicks = 4 clicks':>63}")
    print(f"{'[Press 3]Farm - 90 Cookies - Clicks = 9 clicks':>60}")
    print(f"{'[Press 4]Industry - 130 Cookies - Clicks = 12 clicks':>66}")
    print(f"cookies: {cookies}", end="")
    print(f"\nclicks per click: {clicks_total}", end="")
    print(f"\nLast information buy: {last_buy}")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nClick Enter to get cookies[ENTER]", end="")

def clicks_cookie():
    global cookies
    global clicks_total
    last_info_buy = ""
    last_last_info_buy = ""
    combo = 0

    while True:
        click = str(input(""))
        cookies += clicks_total
        if click in dic_clicks_boost.keys():
            for boosts in dic_clicks_boost.items():
                if boosts[0] == click:
                    last_info_buy = name_boosts[int(boosts[0]) - 1]
                    if last_last_info_buy == last_info_buy:
                        combo += 1
                        last_info_buy = f"{last_info_buy} +{combo}"
                    else:
                        combo = 0
                    price_boost_cookie = boosts[1][1]
                    more_clicks = boosts[1][0]
                    last_last_info_buy = name_boosts[int(boosts[0]) - 1]
            if cookies >= price_boost_cookie:
                cookies -= price_boost_cookie
                clicks_total += more_clicks
            else:
                last_info_buy = "No have cookies to buy"
                combo = 0

        draw_consol(last_info_buy)

clicks_cookie()
