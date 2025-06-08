import React from 'react'
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'


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

    const handleLogin = (event) => {
        navigate('/home')
        event.preventDefault()
    }

    return (
        <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-[#b08968] to-[#ede0d4]">
            <div className="bg-[#f5f5dc] p-8 rounded-lg shadow-lg w-full max-w-md border border-[#ddb892]">
                <h2 className="text-3xl font-extrabold mb-6 text-center text-[#7f5539]">Login</h2>
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
                        <label className="block text-sm font-medium text-[#7f5539] mb-2">Username</label>
                        <input
                            type="text"
                            value={username}
                            onChange={handleUsernameChange}
                            className="border border-[#ddb892] bg-[#fff8e1] rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:border-[#b08968] transition duration-200 text-[#7f5539]"
                            placeholder="Enter your username"
                            required
                        />
                    </div>
                    <div className="mb-6">
                        <label className="block text-sm font-medium text-[#7f5539] mb-2">Password</label>
                        <input
                            type="password"
                            value={password}
                            onChange={handlePasswordChange}
                            className="border border-[#ddb892] bg-[#fff8e1] rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:border-[#b08968] transition duration-200 text-[#7f5539]"
                            placeholder="Enter your password"
                            required
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-[#b08968] text-white py-3 rounded-lg font-semibold hover:bg-[#7f5539] focus:outline-none focus:ring-2 focus:ring-[#b08968] focus:ring-offset-2 transition duration-200"
                        onClick={handleLogin}
                    >
                        Login
                    </button>
                </form>
                <p className="mt-4 text-sm text-center text-[#a98467]">
                    Don't have an account? <a href="/register" className="text-[#b08968] hover:underline">Sign up</a>
                </p>
            </div>
        </div>
    )
}

export default Login