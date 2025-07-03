// src/pages/ReporteClientesMasMaquinas.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../../components/Header';
import { useNavigate } from 'react-router-dom';

function ReporteClientesMasMaquinas() {
    const url_backend = import.meta.env.VITE_BACKEND_URL;
    const [clientes, setClientes] = useState([]);
    const [error, setError] = useState(null);

    const navigate = useNavigate();

    const handleBack = () => {
        navigate('/reportes');
    }


    useEffect(() => {
        axios.get(`${url_backend}/api/reportes/clientes-mas-maquinas`)
            .then(res => setClientes(res.data))
            .catch(() => setError("No se pudieron obtener los clientes con más máquinas"));
    }, [url_backend]);

    return (
        <div>
            <Header />
            <div className="min-h-screen bg-[#f3ebe4] p-6">
                <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Clientes con más máquinas</h1>
                {error && <p className="text-red-500 text-center pb-4">{error}</p>}
                <button
                    className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded mb-4"
                    onClick={handleBack}
                >
                    Volver a Reportes
                </button>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {clientes.map((cli, index) => (
                        <div key={index} className="bg-white p-4 rounded shadow">
                            <p><strong>Nombre:</strong> {cli.nombre}</p>
                            <p><strong>Total de máquinas:</strong> {cli.cantidad_maquinas}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default ReporteClientesMasMaquinas;
