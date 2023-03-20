import requests


class PlateReaderClient:
    def __init__(self, host):
        self.host = host

    def read_number(self, image_id):
        print(f'{self.host}/read-number?id={image_id}')
        response = requests.get(f'{self.host}/read-number?id={image_id}')

        return response.json()

    def read_several_numbers(self, image_id_list):
        response = requests.get(f'{self.host}/read-several-numbers', params={'id': image_id_list})

        return response.json()


if __name__ == "__main__":
    plate_reader_client = PlateReaderClient('http://0.0.0.0:8080')

    print("test reading single number:")
    valid_ids = [10022, 9965]
    for img_id in valid_ids:
        print(f"{img_id}: {plate_reader_client.read_number(img_id)}")

    print("test reading several numbers:")
    print(f"{valid_ids}: {plate_reader_client.read_several_numbers(valid_ids)}")
