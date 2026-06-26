import {
  FiTrendingUp,
  FiShield,
  FiAlertTriangle,
  FiUsers
} from "react-icons/fi";

function MetricCard({ title, value }) {

  const getIcon = () => {

    switch (title) {

      case "Threats":
        return <FiAlertTriangle />;

      case "Blocked Attacks":
        return <FiShield />;

      case "Fraud Alerts":
        return <FiTrendingUp />;

      case "UEBA Alerts":
        return <FiUsers />;

      default:
        return null;

    }

  };

  const icon = getIcon();

  return (

    <div className="metric-card">

      <div className="metric-header">

        <div>

          <h3>{title}</h3>

          <h1>{value}</h1>

        </div>

        {icon}

      </div>

    </div>

  );

}

export default MetricCard;