import './App.css'
import Login from './pages/Login'
import Home from './pages/Home'
import Register from './pages/Register'
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

function App() {

  return (
    <>
      <div>
        <Router>
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/login" element={<Login />} />
            <Route path="/home" element={<Home />} />
            <Route path="/register" element={<Register />} />
            {/* Add other routes here */}
          </Routes>
        </Router>        
      </div>
    </>
  )
}

export default App
