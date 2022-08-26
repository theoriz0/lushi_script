import os, random
import grequests
from dotenv import load_dotenv

load_dotenv()
BARK_URL = os.getenv('BARK_URL')

def exception_handler(request, exception):
    print("Bark request failed")

def send_bark_notification(title, content='From lushi_script, no content specified'):
    if None is title:
        URL = BARK_URL + '/' + content
    else:
        URL = BARK_URL + '/' + title + '/' + content
        # print(URL)
    reqs = [grequests.get(URL)]
    grequests.map(reqs, exception_handler=exception_handler)

# def test_bark():
#     testText = 'But to what purpose, disturbing the dust on a bowl of rose-leaves, I do not know.'
#     sendBarkNotification('Testing lushi_script' + str(random.randint(1,999)), testText)

# test_bark()
