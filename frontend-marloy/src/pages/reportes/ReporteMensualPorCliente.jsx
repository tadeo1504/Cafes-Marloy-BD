// src/pages/ReporteTotalMensualPorCliente.jsx
import React, { useState } from 'react';
import axios from 'axios';
import Header from '../../components/Header';
import { useNavigate } from 'react-router-dom';


function ReporteMensualPorCliente() {
    const url_backend = import.meta.env.VITE_BACKEND_URL;
    const [reporteCliente, setReporteCliente] = useState(null);
    const [anio, setAnio] = useState('');
    const [mes, setMes] = useState('');
    const [error, setError] = useState(null);

    const obtenerReporteCliente = async () => {
        setError(null); // Reseteamos el error al iniciar la solicitud
        if (!anio || !mes) return;
        try {
            const res = await axios.get(`${url_backend}/api/reportes/total-mensual-cliente`, {
                params: { mes, anio }
            });
            console.log('Reporte mensual por cliente:', res.data);
            setReporteCliente(res.data);
        } catch {
            setError("No se pudo obtener el total mensual del cliente");
        }
    };

    const navigate = useNavigate();

    const handleBack = () => {
        navigate('/reportes');
    }

    return (
        <div>
            <Header />
            <div className="min-h-screen bg-[#f3ebe4] p-6">
                <h1 className="text-4xl font-bold text-[#4e342e] text-center">Total mensual por cliente</h1>
                <p className="text-center mb-8 font-bold text-[#4e342e]">(Mayores a cero)</p>
                {error && <p className="text-red-500 text-center mb-4">{error}</p>}
                <button
                    className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded mb-4"
                    onClick={handleBack}
                >
                    Volver a Reportes
                </button>

                <div className="flex gap-4 mb-4 justify-center">
                    <input
                        type="number"
                        placeholder="Mes del reporte"
                        value={mes}
                        onChange={(e) => setMes(e.target.value)}
                        className="p-2 border rounded w-48"
                    />
                    <input
                        type="number"
                        placeholder="Año del reporte"
                        value={anio}
                        onChange={(e) => setAnio(e.target.value)}
                        className="p-2 border rounded w-48"
                    />
                    <button
                        className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                        onClick={obtenerReporteCliente}
                    >
                        Ver reporte
                    </button>
                </div>

                {reporteCliente && (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {Array.isArray(reporteCliente) ? reporteCliente.map((item, index) => (
                            <div key={index} className="bg-white p-4 rounded shadow">
                                <h3 className="text-xl font-semibold">{item.cliente}</h3>
                                <p><strong>Alquiler:</strong> ${Number(item.total_alquiler || 0).toFixed(2)}</p>
                                <p><strong>Consumo:</strong> ${Number(item.total_consumo || 0).toFixed(2)}</p>
                                <p><strong>Total:</strong> ${Number(item.total || 0).toFixed(2)}</p>

                            </div>
                        )) : <p>No hay datos para mostrar.</p>}
                    </div>
                )}
            </div>
        </div>
    );
}

export default ReporteMensualPorCliente;
