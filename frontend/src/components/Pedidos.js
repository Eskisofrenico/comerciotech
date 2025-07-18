import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:5001/pedidos';

export default function Pedidos() {
  const [pedidos, setPedidos] = useState([]);
  const [form, setForm] = useState({ clienteId: '', productos: '', codigo_pedido: '' });
  const [editId, setEditId] = useState(null);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setPedidos(data));
  }, []);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    let productosArr = [];
    try {
      productosArr = JSON.parse(form.productos);
    } catch {
      alert('Productos debe ser un array JSON');
      return;
    }
    const payload = { ...form, productos: productosArr };
    if (editId) {
      fetch(`${API_URL}/${editId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(() => window.location.reload());
    } else {
      fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(() => window.location.reload());
    }
  };

  const handleEdit = pedido => {
    setForm({
      clienteId: pedido.clienteId,
      productos: JSON.stringify(pedido.productos),
      codigo_pedido: pedido.codigo_pedido
    });
    setEditId(pedido._id);
  };

  const handleDelete = id => {
    fetch(`${API_URL}/${id}`, { method: 'DELETE' })
      .then(() => window.location.reload());
  };

  return (
    <div>
      <h2>Pedidos</h2>
      <form onSubmit={handleSubmit}>
        <input name="clienteId" placeholder="ID Cliente" value={form.clienteId} onChange={handleChange} required />
        <input name="codigo_pedido" placeholder="Código Pedido" value={form.codigo_pedido} onChange={handleChange} required />
        <textarea name="productos" placeholder='Productos (JSON array)' value={form.productos} onChange={handleChange} required />
        <button type="submit">{editId ? 'Actualizar' : 'Crear'}</button>
      </form>
      <table border="1" cellPadding="5" style={{ marginTop: 20 }}>
        <thead>
          <tr>
            <th>ID Cliente</th>
            <th>Código Pedido</th>
            <th>Productos</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {pedidos.map(p => (
            <tr key={p._id}>
              <td>{p.clienteId}</td>
              <td>{p.codigo_pedido}</td>
              <td><pre>{JSON.stringify(p.productos, null, 2)}</pre></td>
              <td>
                <button onClick={() => handleEdit(p)}>Editar</button>
                <button onClick={() => handleDelete(p._id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
