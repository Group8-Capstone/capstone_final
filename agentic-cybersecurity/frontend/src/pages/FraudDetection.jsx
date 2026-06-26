import { useState, useEffect } from "react";
import API from "../services/api";

function FraudDetection() {
  const [fraud, setFraud] = useState(null);
  const [loading, setLoading] = useState(false);
  const [countdown, setCountdown] = useState(15);
  const [history, setHistory] = useState([]);

  //----------------------------------------------------
  // Detect Fraud
  //----------------------------------------------------

  const detectFraud = async () => {
    try {
      setLoading(true);

      const response = await API.post("/predict/fraud");

      const result = response.data;

      setFraud(result);

      setHistory((prev) => [
        {
          time: new Date().toLocaleTimeString(),
          status: result.prediction || result.status || "Unknown",

          confidence: result.confidence || 0,
        },

        ...prev.slice(0, 9),
      ]);

      setCountdown(15);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  //----------------------------------------------------
  // Auto Refresh
  //----------------------------------------------------

  useEffect(() => {
    detectFraud();

    const interval = setInterval(() => {
      detectFraud();
    }, 15000);

    return () => clearInterval(interval);
  }, []);

  //----------------------------------------------------
  // Countdown
  //----------------------------------------------------

  useEffect(() => {
    const timer = setInterval(() => {
      setCountdown((prev) => {
        if (prev === 0) return 15;

        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  //----------------------------------------------------
  // Helpers
  //----------------------------------------------------

  const confidence = Math.round((fraud?.confidence || 0) * 100);

  const prediction = fraud?.prediction || fraud?.status || "Unknown";

  const risk =
    fraud?.risk ||
    fraud?.severity ||
    (confidence > 90 ? "HIGH" : confidence > 60 ? "MEDIUM" : "LOW");

  const cardColor = prediction.toLowerCase().includes("fraud")
    ? "#7f1d1d"
    : "#14532d";

  //----------------------------------------------------
  // UI
  //----------------------------------------------------

  return (
    <div>
      <h1>Fraud Detection Dashboard</h1>

      <button onClick={detectFraud}>Run Detection</button>

      <p>
        Next automatic detection in
        <b> {countdown} sec</b>
      </p>

      {loading && (
        <div className="chart-container">Running Fraud Detection...</div>
      )}

      {fraud && (
        <>
          <div
            className="chart-container"
            style={{
              background: cardColor,
              color: "white",
            }}
          >
            <h2>{prediction}</h2>

            <h3>Confidence</h3>

            <div
              style={{
                width: "100%",
                background: "#444",
                height: "20px",
                borderRadius: "15px",
                overflow: "hidden",
              }}
            >
              <div
                style={{
                  width: `${confidence}%`,
                  height: "20px",
                  background: "#00ff99",
                }}
              ></div>
            </div>

            <p>
              <b>{confidence}%</b>
            </p>

            <hr />

            <p>
              <b>Risk Level :</b>

              {risk}
            </p>

            <p>
              <b>Model :</b>
              XGBoost Fraud Detection
            </p>
          </div>

          <div
            className="metric-grid"
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(4,1fr)",
              gap: "20px",
            }}
          >
            <div className="chart-container">
              <h3>Prediction</h3>

              <h2>{prediction}</h2>
            </div>

            <div className="chart-container">
              <h3>Confidence</h3>

              <h2>{confidence}%</h2>
            </div>

            <div className="chart-container">
              <h3>Risk</h3>

              <h2>{risk}</h2>
            </div>

            <div className="chart-container">
              <h3>Dataset</h3>

              <h2>Credit Card</h2>
            </div>
          </div>

          <div className="chart-container">
            <h2>Detection History</h2>

            <table
              style={{
                width: "100%",
                borderCollapse: "collapse",
              }}
            >
              <thead>
                <tr>
                  <th>Time</th>

                  <th>Status</th>

                  <th>Confidence</th>
                </tr>
              </thead>

              <tbody>
                {history.map((item, index) => (
                  <tr key={index}>
                    <td>{item.time}</td>

                    <td>{item.status}</td>

                    <td>{Math.round(item.confidence * 100)}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  );
}

export default FraudDetection;