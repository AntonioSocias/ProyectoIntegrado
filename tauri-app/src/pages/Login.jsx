import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [dni, setDni] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
  try {
    const res = await fetch('http://localhost:5000/empleados');
    const empleados = await res.json();
    console.log('Empleados:', empleados); // 👈 AÑADE ESTO

    const encontrado = empleados.find(e => e.dni === dni);
    if (encontrado) navigate('/dashboard');
    else alert('Empleado no encontrado');
  } catch (error) {
    console.error('Error en login:', error); // 👈 MÁS CLARO
    alert('Error al conectar con el servidor');
  }
};

  return (
    <div className="p-4">
      <h2 className="text-xl mb-4">Login de Empleado</h2>
      <input
        className="border p-2 mb-2"
        placeholder="DNI"
        value={dni}
        onChange={(e) => setDni(e.target.value)}
      />
      <button className="bg-blue-500 text-white px-4 py-2" onClick={handleLogin}>Entrar</button>
    </div>
  );
}

export default Login;