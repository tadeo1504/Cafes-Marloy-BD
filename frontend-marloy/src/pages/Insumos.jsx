import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Modal from 'react-modal';

Modal.setAppElement('#root');

function Insumos() {
  const [insumos, setInsumos] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ModalIsOpenAgregar, setModalIsOpenAgregar] = useState(false);
  const [insumoEditando, setInsumoEditando] = useState(null);
  const [insumoNuevo, setInsumoNuevo] = useState({
    descripcion: '',
    tipo: '',
    precio_unitario: '',
    id_proveedor: ''
  });

  const url_backend = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchInsumos = async () => {
      try {
        const response = await axios.get(`${url_backend}/api/insumos`);
        console.log('Insumos obtenidos:', response.data);
        setInsumos(response.data.data);
      } catch (error) {
        console.error('Error fetching insumos:', error);
      }
    };
    fetchInsumos();
  }, [url_backend, ModalIsOpenAgregar]);

  const handleModify = (insumo) => {
    setInsumoEditando(insumo);
    setModalIsOpen(true);
  };

  const handleAgregarInsumo = () => {
    setInsumoNuevo({
      descripcion: '',
      tipo: '',
      precio_unitario: '',
      id_proveedor: ''
    });
    setModalIsOpenAgregar(true);
  };

  const handleModalChange = (e) => {
    const { name, value } = e.target;
    setInsumoEditando({ ...insumoEditando, [name]: value });
  };

  const handleSaveChanges = async () => {
    try {
      await axios.put(`${url_backend}/api/insumos/${insumoEditando.id}`, insumoEditando);
      setInsumos((prev) =>
        prev.map((i) => (i.id === insumoEditando.id ? insumoEditando : i))
      );
      setModalIsOpen(false);
    } catch (error) {
      console.error('Error updating insumo:', error);
    }
  };

  const handleDelete = async (insumoId) => {
    try {
      await axios.delete(`${url_backend}/api/insumos/${insumoId}`);
      setInsumos(insumos.filter((i) => i.id !== insumoId));
    } catch (error) {
      console.error('Error deleting insumo:', error);
    }
  };

  return (
    <div>
      <Header />
      <div className="min-h-screen bg-[#f3ebe4] p-6">
        <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Insumos</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {insumos.map((insumo) => (
            <div
              key={insumo.id}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4"
            >
              <h2 className="text-xl font-semibold">{insumo.descripcion}</h2>
              <p className="text-gray-600">Tipo: {insumo.tipo}</p>
              <p className="text-gray-600">Precio: ${insumo.precio_unitario}</p>
              <p className="text-gray-600">Proveedor ID: {insumo.id_proveedor}</p>
              <div className="flex flex-col gap-2 mt-4">
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleModify(insumo)}
                >
                  Editar
                </button>
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleDelete(insumo.id)}
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
            onClick={handleAgregarInsumo}
          >
            Agregar Insumo
          </button>
        </div>
      </div>

      {/* Modal de edición */}
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={() => setModalIsOpen(false)}
        className="bg-white p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-20"
        overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
      >
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Editar Insumo</h2>
        {insumoEditando && (
          <>
            <input
              type="text"
              name="descripcion"
              value={insumoEditando.descripcion}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Descripción"
            />
            <input
              type="text"
              name="tipo"
              value={insumoEditando.tipo}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Tipo"
            />
            <input
              type="number"
              step="0.01"
              name="precio_unitario"
              value={insumoEditando.precio_unitario}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Precio Unitario"
            />
            <input
              type="number"
              name="id_proveedor"
              value={insumoEditando.id_proveedor}
              onChange={handleModalChange}
              className="w-full p-2 border mb-4"
              placeholder="ID del Proveedor"
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

      {/* Modal de agregar insumo */}
      <Modal
        isOpen={ModalIsOpenAgregar}
        onRequestClose={() => setModalIsOpenAgregar(false)}
        className="bg-white p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-20"
        overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
      >
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Agregar Insumo</h2>
        <input
          type="text"
          name="descripcion"
          value={insumoNuevo.descripcion}
          onChange={(e) => setInsumoNuevo({ ...insumoNuevo, descripcion: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Descripción"
        />
        <input
          type="text"
          name="tipo"
          value={insumoNuevo.tipo}
          onChange={(e) => setInsumoNuevo({ ...insumoNuevo, tipo: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Tipo"
        />
        <input
          type="number"
          step="0.01"
          name="precio_unitario"
          value={insumoNuevo.precio_unitario}
          onChange={(e) => setInsumoNuevo({ ...insumoNuevo, precio_unitario: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Precio Unitario"
        />
        <input
          type="number"
          name="id_proveedor"
          value={insumoNuevo.id_proveedor}
          onChange={(e) => setInsumoNuevo({ ...insumoNuevo, id_proveedor: e.target.value })}
          className="w-full p-2 border mb-4"
          placeholder="ID del Proveedor"
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
                const res = await axios.post(`${url_backend}/api/insumos`, insumoNuevo);
                setInsumos(prev => [...prev, res.data]);
                setModalIsOpenAgregar(false);
              } catch (error) {
                console.error("Error al agregar insumo:", error);
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

export default Insumos;
