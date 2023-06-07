import os
from PIL import Image, ImageFilter
from io import BytesIO
import requests

def adjust_aspect_ratio(url, output_path, aspect_ratio=(2, 3)):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    width, height = img.size
    new_height = int((width / aspect_ratio[0]) * aspect_ratio[1])
    
    if new_height > height:
        new_width = int((height / aspect_ratio[1]) * aspect_ratio[0])
        new_height = height
    else:
        new_width = width
    
    img = img.resize((new_width, new_height), Image.LANCZOS)
    img.save(output_path)

urls = [
    'https://i.postimg.cc/6q9KhCYY/enter-the-void.jpg',
    'https://i.postimg.cc/XvKstrw8/city-of-god.jpg',
    'https://i.postimg.cc/J4zdtfgQ/ikiru.jpg',
    'https://i.postimg.cc/s2CYGLKX/synecdoche-new-york.jpg',
    'https://i.postimg.cc/HkC7sy6D/spring-summer-winter-fall-and-spring.jpg',
    'https://i.postimg.cc/y8dJYg5v/akira.jpg',
    'https://i.postimg.cc/05KFhPC3/an-autumn-afternoon.jpg',
    'https://i.postimg.cc/wj7cWcLd/late-spring.jpg',
    'https://i.postimg.cc/qM3p8gvM/tokyo-story.jpg',
    'https://i.postimg.cc/fRtnctB2/tampopo.jpg',
    'https://i.postimg.cc/fLYNPDRh/the-400-blows.jpg',
    'https://i.postimg.cc/kGgjf01M/the-shining.jpg',
    'https://i.postimg.cc/MKkYDfCK/in-the-mood-for-love.jpg',
    'https://i.postimg.cc/sf5SnwdQ/the-player.jpg',
    'https://i.postimg.cc/CxrMjPYf/the-handmaiden.jpg',
    'https://i.postimg.cc/QCVq0gMt/the-truman-show.jpg',
    'https://i.postimg.cc/vB5XSJCN/yi-yi.jpg',
    'https://i.postimg.cc/FFSsTNGx/a-brighter-summer-day.jpg',
    'https://i.postimg.cc/kGKG0mmL/terrorizers.jpg',
    'https://i.postimg.cc/sg2NjP6D/the-color-of-pomegranates.jpg',
    'https://i.postimg.cc/GhtnmsmK/roma.jpg',
    'https://i.postimg.cc/cLgXGXxT/y-tu-mama-tambien.jpg',
    'https://i.postimg.cc/BnRgNHGy/children-of-men.jpg',
    'https://i.postimg.cc/k4KzZ1tG/vengeance-is-mine.jpg',
    'https://i.postimg.cc/TwhpzfSY/dear-zachary-a-letter-to-a-son-about-his-father.jpg',
    'https://i.postimg.cc/BnmQ2MD9/belladonna-of-sadness.jpg',
    'https://i.postimg.cc/T1Wh2mHL/rebels-of-the-neon-god.jpg',
    'https://i.postimg.cc/xCfWmbWh/climax.jpg',
    'https://i.postimg.cc/JnVH1Z2w/shoplifters.jpg',
    'https://i.postimg.cc/yYPWSWLR/nobody-knows.jpg',
    'https://i.postimg.cc/Y01HZcrt/something-in-the-air.jpg',
    'https://i.postimg.cc/wMhQmMKf/trainspotting.jpg',
    'https://i.postimg.cc/jdTz1yJC/chungking-express.jpg',
    'https://i.postimg.cc/W4DD4Nmx/fallen-angels.jpg',
    'https://i.postimg.cc/ZqNFstst/manila-in-the-claws-of-light.jpg',
    'https://i.postimg.cc/rmjBrdrQ/the-housemaid.jpg',
    'https://i.postimg.cc/yx1Y0SHx/chinatown.jpg',
    'https://i.postimg.cc/NFG2Qjdh/mulholland-drive.jpg',
    'https://i.postimg.cc/tCYNK97Z/an-elephant-sitting-still.jpg',
    'https://i.postimg.cc/c4cvrLxs/the-thin-blue-line.jpg',
    'https://i.postimg.cc/ydXQPMnK/f-for-fake.jpg',
    'https://i.postimg.cc/WzSXg08w/parasite.jpg',
    'https://i.postimg.cc/BvPrGZcB/mishima-a-life-in-four-chapters.jpg',
    'https://i.postimg.cc/Y0rynQrj/stalker.jpg',
    'https://i.postimg.cc/ncsZxQbN/still-walking.jpg',
    'https://i.postimg.cc/vm8h99NG/contempt.jpg',
    'https://i.postimg.cc/q721gsLY/insiang.jpg',
    'https://i.postimg.cc/rF3mwxz5/the-ballad-of-narayama.jpg',
    'https://i.postimg.cc/28Py7BdR/mommy.jpg',
    'https://i.postimg.cc/k4CQ5pY4/8-1-2.jpg',
    'https://i.postimg.cc/MpB90XMn/perfect-blue.jpg',
    'https://i.postimg.cc/9fBxnMdJ/millenium-actress.jpg',
    'https://i.postimg.cc/0y9KCdfM/close-up.jpg',
    'https://i.postimg.cc/wxZBWKXs/pickpocket.jpg',
    'https://i.postimg.cc/N0rsC8hd/smiles-of-a-summer-night.jpg',
    'https://i.postimg.cc/tgSXN70Q/christiane-f.jpg',
    'https://i.postimg.cc/C1VLK1sf/branded-to-kill.jpg',
    'https://i.postimg.cc/bJ12w4X3/sans-soleil.jpg',
    'https://i.postimg.cc/nz3qskv6/the-koumiko-mystery.jpg',
    'https://i.postimg.cc/RZzLdT9g/flowers-of-shanghai.jpg',
    'https://i.postimg.cc/Fz9XM2yQ/harakiri.jpg',
    'https://i.postimg.cc/qvK2tY15/the-human-condition-I-no-greater-love.jpg',
    'https://i.postimg.cc/zBYkxNcW/persona.jpg',
    'https://i.postimg.cc/mDF3FfTr/the-discreet-charm-of-the-bourgeoisie.jpg',
    'https://i.postimg.cc/ZKHVtVdn/pixote.jpg',
    'https://i.postimg.cc/4NbsC7Zw/the-holy-mountain.jpg',
    'https://i.postimg.cc/kg8DzXGy/boat-people.jpg',
    'https://i.postimg.cc/tg8yF8Fm/streetwise.jpg',
    'https://i.postimg.cc/MKygw5ZQ/onibaba.jpg',
    'https://i.postimg.cc/26CQRWYd/pyaasa.jpg',
    'https://i.postimg.cc/zfRytSc2/fantastic-planet.jpg',
    'https://i.postimg.cc/XNxyHchr/when-the-cat-comes.jpg',
    'https://i.postimg.cc/MTFVwdNP/woman-in-the-dunes.jpg',
    'https://i.postimg.cc/DwvDpckJ/millennium-mambo.jpg',
    'https://i.postimg.cc/5tTCj1wB/the-mad-fox.jpg',
    'https://i.postimg.cc/Wz8hSNCy/au-hasard-balthazar.jpg',
    'https://i.postimg.cc/LXp19bpm/eureka.jpg',
    'https://i.postimg.cc/Gpz0XxD3/throw-away-your-books-rally-in-the-streets.jpg',
    'https://i.postimg.cc/Xvmk7c3Z/haru.jpg',
    'https://i.postimg.cc/GtNmJc27/a-city-of-sadness.jpg',
    'https://i.postimg.cc/PfYjxzzs/hanagatami.jpg',
    'https://i.postimg.cc/Pr9CqhLg/house.jpg',
    'https://i.postimg.cc/gcLCZvC3/perfumed-nightmare.jpg',
    'https://i.postimg.cc/Rhwrk0b0/in-the-heat-of-the-sun.jpg',
]

for i, url in enumerate(urls, 1):
    file_name = url.split('/')[-1].split('.')[0] + '-adjusted.jpg'
    output_dir = '/Users/codyclifton/Desktop/Website_Images/Adjusted_Images/'
    os.makedirs(output_dir, exist_ok=True)  
    output_path = f'{output_dir}{file_name}'
    adjust_aspect_ratio(url, output_path)
