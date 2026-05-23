import { useState } from 'react'

import API from '../services/api'

function IntrusionDetection() {

  const [result, setResult] = useState(null)

  const detectIntrusion = async () => {

    const response = await API.post(
      '/predict/intrusion'
    )

    setResult(response.data)
  }

  const simulateDDoS = async () => {

    const response = await API.post(
      '/simulate/ddos'
    )

    setResult(response.data)
  }

  const simulatePortScan = async () => {

    const response = await API.post(
      '/simulate/portscan'
    )

    setResult(response.data)
  }

  return (

    <div>

      <h1>Intrusion Detection</h1>

      <button onClick={detectIntrusion}>
        Detect Intrusion
      </button>

      <button onClick={simulateDDoS}>
        Simulate DDoS
      </button>

      <button onClick={simulatePortScan}>
        Simulate Port Scan
      </button>

      {

        result && (

          <div
            className="chart-container"
          >

            <h2>Detection Result</h2>

            <pre>

              {
                JSON.stringify(
                  result,
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

export default IntrusionDetection