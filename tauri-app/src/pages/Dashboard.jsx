import React from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
  return (
    <div className="p-4">
      <h2 className="text-xl mb-4">Panel de Control</h2>
      <ul className="space-y-2">
        <li><Link to="/reservas" className="text-blue-600">Ver Reservas</Link></li>
        <li><Link to="/accesos" className="text-blue-600">Accesos del Día</Link></li>
        <li><Link to="/apartamentos" className="text-blue-600">Gestionar Apartamentos</Link></li>
        <li><Link to="/clientes" className="text-blue-600">Gestionar Clientes</Link></li>
      </ul>
    </div>
  );
}

export default Dashboard;