import json
from utils.api import GoogleMapsApi
from utils.checking import CheckAll

"""Create Update Delete methods test"""
def test_create_new_location():

    print("\nStart: test_create_new_location")
    print("\nPOST method")
    result_post = GoogleMapsApi.create_new_location()
    check_post = result_post.json()
    place_id = check_post.get("place_id")
    CheckAll.check_status_code(result_post, 200)
    # print(list(result_post.json()))
    CheckAll.check_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id']) #проверка что ответ содержит ожидаемые ключи
    CheckAll.check_token_values(result_post, 'scope', 'APP') #проверка что значение ключа ответа содержит ожидаемое значение

    print("\nGET method assert POST")
    result_get = GoogleMapsApi.assert_new_location(place_id)
    CheckAll.check_status_code(result_get, 200)
    #print(list(result_get.json()))
    CheckAll.check_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
    CheckAll.check_token_values(result_get, 'website', 'http://google.com')

    print("\nPUT method")
    result_put = GoogleMapsApi.put_new_location(place_id)
    CheckAll.check_status_code(result_put, 200)
    CheckAll.check_token(result_put, ['msg'])
    CheckAll.check_token_values(result_put, 'msg', 'Address successfully updated')

    print("\nGET method assert PUT")
    result_get = GoogleMapsApi.assert_new_location(place_id)
    CheckAll.check_status_code(result_get, 200)
    CheckAll.check_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
    CheckAll.check_token_values(result_get, 'address', '303 Elizavetinskaya street, RU')

    print("\nDELETE method")
    result_del = GoogleMapsApi.del_new_location(place_id)
    CheckAll.check_status_code(result_del, 200)
    CheckAll.check_token(result_del, ['status'])
    CheckAll.check_token_values(result_del, 'status', 'OK')

    print("\nGET method assert DELETE")
    result_get = GoogleMapsApi.assert_new_location(place_id)
    CheckAll.check_status_code(result_get, 404)
    CheckAll.check_token(result_get, ['msg'])
    CheckAll.check_token_values(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")


    print("Finish: test_create_new_location")
