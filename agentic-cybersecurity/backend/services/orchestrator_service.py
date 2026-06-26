from agents.ml_agent import MLAgent
from agents.detection_agent import DetectionAgent
from agents.rule_agent import RuleAgent
from agents.ueba_agent import UEBAAgent
from agents.investigation_agent import InvestigationAgent
from agents.response_agent import ResponseAgent


class OrchestratorService:

    def __init__(self):

        print("=" * 60)
        print("AGENTIC AI ORCHESTRATOR INITIALIZED")
        print("=" * 60)

        self.ml_agent = MLAgent()

        self.detection_agent = DetectionAgent()

        self.rule_agent = RuleAgent()

        self.ueba_agent = UEBAAgent()

        self.investigation_agent = InvestigationAgent()

        self.response_agent = ResponseAgent()

        # =====================================================
        # HISTORY
        # =====================================================

        self.investigation_history = []

        self.response_history = []

    # =====================================================
    # COMPLETE PIPELINE
    # =====================================================

    def run(self, data):

        print("=" * 60)
        print("STARTING AGENTIC AI PIPELINE")
        print("=" * 60)

        # =====================================================
        # STEP 1 : MACHINE LEARNING
        # =====================================================

        ml_result = self.ml_agent.predict(data)

        # =====================================================
        # STEP 2 : DETECTION
        # =====================================================

        detection_result = self.detection_agent.detect(data)

        # =====================================================
        # STEP 3 : RULE ENGINE
        # =====================================================

        rule_result = self.rule_agent.evaluate(data)

        # =====================================================
        # STEP 4 : UEBA
        # =====================================================

        ueba_result = self.ueba_agent.analyze(data)

        # =====================================================
        # STEP 5 : INVESTIGATION
        # =====================================================

        investigation_result = (

            self.investigation_agent.investigate(

                detection_result,

                ml_result,

                rule_result,

                ueba_result

            )

        )

        # =====================================================
        # SAVE INVESTIGATION
        # =====================================================

        self.investigation_history.append(
            investigation_result
        )

        # Keep only last 100 investigations

        if len(self.investigation_history) > 100:

            self.investigation_history.pop(0)

        # =====================================================
        # STEP 6 : RESPONSE
        # =====================================================

        response_result = (

            self.response_agent.respond(

                investigation_result

            )

        )

        # =====================================================
        # SAVE RESPONSE
        # =====================================================

        self.response_history.append(
            response_result
        )

        if len(self.response_history) > 100:

            self.response_history.pop(0)

        # =====================================================
        # FINAL RESULT
        # =====================================================

        result = {

            "pipeline_status": "SUCCESS",

            "ml_result": ml_result,

            "detection": detection_result,

            "rule_engine": rule_result,

            "ueba": ueba_result,

            "investigation": investigation_result,

            "response": response_result

        }

        print("=" * 60)
        print("PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)

        return result

    # =====================================================
    # GET INVESTIGATION HISTORY
    # =====================================================

    def get_investigations(self):

        return self.investigation_history

    # =====================================================
    # GET RESPONSE HISTORY
    # =====================================================

    def get_responses(self):

        return self.response_history

    # =====================================================
    # CLEAR INVESTIGATIONS
    # =====================================================

    def clear_investigations(self):

        self.investigation_history.clear()

    # =====================================================
    # CLEAR RESPONSES
    # =====================================================

    def clear_responses(self):

        self.response_history.clear()


# ==========================================================
# GLOBAL ORCHESTRATOR
# ==========================================================

orchestrator = OrchestratorService()


# ==========================================================
# EXTERNAL API
# ==========================================================

def run_pipeline(data):

    return orchestrator.run(data)