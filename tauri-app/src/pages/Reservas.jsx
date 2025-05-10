import React, { useEffect, useState } from 'react';

function Reservas() {
  const [reservas, setReservas] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/reservas')
      .then(res => res.json())
      .then(setReservas)
      .catch(console.error);
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl mb-4">Reservas</h2>
      <ul>
        {reservas.map(r => (
          <li key={r.reserva_id}>Reserva #{r.reserva_id} - Cliente ID: {r.cliente_id}</li>
        ))}
      </ul>
    </div>
  );
}

export default Reservas;