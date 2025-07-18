import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Clientes from './components/Clientes.jsx';
import Productos from './components/Productos.jsx';
import Pedidos from './components/Pedidos.jsx';

export default function App() {
  return (
    <Router>
      <div style={{ padding: 30 }}>
        <h1>ComercioTech Frontend</h1>
        <nav style={{ marginBottom: 20 }}>
          <Link to="/clientes"><button>Clientes</button></Link>
          <Link to="/productos"><button>Productos</button></Link>
          <Link to="/pedidos"><button>Pedidos</button></Link>
        </nav>
        <Routes>
          <Route path="/clientes" element={<Clientes />} />
          <Route path="/productos" element={<Productos />} />
          <Route path="/pedidos" element={<Pedidos />} />
          <Route path="*" element={<Clientes />} />
        </Routes>
      </div>
    </Router>
  );
}
