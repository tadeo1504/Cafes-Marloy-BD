import React from 'react'
import { useState } from 'react'

function Buscador() {

    const [inputValue, setInputValue] = useState('')

    const handleChange = (event) => {
        setInputValue(event.target.value)
    }

  return (
    <div>
        <input
            type="text"
            value={inputValue}
            onChange={handleChange}
            placeholder="Type something..."
            className="border border-gray-300 rounded p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <p className="mt-2 text-gray-700">You typed: {inputValue}</p>

    </div>
  )
}

export default Buscador