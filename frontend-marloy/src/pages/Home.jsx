import React from 'react'
import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'
import Card from '../components/Card'
import Header from '../components/Header'

function Home() {
  return (
    <div>
        <Header />
        <div className="p-4">
            <p className="text-lg">Explore our categories of cafes and restaurants.</p>
            <Link to="/categories" className="text-blue-100 hover:underline">View Categories</Link>
            <Card />
        </div>

    </div>
  )
}

export default Home