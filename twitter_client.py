from twython import Twython
from PIL import Image
from StringIO import StringIO

class TwitterClient:

  def __init__(self, config):
    self.consumer_key = config['consumer_key']
    self.consumer_secret = config['consumer_secret']
    self.access_token = config['access_token']
    self.access_token_secret = config['access_token_secret']
    self.client = Twython(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)

  def postMedia(self, message, image_path):
    photo = Image.open(image_path)

    basewidth = 640
    wpercent = (basewidth / float(photo.size[0]))
    height = int((float(photo.size[1]) * float(wpercent)))
    photo = photo.resize((basewidth, height), Image.ANTIALIAS)

    image_io = StringIO()
    photo.save(image_io, format='JPEG')
    image_io.seek(0)

    response = self.client.upload_media(media=image_io)
    return self.client.update_status(status=message, media_ids=[response['media_id']])
