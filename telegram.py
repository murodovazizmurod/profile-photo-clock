from telethon.sync import TelegramClient, events
from telethon import functions, types
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from PIL import Image, ImageDraw, ImageFont
import time

client = TelegramClient('name', "1996728", "2b7b16880ef540b5dd29efc460ccf28c")
client.start()

time1 = ''

def tick():
       global time1
       # get the current local time from the PC
       time2 = time.strftime('%H:%M')
       # if time string has changed, update it
       if time2 != time1:
            time1 = time2
            img = Image.new('RGB', (640, 640), color = (40, 40, 40))
            font = ImageFont.truetype('fonts/Roboto-Light.ttf', 55)
            d = ImageDraw.Draw(img)
            d.text(((640-(len(time2)*22))/2,640/2-30), time2, font = font, fill = (238,238,238))
            img.save('profile.jpg')
            upload()


def upload():
    client(DeletePhotosRequest(client.get_profile_photos('me')))
    result = client(UploadProfilePhotoRequest(
        file=client.upload_file('profile.jpg')
    ))
    print(result.stringify())
    tick()

while True:
    tick()

client.run_until_disconnected()
