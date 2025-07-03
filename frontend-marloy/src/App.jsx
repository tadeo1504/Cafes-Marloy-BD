import './App.css'
import Login from './pages/Login'
import Home from './pages/Home'
import Register from './pages/Register'
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Insumos from './pages/Insumos'
import Maquinas from './pages/Maquinas'
import Mantenimientos from './pages/Mantenimientos'
import Proveedores from './pages/Proveedores'
import Tecnicos from './pages/Tecnicos'
import Clientes from './pages/Clientes'
import PrivateRoutes from './components/PrivateRoutes'
import Reportes from './pages/Reportes'
import ReporteClientesMasMaquinas from './pages/reportes/ReporteClientesMasMaquinas'
import ReporteInsumosMasConsumidos from './pages/reportes/ReporteInsumosMasConsumidos'
import ReporteMensualPorCliente from './pages/reportes/ReporteMensualPorCliente'
import ReporteTecnicosMasMantenimientos from './pages/reportes/ReporteTecnicosMasMantenimientos'
import CrearUsuarios from './pages/CrearUsuarios'
import RegistroConsumos from './pages/RegistroConsumos'

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
          <Route path="/mantenimientos" element={<Mantenimientos />} />
          <Route path="/proveedores" element={<Proveedores />} />
          <Route path="/tecnicos" element={<Tecnicos />} />
          <Route path="/clientes" element={<Clientes />} />
          <Route path="/reportes" element={<Reportes />} />
          <Route path='/registro-consumos' element={<RegistroConsumos />} />
          <Route path='/crear-usuarios' element={<CrearUsuarios />} />
          <Route path='/reporte-cliente-maquinas' element={<ReporteClientesMasMaquinas />} />
          <Route path='/reporte-insumos-mas-consumidos' element={<ReporteInsumosMasConsumidos />} />
          <Route path='/reporte-tecnicos-mas-mantenimientos' element={<ReporteTecnicosMasMantenimientos />} />
          <Route path='/reporte-mensual-por-cliente' element={<ReporteMensualPorCliente />} />
        </Route>

        {/* Ruta fallback */}
        <Route path="*" element={<Login />} />
      </Routes>
    </Router>
  )
}

export default App
