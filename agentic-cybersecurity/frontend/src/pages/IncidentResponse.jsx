import { useState, useEffect } from "react";
import API from "../services/api";

function IncidentResponse() {

  const [actions, setActions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [countdown, setCountdown] = useState(15);

  //---------------------------------------------------
  // Load Incident Responses
  //---------------------------------------------------

  const loadResponses = async () => {

    try {

      setLoading(true);

      const response = await API.get(
        "/api/incident-response"
      );

      setActions(response.data || []);

      setCountdown(15);

    }

    catch (error) {

      console.error(
        "Incident Response Error:",
        error
      );

    }

    finally {

      setLoading(false);

    }

  };

  //---------------------------------------------------
  // Auto Refresh
  //---------------------------------------------------

  useEffect(() => {

    loadResponses();

    const refresh = setInterval(() => {

      loadResponses();

    }, 15000);

    return () => clearInterval(refresh);

  }, []);

  //---------------------------------------------------
  // Countdown
  //---------------------------------------------------

  useEffect(() => {

    const timer = setInterval(() => {

      setCountdown(prev => {

        if (prev === 0) return 15;

        return prev - 1;

      });

    }, 1000);

    return () => clearInterval(timer);

  }, []);

  //---------------------------------------------------
  // Statistics
  //---------------------------------------------------

  const total = actions.length;

  const completed = actions.filter(
    a =>
      (a.status || "")
        .toLowerCase()
        .includes("completed")
  ).length;

  const active = actions.filter(
    a =>
      (a.status || "")
        .toLowerCase()
        .includes("progress")
  ).length;

  const pending = actions.filter(
    a =>
      (a.status || "")
        .toLowerCase()
        .includes("pending")
  ).length;

  //---------------------------------------------------
  // Badge Colors
  //---------------------------------------------------

  const statusColor = status => {

    switch ((status || "").toLowerCase()) {

      case "completed":
        return "#166534";

      case "in progress":
        return "#92400e";

      case "pending":
        return "#991b1b";

      default:
        return "#334155";

    }

  };

  const severityColor = severity => {

    switch ((severity || "").toLowerCase()) {

      case "critical":
        return "#dc2626";

      case "high":
        return "#ea580c";

      case "medium":
        return "#ca8a04";

      case "low":
        return "#16a34a";

      default:
        return "#475569";

    }

  };

  //---------------------------------------------------
  // UI
  //---------------------------------------------------

  return (

    <div>

      <h1>Incident Response Dashboard</h1>

      <p>

        Auto Refresh in <b>{countdown}</b> sec

      </p>

      {loading && (

        <div className="chart-container">

          Loading Incident Response...

        </div>

      )}

      {/* Summary */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(4,1fr)",
          gap: "20px",
          marginBottom: "30px"
        }}
      >

        <div className="chart-container">
          <h3>Total Incidents</h3>
          <h1>{total}</h1>
        </div>

        <div className="chart-container">
          <h3>Completed</h3>
          <h1>{completed}</h1>
        </div>

        <div className="chart-container">
          <h3>Active</h3>
          <h1>{active}</h1>
        </div>

        <div className="chart-container">
          <h3>Pending</h3>
          <h1>{pending}</h1>
        </div>

      </div>

      {/* Incident Cards */}

      {actions.map((action, index) => (

        <div

          key={index}

          className="chart-container"

          style={{
            marginBottom: "20px",
            border: "1px solid #334155",
            borderRadius: "12px"
          }}

        >

          <h2>

            {action.title}

          </h2>

          <p>

            {action.description}

          </p>

          <div
            style={{
              display: "flex",
              gap: "15px",
              flexWrap: "wrap",
              marginTop: "15px"
            }}
          >

            <span
              style={{
                background:
                  statusColor(action.status),
                color: "white",
                padding:
                  "6px 12px",
                borderRadius: "20px"
              }}
            >

              {action.status || "Unknown"}

            </span>

            <span
              style={{
                background:
                  severityColor(action.severity),
                color: "white",
                padding:
                  "6px 12px",
                borderRadius: "20px"
              }}
            >

              {action.severity || "N/A"}

            </span>

          </div>

          <br />

          <p>

            <strong>Response Action:</strong>

            {" "}

            {action.action ||
              "Automatic Response"}

          </p>

          <p>

            <strong>Time:</strong>

            {" "}

            {action.timestamp ||
              "Real-Time"}

          </p>

        </div>

      ))}

      {/* History */}

      <div className="chart-container">

        <h2>

          Incident History

        </h2>

        <table
          style={{
            width: "100%",
            borderCollapse:
              "collapse"
          }}
        >

          <thead>

            <tr>

              <th>ID</th>

              <th>Incident</th>

              <th>Status</th>

              <th>Severity</th>

              <th>Action</th>

              <th>Time</th>

            </tr>

          </thead>

          <tbody>

            {actions.map((a, i) => (

              <tr key={i}>

                <td>{i + 1}</td>

                <td>{a.title}</td>

                <td>{a.status}</td>

                <td>{a.severity || "-"}</td>

                <td>{a.action || "-"}</td>

                <td>{a.timestamp || "-"}</td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>

  );

}

export default IncidentResponse;