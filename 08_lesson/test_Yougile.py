from ProjectsAPI import ProjectsAPI


api = ProjectsAPI("https://ru.yougile.com", "login", "password")


# Проверка получения списка ключей
def test_get_keys():
    result = api.get_keys_list()
    assert result


def test_create_project_positive():
    title = "Старый проект"
    resp = api.create_project_positive(title)
    assert resp.status_code == 201
    data = resp.json()
    assert "id" in data
    return data["id"]  # можно сохранить для других тестов


def test_update_project_positive():
    # сначала создадим проект
    create_resp = api.create_project_positive("Для обновления")
    project_id = create_resp.json()["id"]
    new_title = "Новый проект"
    update_resp = api.update_project_positive(project_id, new_title)
    assert update_resp.status_code == 200
    # проверим, что обновилось
    get_resp = api.get_project_id_positive(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == new_title


def test_get_project_id_positive():
    create_resp = api.create_project_positive("Для обновления")
    project_id = create_resp.json()["id"]
    get_resp = api.get_project_id_positive(project_id)
    assert get_resp.status_code == 200


def test_create_project_negative():
    title = "Старый проект"
    resp = api.create_project_negative(title)
    assert resp.status_code == 400


def test_update_project_negative():
    # сначала создадим проект
    create_resp = api.create_project_positive("Для обновления")
    project_id = create_resp.json()["id"]

    new_title = "Новый проект"
    update_resp = api.update_project_negative(project_id, new_title)
    assert update_resp.status_code == 401


def test_get_project_id_negative():
    create_resp = api.create_project_positive("Для обновления")
    project_id = create_resp.json()["id"]
    get_resp = api.get_project_id_negative(project_id)
    assert get_resp.status_code == 401
