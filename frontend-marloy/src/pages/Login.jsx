import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

function Login() {
    const [correo, setCorreo] = useState('')
    const [contrasena, setContrasena] = useState('')
    const navigate = useNavigate()

    useEffect(() => {
        const token = localStorage.getItem('token')
        if (token) {
            navigate('/home')
        }
    }, [navigate])

    const handleLogin = (event) => {
        event.preventDefault()

        axios.post('http://localhost:5000/api/usuarios/login', {
            correo,
            contrasena
        }).then((res) => {
            const token = res.data.token
            localStorage.setItem('token', token)
            console.log("Login exitoso")
            navigate('/home')
        }).catch((err) => {
            console.error("Login failed:", err)
            alert("Error al iniciar sesión: " + (err.response?.data?.error || "Verificá que el backend esté corriendo"))
        })
    }

    return (
        <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-[#b08968] to-[#ede0d4]">
            <div className="bg-[#f5f5dc] p-8 rounded-lg shadow-lg w-full max-w-md border border-[#ddb892]">
                <h2 className="text-3xl font-extrabold mb-6 text-center text-[#7f5539]">Inicio de Sesión</h2>
                <form onSubmit={handleLogin}>
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-[#7f5539] mb-2">Correo electrónico</label>
                        <input
                            type="text"
                            value={correo}
                            onChange={(e) => setCorreo(e.target.value)}
                            className="border border-[#ddb892] bg-[#fff8e1] rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:border-[#b08968] transition duration-200 text-[#7f5539]"
                            placeholder="Ingresa tu correo electrónico"
                            required
                        />
                    </div>
                    <div className="mb-6">
                        <label className="block text-sm font-medium text-[#7f5539] mb-2">Contraseña</label>
                        <input
                            type="password"
                            value={contrasena}
                            onChange={(e) => setContrasena(e.target.value)}
                            className="border border-[#ddb892] bg-[#fff8e1] rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:border-[#b08968] transition duration-200 text-[#7f5539]"
                            placeholder="Ingresa tu contraseña"
                            required
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-[#b08968] text-white py-3 rounded-lg font-semibold hover:bg-[#7f5539] focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:ring-offset-2 transition duration-200"
                    >
                        Iniciar Sesión
                    </button>
                </form>
                <p className="mt-4 text-sm text-center text-[#a98467]">
                    No tienes una cuenta? <a href="/register" className="text-[#b08968] hover:underline">Regístrate</a>
                </p>
            </div>
        </div>
    )
}

export default Login
