class FeedbackAgent:

    def collect_feedback(self, response):

        return {
            "feedback_status": "logged",
            "response": response
        }