import {

  useState,
  useEffect

} from 'react'

import API from '../services/api'

function IntrusionDetection() {

  const [result, setResult] = useState(
    null
  )

  const [loading, setLoading] = useState(
    false
  )

  // =====================================
  // INTRUSION DETECTION
  // =====================================

  const detectIntrusion = async () => {

    try {

      setLoading(true)

      const response = await API.post(
        '/predict/intrusion'
      )

      setResult(
        response.data
      )

    }

    catch (error) {

      console.error(
        'Intrusion Detection Error:',
        error
      )

    }

    finally {

      setLoading(false)
    }
  }

  // =====================================
  // DDoS SIMULATION
  // =====================================

  const simulateDDoS = async () => {

    try {

      setLoading(true)

      const response = await API.post(
        '/simulate/ddos'
      )

      setResult(
        response.data
      )

    }

    catch (error) {

      console.error(
        'DDoS Simulation Error:',
        error
      )

    }

    finally {

      setLoading(false)
    }
  }

  // =====================================
  // PORT SCAN SIMULATION
  // =====================================

  const simulatePortScan = async () => {

    try {

      setLoading(true)

      const response = await API.post(
        '/simulate/portscan'
      )

      setResult(
        response.data
      )

    }

    catch (error) {

      console.error(
        'Port Scan Error:',
        error
      )

    }

    finally {

      setLoading(false)
    }
  }

  // =====================================
  // AUTO DETECTION
  // =====================================

  useEffect(() => {

    detectIntrusion()

    const interval = setInterval(() => {

      detectIntrusion()

    }, 15000)

    return () => clearInterval(
      interval
    )

  }, [])

  return (

    <div>

      <h1>

        Intrusion Detection

      </h1>

      {/* ========================= */}
      {/* BUTTONS */}
      {/* ========================= */}

      <div
        style={{
          marginBottom: '20px'
        }}
      >

        <button
          onClick={detectIntrusion}
        >

          Detect Intrusion

        </button>

        <button
          onClick={simulateDDoS}
          style={{
            marginLeft: '10px'
          }}
        >

          Simulate DDoS

        </button>

        <button
          onClick={simulatePortScan}
          style={{
            marginLeft: '10px'
          }}
        >

          Simulate Port Scan

        </button>

      </div>

      {/* ========================= */}
      {/* LOADING */}
      {/* ========================= */}

      {

        loading && (

          <div
            className="chart-container"
          >

            <h3>

              Running Detection...

            </h3>

          </div>
        )
      }

      {/* ========================= */}
      {/* RESULT */}
      {/* ========================= */}

      {

        result && (

          <div
            className="chart-container"
          >

            <h2>

              Detection Result

            </h2>

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