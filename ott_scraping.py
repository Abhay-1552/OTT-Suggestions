from bs4 import BeautifulSoup
import requests


def ott(content_type):
    try:
        url_extend = ""
        if content_type == "movie":
            url_extend += "https://www.ottplay.com/movies/ott-movie-releases-this-week-watch-online"
        elif content_type == "shows":
            url_extend += "https://www.ottplay.com/shows/ott-web-series-tv-shows-releases-this-week-watch-online"
        else:
            url_extend += "https://www.ottplay.com/ott-releases-streaming-now-this-week-watch-online"

        response = requests.get(url_extend)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        main_content = soup.find_all('li', {'class': 'streamingNow_movieCard__wrapper__peGbN'})

        data_storage = []

        for movie_card in main_content:
            name_element = movie_card.find('span', {'class': 'streamingNow_movieCard__details__title__xwBFv'})
            name = name_element.text.strip() if name_element else "N/A"

            rating_element = movie_card.find('span', {'class': 'streamingNow_newRatings__DT8Fn'})
            rating = rating_element.text.strip() if rating_element else "N/A"

            date_element = movie_card.find('div', {'class': 'streamingNow_movieCard__updates__9SOUX'})
            date = date_element.text.strip() if date_element else "N/A"

            platform_element = movie_card.find('div', {'class': 'streamingNow_movieCard__providerWrap__KuitJ'})
            platform = platform_element.text.strip() if platform_element else "N/A"

            data = []  # data[0]: Type, data[1]: Language, data[2]: Genre
            language_element = movie_card.find('ul', {'class': 'streamingNow_movieCard__details__languages__20uJo'})
            for element in language_element.find_all(
                    'li', {'class': 'streamingNow_movieCard__details__languages__items__qfVlu'}):
                if element.get_text(strip=True):
                    data.append(element.get_text(strip=True))
                else:
                    data.append("N/A")

            data_storage.append({
                "name": name,
                "type": data[0],
                "release_date": date,
                "rating": rating,
                "where_to_watch": platform,
                "language": data[1],
                "genre": data[2]
            })

        return data_storage

    except requests.exceptions.RequestException as e:
        print("Error fetching content:", e)
        return "Error fetching data."


point = ott('shows')
print(point)
