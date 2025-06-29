import React from 'react'
import { useNavigate } from 'react-router-dom';

function Header() {
    const navigate = useNavigate();

    const handleLogout = () => {
        // Clear user session or token if applicable
        localStorage.removeItem('token');
        localStorage.removeItem('usuario');
        console.log("Logout exitoso");
        navigate('/login');
    }

    const handleHome = () => {
        navigate('/home');
    }

    return (
        <div>
            <header className="bg-[#8d6e63] text-white p-4 flex justify-between items-center">
                <h1 className="text-2xl font-bold">Bienvenido al sistema de gestionamiento Marloy!</h1>
                <div className='flex items-center ml-auto'>
                    <button className="ml-auto bg-[#4e342e] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={handleHome}>
                        Home
                    </button>
                    <button onClick={handleLogout} className="ml-4 bg-[#4e342e] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                        Logout
                    </button>
                </div>
            </header>
        </div>
    )
}

export default Header