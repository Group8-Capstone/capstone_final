import { useEffect, useState } from "react";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  Legend,
} from "recharts";

import API from "../services/api";

function UEBA() {
  // =====================================
  // STATES
  // =====================================

  const [users, setUsers] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  // =====================================
  // LOAD DATA
  // =====================================

  useEffect(() => {
    loadLANL();
  }, []);

  const loadLANL = async () => {
    try {
      setLoading(true);

      const response = await API.get("/api/lanl-users");

      console.log("LANL DATA:", response.data);

      console.table(response.data);

      if (Array.isArray(response.data)) {
        const cleaned = response.data.map((item) => ({
          user: item.user ?? "Unknown",

          count: Number(item.count ?? 0),

          systems: Number(item.systems ?? 0),

          risk: Number(item.risk ?? 0),

          reason: item.reason ?? "Normal",

          action: item.action ?? "Allow",
        }));

        setUsers(cleaned);

        setError("");
      } else {
        setError("Invalid API response");
      }
    } catch (err) {
      console.error(err);

      setError("Failed to load LANL Dataset");
    } finally {
      setLoading(false);
    }
  };

  // =====================================
  // SUMMARY
  // =====================================

  const totalUsers = users.length;

  const criticalUsers = users.filter((u) => u.risk > 1.2).length;

  const warningUsers = users.filter(
    (u) => u.risk > 0.9 && u.risk <= 1.2
  ).length;

  const normalUsers = users.filter((u) => u.risk <= 0.9).length;

  // =====================================
  // LOADING
  // =====================================

  if (loading) {
    return (
      <div>
        <h2>Loading UEBA Dashboard...</h2>
      </div>
    );
  }

  // =====================================
  // ERROR
  // =====================================

  if (error) {
    return (
      <div>
        <h2>UEBA Error</h2>

        <p>{error}</p>
      </div>
    );
  }

  // =====================================
  // UI
  // =====================================

  return (
    <div>
      <h1>LANL UEBA Dashboard</h1>

      {/* ================================= */}
      {/* SUMMARY CARDS */}
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
          <h3>Total Users</h3>

          <h1>{totalUsers}</h1>
        </div>

        <div className="metric-card">
          <h3>Critical</h3>

          <h1>{criticalUsers}</h1>
        </div>

        <div className="metric-card">
          <h3>Warning</h3>

          <h1>{warningUsers}</h1>
        </div>

        <div className="metric-card">
          <h3>Normal</h3>

          <h1>{normalUsers}</h1>
        </div>
      </div>

      {/* ================================= */}
      {/* USER ACTIVITY */}
      {/* ================================= */}

      <div className="chart-container">
        <h2>User Activity</h2>

        <ResponsiveContainer width="100%" height={350}>
          <BarChart data={users}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="user" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Bar dataKey="count" fill="#00ffcc" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* ================================= */}
      {/* RISK */}
      {/* ================================= */}

      <div className="chart-container">
        <h2>User Risk Score</h2>

        <ResponsiveContainer width="100%" height={350}>
          <BarChart data={users}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="user" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Bar dataKey="risk" fill="#ff4d4d" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* ================================= */}
      {/* TABLE */}
      {/* ================================= */}

      <div className="chart-container">
        <h2>User Investigation Report</h2>

        <table className="ueba-table">
          <thead>
            <tr>
              <th>User</th>

              <th>Activity Count</th>

              <th>Systems</th>

              <th>Risk</th>

              <th>Reason</th>

              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            {users.map((u, index) => (
              <tr
                key={u.user || index}
                className={
                  u.risk > 1.2
                    ? "critical-row"
                    : u.risk > 0.9
                    ? "warning-row"
                    : ""
                }
              >
                <td>{u.user}</td>

                <td>{(u.count ?? 0).toLocaleString()}</td>

                <td>{u.systems ?? 0}</td>

                <td>{Number(u.risk ?? 0).toFixed(2)}</td>

                <td>{u.reason}</td>

                <td>
                  <strong>{u.action}</strong>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default UEBA;