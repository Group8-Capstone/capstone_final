import json
import datetime

from fastapi import WebSocket


class WebSocketManager:

    def __init__(self):

        self.active_connections = []

        print("=" * 60)
        print("WEBSOCKET MANAGER INITIALIZED")
        print("=" * 60)

    # =====================================================
    # CONNECT
    # =====================================================

    async def connect(self, websocket: WebSocket):

        await websocket.accept()

        self.active_connections.append(websocket)

        print(
            f"Client Connected | Active Clients: "
            f"{len(self.active_connections)}"
        )

    # =====================================================
    # DISCONNECT
    # =====================================================

    def disconnect(self, websocket: WebSocket):

        if websocket in self.active_connections:

            self.active_connections.remove(websocket)

        print(
            f"Client Disconnected | Active Clients: "
            f"{len(self.active_connections)}"
        )

    # =====================================================
    # SEND MESSAGE
    # =====================================================

    async def send_message(

        self,

        websocket: WebSocket,

        message

    ):

        if isinstance(message, dict):

            await websocket.send_json(message)

        else:

            await websocket.send_text(str(message))

    # =====================================================
    # BROADCAST
    # =====================================================

    async def broadcast(self, data):

        if not isinstance(data, dict):

            data = {

                "type": "SYSTEM",

                "message": str(data)

            }

        # Add timestamp automatically

        data.setdefault(

            "timestamp",

            datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )

        disconnected = []

        for websocket in self.active_connections:

            try:

                await websocket.send_json(data)

            except Exception:

                disconnected.append(websocket)

        for websocket in disconnected:

            self.disconnect(websocket)

        print(

            f"Broadcast Sent -> "

            f"{data.get('type','SYSTEM')}"

        )

    # =====================================================
    # SECURITY ALERT
    # =====================================================

    async def security_alert(

        self,

        detection,

        investigation,

        response

    ):

        payload = {

            "type": "SECURITY_ALERT",

            "attack_type":

            detection.get(

                "attack_type"

            ),

            "severity":

            detection.get(

                "severity"

            ),

            "confidence":

            detection.get(

                "score"

            ),

            "threat_level":

            investigation.get(

                "threat_level"

            ),

            "recommendation":

            investigation.get(

                "recommendation"

            ),

            "response":

            response.get(

                "response_action"

            ),

            "status":

            response.get(

                "status"

            )

        }

        await self.broadcast(payload)

    # =====================================================
    # FRAUD ALERT
    # =====================================================

    async def fraud_alert(

        self,

        result

    ):

        payload = {

            "type": "FRAUD_ALERT",

            "prediction":

            result.get(

                "prediction"

            ),

            "confidence":

            result.get(

                "confidence"

            ),

            "message":

            "Fraudulent transaction detected."

        }

        await self.broadcast(payload)

    # =====================================================
    # UEBA ALERT
    # =====================================================

    async def ueba_alert(

        self,

        result

    ):

        payload = {

            "type": "UEBA_ALERT",

            "risk":

            result.get(

                "risk_level",

                "UNKNOWN"

            ),

            "message":

            "Suspicious user behaviour detected."

        }

        await self.broadcast(payload)

    # =====================================================
    # SYSTEM EVENT
    # =====================================================

    async def system_message(

        self,

        message

    ):

        await self.broadcast({

            "type": "SYSTEM",

            "message": message

        })

    # =====================================================
    # CONNECTION COUNT
    # =====================================================

    def connection_count(self):

        return len(self.active_connections)


# =====================================================
# GLOBAL INSTANCE
# =====================================================

websocket_manager = WebSocketManager()