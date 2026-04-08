class PromptInjectionEnv:
    def __init__(self):
        self.state = {}

    def step(self, action):
        # dummy step function
        obs = {"message": "Processed"}
        
        class Reward:
            def __init__(self):
                self.value = 1
        
        reward = Reward()
        done = True
        info = {"status": "ok"}

        return obs, reward, done, info