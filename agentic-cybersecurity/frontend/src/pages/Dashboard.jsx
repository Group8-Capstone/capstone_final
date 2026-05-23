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
  Bar
} from 'recharts'

import MetricCard from '../components/MetricCard'

function Dashboard() {

  const trafficData = [
    { time: '1', traffic: 120 },
    { time: '2', traffic: 210 },
    { time: '3', traffic: 180 },
    { time: '4', traffic: 320 },
    { time: '5', traffic: 280 }
  ]

  const attackData = [
    { name: 'DDoS', value: 45 },
    { name: 'Port Scan', value: 25 },
    { name: 'Brute Force', value: 30 }
  ]

  const modelData = [
    { model: 'CNN-LSTM', accuracy: 91 },
    { model: 'Transformer', accuracy: 93 },
    { model: 'Ensemble', accuracy: 96 }
  ]

  return (
    <div>

      <h1>Agentic AI Cybersecurity Dashboard</h1>

      <div className="metric-grid">

        <MetricCard title="Threats" value="124" />

        <MetricCard title="Fraud Alerts" value="18" />

        <MetricCard title="UEBA Alerts" value="9" />

        <MetricCard title="Blocked Attacks" value="98" />

      </div>

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

      <div className="chart-container">

        <h2>Attack Distribution</h2>

        <ResponsiveContainer width="100%" height={300}>

          <PieChart>

            <Pie
              data={attackData}
              dataKey="value"
              outerRadius={100}
              fill="#8884d8"
              label
            >
              <Cell fill="#ff4d4d" />
              <Cell fill="#ffcc00" />
              <Cell fill="#00ccff" />
            </Pie>

            <Tooltip />

          </PieChart>

        </ResponsiveContainer>

      </div>

      <div className="chart-container">

        <h2>Model Accuracy</h2>

        <ResponsiveContainer width="100%" height={300}>

          <BarChart data={modelData}>

            <XAxis dataKey="model" />

            <YAxis />

            <Tooltip />

            <Bar dataKey="accuracy" fill="#00ff99" />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  )
}

export default Dashboard