import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Reservas from './pages/Reservas';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/reservas" element={<Reservas />} />
        {/* Aquí agregarás accesos, apartamentos, clientes */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;