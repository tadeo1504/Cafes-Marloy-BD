// src/pages/ReporteTecnicosMasMantenimientos.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../../components/Header';
import { useNavigate } from 'react-router-dom';

function ReporteTecnicosMasMantenimientos() {
    const url_backend = import.meta.env.VITE_BACKEND_URL;
    const [tecnicos, setTecnicos] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get(`${url_backend}/api/reportes/tecnicos-mas-mantenimientos`)
            .then(res => setTecnicos(res.data))
            .catch(() => setError("No se pudieron obtener los técnicos con más mantenimientos"));
    }, [url_backend]);

    const navigate = useNavigate();

    const handleBack = () => {
        navigate('/reportes');
    }

    return (
        <div>
            <Header />
            <div className="min-h-screen bg-[#f3ebe4] p-6">
                <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Técnicos con más mantenimientos</h1>
                <button
                    className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded mb-4"
                    onClick={handleBack}
                >
                    Volver a Reportes
                </button>
                {error && <p className="text-red-500 text-center pb-4">{error}</p>}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {tecnicos.map((tec, index) => (
                        <div key={index} className="bg-white p-4 rounded shadow">
                            <p><strong>Nombre:</strong> {tec.nombre} {tec.apellido}</p>
                            <p><strong>Mantenimientos:</strong> {tec.total_mantenimientos}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default ReporteTecnicosMasMantenimientos;
