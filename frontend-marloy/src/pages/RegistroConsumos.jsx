// src/pages/RegistroConsumos.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Modal from 'react-modal';

Modal.setAppElement('#root');

function RegistroConsumos() {
    const [registros, setRegistros] = useState([]);
    const [modalEditar, setModalEditar] = useState(false);
    const [modalAgregar, setModalAgregar] = useState(false);
    const [registroEditando, setRegistroEditando] = useState(null);
    const [registroNuevo, setRegistroNuevo] = useState({
        id_maquina: '',
        id_insumo: '',
        cantidad_usada: '',
    });
    const [error, setError] = useState(null);

    const url_backend = import.meta.env.VITE_BACKEND_URL;

    const fetchRegistros = async () => {
        try {
            const res = await axios.get(`${url_backend}/api/registros_consumo`);
            setRegistros(res.data.data || []);
        } catch (err) {
            console.error(err);
            setError("No se pudieron obtener los registros de consumo");
        }
    };

    useEffect(() => {
        fetchRegistros();
    }, []);

    const handleEditar = (registro) => {
        setRegistroEditando(registro);
        setError(null);
        setModalEditar(true);
    };

    const handleEliminar = async (id) => {
        try {
            await axios.delete(`${url_backend}/api/registros_consumo/${id}`);
            setRegistros((prev) => prev.filter((r) => r.id !== id));
        } catch (err) {
            console.error(err);
            setError("No se pudo eliminar el registro");
        }
    };

    const handleGuardarEdicion = async () => {
        try {
            await axios.put(`${url_backend}/api/registros_consumo/${registroEditando.id}`, registroEditando);
            setModalEditar(false);
            fetchRegistros();
        } catch (err) {
            console.error(err);
            setError("Error al editar registro");
        }
    };

    const handleGuardarNuevo = async () => {
        try {
            await axios.post(`${url_backend}/api/registros_consumo`, registroNuevo);
            setModalAgregar(false);
            fetchRegistros();
        } catch (err) {
            console.error(err);
            setError("Error al agregar registro");
        }
    };

    return (
        <div>
            <Header />
            <div className="min-h-screen bg-[#f3ebe4] p-6">
                <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Registros de Consumo</h1>
                {error && <p className="text-red-500 text-center pb-4">{error}</p>}

                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                    {registros.map((r) => (
                        <div key={r.id} className="bg-white p-4 rounded shadow">
                            <p><strong>Máquina ID:</strong> {r.id_maquina}</p>
                            <p><strong>Insumo ID:</strong> {r.id_insumo}</p>
                            <p><strong>Cantidad:</strong> {r.cantidad_usada}</p>
                            <p><strong>Fecha:</strong> {r.fecha}</p>
                            <div className="flex gap-2 mt-2">
                                <button onClick={() => handleEditar(r)} className="bg-[#8d6e63] text-white px-4 py-2 rounded">Editar</button>
                                <button onClick={() => handleEliminar(r.id)} className="bg-[#8d6e63] text-white px-4 py-2 rounded">Eliminar</button>
                            </div>
                        </div>
                    ))}
                </div>

                <div className="text-center mt-8">
                    <button onClick={() => setModalAgregar(true)} className="bg-[#8d6e63] text-white px-6 py-2 rounded">
                        Agregar Registro
                    </button>
                </div>

                {/* Modal Editar */}
                <Modal
                    isOpen={modalEditar}
                    onRequestClose={() => setModalEditar(false)}
                    className="bg-white p-6 rounded max-w-lg mx-auto mt-20"
                    overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
                >
                    <h2 className="text-2xl font-bold mb-4">Editar Registro</h2>
                    {registroEditando && (
                        <>
                            <input type="text" name="id_maquina" value={registroEditando.id_maquina} onChange={(e) => setRegistroEditando({ ...registroEditando, id_maquina: e.target.value })} className="w-full p-2 border mb-2" placeholder="ID Máquina" />
                            <input type="text" name="id_insumo" value={registroEditando.id_insumo} onChange={(e) => setRegistroEditando({ ...registroEditando, id_insumo: e.target.value })} className="w-full p-2 border mb-2" placeholder="ID Insumo" />
                            <input type="number" name="cantidad_usada" value={registroEditando.cantidad_usada} onChange={(e) => setRegistroEditando({ ...registroEditando, cantidad_usada: e.target.value })} className="w-full p-2 border mb-2" placeholder="Cantidad usada" />
                            <input type="datetime-local" name="fecha" value={registroEditando.fecha} onChange={(e) => setRegistroEditando({ ...registroEditando, fecha: e.target.value })} className="w-full p-2 border mb-4" />
                            <div className="flex justify-end gap-2">
                                <button onClick={() => setModalEditar(false)} className="bg-gray-400 px-4 py-2 rounded text-white">Cancelar</button>
                                <button onClick={handleGuardarEdicion} className="bg-[#8d6e63] px-4 py-2 rounded text-white">Guardar</button>
                            </div>
                        </>
                    )}
                </Modal>

                {/* Modal Agregar */}
                <Modal
                    isOpen={modalAgregar}
                    onRequestClose={() => setModalAgregar(false)}
                    className="bg-white p-6 rounded max-w-lg mx-auto mt-20"
                    overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
                >
                    <h2 className="text-2xl font-bold mb-4">Agregar Registro</h2>
                    <input type="text" value={registroNuevo.id_maquina} onChange={(e) => setRegistroNuevo({ ...registroNuevo, id_maquina: e.target.value })} className="w-full p-2 border mb-2" placeholder="ID Máquina" />
                    <input type="text" value={registroNuevo.id_insumo} onChange={(e) => setRegistroNuevo({ ...registroNuevo, id_insumo: e.target.value })} className="w-full p-2 border mb-2" placeholder="ID Insumo" />
                    <input type="number" value={registroNuevo.cantidad_usada} onChange={(e) => setRegistroNuevo({ ...registroNuevo, cantidad_usada: e.target.value })} className="w-full p-2 border mb-2" placeholder="Cantidad usada" />
                    {/* <input type="date" value={registroNuevo.fecha} onChange={(e) => setRegistroNuevo({ ...registroNuevo, fecha: e.target.value })} className="w-full p-2 border mb-4" /> */}
                    <div className="flex justify-end gap-2">
                        <button onClick={() => setModalAgregar(false)} className="bg-gray-400 px-4 py-2 rounded text-white">Cancelar</button>
                        <button onClick={handleGuardarNuevo} className="bg-[#8d6e63] px-4 py-2 rounded text-white">Guardar</button>
                    </div>
                </Modal>
            </div>
        </div>
    );
}

export default RegistroConsumos;