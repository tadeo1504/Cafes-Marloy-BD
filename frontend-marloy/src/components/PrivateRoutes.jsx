// src/components/PrivateRoutes.jsx
import React from 'react'
import { Navigate, Outlet } from 'react-router-dom'

const PrivateRoutes = () => {
  const token = localStorage.getItem('token')

  // Si hay token, renderiza las rutas hijas, sino redirige a login
  return token ? <Outlet /> : <Navigate to="/login" replace />
}

export default PrivateRoutes
