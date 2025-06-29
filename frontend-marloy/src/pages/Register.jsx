import React from 'react'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

// import { url_backend } from '../env' // Assuming you have a .env file with the backend URL


function Register() {

    const url_backend = import.meta.env.VITE_BACKEND_URL;

    const [correo, setCorreo] = useState('')
    const [contrasena, setContrasena] = useState('')
    // const [admin, setAdmin] = useState(0)

    const handleCorreoChange = (event) => {
        setCorreo(event.target.value)
    }
    const handlePasswordChange = (event) => {
        setContrasena(event.target.value)
    }

    const navigate = useNavigate()

    const handleRegister = (event) => {
        event.preventDefault()
        axios.post(`${url_backend}/api/usuarios/registro`, { correo, contrasena })
            .then(response => {
                console.log('Registro exitoso:', response.data.mensaje);
                navigate('/login'); // lo mandás al login después de registrarse
            })
            .catch(error => {
                console.error('Fallo el registro:', error.response?.data?.error || error.message);
            })

    }


    return (
        <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-[#ede0d4] to-[#b08968]">
            <div className="bg-[#f5f5dc] p-8 rounded-lg shadow-lg w-full max-w-md border border-[#ddb892]">
                <h2 className="text-3xl font-extrabold mb-6 text-center text-[#7f5539]">Registro </h2>
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
                    <button
                        type="submit"
                        className="w-full bg-[#b08968] text-white py-3 rounded-lg font-semibold hover:bg-[#7f5539] focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:ring-offset-2 transition duration-200"
                        onClick={handleRegister}
                    >
                        Registrarse
                    </button>
                </form>
                <p className="mt-4 text-sm text-center text-[#a98467]">
                    Ya tienes una cuenta? <a href="/login" className="text-[#b08968] hover:underline">Inicia sesión</a>
                </p>
            </div>
        </div>
    )
}

export default Register