import requests

# URL duckduckgo : https://duckduckgo.com/?q=wis+epsi&atb=v389-1&iar=images&iax=images&ia=images&iai=http%3A%2F%2Fsafaridesmetiers.tech%2Fwp-content%2Fuploads%2F2021%2F08%2FEpsi-Wiz-Format-page-Partenaires.png

# URL image : http://safaridesmetiers.tech/wp-content/uploads/2021/08/Epsi-Wiz-Format-page-Partenaires.png
# trigger get method with URL

# check response status

# write response image into file

def get_image_wis():

    url_image = 'http://safaridesmetiers.tech/wp-content/uploads/2021/08/Epsi-Wiz-Format-page-Partenaires.png'

    response = requests.get(url_image)
    if response.status_code == 200:
        binary_content = response.content
        with open(file = './image.png', mode = 'wb') as f:
            f.write(binary_content)

def get_tasks():
    # query web service tasks
    url_api_tasks = 'https://my-json-server.typicode.com/argonaultes-public/tp-wis-webservices-python-2024/tasks'
    response = requests.get(url_api_tasks)

    response.raise_for_status()
    if response.status_code == 200:
        print(response.content)
        tasks = response.json()
        print(tasks)
        for task in tasks:
            print(f'Tâche n°{task['id']}: {task['title'].capitalize()}')
            
get_tasks()
# requests.

# display all tasks

# loop over the result to display each task