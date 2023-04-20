from lib import *

logo2 = f"""\033[30m
                            ⠛⠉⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
                            ⠀⠀⠀⠀⢿⣿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣉⣩⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
                            ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
                            ⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⢀
                            ⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⢀⣠⣾⣿
                            ⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⢀⣰⣶⣿⣿⣿⣿
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠁⠀⠀⢀⣴⣾⣿⣿⣿⣿⡿⠟⠋
                            ⢛⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⡿⠟⢋⣡⣴⣶⡆
                            ⠈⠛⢿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⣿⣿⡿⠋⣁⣴⣾⣿⣿⣿⣿⣷
                            ⣆⢳⣦⡈⣙⠻⠿⢷⣶⣦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣿⣿⣿⣿⣿⡿⠟⠋⠁⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣷⣿⣷⣄⠀⠀⣶⠀⠈⣉⡉⠛⠛⠿⠿⠷⢶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⡿⠿⢛⣋⡁⠀⠀⠀⣷⣸⣿⣿⣿⣿⣿⣿⣿⣿⡏
                            ⣿⣿⣿⣿⣿⢿⡆⢿⣾⠀⢿⣿⣿⣷⣶⣶⠀⡀⠀⠀⠀⣭⣉⣉⣉⣉⣉⣩⣤⣤⣶⣶⣿⣿⣿⡇⠀⠀⠀⢹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷
                            ⣿⣿⣿⣿⣿⣇⢿⡘⣿⡟⠜⣿⣿⣿⣿⣿⡆⣿⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⢸⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣾⣿⣎⢿⣆⠹⣿⣿⣿⣿⣿⡜⣇⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⡇⣿⣿⣿⣿⣿⣿⣿⣿⠟
                            ⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⡙⢦⢻⣿⣿⣿⣿⣿⡽⣆⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⣸⢱⣿⣿⣿⣿⡿⠋⢩⠴⡆
                            ⣿⣿⣿⣿⣿⣿⣿⣧⠙⠛⠛⠀⠁⢻⣿⣿⣿⣿⣿⣝⢦⣀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣣⣿⣿⣿⣿⣿⠀⠀⣿⡇⠁
                            ⣿⣿⡿⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠠⢻⣿⣿⣿⣿⣿⣷⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⡀⠀⠉⠀⠀
                            ⣿⣿⣿⣶⣭⣛⠿⣿⣿⣿⣷⡶⢀⣀⠀⢀⣀⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢡⢆⣿⣿⣿⣿⡿⣡⢀⠀
                            ⣿⣿⣿⢿⣿⣿⣷⣌⢿⣿⣿⣿⣿⣟⣷⡈⠙⠻⠄⠘⣿⣿⡆⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⢠⡿⣸⣿⣿⣿⠟⢀⣿⢻⣿
                            ⣿⣿⣶⣀⣿⣿⣿⣿⢠⣿⣿⣿⣿⣿⣾⣷⣤⠀⠀⣴⣿⣿⣿⣜⢷⣄⠉⠙⠛⠻⠿⠟⠛⠛⠉⠁⠀⠀⣠⠞⣵⣿⣿⣿⠋⢀⣾⣿⠸⣿
                            ⣿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⡻⠿⠟⠀⠀⠈⠛⢿⣿⣿⣷⣿⣶⣄⣀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣵⣾⣿⣿⠟⣵⢠⣿⣿⣿⢰⡌
                            ⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣃⣴⣷⣌⠻⢿⣿⣿⣮⣭⣟⣿⣿⣟⣛⣭⣵⣾⣿⣿⣿⠟⠁⠠⢇⣾⣿⣿⣿⠄⣿
                            ⣬⡛⠿⠿⠿⣋⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⡤⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠔⢂⣠⣾⣿⣿⣿⡿⣰⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⣾⡇⣄⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠛⠉⣀⠔⣠⣴⣿⣿⣿⣿⣿⣿⣳⣿⣿
                            ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⣸⣿⣧⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⢀⠶⢞⣵⣾⣿⣟⣽⣿⣿⣿⡿⣱⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                                              |- Programmed By : Dexter -|
                                              |- GitHub : Dexter-90     -| 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             |- Instagram : ishussain_ -|

"""

