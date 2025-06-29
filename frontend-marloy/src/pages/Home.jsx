import React from 'react'
import Header from '../components/Header'
import { useEffect, useState } from 'react'


function Home() {

  const usuario = JSON.parse(localStorage.getItem('usuario'));
  const esAdmin = usuario?.es_administrador;


  // Estado para manejar la autenticación del usuario
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Verificar si el usuario está autenticado al cargar la página
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      console.log("Token encontrado:", token);
      setIsAuthenticated(true);
    } else {
      setIsAuthenticated(false);
      // Redirigir a la página de login si no hay token
      window.location.href = '/login';
    }
  }, []);

  // useEffect para verificar si el usuario está autenticado
  useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) {
      // Redirigir a la página de login si no hay token
      window.location.href = '/login'
    }
  }, [isAuthenticated]);

  // navegar entre los distintos botones de la page
  const navigateTo = (path) => {
    window.location.href = path;
  }

  return (
    <div className="min-h-screen bg-[#f3ebe4]">
      <Header />

      <div className="text-center mt-8">
        <h1 className="text-4xl font-bold text-[#4e342e]">Sistema de Gestión de Café</h1>
        <p className="text-lg text-[#6d4c41] mt-2">Accedé a todas las funciones del sistema desde aquí</p>
      </div>

      <div className="p-6 grid grid-cols-2 md:grid-cols-3 gap-6 max-w-4xl mx-auto mt-10">
        {esAdmin && (
          <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/proveedores')}>
            Proveedores
          </button>
        )}
        {esAdmin && (
          <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/maquinas')}>
            Maquinas
          </button>
        )}
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/clientes')}>
          Clientes
        </button>
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/insumos')}>
          Insumos
        </button>
        {esAdmin && (
          <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/tecnicos')}>
            Técnicos
          </button>
        )}
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/mantenimientos')}>
          Mantenimientos
        </button>
      </div>
    </div>
  )
}

export default Home
