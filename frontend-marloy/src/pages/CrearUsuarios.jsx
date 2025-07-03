import React from 'react'
import Header from '../components/Header'
import { useState } from 'react'
import axios from 'axios'

function CrearUsuarios() {
    const url_backend = import.meta.env.VITE_BACKEND_URL;

    const [correo, setCorreo] = useState('')
    const [contrasena, setContrasena] = useState('')
    const [admin, setAdmin] = useState(0)
    const [error, setError] = useState(null)
    const [success, setSuccess] = useState(null)

    const handleCorreoChange = (event) => {
        setError(null) // Reseteamos el error al cambiar el correo
        setSuccess(null) // Reseteamos el éxito al cambiar el correo
        setCorreo(event.target.value)
    }
    const handlePasswordChange = (event) => {
        setError(null) // Reseteamos el error al cambiar la contraseña
        setSuccess(null) // Reseteamos el éxito al cambiar la contraseña
        setContrasena(event.target.value)
    }


    const handleRegister = (event) => {

        event.preventDefault()
        axios.post(`${url_backend}/api/usuarios/registro`, { correo, contrasena, admin })
            .then(response => {
                console.log('Registro exitoso:', response.data.mensaje);
                console.log(response.data);
                setSuccess('Usuario registrado exitosamente 🎉');
            })
            .catch(error => {
                console.error('Fallo el registro:', error.response?.data?.error || error.message);
                setError(error.response?.data?.error || 'Error al registrar el usuario');
            })

    }

    return (
        <div className="min-h-screen bg-[#f3ebe4]">
            <Header />

            <div className="text-center mt-8">
                <h1 className="text-4xl font-bold text-[#4e342e]">Sistema de Gestión de Café</h1>
                <p className="text-lg text-[#6d4c41] mt-2 mb-8">Crea nuevos usuarios aquí</p>
            </div>
            <div className="bg-[#f5f5dc] p-8 rounded-lg shadow-lg w-full max-w-md border border-[#ddb892] mx-auto mt-8">
                <form
                    onSubmit={handleRegister}
                    className="space-y-4"
                >
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-[#7f5539] mb-2">Correo electrónico</label>
                        <input
                            type="text"
                            value={correo}
                            onChange={handleCorreoChange}
                            className="border border-[#ddb892] bg-[#fff8e1] rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:border-[#b08968] transition duration-200 text-[#7f5539]"
                            placeholder="Ingresa tu correo electrónico"
                            required
                        />
                    </div>
                    <div className="mb-6">
                        <label className="block text-sm font-medium text-[#7f5539] mb-2">Contrasena</label>
                        <input
                            type="password"
                            value={contrasena}
                            onChange={handlePasswordChange}
                            className="border border-[#ddb892] bg-[#fff8e1] rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:border-[#b08968] transition duration-200 text-[#7f5539]"
                            placeholder="Ingresa tu contraseña"
                            required
                        />
                    </div>
                    <div className="mb-6">
                        <label className="block text-sm font-medium text-[#7f5539] mb-2">Admin</label>
                        <select
                            value={admin}
                            onChange={(e) => setAdmin(e.target.value)}
                            className="border border-[#ddb892] bg-[#fff8e1] rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:border-[#b08968] transition duration-200 text-[#7f5539]"
                        >
                            <option value="0">No</option>
                            <option value="1">Sí</option>
                        </select>
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-[#b08968] text-white py-3 rounded-lg font-semibold hover:bg-[#7f5539] focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:ring-offset-2 transition duration-200"
                        onClick={handleRegister}
                    >
                        Registrarse
                    </button>
                </form>
                {error && <p className="text-red-500 text-center mt-4">{error}</p>}
                {success && <p className="text-green-500 text-center mt-4">{success}</p>}
            </div>

        </div>
    )
}

export default CrearUsuarios