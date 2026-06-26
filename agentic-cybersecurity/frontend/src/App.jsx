import React, { Suspense } from "react";

import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

/* =====================================
   COMPONENTS
===================================== */

import Sidebar from "./components/Sidebar";

/* =====================================
   PAGES
===================================== */

import Dashboard from "./pages/Dashboard";

import StreamingMonitor from "./pages/StreamingMonitor";

import IntrusionDetection from "./pages/IntrusionDetection";

import FraudDetection from "./pages/FraudDetection";

import Investigation from "./pages/Investigation";

import IncidentResponse from "./pages/IncidentResponse";

import Explainability from "./pages/Explainability";

import UEBA from "./pages/UEBA";

/* =====================================
   APP
===================================== */

function App() {

    return (

        <BrowserRouter

            future={{

                v7_startTransition: true,

                v7_relativeSplatPath: true

            }}

        >

            <div className="app-layout">

                {/* ========================= */}
                {/* SIDEBAR */}
                {/* ========================= */}

                <Sidebar />

                {/* ========================= */}
                {/* MAIN CONTENT */}
                {/* ========================= */}

                <main className="main-content">

                    <Suspense

                        fallback={

                            <div
                                style={{
                                    color: "white",
                                    padding: "30px",
                                    textAlign: "center"
                                }}
                            >

                                Loading...

                            </div>

                        }

                    >

                        <Routes>

                            {/* Dashboard */}

                            <Route

                                path="/"

                                element={<Dashboard />}

                            />

                            {/* Streaming */}

                            <Route

                                path="/streaming"

                                element={<StreamingMonitor />}

                            />

                            {/* Intrusion */}

                            <Route

                                path="/intrusion"

                                element={<IntrusionDetection />}

                            />

                            {/* Fraud */}

                            <Route

                                path="/fraud"

                                element={<FraudDetection />}

                            />

                            {/* Investigation */}

                            <Route

                                path="/investigation"

                                element={<Investigation />}

                            />

                            {/* Incident Response */}

                            <Route

                                path="/response"

                                element={<IncidentResponse />}

                            />

                            {/* Explainability */}

                            <Route

                                path="/explainability"

                                element={<Explainability />}

                            />

                            {/* UEBA */}

                            <Route

                                path="/ueba"

                                element={<UEBA />}

                            />

                            {/* 404 */}

                            <Route

                                path="*"

                                element={

                                    <div
                                        style={{
                                            color: "white",
                                            padding: "50px",
                                            textAlign: "center",
                                            fontSize: "24px"
                                        }}
                                    >

                                        404 - Page Not Found

                                    </div>

                                }

                            />

                        </Routes>

                    </Suspense>

                </main>

            </div>

        </BrowserRouter>

    );

}

export default App;