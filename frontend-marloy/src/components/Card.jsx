/*here i will need doing a card components to prefabric each category inside the web. the name will be exctracted from db */
// use tailwind css to style the card

import React from 'react'
import { Link } from 'react-router-dom'
import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'


function Card() {
    // This component will be used to display each category card
    const [categories, setCategories] = useState([])
    const navigate = useNavigate()
    useEffect(() => {
        // Fetch categories from the backend
        const fetchCategories = async () => {
            try {
                const response = await axios.get('http://localhost:5000/api/categories')
                setCategories(response.data)
            } catch (error) {
                console.error('Error fetching categories:', error)
            }
        }
        fetchCategories()
    }, [])
    // Function to handle card click
    const handleCardClick = (categoryId) => {
        // Navigate to the category page
        navigate(`/categories/${categoryId}`)
    }
    // Render the categories as cards

    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
            {categories.map((category) => (
                <div
                    key={category._id}
                    className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 cursor-pointer"
                    onClick={() => handleCardClick(category._id)}
                >
                    <img
                        src={category.imageUrl}
                        alt={category.name}
                        className="w-full h-48 object-cover rounded-t-lg"
                    />
                    <div className="p-4">
                        <h2 className="text-xl font-semibold">{category.name}</h2>
                        <p className="text-gray-600">{category.description}</p>
                    </div>
                </div>
            ))}
        </div>
  )
}

export default Card