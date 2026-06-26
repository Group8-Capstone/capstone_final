import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  BarChart,
  Bar,
} from "recharts";

import MetricCard from "../components/MetricCard";
import API from "../services/api";

const COLORS = ["#ff4d4d", "#ffcc00", "#00ccff", "#66cc66", "#9966ff"];

const defaultMetrics = {
  total_threats: 0,
  blocked_attacks: 0,
  fraud_alerts: 0,
  ueba_alerts: 0,
  system_health: "Unknown",
};

function Dashboard() {
  const [metrics, setMetrics] = useState(defaultMetrics);

  const [trafficData, setTrafficData] = useState([]);

  const [attackData, setAttackData] = useState([]);

  const [modelData, setModelData] = useState([]);

  const [autoencoder, setAutoencoder] = useState({});

  const [lanl, setLanl] = useState({});

  const [loading, setLoading] = useState(true);

  const loadDashboard = async () => {
    try {
      const { data } = await API.get("/api/dashboard");

      setMetrics(data?.metrics ?? defaultMetrics);

      setTrafficData(data?.traffic ?? []);

      setAttackData(data?.attack_distribution ?? []);

      setModelData(data?.model_accuracy ?? []);

      setAutoencoder(data?.autoencoder ?? {});

      setLanl(data?.lanl ?? {});
    } catch (err) {
      console.error("Dashboard API Error:", err);

      setMetrics(defaultMetrics);

      setTrafficData([]);

      setAttackData([]);

      setModelData([]);

      setAutoencoder({});

      setLanl({});
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDashboard();

    const timer = setInterval(loadDashboard, 5000);

    return () => clearInterval(timer);
  }, []);

  if (loading) return <h2>Loading dashboard...</h2>;

  return (
    <div>
      <h1>Agentic AI Cybersecurity Dashboard</h1>

      {/* ===========================
            TOP METRICS
      =========================== */}

      <div className="metric-grid">
        <MetricCard title="Threats" value={metrics?.total_threats ?? 0} />

        <MetricCard
          title="Blocked Attacks"
          value={metrics?.blocked_attacks ?? 0}
        />

        <MetricCard title="Fraud Alerts" value={metrics?.fraud_alerts ?? 0} />

        <MetricCard title="UEBA Alerts" value={metrics?.ueba_alerts ?? 0} />
      </div>

      {/* ===========================
            NETWORK TRAFFIC
      =========================== */}

      <div className="chart-container">
        <h2>Network Traffic</h2>

        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={trafficData}>
            <XAxis dataKey="time" />

            <YAxis />

            <Tooltip />

            <Line type="monotone" dataKey="traffic" stroke="#00ffcc" />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* ===========================
            ATTACK DISTRIBUTION
      =========================== */}

      <div className="chart-container">
        <h2>Attack Distribution</h2>

        <ResponsiveContainer width="100%" height={320}>
          <PieChart>
            <Pie
              data={attackData}
              dataKey="value"
              nameKey="name"
              outerRadius={110}
              label
            >
              {attackData.map((entry, index) => (
                <Cell key={index} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* ===========================
            MODEL ACCURACY
      =========================== */}

      <div className="chart-container">
        <h2>Model Accuracy</h2>

        <ResponsiveContainer width="100%" height={320}>
          <BarChart data={modelData}>
            <XAxis dataKey="model" />

            <YAxis domain={[0, 100]} />

            <Tooltip />

            <Bar dataKey="accuracy" fill="#00ff99" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* ===========================
            AUTOENCODER
      =========================== */}

      <div className="chart-container">
        <h2>Autoencoder Performance</h2>

        <div className="metric-grid">
          <MetricCard
            title="Avg Error"
            value={autoencoder?.average_error ?? 0}
          />

          <MetricCard
            title="Max Error"
            value={autoencoder?.maximum_error ?? 0}
          />

          <MetricCard title="Threshold" value={autoencoder?.threshold ?? 0} />

          <MetricCard
            title="Anomalies"
            value={autoencoder?.anomalies_detected ?? 0}
          />

          <MetricCard
            title="Normal Records"
            value={autoencoder?.normal_records ?? 0}
          />

          <MetricCard
            title="Anomaly %"
            value={`${autoencoder?.anomaly_percentage ?? 0}%`}
          />
        </div>
      </div>

      {/* ===========================
            LANL
      =========================== */}

      <div className="chart-container">
        <h2>LANL UEBA Performance</h2>

        <div className="metric-grid">
          <MetricCard title="Algorithm" value={lanl?.algorithm ?? "-"} />

          <MetricCard title="Records" value={lanl?.total_records ?? 0} />

          <MetricCard title="Anomalies" value={lanl?.anomalies_detected ?? 0} />

          <MetricCard
            title="Normal Records"
            value={lanl?.normal_records ?? 0}
          />

          <MetricCard title="Users" value={lanl?.unique_users ?? 0} />

          <MetricCard title="Computers" value={lanl?.unique_computers ?? 0} />

          <MetricCard
            title="Anomaly %"
            value={`${lanl?.anomaly_percentage ?? 0}%`}
          />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;