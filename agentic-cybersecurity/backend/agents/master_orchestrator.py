from agents.detection_agent import DetectionAgent
from agents.investigation_agent import InvestigationAgent
from agents.response_agent import ResponseAgent
from agents.ueba_agent import UEBAAgent
from agents.rule_agent import RuleAgent
from agents.ml_agent import MLAgent
from agents.feedback_agent import FeedbackAgent


class MasterOrchestrator:

    def __init__(self):

        self.detector = DetectionAgent()
        self.ml_agent = MLAgent()
        self.rule_agent = RuleAgent()
        self.ueba_agent = UEBAAgent()
        self.investigation_agent = InvestigationAgent()
        self.response_agent = ResponseAgent()
        self.feedback_agent = FeedbackAgent()

    def execute(self, data):

        detection = self.detector.detect(data)

        ml_result = self.ml_agent.predict(data)

        rule_result = self.rule_agent.evaluate(data)

        ueba_result = self.ueba_agent.analyze(data)

        investigation = self.investigation_agent.investigate(
            detection,
            ml_result,
            rule_result,
            ueba_result
        )

        response = self.response_agent.respond(investigation)

        feedback = self.feedback_agent.collect_feedback(response)

        return {
            "detection": detection,
            "ml": ml_result,
            "rule": rule_result,
            "ueba": ueba_result,
            "investigation": investigation,
            "response": response,
            "feedback": feedback
        }