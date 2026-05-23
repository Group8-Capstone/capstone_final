from agents.detection_agent import DetectionAgent
from agents.investigation_agent import InvestigationAgent
from agents.response_agent import ResponseAgent
from agents.ueba_agent import UEBAAgent
from agents.rule_agent import RuleAgent
from agents.ml_agent import MLAgent


def run_pipeline(data):

    detection_agent = DetectionAgent()
    ml_agent = MLAgent()
    rule_agent = RuleAgent()
    ueba_agent = UEBAAgent()
    investigation_agent = InvestigationAgent()
    response_agent = ResponseAgent()

    detection_result = detection_agent.detect(data)

    ml_result = ml_agent.predict(data)

    rule_result = rule_agent.evaluate(data)

    ueba_result = ueba_agent.analyze(data)

    investigation_result = investigation_agent.investigate(
        detection_result,
        ml_result,
        rule_result,
        ueba_result
    )

    response_result = response_agent.respond(investigation_result)

    return {
        "detection": detection_result,
        "ml": ml_result,
        "rule": rule_result,
        "ueba": ueba_result,
        "investigation": investigation_result,
        "response": response_result
    }