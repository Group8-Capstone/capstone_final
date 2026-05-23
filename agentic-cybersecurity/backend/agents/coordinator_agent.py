from utils.save_agent_report import (
    save_agent_report
)

from utils.logger import (
    log_message
)


class CoordinatorAgent:

    def __init__(

        self,

        detection_agent,

        investigation_agent,

        response_agent
    ):

        self.detection_agent = (
            detection_agent
        )

        self.investigation_agent = (
            investigation_agent
        )

        self.response_agent = (
            response_agent
        )

        self.pipeline_history = []

        print("=" * 60)
        print("COORDINATOR AGENT INITIALIZED")
        print("=" * 60)

        log_message(
            "Coordinator Agent initialized"
        )

    def run_pipeline(

        self,

        network_data
    ):

        print("=" * 60)
        print("AGENTIC AI PIPELINE STARTED")
        print("=" * 60)

        try:

            # =====================================
            # STEP 1: DETECTION
            # =====================================

            detection_result = (

                self.detection_agent.detect(
                    network_data
                )
            )

            detection_status = (

                detection_result.get(
                    'status',
                    'unknown'
                )
            )

            print(
                f"Detection Status: "
                f"{detection_status}"
            )

            # =====================================
            # STEP 2: INVESTIGATION
            # =====================================

            investigation_result = (

                self.investigation_agent.investigate(

                    detection_result
                )
            )

            threat_level = (

                investigation_result.get(
                    'threat_level',
                    'LOW'
                )
            )

            print(
                f"Threat Level: "
                f"{threat_level}"
            )

            # =====================================
            # STEP 3: RESPONSE
            # =====================================

            response_result = (

                self.response_agent.respond(

                    investigation_result
                )
            )

            response_action = (

                response_result.get(
                    'action',
                    'NONE'
                )
            )

            print(
                f"Response Action: "
                f"{response_action}"
            )

            # =====================================
            # PIPELINE RESULT
            # =====================================

            pipeline_result = {

                'status': 'COMPLETED',

                'flows_analyzed': len(
                    network_data
                ),

                'detection': detection_result,

                'investigation': (
                    investigation_result
                ),

                'response': response_result,

                'alerts': 1
                if detection_status ==
                'anomaly_detected'
                else 0,

                'investigations': 1,

                'responses': 1,

                'escalations': 1
                if threat_level in [
                    'HIGH',
                    'CRITICAL'
                ]
                else 0
            }

            # =====================================
            # SAVE PIPELINE HISTORY
            # =====================================

            self.pipeline_history.append(
                pipeline_result
            )

            # =====================================
            # SAVE REPORT
            # =====================================

            save_agent_report(

                pipeline_result,

                'coordinator_pipeline_report'
            )

            log_message(
                "Coordinator pipeline completed"
            )

            print("=" * 60)
            print("PIPELINE COMPLETED")
            print("=" * 60)

            return pipeline_result

        except Exception as e:

            print(
                f"Pipeline execution error: {e}"
            )

            log_message(
                f"Pipeline error: {e}"
            )

            return {

                'status': 'FAILED',

                'message': str(e)
            }

    def generate_comprehensive_report(self):

        print("=" * 60)
        print("GENERATING COMPREHENSIVE REPORT")
        print("=" * 60)

        try:

            report = {

                'total_runs': len(
                    self.pipeline_history
                ),

                'history': (
                    self.pipeline_history
                )
            }

            save_agent_report(

                report,

                'comprehensive_agent_report'
            )

            log_message(
                "Comprehensive report generated"
            )

            print(
                "Comprehensive report saved"
            )

            print("=" * 60)

            return report

        except Exception as e:

            print(
                f"Comprehensive report "
                f"generation error: {e}"
            )

            return {

                'status': 'FAILED',

                'message': str(e)
            }