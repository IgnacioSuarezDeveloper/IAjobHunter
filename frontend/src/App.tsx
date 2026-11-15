import { useEffect, useState } from 'react'
import './App.css'

function App() {  
  
  const [mensaje, setMensaje] = useState("")

  useEffect(() => {
  fetch("http://localhost:8000/").then(response => response.json())
  .then(data => setMensaje(data))
}, [])
  return (
    <>
      <h1>mensaje</h1>
    </>
  )
}

export default App
