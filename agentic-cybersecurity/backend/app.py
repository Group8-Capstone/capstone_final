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

from services.monitoring_engine import (
    start_monitoring
)

from streaming.websocket_manager import (
    websocket_manager
)

from utils.logger import (
    log_message
)

from utils.create_output_folders import (
    create_output_folders
)

# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(

    title="Agentic AI Cybersecurity",

    description="AI-powered Cybersecurity Monitoring Platform",

    version="1.0.0"

)

# =====================================================
# CORS
# =====================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# =====================================================
# STATIC FILES
# =====================================================

app.mount(

    "/outputs",

    StaticFiles(directory="outputs"),

    name="outputs"

)

app.mount(

    "/dashboard",

    StaticFiles(directory="dashboard"),

    name="dashboard"

)

# =====================================================
# STARTUP
# =====================================================

@app.on_event("startup")
async def startup_event():

    print("=" * 70)
    print("STARTING CYBERSECURITY PLATFORM")
    print("=" * 70)

    create_output_folders()

    try:

        initialize_models()

        print("Models initialized successfully")

        log_message(
            "Models initialized successfully"
        )

    except Exception as e:

        print(f"Model initialization failed: {e}")

        log_message(
            f"Model initialization failed: {e}"
        )

    asyncio.create_task(
        start_monitoring()
    )

    print("Automatic Monitoring Started")

# =====================================================
# ROUTES
# =====================================================

app.include_router(router)

# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():

    return {

        "message":

        "Agentic AI Cybersecurity Platform Running",

        "status":

        "ACTIVE"

    }

# =====================================================
# HEALTH
# =====================================================

@app.get("/health")
def health():

    return {

        "status":

        "healthy"

    }

# =====================================================
# WEBSOCKET
# =====================================================

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket_manager.connect(websocket)

    try:

        while True:

            await asyncio.sleep(1)

    except Exception:

        websocket_manager.disconnect(websocket)

# =====================================================
# TEST ALERT
# =====================================================

@app.get("/send-alert")
async def send_alert():

    await websocket_manager.broadcast({

        "type": "SECURITY_ALERT",

        "severity": "HIGH",

        "message": "DDoS Attack Detected"

    })

    return {

        "status": "Alert Sent"

    }

# =====================================================
# TEST FRAUD
# =====================================================

@app.get("/send-fraud-alert")
async def send_fraud():

    await websocket_manager.broadcast({

        "type": "FRAUD_ALERT",

        "severity": "CRITICAL",

        "message": "Fraud Detected"

    })

    return {

        "status": "Fraud Alert Sent"

    }