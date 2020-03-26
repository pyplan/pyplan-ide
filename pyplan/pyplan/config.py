import sys
import webbrowser
from os import mkdir
from os.path import exists, join
from shutil import copyfile, copytree
from threading import Thread
from time import sleep

from django.apps import AppConfig
from django.conf import settings
from requests import get as requests_get


class PyplanAppConfig(AppConfig):
    name = 'pyplan.pyplan'
    verbose_name = "Pyplan API"

    def ready(self):
        try:
            from django.contrib.sessions.models import Session
            Session.objects.all().delete()
        except:
            pass
        print('Pyplan is ready')

        try:
            tmp_folder = join(settings.MEDIA_ROOT, 'tmp')
            if not exists(tmp_folder):
                mkdir(tmp_folder)
            # Check if the user has demo models
            examples_folder = join(settings.MEDIA_ROOT, 'models', 'Examples')
            if not exists(examples_folder):
                copytree(join(settings.BACKEND_DIR, 'demos', 'Examples'),
                         examples_folder)
            tutorials_folder = join(settings.MEDIA_ROOT, 'models', 'Tutorials')
            if not exists(tutorials_folder):
                copytree(join(settings.BACKEND_DIR, 'demos', 'Tutorials'),
                         tutorials_folder)
            home_file = join(settings.MEDIA_ROOT, 'models', 'home.json')
            if not exists(home_file):
                copyfile(join(settings.BACKEND_DIR, 'demos', 'home.json'),
                         home_file)
        except Exception as ex:
            print(ex)

        try:
            port = str(sys.argv[1])

            def _wait_for_ready(retries):
                response = None
                try:
                    response = requests_get(
                        f'http://localhost:{port}/api/healthcheck/')
                except:
                    pass
                finally:
                    if not response is None and response.status_code == 200:
                        webbrowser.open(f'http://localhost:{port}', new=2)
                    else:
                        if retries < 40:
                            sleep(1)
                            _wait_for_ready(retries+1)
                        else:
                            print("Open the browser and go to http://localhost:9740")

            waiter = Thread(target=_wait_for_ready, args=(1,))
            waiter.start()

        except Exception as ex:
            print(ex)
            print("Open the browser and go to http://localhost:9740")
