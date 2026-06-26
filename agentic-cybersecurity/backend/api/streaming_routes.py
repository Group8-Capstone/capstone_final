from fastapi import APIRouter
import numpy as np

from streaming.websocket_manager import (
    websocket_manager
)

router = APIRouter(
    tags=["Streaming"]
)


# =====================================================
# STREAM STATUS
# =====================================================

@router.get("/api/stream")
def stream_status():

    return {

        "status": "ACTIVE",
        "websocket": "CONNECTED",
        "traffic_per_second": int(
            np.random.randint(
                1800,
                3500
            )
        ),

        "active_alerts": int(
            np.random.randint(
                1,
                15
            )
        )

    }


# =====================================================
# SIMULATE DDOS
# =====================================================

@router.post("/simulate/ddos")
async def simulate_ddos():

    packets = int(

        np.random.randint(

            10000,

            50000

        )

    )

    result = {

        "simulation": "DDoS",

        "status": "TRIGGERED",

        "packets": packets

    }

    await websocket_manager.broadcast({

        "type": "SECURITY_ALERT",

        "severity": "HIGH",

        "attack_type": "DDoS",

        "message":

        f"DDoS Attack Detected ({packets} packets)"

    })

    return result


# =====================================================
# SIMULATE PORT SCAN
# =====================================================

@router.post("/simulate/portscan")
async def simulate_portscan():

    ports = int(

        np.random.randint(

            100,

            1000

        )

    )

    result = {

        "simulation": "PortScan",

        "status": "TRIGGERED",

        "ports_scanned": ports

    }

    await websocket_manager.broadcast({

        "type": "PORTSCAN_ALERT",

        "severity": "MEDIUM",

        "attack_type": "PortScan",

        "message":

        f"Port Scan Detected ({ports} ports)"

    })

    return result


# =====================================================
# SIMULATE MALWARE
# =====================================================

@router.post("/simulate/malware")
async def simulate_malware():

    hosts = int(

        np.random.randint(

            1,

            20

        )

    )

    result = {

        "simulation": "Malware",

        "status": "TRIGGERED",

        "infected_hosts": hosts

    }

    await websocket_manager.broadcast({

        "type": "MALWARE_ALERT",

        "severity": "CRITICAL",

        "attack_type": "Malware",

        "message":

        f"Malware Activity Detected ({hosts} hosts)"

    })

    return result


# =====================================================
# TEST WEBSOCKET
# =====================================================

@router.post("/simulate/test")
async def simulate_test():

    message = {

        "type": "SYSTEM",

        "severity": "INFO",

        "message": "Streaming connection verified."

    }

    await websocket_manager.broadcast(message)

    return {

        "status": "SUCCESS",

        "message": "WebSocket test completed."

    }


# =====================================================
# MANUAL ALERT
# =====================================================

@router.post("/simulate/custom")
async def custom_alert():

    message = {

        "type": "CUSTOM_ALERT",

        "severity": "HIGH",

        "message":

        "Manual security alert generated."

    }

    await websocket_manager.broadcast(message)

    return {

        "status": "SUCCESS",

        "alert": message

    }