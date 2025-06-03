import React from 'react'
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Buscador from '../components/Buscador'

function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleUsernameChange = (event) => {
        setUsername(event.target.value)
    }
    const handlePasswordChange = (event) => {
        setPassword(event.target.value)
    }

    const navigate = useNavigate()

    useEffect(() => {
        const token = localStorage.getItem('token')
        if (token) {
            navigate('/home') // Redirect to home if token exists
        }
    }, [navigate])

    return (
        <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-blue-500 to-indigo-600">
            <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
                <h2 className="text-3xl font-extrabold mb-6 text-center text-gray-800">Login</h2>
                <form
                    onSubmit={(e) => {
                        e.preventDefault()
                        axios.post('http://localhost:8000/api/login', { username, password })
                            .then(response => {
                                localStorage.setItem('token', response.data.token)
                                navigate('/home')
                            })
                            .catch(error => {
                                console.error('Login failed:', error)
                            })
                    }}
                >
                    <div className="mb-4">
                        <label className="block text-sm font-medium text-gray-700 mb-2">Username</label>
                        <input
                            type="text"
                            value={username}
                            onChange={handleUsernameChange}
                            className="border border-gray-300 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200"
                            placeholder="Enter your username"
                            required
                        />
                    </div>
                    <div className="mb-6">
                        <label className="block text-sm font-medium text-gray-700 mb-2">Password</label>
                        <input
                            type="password"
                            value={password}
                            onChange={handlePasswordChange}
                            className="border border-gray-300 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200"
                            placeholder="Enter your password"
                            required
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-200"
                    >
                        Login
                    </button>
                </form>
                <p className="mt-4 text-sm text-center text-gray-600">
                    Don't have an account? <a href="/register" className="text-blue-550 hover:underline">Sign up</a>
                </p>
            </div>
        </div>
    )
}

export default Login