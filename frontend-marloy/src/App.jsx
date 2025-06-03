import './App.css'
import Login from './pages/Login'
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
// import './index.css';
function App() {

  return (
    <>
      <div>
        <Router>
          <Routes>
            <Route path="/" element={<Login />} />
            {/* Add other routes here */}
          </Routes>
        </Router>        
      </div>
    </>
  )
}

export default App
