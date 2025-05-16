import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [dni, setDni] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dni, password })
      });

      const data = await res.json();

      if (res.ok) {
        navigate('/dashboard');
      } else {
        alert(data.error || 'Login fallido');
      }
    } catch (error) {
      console.error('Error en login:', error);
      alert('Error al conectar con el servidor');
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl mb-4">Login de Empleado</h2>
      <input
        className="border p-2 mb-2 block w-full"
        placeholder="DNI"
        value={dni}
        onChange={(e) => setDni(e.target.value)}
      />
      <input
        type="password"
        className="border p-2 mb-2 block w-full"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button className="bg-blue-500 text-white px-4 py-2" onClick={handleLogin}>Entrar</button>
    </div>
  );
}

export default Login;
