# Алексей Цветков, Venus - Финальный проект, Инженер по тестированию плюс
import requests
import data
import configuration


# создаем новый заказ
def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


# получаем заказ по треку
def get_order_from_track():
    track_number = create_new_order().json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params={"t": track_number})


# проверяем, что код ответа 200
def test_get_order_from_track_successful():
    assert get_order_from_track().status_code == 200
