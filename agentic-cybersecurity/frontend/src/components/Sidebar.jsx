import { Link } from 'react-router-dom'

function Sidebar() {

  return (
    <div className="sidebar">

      <h2>Menu</h2>

      <Link to="/">Dashboard</Link>

      <Link to="/streaming">Streaming</Link>

      <Link to="/intrusion">Intrusion Detection</Link>

      <Link to="/fraud">Fraud Detection</Link>

      <Link to="/investigation">Investigation</Link>

      <Link to="/response">Incident Response</Link>

      <Link to="/explainability">Explainability</Link>

      <Link to="/ueba">UEBA</Link>

    </div>
  )
}

export default Sidebar