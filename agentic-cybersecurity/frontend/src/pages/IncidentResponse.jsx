function IncidentResponse() {

  const actions = [

    'Blocked IP Address',

    'Generated Alert',

    'Escalated Incident',

    'Isolated Endpoint'
  ]

  return (

    <div>

      <h1>Incident Response</h1>

      {

        actions.map((action, index) => (

          <div

            key={index}

            className="chart-container"
          >

            {action}

          </div>
        ))
      }

    </div>
  )
}

export default IncidentResponse