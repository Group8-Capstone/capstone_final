import asyncio

from api.routes import (
    simulate_ddos,
    simulate_portscan,
    simulate_malware,
    predict_fraud,
    predict_ueba
)

async def start_monitoring():

    print("=" * 60)
    print("AUTOMATIC MONITORING ENGINE STARTED")
    print("=" * 60)

    while True:

        try:

            await simulate_ddos()

            await asyncio.sleep(5)

            await simulate_portscan()

            await asyncio.sleep(5)

            await simulate_malware()

            await asyncio.sleep(5)

            await predict_fraud()

            await asyncio.sleep(5)

            await predict_ueba()

            print(
                "Monitoring cycle completed"
            )

        except Exception as e:

            print(
                f"Monitoring error: {e}"
            )

        await asyncio.sleep(20)