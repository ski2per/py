from locust import HttpLocust, TaskSet, task, between


class APITest(TaskSet):
    token = ''
    headers = {}
    def setup(self):
        print("setup")

    def on_start(self):
        r = self.client.post('/api/auth/login', {'username': 'ted', 'password': 'abc'})
        print(r.status_code)
        if r.status_code == 200:
            response_data = r.json()
            self.token = response_data['access_token']
            self.headers['Authorization'] = f'Bearer {self.token}'
        else:
            print('Auth error, quit')
            # Find no other way to quit currently
            exit()

    def on_stop(self):
        print("on stop")

    def teardown(self):
        print('teardown')

    @task(1)
    def get_common_menu(self):
        self.client.get('/api/common/menu', headers=self.headers)

    @task(1)
    def get_api_users(self):
        self.client.get('/api/users/', headers=self.headers)

    @task(1)
    def get_api_groups(self):
        self.client.get('/api/groups/', headers=self.headers)

    @task(1)
    def get_api_maillists(self):
        self.client.get('/api/maillists/', headers=self.headers)



class APITester(HttpLocust):
    task_set = APITest
    wait_time = between(2, 6)
