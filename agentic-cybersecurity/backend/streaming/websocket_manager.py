import json

from fastapi import WebSocket


class WebSocketManager:

    def __init__(self):

        self.active_connections = []

        print("=" * 60)
        print("WEBSOCKET MANAGER INITIALIZED")
        print("=" * 60)

    # =====================================
    # CONNECT
    # =====================================

    async def connect(

        self,

        websocket: WebSocket
    ):

        await websocket.accept()

        self.active_connections.append(
            websocket
        )

        print(
            "New WebSocket connection established"
        )

    # =====================================
    # DISCONNECT
    # =====================================

    def disconnect(

        self,

        websocket: WebSocket
    ):

        if websocket in self.active_connections:

            self.active_connections.remove(
                websocket
            )

        print(
            "WebSocket disconnected"
        )

    # =====================================
    # SEND MESSAGE
    # =====================================

    async def send_message(

        self,

        websocket: WebSocket,

        message: str
    ):

        await websocket.send_text(
            message
        )

    # =====================================
    # BROADCAST
    # =====================================

    async def broadcast(

        self,

        data
    ):

        message = json.dumps(data)

        disconnected_clients = []

        for connection in self.active_connections:

            try:

                await connection.send_text(
                    message
                )

            except Exception:

                disconnected_clients.append(
                    connection
                )

        # Remove disconnected clients
        for connection in disconnected_clients:

            self.disconnect(
                connection
            )

        print(
            "Broadcast message sent"
        )

    # =====================================
    # SECURITY ALERT
    # =====================================

    async def broadcast_alert(

        self,

        alert_data
    ):

        await self.broadcast({

            'type': 'SECURITY_ALERT',

            'data': alert_data
        })

        print(
            "Security alert broadcasted"
        )


# =====================================
# GLOBAL INSTANCE
# =====================================

websocket_manager = WebSocketManager()