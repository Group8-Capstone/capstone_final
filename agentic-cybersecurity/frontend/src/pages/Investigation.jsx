function Investigation() {

  const investigations = [

    {
      id: 1,
      incident: 'DDoS Attack',
      severity: 'HIGH'
    },

    {
      id: 2,
      incident: 'Fraud Transaction',
      severity: 'CRITICAL'
    }
  ]

  return (

    <div>

      <h1>Investigation Center</h1>

      {

        investigations.map((item) => (

          <div

            key={item.id}

            className="chart-container"
          >

            <h3>
              {item.incident}
            </h3>

            <p>
              Severity:
              {' '}
              {item.severity}
            </p>

          </div>
        ))
      }

    </div>
  )
}

export default Investigation