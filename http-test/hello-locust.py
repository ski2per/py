from locust import Locust, TaskSet, task, HttpLocust


class SimpleGET(TaskSet):
    @task
    def my_task(self):
        resp = self.client.get("/")
        print("{}: {}".format(resp.status_code, resp.text))


class MyLocust(HttpLocust):
    task_set = SimpleGET
