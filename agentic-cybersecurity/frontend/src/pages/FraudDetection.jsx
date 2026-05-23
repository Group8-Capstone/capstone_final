import { useState } from 'react'

import API from '../services/api'

function FraudDetection() {

  const [fraud, setFraud] = useState(null)

  const detectFraud = async () => {

    const response = await API.post(
      '/predict/fraud'
    )

    setFraud(response.data)
  }

  return (

    <div>

      <h1>Fraud Detection</h1>

      <button onClick={detectFraud}>
        Detect Fraud
      </button>

      {

        fraud && (

          <div
            className="chart-container"
          >

            <h2>Fraud Result</h2>

            <pre>

              {
                JSON.stringify(
                  fraud,
                  null,
                  2
                )
              }

            </pre>

          </div>
        )
      }

    </div>
  )
}

export default FraudDetection