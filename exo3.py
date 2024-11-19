import requests

# URL duckduckgo : https://duckduckgo.com/?q=wis+epsi&atb=v389-1&iar=images&iax=images&ia=images&iai=http%3A%2F%2Fsafaridesmetiers.tech%2Fwp-content%2Fuploads%2F2021%2F08%2FEpsi-Wiz-Format-page-Partenaires.png

# URL image : http://safaridesmetiers.tech/wp-content/uploads/2021/08/Epsi-Wiz-Format-page-Partenaires.png
# trigger get method with URL

# check response status

# write response image into file

def get_image_wis():

    url_image = 'http://safaridesmetiers.tech/wp-content/uploads/2021/08/Epsi-Wiz-Format-page-Partenaires.png'

    response = requests.get(url_image)
    if response.status_code:
        binary_content = response.content
        with open(file = './image.png', mode = 'wb') as f:
            f.write(binary_content)

def get_tasks():
    pass

# query web service tasks

# requests.

# display all tasks

# loop over the result to display each task