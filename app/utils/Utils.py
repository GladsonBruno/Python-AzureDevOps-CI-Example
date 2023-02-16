import json

class Utils:
    @staticmethod
    def convert_object_list_to_json(list):
        json_list = '['
        for i in range(len(list)):
            item = list[i]
            obj_json = item.to_json()
            json_list += obj_json

            if i + 1 < len(list):
                json_list += ','

        json_list += ']'
        return json.loads(json_list)

    @staticmethod
    def convert_object_to_json(obj):
        json_object = obj.to_json()
        return json.loads(json_object)