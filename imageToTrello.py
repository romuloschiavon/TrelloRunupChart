import requests

def fileToCard(key, token, image, cardid):
    params = (
        ('key', key),
        ('token', token),
    )

    files = {
        'file': (image, open(image, 'rb')),
    }

    response = requests.post('https://api.trello.com/1/cards/%s/attachments' % cardid, params=params, files=files)

    print(response.text)
    return response