print(logo2)
print('\033[32m\033[1m Welcome To "WitAnimePy", You Can Search About Anime, Get Info, Download, And More !\n\n\033[0m')

anime = str(input(f"\033[1m=> Enter anime name : "))
print("\033[32m\033[1m[+] Looking for Anime's ...\033[0m")

search = Witanime(anime).Search()
index = 0
name_keys = []

try:
    for key, value in search.items():
        print(f"\033[1m[ {str(index)} ] ({value['type']}) {key}")
        index += 1
        name_keys.append(key)

except AttributeError:
    raise ValueError(f'\033[1mError With Found Anime Named "{anime}" !')

choice = int(input('\n\033[1m=> Choose anime : '))

try:
    name = name_keys[choice]
    url = search[name]["url"]
    info = Witanime.Info(url)
except IndexError:
    raise ValueError(f'\033[1mError With Found Anime Named "{anime}" With ID "{choice}" !')

print(f"\033[33m\033[1mSo You Choose \"{name}\" Anime That Have {len(info['episodes'])} Episodes !")

choice = int(input("""\n\033[34m\033[1m- [1] Download Episodes    [2] Anime Info
- [3] Episodes URL         \033[31m[4] Exit\033[0m\n
\033[1m=> Choose Mode : \033[0m"""))

if choice == 1:
    episodes = str(input('\033[1m=>\033[0m Enter episode (example: 1-10): \033[1m ')).split("-")
    start = episodes[0]
    end = episodes[1]
    episodes = info["episodes"].values()[start:end]

    if end < start or end > info["episodes-count"]:
        raise ValueError(f"Error With Find Episodes ({episodes})!")

    print(f"\033[33m\033[1m So You Want To Download From Episode {start} To {end} Episodes From {name} Anime !")
    Witanime.Download(episodes)

elif choice == 2:
    print("\033[32m\033[1m [+] General Info:\033[33m\033[1m\n")

    for key, value in info.items():
        print(f"- {key} - {value}")

elif choice == 3:
    see = str(input('\033[1m=> Enter episode (example: 1-10): \033[1m ')).split("-")

    try:
        start = int(see[0])
        end = int(see[1])

    except IndexError:
        raise ValueError("Error With Indexing Your Episodes")

    if end < start or end > len(info["episodes"]):
        raise ValueError(f"Error With Find Episodes ({see})!")

    a = info["episodes"]

    episodes = [a[f"الحلقة {i}"]for i in range(start, end + 1)]

    print("\033[32m\033[1m[+] Collecting Anime Download Links ...\033[0m\n")

    links = []
    a = 0
    for episode in episodes:
        try:
            link = requests.get(Witanime.Episode_Link(episode, 2)["google drive"])
            server = "google drive"
            if link.status_code != 200:
                var = {"hello": "world"}["dexter"]
        except KeyError:
            try:
                link = requests.get(Witanime.Episode_Link(episode, 2)["mega"])
                server = "mega"
                if link.status_code != 200:
                    var = {"hello": "world"}["dexter"]
            except KeyError:
                try:
                    link = requests.get(Witanime.Episode_Link(episode, 2)["mediafire"])
                    server = "mediafire"
                    if link.status_code != 200:
                        var = {"hello": "world"}["dexter"]
                except KeyError:
                    try:
                        link = requests.get(Witanime.Episode_Link(episode, 2)["mega4upload"])
                        server = "mega4upload"
                        if link.status_code != 200:
                            var = {"hello": "world"}["dexter"]
                    except KeyError:
                        raise Exception("Can't Find The Video URL")
        a += 1

        print(f"\033[32m\033[ {'Episodes ' + str(a)}- {server.title()} - {link.url} ")
