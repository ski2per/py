from locust import HttpLocust, TaskSet, task, between


class APITest(TaskSet):
    def setup(self):
        print("setup")

    def on_start(self):
        r = self.client.post('/api/auth/login', {'username': 'ted', 'password': 'ted'})
        print(r.text)

    def on_stop(self):
        print("on stop")

    def teardown(self):
        print('teardown')

    @task
    def get_menu(self):
        self.client.get('/api/common/menu')


class APITester(HttpLocust):
    task_set = APITest
    wait_time = between(2, 6)
