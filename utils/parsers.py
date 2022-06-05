import asyncio
from requests import session
from requests_html import HTMLSession
import json

session = HTMLSession()


async def ranobehub(url: str):
    id = url.split('/')[-1].split('-')[0]
    API_URL = f'https://ranobehub.org/api/ranobe/{id}/contents'
    r = session.get(API_URL)
    last_chapter = json.loads(r.text)['volumes'][-1]['chapters'][-1]
    return (last_chapter['num'], last_chapter['url'])


async def mangaclub(url: str):
    r = session.get(url)
    chapters = r.html.find('.chapters > *')
    return (len(chapters), chapters[0].find('a', first=True).attrs['href'])


async def main():
    print(await mangaclub('https://mangaclub.ru/3854-the-death-mage-who-doesnt-want-a-fourth-time-9A82.html'))


if __name__ == '__main__':
    asyncio.run(main())
