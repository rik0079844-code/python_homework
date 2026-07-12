import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Place import Place

engine = create_engine("postgresql://postgres:123@localhost:5432/postgres")

Session = sessionmaker(bind=engine)

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

@pytest.mark.usefixtures("session")

def create_place(session, name='Park', size=500):
    # Создание тестовой записи
    new_place = Place(place_name=name, place_size=size)
    session.add(new_place)
    session.commit()
    return new_place

def test_get_all_places(session):
    # Запрос на получение всех записей из таблицы places
    places = session.query(Place).all()
    
    # Проверка, что результат не пустой список (для примера)
    assert len(places) > 0, "Список мест пуст"

def test_get_new_places():

    Session = sessionmaker(bind=engine)
    session = Session()
    # Создание тестовой записи
    new_place = Place(place_name='Park', place_size=500)
    session.add(new_place)
    session.commit()
    places = session.query(Place).all()
    #  Проверяем, что все атрибуты каждого места заполнены корректно.
    for place in places:
        assert place.place_name is not None, "Название места отсутствует"
        assert place.place_size is not None, "Размер места отсутствует"

    session.delete(new_place)
    session.commit()

def test_update_place(session):
    # Создание тестовой записи
    new_place = create_place(session)

    # Изменение записи
    new_place.place_size = 600
    session.commit()

    # Проверка изменений
    updated_place = session.query(Place).filter_by(place_id=new_place.place_id).one()
    assert updated_place.place_size == 600, "Размер места не обновился"

    session.delete(new_place)
    session.commit()

def test_delete_place(session):
    # Создание тестовой записи
    new_place = create_place(session)

    # Удаление записи
    session.delete(new_place)
    session.commit()

    # Проверка удаления
    deleted_place = session.query(Place).filter_by(place_id=new_place.place_id).first()
    assert deleted_place is None, "Запись не была удалена"