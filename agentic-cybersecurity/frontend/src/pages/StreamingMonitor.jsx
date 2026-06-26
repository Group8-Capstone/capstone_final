import { useEffect, useState } from "react";

function StreamingMonitor() {

  const [alerts, setAlerts] = useState([]);

  const [connectionStatus, setConnectionStatus] = useState("Connecting...");

  const WS_URL =
    import.meta.env.VITE_WS_URL ||
    `ws://${window.location.hostname}:8000/ws`;

  useEffect(() => {

    let socket;

    const connect = () => {

      socket = new WebSocket(WS_URL);

      socket.onopen = () => {

        console.log("WebSocket Connected");

        setConnectionStatus("Connected");

        socket.send(
          JSON.stringify({
            type: "CLIENT_CONNECTED"
          })
        );

      };

      socket.onmessage = (event) => {

        try {

          const data = JSON.parse(event.data);

          setAlerts(prev => [

            {

              ...data,

              timestamp: new Date().toLocaleTimeString()

            },

            ...prev.slice(0, 19)

          ]);

        }

        catch (err) {

          console.error(err);

        }

      };

      socket.onerror = (err) => {

        console.error(err);

        setConnectionStatus("Connection Error");

      };

      socket.onclose = () => {

        console.log("Socket Closed");

        setConnectionStatus("Disconnected");

        setTimeout(connect, 3000);

      };

    };

    connect();

    return () => {

      if (socket) {

        socket.onclose = null;

        socket.close();

      }

    };

  }, [WS_URL]);

  const getAlertColor = (type) => {

    switch (type) {

      case "SECURITY_ALERT":
        return "#991b1b";

      case "FRAUD_ALERT":
        return "#92400e";

      case "UEBA_ALERT":
        return "#1e40af";

      case "ANOMALY_ALERT":
        return "#7c3aed";

      case "PORTSCAN_ALERT":
        return "#0f766e";

      case "MALWARE_ALERT":
        return "#7f1d1d";

      default:
        return "#1e293b";

    }

  };

  const getAlertIcon = (type) => {

    switch (type) {

      case "SECURITY_ALERT":
        return "🚨";

      case "FRAUD_ALERT":
        return "💳";

      case "UEBA_ALERT":
        return "👤";

      case "ANOMALY_ALERT":
        return "⚠️";

      case "PORTSCAN_ALERT":
        return "🌐";

      case "MALWARE_ALERT":
        return "🦠";

      default:
        return "📢";

    }

  };

  return (

    <div>

      <h1>Real-Time Security Alerts</h1>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 20
        }}
      >

        <div
          style={{
            padding: "12px",
            borderRadius: "8px",
            background:
              connectionStatus === "Connected"
                ? "#14532d"
                : "#7f1d1d",
            color: "white",
            fontWeight: "bold"
          }}
        >
          WebSocket : {connectionStatus}
        </div>

        <button

          onClick={() => setAlerts([])}

          style={{
            padding: "10px 18px",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer"
          }}

        >
          Clear Alerts
        </button>

      </div>

      <h2>

        Security Alerts ({alerts.length})

      </h2>

      {

        alerts.length === 0 &&

        (

          <div

            style={{

              padding: 20,

              background: "#111827",

              borderRadius: 10,

              border: "1px solid #334155"

            }}

          >

            Waiting for security alerts...

          </div>

        )

      }

      {

        alerts.map((alert, index) => (

          <div

            key={index}

            style={{

              background: getAlertColor(alert.type),

              padding: 20,

              marginBottom: 20,

              borderRadius: 10,

              border: "1px solid #00ffcc"

            }}

          >

            <h3>

              {getAlertIcon(alert.type)}{" "}

              {alert.type || "UNKNOWN"}

            </h3>

            <p>

              {alert.message || "No message"}

            </p>

            {

              alert.attack_type &&

              (

                <p>

                  <strong>Attack :</strong>{" "}

                  {alert.attack_type}

                </p>

              )

            }

            {

              alert.severity &&

              (

                <p>

                  <strong>Severity :</strong>{" "}

                  {alert.severity}

                </p>

              )

            }

            {

              alert.score !== undefined &&

              (

                <p>

                  <strong>Confidence :</strong>{" "}

                  {(alert.score * 100).toFixed(2)}%

                </p>

              )

            }

            {

              alert.records_analyzed &&

              (

                <p>

                  <strong>Records :</strong>{" "}

                  {alert.records_analyzed}

                </p>

              )

            }

            {

              alert.source_ip &&

              (

                <p>

                  <strong>Source IP :</strong>{" "}

                  {alert.source_ip}

                </p>

              )

            }

            {

              alert.destination_ip &&

              (

                <p>

                  <strong>Destination IP :</strong>{" "}

                  {alert.destination_ip}

                </p>

              )

            }

            <small>

              {alert.timestamp}

            </small>

          </div>

        ))

      }

    </div>

  );

}

export default StreamingMonitor;