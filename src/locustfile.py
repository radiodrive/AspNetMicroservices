from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/api/v1/Catalog")
        self.client.get("/api/v1/Discount/IPhone%20X")