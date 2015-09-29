#!/usr/bin/env python3

from subprocess import call
from datetime import datetime
from imgurpython import ImgurClient

filetype = "png"
filename = "shot." + filetype

def take_ss():
    call(["import", filename])

def cleanup():
    call(["rm", filename])

def get_client():
    id = '43c5f165ea223e2'
    secret = 'ac8331bf126e58e2c733f348035b0bd074d96a21'
    return ImgurClient(id, secret)
	
def upload_ss(client):
    image_path = filename
    print("Uploading image to imgur... ")
    image = client.upload_from_path(image_path)
    return image


if __name__ == "__main__":
    take_ss()
    image = upload_ss(get_client())
    print("Image uploaded: {0}".format(image['link']))
    cleanup()

