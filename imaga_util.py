import shutil
import os
import requests
import random

if not os.path.exists('data'):
    os.mkdir('data')



def get_image(name,size=(400,400),url=''):
    if url:
        pass
    else:
        url = f'https://picsum.photos/{size[0]}/{size[1]}'
    response = requests.get(url, stream=True)
    with open(f'data/{name}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        return out_file.name

# get_image(url='https://images.pexels.com/photos/10646596/pexels-photo-10646596.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=1200&w=800')
def gen_image(search='medical',apiKey='563492ad6f9170000100000199b5a66c11e340cf9736b0942e930f4c'):

    headers={"Authorization": apiKey}
    url=f"https://api.pexels.com/v1/search?query={search}&page={random.randint(1,30)}&per_page=40"
    r=requests.get(url,headers=headers)
    photos=r.json()['photos']
    images=[]
    for index,p in enumerate(photos):
        print(p['src']['landscape'])
        name=get_image(p['alt'])
        return name

# gen_image(search='medical')