import requests

class YaDiskClass:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_dir(self, disk_file_path='test'):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()

        params = {'path': disk_file_path}
        response = requests.put(url=upload_url, headers=headers, params=params)

        return response.status_code


