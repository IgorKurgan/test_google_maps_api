import requests
from utils.http_method import Http_methods
"""Методы для тестирования G_M api"""

# Базовый url
base_url = "https://rahulshettyacademy.com"
# Параметр для всех запросов
key = "?key=qaclick123"

class Google_maps_api():
    # метод для создания новой локации
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }
        # ресурс метода пост
        post_resousce = "/maps/api/place/add/json"
        post_url = base_url + post_resousce +key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    # метод для проверки новой локации
    @staticmethod
    def get_new_place(place_id):
        # ресурс метода get
        get_resourse = "/maps/api/place/get/json"
        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get
    # метод для изменения новой локации
    @staticmethod
    def put_new_place(place_id):

        put_resourse = "/maps/api/place/update/json"
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    # метод для удаления новой локации
    @staticmethod
    def delete_new_place(place_id):
        # ресурс метода delete
        delete_resourse = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id,

        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete




