import { useEffect, useState } from "react";

import API from "../services/api";

function Investigation() {
  // =====================================
  // STATE
  // =====================================

  const [investigations, setInvestigations] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [lastUpdated, setLastUpdated] = useState("");

  // =====================================
  // LOAD INVESTIGATIONS
  // =====================================

  const loadInvestigations = async () => {
    try {
      setLoading(true);

      const response = await API.get("/api/investigations");

      if (Array.isArray(response.data)) {
        setInvestigations(response.data);

        setLastUpdated(new Date().toLocaleTimeString());

        setError("");
      } else {
        setError("Invalid API response");
      }
    } catch (err) {
      console.error(err);

      setError("Unable to load investigation history.");
    } finally {
      setLoading(false);
    }
  };

  // =====================================
  // AUTO REFRESH
  // =====================================

  useEffect(() => {
    loadInvestigations();

    const interval = setInterval(() => {
      loadInvestigations();
    }, 15000);

    return () => clearInterval(interval);
  }, []);

  // =====================================
  // LOADING
  // =====================================

  if (loading) {
    return (
      <div>
        <h2>Loading Investigation Center...</h2>
      </div>
    );
  }

  // =====================================
  // ERROR
  // =====================================

  if (error) {
    return (
      <div>
        <h2>Investigation Error</h2>

        <p>{error}</p>
      </div>
    );
  }

  // =====================================
  // SUMMARY
  // =====================================

  const critical = investigations.filter(
    (i) => i.threat_level === "CRITICAL"
  ).length;

  const high = investigations.filter((i) => i.threat_level === "HIGH").length;

  const medium = investigations.filter(
    (i) => i.threat_level === "MEDIUM"
  ).length;

  const low = investigations.filter((i) => i.threat_level === "LOW").length;

  // =====================================
  // UI
  // =====================================

  return (
    <div>
      <h1>Investigation Center</h1>

      <p>
        Last Updated :<strong> {lastUpdated}</strong>
      </p>

      {/* ================================= */}

      {/* SUMMARY */}

      {/* ================================= */}

      <div
        className="metric-grid"
        style={{
          display: "grid",

          gridTemplateColumns: "repeat(4,1fr)",

          gap: "20px",

          marginBottom: "30px",
        }}
      >
        <div className="metric-card">
          <h3>Critical</h3>

          <h1>{critical}</h1>
        </div>

        <div className="metric-card">
          <h3>High</h3>

          <h1>{high}</h1>
        </div>

        <div className="metric-card">
          <h3>Medium</h3>

          <h1>{medium}</h1>
        </div>

        <div className="metric-card">
          <h3>Low</h3>

          <h1>{low}</h1>
        </div>
      </div>

      {/* ================================= */}

      {/* TABLE */}

      {/* ================================= */}

      <div className="chart-container">
        <h2>Investigation History</h2>

        <table className="ueba-table">
          <thead>
            <tr>
              <th>Time</th>

              <th>Attack</th>

              <th>Threat</th>

              <th>Confidence</th>

              <th>Details</th>
            </tr>
          </thead>

          <tbody>
            {investigations.length === 0 ? (
              <tr>
                <td
                  colSpan="5"
                  style={{
                    textAlign: "center",
                  }}
                >
                  No investigations available
                </td>
              </tr>
            ) : (
              investigations.map((item, index) => (
                <tr
                  key={index}
                  className={
                    item.threat_level === "CRITICAL"
                      ? "critical-row"
                      : item.threat_level === "HIGH"
                      ? "warning-row"
                      : ""
                  }
                >
                  <td>{item.timestamp}</td>

                  <td>{item.attack_type}</td>

                  <td>{item.threat_level}</td>

                  <td>{Number(item.confidence_score ?? 0).toFixed(2)}</td>

                  <td>{item.details}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Investigation;