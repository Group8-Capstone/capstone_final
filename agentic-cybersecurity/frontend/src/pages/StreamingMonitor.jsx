import { useEffect, useState } from 'react'

function StreamingMonitor() {

  const [alerts, setAlerts] = useState([])

  const [connectionStatus, setConnectionStatus] =
    useState('Connecting...')

  useEffect(() => {

    const socket = new WebSocket(
      'ws://127.0.0.1:8000/ws'
    )

    // =====================================
    // CONNECTION OPEN
    // =====================================

    socket.onopen = () => {

      console.log(
        'WebSocket Connected'
      )

      setConnectionStatus(
        'Connected'
      )
    }

    // =====================================
    // RECEIVE ALERTS
    // =====================================

    socket.onmessage = (event) => {

      console.log(
        'Received:',
        event.data
      )

      const data = JSON.parse(
        event.data
      )

      setAlerts((prevAlerts) => [

        data,

        ...prevAlerts
      ])
    }

    // =====================================
    // ERROR
    // =====================================

    socket.onerror = (error) => {

      console.log(
        'WebSocket Error:',
        error
      )

      setConnectionStatus(
        'Connection Error'
      )
    }

    // =====================================
    // CLOSE
    // =====================================

    socket.onclose = () => {

      console.log(
        'WebSocket Closed'
      )

      setConnectionStatus(
        'Disconnected'
      )
    }

    // =====================================
    // CLEANUP
    // =====================================

    return () => {

      socket.close()
    }

  }, [])

  return (

    <div>

      <h1>
        Real-Time Security Alerts
      </h1>

      {/* ============================== */}
      {/* CONNECTION STATUS */}
      {/* ============================== */}

      <div

        style={{

          marginBottom: '20px',

          padding: '10px',

          background: '#1e293b',

          borderRadius: '8px',

          border: '1px solid #00ffcc'
        }}
      >

        <strong>
          WebSocket Status:
        </strong>

        {' '}

        {connectionStatus}

      </div>

      {/* ============================== */}
      {/* NO ALERTS */}
      {/* ============================== */}

      {

        alerts.length === 0 ? (

          <div

            style={{

              padding: '20px',

              background: '#111827',

              borderRadius: '10px',

              border:
                '1px solid #334155'
            }}
          >

            Waiting for security alerts...

          </div>

        ) : (

          alerts.map((alert, index) => (

            <div

              key={index}

              className="alert-box"

              style={{

                background:

                  alert.severity === 'CRITICAL'

                    ? '#7f1d1d'

                    : alert.severity === 'HIGH'

                    ? '#991b1b'

                    : '#1e293b',

                padding: '15px',

                marginBottom: '15px',

                borderRadius: '10px',

                border:
                  '1px solid #00ffcc'
              }}
            >

              <h3>

                {alert.type}

              </h3>

              <p>

                {alert.message}

              </p>

              <strong>

                Severity:

              </strong>

              {' '}

              {alert.severity}

            </div>
          ))
        )
      }

    </div>
  )
}

export default StreamingMonitor