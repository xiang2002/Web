import os, shutil

from filter.models import Queue


# def init_queue():
# #     for i, img in enumerate(os.listdir('filter/data/')):
# #         Queue.objects.create(name=img)
# #         print(i)
# #     return 0

def delete_img(name):
    print(os.getcwd())
    path = "filter/static/data/"+name
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False


def move_img(name):
    print(os.getcwd())
    path = "filter/static/data/"+name
    move_to = "filter/static/bl/"
    shutil.move(path, move_to)
