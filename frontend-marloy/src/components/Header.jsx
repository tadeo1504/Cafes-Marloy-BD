import React from 'react'

function Header() {
  return (
    <div>
        <header className="bg-[#8d6e63] text-white p-4 flex justify-between items-center">
            <h1 className="text-2xl font-bold">Bienvenido al sistema de gestionamiento Marloy!</h1>
            <div className='flex items-center ml-auto'>
                <button className="ml-auto bg-[#4e342e] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Home
                </button>
                <button className="ml-4 bg-[#4e342e] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Profile
                </button>
                <button className="ml-4 bg-[#4e342e] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Logout
                </button>
            </div>
        </header>
    </div>
  )
}

export default Header