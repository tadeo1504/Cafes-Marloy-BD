import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Modal from 'react-modal';

Modal.setAppElement('#root');

function Tecnicos() {
  const [tecnicos, setTecnicos] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [ModalIsOpenAgregar, setModalIsOpenAgregar] = useState(false);
  const [tecnicoEditando, setTecnicoEditando] = useState(null);
  const [tecnicoNuevo, setTecnicoNuevo] = useState({
    ci: '',
    nombre: '',
    apellido: '',
    telefono: ''
  });

  const url_backend = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchTecnicos = async () => {
      try {
        const response = await axios.get(`${url_backend}/api/tecnicos`);
        setTecnicos(response.data.data);
      } catch (error) {
        console.error('Error fetching tecnicos:', error);
      }
    };
    fetchTecnicos();
  }, [url_backend, ModalIsOpenAgregar]);

  const handleModify = (tecnico) => {
    setTecnicoEditando(tecnico);
    setModalIsOpen(true);
  };

  const handleAgregarTecnico = () => {
    setTecnicoNuevo({
      ci: '',
      nombre: '',
      apellido: '',
      telefono: ''
    });
    setModalIsOpenAgregar(true);
  };

  const handleModalChange = (e) => {
    const { name, value } = e.target;
    setTecnicoEditando({ ...tecnicoEditando, [name]: value });
  };

  const handleSaveChanges = async () => {
    try {
      await axios.put(`${url_backend}/api/tecnicos/${tecnicoEditando.ci}`, tecnicoEditando);
      setTecnicos((prev) =>
        prev.map((t) => (t.ci === tecnicoEditando.ci ? tecnicoEditando : t))
      );
      setModalIsOpen(false);
    } catch (error) {
      console.error('Error updating tecnico:', error);
    }
  };

  const handleDelete = async (tecnicoId) => {
    try {
      await axios.delete(`${url_backend}/api/tecnicos/${tecnicoId}`);
      setTecnicos(tecnicos.filter((t) => t.ci !== tecnicoId));
    } catch (error) {
      console.error('Error deleting tecnico:', error);
    }
  };

  return (
    <div>
      <Header />
      <div className="min-h-screen bg-[#f3ebe4] p-6">
        <h1 className="text-4xl font-bold text-[#4e342e] text-center mb-8">Técnicos</h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {tecnicos.map((tecnico) => (
            <div
              key={tecnico.ci}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4"
            >
              <h2 className="text-xl font-semibold">{tecnico.nombre} {tecnico.apellido}</h2>
              <p className="text-gray-600">CI: {tecnico.ci}</p>
              <p className="text-gray-600">Teléfono: {tecnico.telefono}</p>
              <div className="flex flex-col gap-2 mt-4">
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleModify(tecnico)}
                >
                  Editar
                </button>
                <button
                  className="bg-[#8d6e63] hover:bg-[#6d4c41] text-white font-bold py-2 px-4 rounded"
                  onClick={() => handleDelete(tecnico.ci)}
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
            onClick={handleAgregarTecnico}
          >
            Agregar Técnico
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
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Editar Técnico</h2>
        {tecnicoEditando && (
          <>
            <input
              type="text"
              name="nombre"
              value={tecnicoEditando.nombre}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Nombre"
            />
            <input
              type="text"
              name="apellido"
              value={tecnicoEditando.apellido}
              onChange={handleModalChange}
              className="w-full p-2 border mb-2"
              placeholder="Apellido"
            />
            <input
              type="text"
              name="telefono"
              value={tecnicoEditando.telefono}
              onChange={handleModalChange}
              className="w-full p-2 border mb-4"
              placeholder="Teléfono"
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

      {/* Modal de agregar técnico */}
      <Modal
        isOpen={ModalIsOpenAgregar}
        onRequestClose={() => setModalIsOpenAgregar(false)}
        className="bg-white p-6 rounded-lg shadow-lg max-w-lg mx-auto mt-20"
        overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-start"
      >
        <h2 className="text-2xl font-bold mb-4 text-[#4e342e]">Agregar Técnico</h2>
        <input
          type="text"
          name="ci"
          value={tecnicoNuevo.ci}
          onChange={(e) => setTecnicoNuevo({ ...tecnicoNuevo, ci: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="CI"
        />
        <input
          type="text"
          name="nombre"
          value={tecnicoNuevo.nombre}
          onChange={(e) => setTecnicoNuevo({ ...tecnicoNuevo, nombre: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Nombre"
        />
        <input
          type="text"
          name="apellido"
          value={tecnicoNuevo.apellido}
          onChange={(e) => setTecnicoNuevo({ ...tecnicoNuevo, apellido: e.target.value })}
          className="w-full p-2 border mb-2"
          placeholder="Apellido"
        />
        <input
          type="text"
          name="telefono"
          value={tecnicoNuevo.telefono}
          onChange={(e) => setTecnicoNuevo({ ...tecnicoNuevo, telefono: e.target.value })}
          className="w-full p-2 border mb-4"
          placeholder="Teléfono"
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
                const res = await axios.post(`${url_backend}/api/tecnicos`, tecnicoNuevo);
                setTecnicos(prev => [...prev, res.data]);
                setModalIsOpenAgregar(false);
              } catch (error) {
                console.error("Error al agregar técnico:", error);
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

export default Tecnicos;
