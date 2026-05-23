import {

  useEffect,
  useState

} from 'react'

import {

  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer

} from 'recharts'

import API from '../services/api'

function UEBA() {

  // =====================================
  // STATES
  // =====================================

  const [users, setUsers] = useState([])

  const [loading, setLoading] = useState(true)

  const [error, setError] = useState(null)

  // =====================================
  // LOAD DATA
  // =====================================

  useEffect(() => {

    loadLANL()

  }, [])

  const loadLANL = async () => {

    try {

      setLoading(true)

      const response = await API.get(
        '/api/lanl-users'
      )

      console.log(
        'LANL DATA:',
        response.data
      )

      if (

        Array.isArray(response.data)
      ) {

        setUsers(response.data)

      } else {

        setError(
          'Invalid API response'
        )
      }

    } catch (err) {

      console.log(err)

      setError(
        'Failed to load LANL dataset'
      )

    } finally {

      setLoading(false)
    }
  }

  // =====================================
  // LOADING
  // =====================================

  if (loading) {

    return (

      <div>

        <h1>
          Loading LANL UEBA Dashboard...
        </h1>

      </div>
    )
  }

  // =====================================
  // ERROR
  // =====================================

  if (error) {

    return (

      <div>

        <h1>
          UEBA Error
        </h1>

        <p>
          {error}
        </p>

      </div>
    )
  }

  return (

    <div>

      {/* ============================== */}
      {/* PAGE TITLE */}
      {/* ============================== */}

      <h1>
        LANL UEBA Dashboard
      </h1>

      {/* ============================== */}
      {/* USER ACTIVITY */}
      {/* ============================== */}

      <div className="chart-container">

        <h2>
          User Activity Count
        </h2>

        <ResponsiveContainer
          width="100%"
          height={350}
        >

          <BarChart data={users}>

            <XAxis
              dataKey="user"
            />

            <YAxis />

            <Tooltip />

            <Bar

              dataKey="count"

              fill="#00ffcc"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

      {/* ============================== */}
      {/* RISK SCORES */}
      {/* ============================== */}

      <div className="chart-container">

        <h2>
          Risk Scores
        </h2>

        <ResponsiveContainer
          width="100%"
          height={350}
        >

          <BarChart data={users}>

            <XAxis
              dataKey="user"
            />

            <YAxis />

            <Tooltip />

            <Bar

              dataKey="risk"

              fill="#ff4d4d"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

      {/* ============================== */}
      {/* INVESTIGATION TABLE */}
      {/* ============================== */}

      <div className="chart-container">

        <h2>
          Investigation Table
        </h2>

        <table className="ueba-table">

          <thead>

            <tr>

              <th>User</th>

              <th>Count</th>

              <th>Systems</th>

              <th>Risk</th>

              <th>Reason</th>

              <th>Action</th>

            </tr>

          </thead>

          <tbody>

            {

              users.map((u, i) => (

                <tr

                  key={i}

                  className={

                    u.risk > 1.2

                      ? 'critical-row'

                      : u.risk > 0.9

                      ? 'warning-row'

                      : ''
                  }
                >

                  <td>

                    {u.user}

                  </td>

                  <td>

                    {
                      u.count.toLocaleString()
                    }

                  </td>

                  <td>

                    {u.systems}

                  </td>

                  <td>

                    {
                      u.risk.toFixed(2)
                    }

                  </td>

                  <td>

                    {u.reason}

                  </td>

                  <td>

                    {u.action}

                  </td>

                </tr>
              ))
            }

          </tbody>

        </table>

      </div>

    </div>
  )
}

export default UEBA