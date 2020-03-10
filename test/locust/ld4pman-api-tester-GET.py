from locust import HttpLocust, TaskSet, task, between


def get_common_menu(l):
    l.client.get('/api/common/menu', headers=l.headers)


def get_api_users(l):
    l.client.get('/api/users/', headers=l.headers)


def get_api_users_me(l):
    l.client.get('/api/users/me', headers=l.headers)


def get_api_groups(l):
    l.client.get('/api/groups/', headers=l.headers)


def get_api_maillists(l):
    l.client.get('/api/maillists/', headers=l.headers)


class APITest(TaskSet):
    token = ''
    headers = {}

    tasks = [
        get_api_users_me,
        get_api_users,
        get_api_groups,
        get_api_maillists,
    ]

    def on_start(self):
        r = self.client.post('/api/auth/login', {'username': 'ted', 'password': 'ted'})
        print(r.status_code)
        if r.status_code == 200:
            response_data = r.json()
            self.token = response_data['access_token']
            self.headers['Authorization'] = f'Bearer {self.token}'
        else:
            pass
            # print('Auth error, quit')
            # Find no other way to quit currently
            # exit()

    def on_stop(self):
        print("on stop")


class APITester(HttpLocust):
    task_set = APITest
    wait_time = between(2, 6)
