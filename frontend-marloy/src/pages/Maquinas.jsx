import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Modal from 'react-modal';

Modal.setAppElement('#root');

function Maquinas() {
  const [maquinas, setMaquinas] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ModalIsOpenAgregar, setModalIsOpenAgregar] = useState(false);
  const [maquinaEditando, setMaquinaEditando] = useState(null);
  const [maquinaNueva, setMaquinaNueva] = useState({
    costo_alquiler_mensual: 0,
    ubicacion_cliente: '',
    id_cliente: '',
    modelo: ''
  });

  const url_backend = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchMaquinas = async () => {
      try {
        const response = await axios.get(`${url_backend}/api/maquinas`);
        console.log('Máquinas obtenidas:', response.data);
        setMaquinas(response.data.data);
      } catch (error) {
        console.error('Error fetching maquinas:', error);
      }
    };
    fetchMaquinas();
  }, [url_backend, ModalIsOpenAgregar]);

  const handleModify = (maquina) => {
    setMaquinaEditando(maquina);
    setModalIsOpen(true);
  };

  const handleAgregarMaquina = () => {
    setMaquinaNueva({
      modelo: '',
      descripcion: '',
      costo_alquiler_mensual: '',
      id_cliente: ''
    });
    setModalIsOpenAgregar(true);
  };

  const handleModalChange = (e) => {
    const { name, value } = e.target;
    setMaquinaEditando({ ...maquinaEditando, [name]: value });
  };

  const handleSaveChanges = async () => {
    try {
      await axios.put(`${url_backend}/api/maquinas/${maquinaEditando.id}`, maquinaEditando);
      setMaquinas((prev) =>
        prev.map((m) => (m.id === maquinaEditando.id ? maquinaEditando : m))
      );
      setModalIsOpen(false);
    } catch (error) {
      console.error('Error updating maquina:', error);
    }
  };

  const handleDelete = async (maquinaId) => {
    try {
      await axios.delete(`${url_backend}/api/maquinas/${maquinaId}`);
      setMaquinas(maquinas.filter((m) => m.id !== maquinaId));
    } catch (error) {
      console.error('Error deleting maquina:', error);
    }
  };

  return (
    <div>
      <Header />
      <div className="min-h-screen bg-[#f3ebe4] p-6">
        <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Máquinas</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {maquinas.map((maquina) => (
            <div
              key={maquina.id}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4"
            >
              <h2 className="text-xl font-semibold">{maquina.modelo}</h2>
              <p className="text-gray-600">Costo: {maquina.costo_alquiler_mensual}</p>
              <p className="text-gray-600">Ubicacion: {maquina.ubicacion_cliente}</p>
              <p className="text-gray-600">Cliente ID: {maquina.id_cliente}</p>
              <p className="text-gray-600">Maquina ID: {maquina.id}</p>
              <div className="flex flex-col gap-2 mt-4">
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleModify(maquina)}
                >
                  Editar
                </button>
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleDelete(maquina.id)}
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
            onClick={handleAgregarMaquina}
          >
            Agregar Máquina
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
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Editar Máquina</h2>
        {maquinaEditando && (
          <>
            <input
              type="text"
              name="modelo"
              value={maquinaEditando.modelo}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Modelo"
            />
            <input
              type="number"
              name="costo_alquiler_mensual"
              value={maquinaEditando.costo_alquiler_mensual}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Costo de Alquiler Mensual"
            />
            <input
              type="text"
              name="ubicacion_cliente"
              value={maquinaEditando.ubicacion_cliente}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Ubicación del Cliente"
            />
            <input
              type="number"
              name="id_cliente"
              value={maquinaEditando.id_cliente}
              onChange={handleModalChange}
              className="w-full p-2 border mb-4"
              placeholder="ID del Cliente"
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
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Agregar Máquina</h2>
        <input
          type="text"
          name="modelo"
          value={maquinaNueva.modelo}
          onChange={(e) => setMaquinaNueva({ ...maquinaNueva, modelo: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Modelo"
        />
        <input
          type="number"
          name="costo_alquiler_mensual"
          value={maquinaNueva.costo_alquiler_mensual}
          onChange={(e) => setMaquinaNueva({ ...maquinaNueva, costo_alquiler_mensual: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Costo de Alquiler Mensual"
        />
        <input
          type="text"
          name="ubicacion_cliente"
          value={maquinaNueva.ubicacion_cliente}
          onChange={(e) => setMaquinaNueva({ ...maquinaNueva, ubicacion_cliente: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Ubicación del Cliente"
        />
        <input
          type="number"
          name="id_cliente"
          value={maquinaNueva.id_cliente}
          onChange={(e) => setMaquinaNueva({ ...maquinaNueva, id_cliente: e.target.value })}
          className="w-full p-2 border mb-4"
          placeholder="ID del Cliente"
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
                const res = await axios.post(`${url_backend}/api/maquinas`, maquinaNueva);
                setMaquinas(prev => [...prev, res.data]);
                setModalIsOpenAgregar(false);
              } catch (error) {
                console.error("Error al agregar maquina:", error);
              }
            }}
          >
            Guardar
          </button>
        </div>
      </Modal>
    </div>
  );
}

export default Maquinas;