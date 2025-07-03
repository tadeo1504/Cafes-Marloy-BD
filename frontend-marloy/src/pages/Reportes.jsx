import React from 'react'
import Header from '../components/Header'
// import { useEffect, useState } from 'react'


function Reportes() {


    // navegar entre los distintos botones de la page
    const navigateTo = (path) => {
        window.location.href = path;
    }

    return (
        <div className="min-h-screen bg-[#f3ebe4]">
            <Header />

            <div className="text-center mt-8">
                <h1 className="text-4xl font-bold text-[#4e342e]">Sistema de Reportes</h1>
            </div>

            <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-6 max-w-6xl mx-auto mt-10">
                <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/reporte-cliente-maquinas')}>
                    Clientes con mas maquinas
                </button>
                <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/reporte-insumos-mas-consumidos')}>
                    Insumos mas consumidos
                </button>
                <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/reporte-mensual-por-cliente')}>
                    Reporte mensual por cliente
                </button>
                <button className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white h-32 w-full rounded-xl shadow-md text-xl font-semibold" onClick={() => navigateTo('/reporte-tecnicos-mas-mantenimientos')}>
                    Tecnicos con mas mantenimientos
                </button>
            </div>
        </div>
    )
}

export default Reportes
