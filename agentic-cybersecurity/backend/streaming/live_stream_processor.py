import time
import random
import pandas as pd

from utils.logger import log_message

from utils.save_anomaly_scores import (
    save_anomaly_scores
)


class LiveStreamProcessor:

    def __init__(self):

        self.total_packets = 0

        self.total_alerts = 0

        self.anomaly_scores = []

        print("=" * 60)
        print("LIVE STREAM PROCESSOR INITIALIZED")
        print("=" * 60)

    def generate_network_packet(self):

        packet = {

            'packet_id': random.randint(
                1000,
                9999
            ),

            'source_ip': (
                f"192.168.1."
                f"{random.randint(1, 255)}"
            ),

            'destination_ip': (
                f"10.0.0."
                f"{random.randint(1, 255)}"
            ),

            'packet_size': random.randint(
                64,
                1500
            ),

            'protocol': random.choice([
                'TCP',
                'UDP',
                'HTTP',
                'HTTPS'
            ]),

            'anomaly_score': round(
                random.uniform(0, 1),
                4
            )
        }

        return packet

    def process_stream(

        self,

        iterations=50
    ):

        print("=" * 60)
        print("STARTING LIVE STREAM")
        print("=" * 60)

        stream_results = []

        for _ in range(iterations):

            packet = (
                self.generate_network_packet()
            )

            self.total_packets += 1

            anomaly_score = packet[
                'anomaly_score'
            ]

            self.anomaly_scores.append(
                anomaly_score
            )

            if anomaly_score > 0.80:

                self.total_alerts += 1

                packet['status'] = (
                    'ANOMALY DETECTED'
                )

                print(
                    f"[ALERT] "
                    f"{packet}"
                )

                log_message(
                    f"Anomaly detected: {packet}"
                )

            else:

                packet['status'] = 'NORMAL'

                print(
                    f"[NORMAL] "
                    f"{packet}"
                )

            stream_results.append(
                packet
            )

            time.sleep(0.1)

        # =====================================
        # SAVE STREAM RESULTS
        # =====================================

        df = pd.DataFrame(
            stream_results
        )

        save_path = (
            'outputs/predictions/'
            'live_stream_results.csv'
        )

        df.to_csv(

            save_path,

            index=False
        )

        print(
            f"Live stream saved: "
            f"{save_path}"
        )

        # =====================================
        # SAVE ANOMALY SCORES
        # =====================================

        save_anomaly_scores(
            self.anomaly_scores
        )

        print("=" * 60)
        print("LIVE STREAM COMPLETED")
        print("=" * 60)

        print(
            f"Total Packets: "
            f"{self.total_packets}"
        )

        print(
            f"Total Alerts: "
            f"{self.total_alerts}"
        )

        return stream_results