import requests


class ProjectsAPI:

    # Инициализация
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        self.token = self.get_keys_list()  # можно сразу получить

    def get_keys_list(self):
        body = {"login": self.login, "password": self.password}
        resp = requests.post(self.url + '/api-v2/auth/keys/get', json=body)
        return resp.json()[0]["key"]

    # Позитивные методы

    # Создание проект
    def create_project_positive(self, title):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token
        }
        payload = {"title": title}
        resp = requests.post(self.url + '/api-v2/projects', json=payload,
                             headers=headers)
        return resp

    # Изменение проекта
    def update_project_positive(self, project_id, new_title):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + self.token}
        payload = {"title": new_title}
        resp = requests.put(self.url + f'/api-v2/projects/{project_id}',
                            json=payload, headers=headers)
        return resp

    # Получение проекта по ID
    def get_project_id_positive(self, project_id):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + self.token}
        resp = requests.get(self.url + f'/api-v2/projects/{project_id}',
                            headers=headers)
        return resp

    # Негативные методы

    # Создание проект
    def create_project_negative(self, title):
        headers = {
            "Content-Type": "application/jso",
            "Authorization": "Bearer " + self.token
        }
        payloar = {"title": title}
        resp = requests.post(self.url + '/api-v2/projects',
                             json=payloar, headers=headers)
        return resp

    # Изменение проекта
    def update_project_negative(self, project_id, new_title):
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer "}
        payload = {"title": new_title}
        resp = requests.put(self.url + f'/api-v2/projects/{project_id}',
                            json=payload, headers=headers)
        return resp

    # Получение проекта по ID
    def get_project_id_negative(self, project_id):
        resp = requests.get(self.url + f'/api-v2/projects/{project_id}',
                            headers="")
        return resp
