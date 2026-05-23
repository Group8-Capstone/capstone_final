import {

  BrowserRouter,

  Routes,

  Route

} from 'react-router-dom'

/* =====================================
   COMPONENTS
===================================== */

import Sidebar from './components/Sidebar'

/* =====================================
   PAGES
===================================== */

import Dashboard from './pages/Dashboard'

import StreamingMonitor from './pages/StreamingMonitor'

import IntrusionDetection from './pages/IntrusionDetection'

import FraudDetection from './pages/FraudDetection'

import Investigation from './pages/Investigation'

import IncidentResponse from './pages/IncidentResponse'

import Explainability from './pages/Explainability'

import UEBA from './pages/UEBA'

/* =====================================
   APP
===================================== */

function App() {

  return (

    <BrowserRouter>

      <div className="app-layout">

        {/* ========================= */}
        {/* SIDEBAR */}
        {/* ========================= */}

        <Sidebar />

        {/* ========================= */}
        {/* MAIN CONTENT */}
        {/* ========================= */}

        <div className="main-content">

          <Routes>

            {/* ===================== */}
            {/* DASHBOARD */}
            {/* ===================== */}

            <Route

              path="/"

              element={<Dashboard />}
            />

            {/* ===================== */}
            {/* STREAMING */}
            {/* ===================== */}

            <Route

              path="/streaming"

              element={<StreamingMonitor />}
            />

            {/* ===================== */}
            {/* INTRUSION DETECTION */}
            {/* ===================== */}

            <Route

              path="/intrusion"

              element={<IntrusionDetection />}
            />

            {/* ===================== */}
            {/* FRAUD DETECTION */}
            {/* ===================== */}

            <Route

              path="/fraud"

              element={<FraudDetection />}
            />

            {/* ===================== */}
            {/* INVESTIGATION */}
            {/* ===================== */}

            <Route

              path="/investigation"

              element={<Investigation />}
            />

            {/* ===================== */}
            {/* INCIDENT RESPONSE */}
            {/* ===================== */}

            <Route

              path="/response"

              element={<IncidentResponse />}
            />

            {/* ===================== */}
            {/* EXPLAINABILITY */}
            {/* ===================== */}

            <Route

              path="/explainability"

              element={<Explainability />}
            />

            {/* ===================== */}
            {/* UEBA */}
            {/* ===================== */}

            <Route

              path="/ueba"

              element={<UEBA />}
            />

          </Routes>

        </div>

      </div>

    </BrowserRouter>
  )
}

export default App