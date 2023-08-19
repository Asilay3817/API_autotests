from utils.http_methods import HTTP_methods

"""Test Methods for Google Maps API"""

url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class GoogleMapsApi():

    """Create new location method"""
    @staticmethod
    def create_new_location():
        post_resource = "/maps/api/place/add/json" # resource POST method
        post_url = f"{url}{post_resource}{key}"
        print(post_url)
        json_body = {
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

        result = HTTP_methods.post(post_url, json_body)
        print(result.text)
        return result


    """Assert new location method"""
    @staticmethod
    def assert_new_location(place_id):
        get_resource = "/maps/api/place/get/json"  # resource GET method
        get_url = f"{url}{get_resource}{key}&place_id={place_id}"
        print(get_url)
        result = HTTP_methods.get(get_url)
        print(result.text)
        return result

    """Update new location method"""
    @staticmethod
    def put_new_location(place_id):
        update_resource = "/maps/api/place/update/json"  # resource PUT method
        put_url = f"{url}{update_resource}{key}"
        print(put_url)
        json_body = {
            "place_id": f"{place_id}",
            "address": "303 Elizavetinskaya street, RU",
            "key": "qaclick123"
        }
        result = HTTP_methods.put(put_url, json_body)
        print(result.text)
        return result

    """Delete new location method"""
    @staticmethod
    def del_new_location(place_id):
        delete_resource = "/maps/api/place/delete/json"  # resource DELETE method
        del_url = f"{url}{delete_resource}{key}"
        print(del_url)
        json_body = {
            "place_id": place_id
        }
        result = HTTP_methods.delete(del_url, json_body)
        print(result)
        return result

