import { NavLink } from "react-router-dom";

import {
  FiHome,
  FiActivity,
  FiShield,
  FiCreditCard,
  FiSearch,
  FiAlertTriangle,
  FiCpu,
  FiUsers
} from "react-icons/fi";

function Sidebar() {

  return (

    <div className="sidebar">

      <div className="sidebar-header">

        <h2>🛡 Agentic AI</h2>

        <p>Cybersecurity SOC</p>

      </div>

      <nav>

        <NavLink to="/" end>

          <FiHome />

          <span>Dashboard</span>

        </NavLink>

        <NavLink to="/streaming">

          <FiActivity />

          <span>Streaming</span>

        </NavLink>

        <NavLink to="/intrusion">

          <FiShield />

          <span>Intrusion Detection</span>

        </NavLink>

        <NavLink to="/fraud">

          <FiCreditCard />

          <span>Fraud Detection</span>

        </NavLink>

        <NavLink to="/investigation">

          <FiSearch />

          <span>Investigation</span>

        </NavLink>

        <NavLink to="/response">

          <FiAlertTriangle />

          <span>Incident Response</span>

        </NavLink>

        <NavLink to="/explainability">

          <FiCpu />

          <span>Explainability</span>

        </NavLink>

        <NavLink to="/ueba">

          <FiUsers />

          <span>UEBA</span>

        </NavLink>

      </nav>

    </div>

  );

}

export default Sidebar;