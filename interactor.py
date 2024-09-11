from main import chat

class Chat():
    def __init__(self, username, test, model): self.client = chat.completions(username="Kazenoko", test=test, model=model)
    def run(self, prompt): return f"{self.client.getModel()}: " + self.client.create(prompt=prompt, time_elapse=True)