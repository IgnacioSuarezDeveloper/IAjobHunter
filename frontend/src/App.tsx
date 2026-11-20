import { useEffect, useState } from 'react'
import './App.css'


type Usuario = {
  id: number
  nombre: string
  email: string
}

function App() {  
  
  const [usuarios, setUsuarios] = useState<Usuario[]>([])
  const [nombre, setNombre] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  
  async function crearUsuario() {
  await fetch("http://localhost:8000/usuarios/nuevoUsuario/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      nombre: nombre,
      email: email,
      password: password
    })
  })
  setNombre("")
  setEmail("")
  setPassword("")
}
  useEffect(() => {
    fetch("http://localhost:8000/usuarios")
      .then(response => response.json())
      .then(data => setUsuarios(data))
  }, [])

  return (
    <>
      <h1>Usuarios</h1>
      
      <input type="text" placeholder="Nombre" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
      <p>nombre escrito : {nombre}</p>
      <input type="email" placeholder="Email" value = {email} onChange={(e) => setEmail(e.target.value)}/>
      <p>email escrito : {email}</p>

      <input type="password" placeholder="Contraseña" value={password} onChange={(e) => setPassword(e.target.value)} />

      <p>{password}</p>

      <button onClick={crearUsuario}>Crear usuario: </button>

      {usuarios.map((usuario) => (
        <p key={usuario.id} style={{fontSize: 8}}>
          {usuario.nombre} - {usuario.email}
        </p>
      ))}
    </>
  )
}

export default App
