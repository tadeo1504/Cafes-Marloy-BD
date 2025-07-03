import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Modal from 'react-modal';

Modal.setAppElement('#root');

function Mantenimientos() {
  const [mantenimientos, setMantenimientos] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ModalIsOpenAgregar, setModalIsOpenAgregar] = useState(false);
  const [mantenimientoEditando, setMantenimientoEditando] = useState(null);
  const [mantenimientoNuevo, setMantenimientoNuevo] = useState({
    id_maquina: 0,
    ci_tecnico: 0,
    fecha: '',
    observaciones: ''
  });
  const [error, setError] = useState(null);

  const url_backend = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchMantenimientos = async () => {
      try {
        const response = await axios.get(`${url_backend}/api/mantenimientos`);
        console.log('Mantenimientos obtenidos:', response.data);
        setMantenimientos(response.data.data);
      } catch (error) {
        console.error('Error fetching mantenimientos:', error);
      }
    };
    fetchMantenimientos();
  }, [url_backend, ModalIsOpenAgregar]);

  const handleModify = (mantenimiento) => {
    setMantenimientoEditando(mantenimiento);
    setError(null);
    setModalIsOpen(true);
  };

  const handleAgregarMantenimiento = () => {
    setMantenimientoNuevo({
      id_maquina: 0,
      ci_tecnico: 0,
      tipo: '',
      fecha: '',
      observaciones: ''
    });
    setModalIsOpenAgregar(true);
  };

  const handleModalChange = (e) => {
    const { name, value } = e.target;
    setMantenimientoEditando({ ...mantenimientoEditando, [name]: value });
  };


  // const handleModalChangeAgregar = (e) => {
  //   const { name, value } = e.target;
  //   setMantenimientoNuevo({ ...mantenimientoNuevo, [name]: value });
  // };

  const handleSaveChanges = async () => {
    try {
      // setError(null);
      await axios.put(`${url_backend}/api/mantenimientos/${mantenimientoEditando.id}`, mantenimientoEditando);
      setMantenimientos((prev) =>
        prev.map((m) => (m.id === mantenimientoEditando.id ? mantenimientoEditando : m))
      );
      setModalIsOpen(false);
    } catch (error) {
      setError('Error updating mantenimiento', error);
      console.error('Error updating mantenimiento:', error);
    }
  };

  const handleDelete = async (mantenimientoId) => {
    try {
      await axios.delete(`${url_backend}/api/mantenimientos/${mantenimientoId}`);
      setMantenimientos(mantenimientos.filter((m) => m.id !== mantenimientoId));
    } catch (error) {
      console.error('Error deleting mantenimiento:', error);
    }
  };


  return (
    <div>
      <Header />
      <div className="min-h-screen bg-[#f3ebe4] p-6">
        <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Mantenimientos</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {mantenimientos.map((mantenimiento) => (
            <div
              key={mantenimiento.id}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4"
            >
              <h2 className="text-xl font-semibold">ID maquina: {mantenimiento.id_maquina}</h2>
              <p className="text-gray-600">Tecnico ci: {mantenimiento.ci_tecnico}</p>
              <p className="text-gray-600">tipo: {mantenimiento.tipo}</p>
              <p className="text-gray-600">Fecha mantenimiento: {mantenimiento.fecha}</p>
              <p className="text-gray-600">Observaciones: {mantenimiento.observaciones}</p>
              <div className="flex flex-col gap-2 mt-4">
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleModify(mantenimiento)}
                >
                  Editar
                </button>
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleDelete(mantenimiento.id)}
                >
                  Eliminar
                </button>
              </div>
            </div>
          ))}
        </div>
        <div className="mt-8 text-center">
          <button
            className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
            onClick={handleAgregarMantenimiento}
          >
            Agregar mantenimiento
          </button>
        </div>
      </div>

      {/* Modal edición */}
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={() => setModalIsOpen(false)}
        className="bg-white p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-20"
        overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
      >
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Editar mantenimiento</h2>
        {mantenimientoEditando && (
          <>
            <input
              type="number"
              name="Tecnico CI"
              value={mantenimientoEditando.ci_tecnico}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Técnico CI"
            />
            <input
              type="text"
              name="tipo"
              value={mantenimientoEditando.tipo}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Tipo "
            />
            <input
              type="date"
              name="fecha"
              value={mantenimientoEditando.fecha}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Fecha"
            />
            <input
              type="text"
              name="observaciones"
              value={mantenimientoEditando.observaciones}
              onChange={handleModalChange}
              className="w-full p-2 border mb-4"
              placeholder="Observaciones"
            />
            <div className="flex justify-end gap-2">
              <button
                className="bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded"
                onClick={() => setModalIsOpen(false)}
              >
                Cancelar
              </button>
              <button
                className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                onClick={handleSaveChanges}
              >
                Guardar
              </button>
            </div>
            <div className="mt-4">
              {error && <p className="text-red-500">{error}</p>}
            </div>
          </>
        )}
      </Modal>

      {/* Modal agregar */}
      <Modal
        isOpen={ModalIsOpenAgregar}
        onRequestClose={() => setModalIsOpenAgregar(false)}
        className="bg-white p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-20"
        overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
      >
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Agregar mantenimiento</h2>
        <input
          type="number"
          name="id_maquina"
          value={mantenimientoNuevo.id_maquina}
          onChange={(e) => setMantenimientoNuevo({ ...mantenimientoNuevo, id_maquina: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="ID de la Máquina"
        />
        <input
          type="number"
          name="ci_tecnico"
          value={mantenimientoNuevo.ci_tecnico}
          onChange={(e) => setMantenimientoNuevo({ ...mantenimientoNuevo, ci_tecnico: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="CI del Técnico"
        />
        <input
          type="text"
          name="tipo"
          value={mantenimientoNuevo.tipo}
          onChange={(e) => setMantenimientoNuevo({ ...mantenimientoNuevo, tipo: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Tipo"
        />
        <input
          type="text"
          name="observaciones"
          value={mantenimientoNuevo.observaciones}
          onChange={(e) => setMantenimientoNuevo({ ...mantenimientoNuevo, observaciones: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Observaciones"
        />
        <div className="flex justify-end gap-2">
          <button
            className="bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded"
            onClick={() => setModalIsOpenAgregar(false)}
          >
            Cancelar
          </button>
          <button
            className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
            onClick={async () => {
              try {
                setError(null);
                const res = await axios.post(`${url_backend}/api/mantenimientos`, mantenimientoNuevo);
                setMantenimientos(prev => [...prev, res.data]);
                setModalIsOpenAgregar(false);
              } catch (error) {
                console.error("Error al agregar mantenimiento:", error);
                setError('Error al agregar mantenimiento');
                // setModalIsOpenAgregar(false); 
              }
            }}
          >
            Guardar
          </button>
        </div>
        <div className="mt-4">
          {error && <p className="text-red-500">{error}</p>}
        </div>
      </Modal>
    </div>
  );
}

export default Mantenimientos;