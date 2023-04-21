import gdown
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class Witanime:

    def __init__(self, name=None) -> None:
        self.name = name

    def Search(self):

        soup = BeautifulSoup(
            requests.get(f"https://witanime.com/?search_param=animes&s={self.name.replace(' ', '+')}").content,
            "html.parser")
        if not soup.find("div", class_="no-posts-found"):
            title_cards = soup.find_all("div", class_="anime-card-title")
            type_cards = soup.find_all("div", class_="anime-card-type")
            url_cards = soup.find_all("a", class_="overlay")

            result = {}
            for tc, tc2, uc in zip(title_cards, type_cards, url_cards):
                card = tc.find("a")
                result[card.text] = {"url": uc["href"], "type": tc2.find("a").text.strip()}
            return result

    @staticmethod
    def Episodes(url):
        cards = BeautifulSoup(requests.get(str(url)).content, "html.parser").find_all("div",
                                                                                      class_="episodes-card-title")
        result = {}
        for card in cards:
            result[card.text.strip()] = card.find("a")["href"]
        return result

    @staticmethod
    def Episode_Link(episode: str, Type=1):
        if Type == 1:
            response = requests.get(episode).content
            soup = BeautifulSoup(response, 'html.parser')
            result = {quality.find('li').text: {l.find('a').text: l.a['href'] for l in quality.find_all('li')[1:]} for
                      quality in soup.find_all('ul', class_='quality-list')}
            return result
        elif Type == 2:
            url = str(episode)
            soup = BeautifulSoup(requests.get(url).content, 'html.parser')
            result = {i.text: i.get("href") for i in soup.find_all("a", class_="btn btn-default")}
            return result

    @staticmethod
    def Info(url):

        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        anime_info = soup.find_all("div", class_="anime-info")

        title = soup.find('h1', class_='anime-details-title').text.strip()
        story = soup.find("p", class_="anime-story").text.strip()
        genres = [genre.text.strip() for genre in soup.find('ul', class_='anime-genres').find_all('a')]
        anime_type = anime_info[0].find('a').text
        status = anime_info[2].find('a').text.strip()
        cover = soup.find('img', class_='thumbnail img-responsive')['src']
        episode_duration = anime_info[2].text.strip()
        premiered = anime_info[1].text.strip()
        episodes = Witanime.Episodes(url)
        episodes_count = len(episodes)
        season = anime_info[4].text.strip()
        source = anime_info[5].text.strip()
        mal = soup.find('a', class_='anime-mal')['href']
        try:
            teaser = soup.find('a', class_='anime-trailer')['href']
        except TypeError:
            teaser = None

        is_movie = True if "Movie" in anime_type else False

        return {"title": title, "story": story, "genres": genres, "type": anime_type, "status": status, "cover": cover,
                "episode-duration": episode_duration, "premiered": premiered, "episodes": episodes,
                "episodes-count": episodes_count, "season": season, "source": source, "mal": mal, "teaser": teaser,
                "is-movie": is_movie}

    @staticmethod
    def Download(url, fn):
        global response
        if "mega" in url:
            mega_key = url.split("#")[1]
            mega_cipher = mega_key.split("!")
            file_id = url.split("/")[-1].split("#")[0]

            download_link = f"https://mega.nz/#!{mega_cipher[0]}!{mega_key}!{file_id}"

            response = requests.get(download_link, stream=True)

            with open(fn, "wb") as f:
                file_size = int(response.headers.get("Content-Length", 0))
                chunk_size = 1024
                progress_bar = tqdm(total=file_size, unit="iB", unit_scale=True)

                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        progress_bar.update(len(chunk))

            progress_bar.close()

        elif "drive" in url:
            gdown.download(url, fn, quiet=False)

        elif "file upload" in url or "mediafire" in url:

            response = requests.get(url, stream=True)

            with open(fn, "wb") as f:
                file_size = int(response.headers.get("Content-Length", 0))
                chunk_size = 1024
                progress_bar = tqdm(total=file_size, unit="iB", unit_scale=True)

                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        progress_bar.update(len(chunk))

            progress_bar.close()

        else:
            print("Can't Find Video Server URL")
