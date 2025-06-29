import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Modal from 'react-modal';

Modal.setAppElement('#root'); // importante para accesibilidad

function Clientes() {
  const [clientes, setClientes] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ModalIsOpenAgregar, setModalIsOpenAgregar] = useState(false);
  const [clienteEditando, setClienteEditando] = useState(null);
  const [clienteNuevo, setClienteNuevo] = useState({
    nombre: '',
    direccion: '',
    telefono: '',
    correo: ''
  });


  const url_backend = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchClientes = async () => {
      try {
        const response = await axios.get(`${url_backend}/api/clientes`);
        console.log('Clientes obtenidos:', response.data);
        setClientes(response.data.data);
      } catch (error) {
        console.error('Error fetching clientes:', error);
      }
    };
    fetchClientes();
  }, [url_backend]);

  const handleModify = (cliente) => {
    setClienteEditando(cliente);
    setModalIsOpen(true);
  };

  const handleAgregarCliente = () => {
    setClienteNuevo({
      nombre: '',
      direccion: '',
      telefono: '',
      correo: ''
    });
    setModalIsOpenAgregar(true);
  };

  const handleModalChange = (e) => {
    const { name, value } = e.target;
    setClienteEditando({ ...clienteEditando, [name]: value });
  };

  const handleSaveChanges = async () => {
    try {
      await axios.put(`${url_backend}/api/clientes/${clienteEditando.id}`, clienteEditando);
      setClientes((prev) =>
        prev.map((c) => (c.id === clienteEditando.id ? clienteEditando : c))
      );
      setModalIsOpen(false);
    } catch (error) {
      console.error('Error updating cliente:', error);
    }
  };

  const handleDelete = async (clienteId) => {
    try {
      await axios.delete(`${url_backend}/api/clientes/${clienteId}`);
      setClientes(clientes.filter((c) => c.id !== clienteId));
    } catch (error) {
      console.error('Error deleting cliente:', error);
    }
  };

  return (
    <div>
      <Header />
      <div className="min-h-screen bg-[#f3ebe4] p-6">
        <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Clientes</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {clientes.map((cliente) => (
            <div
              key={cliente.id}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4"
            >
              <h2 className="text-xl font-semibold">{cliente.nombre}</h2>
              <p className="text-gray-600">{cliente.correo}</p>
              <p className="text-gray-600">{cliente.telefono}</p>
              <p className="text-gray-600">{cliente.direccion}</p>
              <div className="flex flex-col gap-2 mt-4">
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleModify(cliente)}
                >
                  Editar
                </button>
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleDelete(cliente.id)}
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
            onClick={() => handleAgregarCliente()}
          >
            Agregar Cliente
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
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Editar Cliente</h2>
        {clienteEditando && (
          <>
            <input
              type="text"
              name="nombre"
              value={clienteEditando.nombre}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Nombre"
            />
            <input
              type="text"
              name="direccion"
              value={clienteEditando.direccion}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Dirección"
            />
            <input
              type="text"
              name="telefono"
              value={clienteEditando.telefono}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Teléfono"
            />
            <input
              type="email"
              name="correo"
              value={clienteEditando.correo}
              onChange={handleModalChange}
              className="w-full p-2 border mb-4"
              placeholder="Correo"
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
      {/* Modal para agregar cliente */}
      {/* Modal de agregar cliente */}
      <Modal
        isOpen={ModalIsOpenAgregar}
        onRequestClose={() => setModalIsOpenAgregar(false)}
        className="bg-white p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-20"
        overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
      >
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Agregar Cliente</h2>
        <input
          type="text"
          name="nombre"
          value={clienteNuevo.nombre}
          onChange={(e) => setClienteNuevo({ ...clienteNuevo, nombre: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Nombre"
        />
        <input
          type="text"
          name="direccion"
          value={clienteNuevo.direccion}
          onChange={(e) => setClienteNuevo({ ...clienteNuevo, direccion: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Dirección"
        />
        <input
          type="text"
          name="telefono"
          value={clienteNuevo.telefono}
          onChange={(e) => setClienteNuevo({ ...clienteNuevo, telefono: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Teléfono"
        />
        <input
          type="email"
          name="correo"
          value={clienteNuevo.correo}
          onChange={(e) => setClienteNuevo({ ...clienteNuevo, correo: e.target.value })}
          className="w-full p-2 border mb-4"
          placeholder="Correo"
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
                const res = await axios.post(`${url_backend}/api/clientes`, clienteNuevo);
                setClientes(prev => [...prev, res.data]); // asumimos que el backend responde con el nuevo cliente
                setModalIsOpenAgregar(false);
              } catch (error) {
                console.error("Error al agregar cliente:", error);
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

export default Clientes;
