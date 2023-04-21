from lib import *

try:
    logo2 = f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                                    |-\033[1m Programmed By :\033[31;1m  Dexter \033[0m-|
                                    |\033[1m- GitHub : \033[31;1m Dexter-90     \033[0m-| 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 |\033[1m- Instagram : \033[31;1m ishussain_ \033[0m-|

    """

    print(logo2)
    print('\033[32m\033[1m Welcome To \033[31m\033[1m"WitAnimePy"\033[32m, You Can Download Anime, Get Anime Info, Search For Anime And More !\n\033[0m')

    anime = str(input(f"\033[1m=> Enter anime name : "))
    print("\033[32m\033[1m[+] Looking for Anime's ...\033[0m\n")

    search = Witanime(anime).Search()
    index = 0
    name_keys = []

    try:
        for key, value in search.items():
            print(f"\033[0m[ {str(index)} ] \033[33m({value['type']})\033[0m\033[1m {key}")
            index += 1
            name_keys.append(key)

    except AttributeError:
        raise ValueError(f'\033[0mError With Found Anime Named "{anime}" !')

    choice = int(input('\n\033[0m\033[1m=> Choose anime : '))

    try:
        name = name_keys[choice]
        a = search[name]
        Type = a["type"]
        info = Witanime.Info(a["url"])
        ec = info["episodes-count"]

    except IndexError:
        raise ValueError(f'\033[1mError With Found Anime Named "{anime}" With ID "{choice}" !')

    print(f"\033[32m\033[1mSo You Choose \"{name}\" {Type} That Have {ec} Episodes !")

    if Type == "Movie":
        choice = int(input("""\n\033[34m\033[1m- [1] Download Movie    [2] Movie Info
        - [3] Movie Server URL         \033[31m[4] Exit\033[0m\n
        \033[1m=> Choose Mode : \033[0m"""))
    else:
        choice = int(input("""\n\033[34m\033[1m- [1] Download Episodes    [2] Anime Info
- [3] Episodes Server URL  \033[31m[4] Exit\033[0m\n
\033[1m=> Choose mode : \033[0m"""))

    if choice == 1:
        if type == "Movie":
            if ec > 1:
                episodes = str(input(f'\033[1m=>\033[0m Enter movie episodes (example: 1-{ec}): \033[1m ')).split("-")
            else:
                episodes = "1"
        else:
            episodes = str(input(f'\033[0m\033[1m=> Enter episode (example: 1-{ec}): ')).split("-")

        if not episodes == "1":
            try:
                start = int(episodes[0])
                end = int(episodes[1])
            except IndexError:
                raise ValueError("Error With Indexing Your Episodes")

            if end < start or end > len(info["episodes"]):
                raise ValueError(f"Error With Find Episodes ({episodes})!")

            a = info["episodes"]
            try:
                episodes = [a[f"الحلقة {i}"]for i in range(start, end + 1)]
            except KeyError:
                print("Error")


            print(f"\033[33m\033[1mSo You Want To Download From Episode {start} To {end} Episodes From {name} Anime !")
            s = start
        else:
            s = episodes
            print(f"\033[33m\033[1mSo You Want To Download {name} Anime Movie !")

        link = ""
        for episode in episodes:
            try:
                link = Witanime.Episode_Link(episode, 2)["google drive"]
                server = "google drive"
            except KeyError or KeyError:
                try:
                    link = Witanime.Episode_Link(episode, 2)["mega"]
                    server = "mega"
                except KeyError or KeyError:
                    try:
                        link = Witanime.Episode_Link(episode, 2)["mediafire"]
                        server = "mediafire"
                    except KeyError or KeyError:
                        try:
                            link = Witanime.Episode_Link(episode, 2)["file upload"]
                            server = "file upload"
                        except KeyError or KeyError:
                            print(f"Can't Find The Video URL For {s}")

            if episodes == "1":

                Witanime.Download(link, f"@{name}{s}.mp4")

            else:
                Witanime.Download(link, f"@{name}{s}.mp4")
                s += 1


    elif choice == 2:
        print("\033[32m\033[1m [+] General Info:\033[33m\033[1m\n")

        for key, value in info.items():
            print(f"- {key} - {value}")

    elif choice == 3:
        if type == "Movie":
            if ec > 1:
                episodes = str(input(f'\033[0m\033[1m=> Enter movie episodes (example: 1-{ec}): ')).split("-")
            else:
                episodes = "1"
        else:
            episodes = str(input(f'V\033[1m=> Enter episode (example: 1-{ec}): ')).split("-")

        if not episodes == "1":
            try:
                start = int(episodes[0])
                end = int(episodes[1])
            except IndexError:
                raise ValueError("Error With Indexing Your Episodes")

            if end < start or end > len(info["episodes"]):
                raise ValueError(f"Error With Find Episodes ({episodes})!")

            a = info["episodes"]
            try:
                episodes = [a[f"الحلقة {i}"] for i in range(start, end + 1)]
            except KeyError:
                print("Error")

            print("\033[32m\033[1m[+] Collecting Anime Download Links ...\033[0m\n")
            s = start
        else:
            s = episodes
            print("\033[32m\033[1m[+] Collecting Anime Download Links ...\033[0m\n")

        link = ""
        server = ""
        index = 1
        for episode in episodes:
            try:
                link = Witanime.Episode_Link(episode, 2)["google drive"]
                server = "google drive"
            except KeyError or KeyError:
                try:
                    link = Witanime.Episode_Link(episode, 2)["mega"]
                    server = "mega"
                except KeyError or KeyError:
                    try:
                        link = Witanime.Episode_Link(episode, 2)["mediafire"]
                        server = "mediafire"
                    except KeyError or KeyError:
                        try:
                            link = Witanime.Episode_Link(episode, 2)["file upload"]
                            server = "file upload"
                        except KeyError or KeyError:
                            print(f"Can't Find The Video URL For {s}")
            title = f"Episode {index}"
            print(f"\033[32m[ {title} - {server.title()} - {link} ")
            index += 1
except KeyboardInterrupt:
    exit("bye")
