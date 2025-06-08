import React from 'react'
import Header from '../components/Header'

function Home() {
  return (
    <div className="min-h-screen bg-[#f3ebe4]">
      <Header />

      <div className="text-center mt-8">
        <h1 className="text-4xl font-bold text-[#4e342e]">Sistema de Gestión de Café</h1>
        <p className="text-lg text-[#6d4c41] mt-2">Accedé a todas las funciones del sistema desde aquí</p>
      </div>

      <div className="p-6 grid grid-cols-2 md:grid-cols-3 gap-6 max-w-4xl mx-auto mt-10">
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold">
          Proveedores
        </button>
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold">
          Maquinas
        </button>
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold">
          Clientes
        </button>
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold">
          Insumos
        </button>
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold">
          Técnicos
        </button>
        <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold">
          Mantenimientos
        </button>
      </div>
    </div>
  )
}

export default Home
