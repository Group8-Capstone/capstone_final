import asyncio

from fastapi import (
    FastAPI,
    WebSocket
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi.staticfiles import (
    StaticFiles
)

from api.routes import router

from services.model_initializer import (
    initialize_models
)

from utils.logger import (
    log_message
)

from streaming.websocket_manager import (
    websocket_manager
)

from services.monitoring_engine import (
    start_monitoring
)

# =====================================
# FASTAPI APP
# =====================================

app = FastAPI(

    title="Agentic AI Cybersecurity",

    description=(
        "AI-powered Cybersecurity "
        "Monitoring Platform"
    ),

    version="1.0.0"
)

# =====================================
# CORS
# =====================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# =====================================
# STATIC OUTPUTS
# =====================================

app.mount(

    "/outputs",

    StaticFiles(directory="outputs"),

    name="outputs"
)

# =====================================
# DASHBOARD FILES
# =====================================

app.mount(

    "/dashboard",

    StaticFiles(directory="dashboard"),

    name="dashboard"
)

# =====================================
# STARTUP EVENT
# =====================================

@app.on_event("startup")
async def startup_event():

    initialize_models()
    
    asyncio.create_task(
        start_monitoring()
    )

    print(
        "Automatic Monitoring Enabled"
    )

    print("=" * 70)
    print("STARTING CYBERSECURITY API")
    print("=" * 70)

    log_message(
        "FastAPI startup initialized"
    )

    try:

        # =================================
        # INITIALIZE MODELS
        # =================================

        initialize_models()

        print("=" * 70)
        print("MODELS LOADED SUCCESSFULLY")
        print("=" * 70)

        log_message(
            "Models loaded successfully"
        )

    except Exception as e:

        print(
            f"Startup error: {e}"
        )

        log_message(
            f"Startup error: {e}"
        )

# =====================================
# INCLUDE ROUTES
# =====================================

app.include_router(

    router,

    tags=["Cybersecurity APIs"]
)

# =====================================
# HOME
# =====================================

@app.get("/")
def home():

    return {

        "message":

        "Agentic AI Cybersecurity Platform Running",

        "status": "ACTIVE"
    }

# =====================================
# HEALTH CHECK
# =====================================

@app.get("/health")
def health_check():

    return {

        "status": "healthy",

        "api": "running",

        "models": "loaded"
    }

# =====================================
# WEBSOCKET ENDPOINT
# =====================================

@app.websocket("/ws")
async def websocket_endpoint(

    websocket: WebSocket
):

    await websocket_manager.connect(
        websocket
    )

    print(
        "WebSocket connected"
    )

    try:

        while True:

            # Keep websocket alive
            await asyncio.sleep(1)

    except Exception as e:

        print(
            f"WebSocket disconnected: {e}"
        )

        websocket_manager.disconnect(
            websocket
        )

# =====================================
# TEST ALERT API
# =====================================

@app.get("/send-alert")
async def send_alert():

    await websocket_manager.broadcast({

        "type": "SECURITY_ALERT",

        "severity": "HIGH",

        "message": "DDoS Attack Detected"
    })

    return {

        "status": "Alert sent"
    }

# =====================================
# TEST LOW ALERT
# =====================================

@app.get("/send-low-alert")
async def send_low_alert():

    await websocket_manager.broadcast({

        "type": "SECURITY_ALERT",

        "severity": "LOW",

        "message": "Suspicious Login Attempt"
    })

    return {

        "status": "Low alert sent"
    }

# =====================================
# TEST FRAUD ALERT
# =====================================

@app.get("/send-fraud-alert")
async def send_fraud_alert():

    await websocket_manager.broadcast({

        "type": "FRAUD_ALERT",

        "severity": "CRITICAL",

        "message": "Fraudulent Transaction Detected"
    })

    return {

        "status": "Fraud alert sent"
    }