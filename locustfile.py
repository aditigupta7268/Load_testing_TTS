from locust import HttpUser, task, between

class TTSUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def generate_audio(self):
        self.client.post(
            "/generate",
            json={"text": "AI Podcast Test"}
        )
