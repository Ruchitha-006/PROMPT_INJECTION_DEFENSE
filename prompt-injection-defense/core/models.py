class AgentAction:
    def __init__(self, action_type="safe"):
        self.action_type = action_type

    def __repr__(self):
        return f"AgentAction(type={self.action_type})"