import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Modal from 'react-modal';

Modal.setAppElement('#root');

function Proveedores() {
  const [proveedores, setProveedores] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ModalIsOpenAgregar, setModalIsOpenAgregar] = useState(false);
  const [proveedorEditando, setProveedorEditando] = useState(null);
  const [proveedorNuevo, setProveedorNuevo] = useState({
    nombre: '',
    contacto: ''
  });

  const url_backend = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchProveedores = async () => {
      try {
        const response = await axios.get(`${url_backend}/api/proveedores`);
        console.log('Proveedores obtenidos:', response.data);
        setProveedores(response.data.data);
      } catch (error) {
        console.error('Error fetching proveedores:', error);
      }
    };
    fetchProveedores();
  }, [url_backend, ModalIsOpenAgregar]);

  const handleModify = (proveedor) => {
    setProveedorEditando(proveedor);
    setModalIsOpen(true);
  };

  const handleAgregarProveedor = () => {
    setProveedorNuevo({ nombre: '', contacto: '' });
    setModalIsOpenAgregar(true);
  };

  const handleModalChange = (e) => {
    const { name, value } = e.target;
    setProveedorEditando({ ...proveedorEditando, [name]: value });
  };

  const handleSaveChanges = async () => {
    try {
      await axios.put(`${url_backend}/api/proveedores/${proveedorEditando.id}`, proveedorEditando);
      setProveedores((prev) =>
        prev.map((p) => (p.id === proveedorEditando.id ? proveedorEditando : p))
      );
      setModalIsOpen(false);
    } catch (error) {
      console.error('Error updating proveedor:', error);
    }
  };

  const handleDelete = async (proveedorId) => {
    try {
      await axios.delete(`${url_backend}/api/proveedores/${proveedorId}`);
      setProveedores(proveedores.filter((p) => p.id !== proveedorId));
    } catch (error) {
      console.error('Error deleting proveedor:', error);
    }
  };

  return (
    <div>
      <Header />
      <div className="min-h-screen bg-[#f3ebe4] p-6">
        <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Proveedores</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {proveedores.map((proveedor) => (
            <div
              key={proveedor.id}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4"
            >
              <h2 className="text-xl font-semibold">{proveedor.nombre}</h2>
              <p className="text-gray-600">{proveedor.contacto}</p>
              <div className="flex flex-col gap-2 mt-4">
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleModify(proveedor)}
                >
                  Editar
                </button>
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleDelete(proveedor.id)}
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
            onClick={handleAgregarProveedor}
          >
            Agregar Proveedor
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
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Editar Proveedor</h2>
        {proveedorEditando && (
          <>
            <input
              type="text"
              name="nombre"
              value={proveedorEditando.nombre}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Nombre"
            />
            <input
              type="text"
              name="contacto"
              value={proveedorEditando.contacto}
              onChange={handleModalChange}
              className="w-full p-2 border mb-4"
              placeholder="Contacto"
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

      {/* Modal de agregar proveedor */}
      <Modal
        isOpen={ModalIsOpenAgregar}
        onRequestClose={() => setModalIsOpenAgregar(false)}
        className="bg-white p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-20"
        overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
      >
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Agregar Proveedor</h2>
        <input
          type="text"
          name="nombre"
          value={proveedorNuevo.nombre}
          onChange={(e) => setProveedorNuevo({ ...proveedorNuevo, nombre: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Nombre"
        />
        <input
          type="text"
          name="contacto"
          value={proveedorNuevo.contacto}
          onChange={(e) => setProveedorNuevo({ ...proveedorNuevo, contacto: e.target.value })}
          className="w-full p-2 border mb-4"
          placeholder="Contacto"
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
                const res = await axios.post(`${url_backend}/api/proveedores`, proveedorNuevo);
                setProveedores((prev) => [...prev, res.data]);
                setModalIsOpenAgregar(false);
              } catch (error) {
                console.error('Error al agregar proveedor:', error);
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

export default Proveedores;
