import './App.css'
import Login from './pages/Login'
import Home from './pages/Home'
import Register from './pages/Register'
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Insumos from './pages/Insumos'
import Maquinas from './pages/Maquinas'
import Proveedores from './pages/Proveedores'
import Tecnicos from './pages/Tecnicos'
import Clientes from './pages/Clientes'
import PrivateRoutes from './components/PrivateRoutes'

function App() {
  return (
    <Router>
      <Routes>
        {/* Rutas públicas */}
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Rutas protegidas */}
        <Route element={<PrivateRoutes />}>
          <Route path="/home" element={<Home />} />
          <Route path="/insumos" element={<Insumos />} />
          <Route path="/maquinas" element={<Maquinas />} />
          <Route path="/proveedores" element={<Proveedores />} />
          <Route path="/tecnicos" element={<Tecnicos />} />
          <Route path="/clientes" element={<Clientes />} />
        </Route>

        {/* Ruta fallback */}
        <Route path="*" element={<Login />} />
      </Routes>
    </Router>
  )
}

export default App
