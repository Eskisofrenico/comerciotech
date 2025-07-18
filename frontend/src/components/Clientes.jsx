import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:5001/clientes';

export default function Clientes() {
  const [clientes, setClientes] = useState([]);
  const [form, setForm] = useState({ nombre: '', apellidos: '', identificador: '' });
  const [editId, setEditId] = useState(null);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setClientes(data));
  }, []);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    if (editId) {
      fetch(`${API_URL}/${editId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })
        .then(() => window.location.reload());
    } else {
      fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })
        .then(() => window.location.reload());
    }
  };

  const handleEdit = cliente => {
    setForm({
      nombre: cliente.nombre,
      apellidos: cliente.apellidos,
      identificador: cliente.identificador
    });
    setEditId(cliente._id);
  };

  const handleDelete = id => {
    fetch(`${API_URL}/${id}`, { method: 'DELETE' })
      .then(() => window.location.reload());
  };

  return (
    <div>
      <h2>Clientes</h2>
      <form onSubmit={handleSubmit}>
        <input name="nombre" placeholder="Nombre" value={form.nombre} onChange={handleChange} required />
        <input name="apellidos" placeholder="Apellidos" value={form.apellidos} onChange={handleChange} required />
        <input name="identificador" placeholder="Identificador" value={form.identificador} onChange={handleChange} required />
        <button type="submit">{editId ? 'Actualizar' : 'Crear'}</button>
      </form>
      <table border="1" cellPadding="5" style={{ marginTop: 20 }}>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>Identificador</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {clientes.map(c => (
            <tr key={c._id}>
              <td>{c.nombre}</td>
              <td>{c.apellidos}</td>
              <td>{c.identificador}</td>
              <td>
                <button onClick={() => handleEdit(c)}>Editar</button>
                <button onClick={() => handleDelete(c._id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
