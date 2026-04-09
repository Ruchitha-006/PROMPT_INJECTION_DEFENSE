class AgentAction:
    def __init__(self, task_output="", injection_detected=False, injection_locations=None, reasoning=""):
        self.task_output = task_output
        self.injection_detected = injection_detected
        self.injection_locations = injection_locations or []
        self.reasoning = reasoning

    def __repr__(self):
        return f"AgentAction(output={self.task_output[:30]})"