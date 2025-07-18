import React, { useEffect, useState } from 'react';

const API_URL = 'http://localhost:5001/pedidos';

export default function Pedidos() {
  const [pedidos, setPedidos] = useState([]);
  const [form, setForm] = useState({ clienteId: '', productos: [], codigo_pedido: '' });
  const [editId, setEditId] = useState(null);
  const [editingProductos, setEditingProductos] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setPedidos(data));
  }, []);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleProductoChange = (idx, field, value) => {
    const updated = [...editingProductos];
    updated[idx][field] = value;
    setEditingProductos(updated);
  };

  const handleSubmit = e => {
    e.preventDefault();
    const payload = { ...form, productos: editingProductos };
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
      productos: pedido.productos,
      codigo_pedido: pedido.codigo_pedido
    });
    setEditingProductos(Array.isArray(pedido.productos) ? pedido.productos : []);
    setEditId(pedido._id);
  };

  const handleDelete = id => {
    fetch(`${API_URL}/${id}`, { method: 'DELETE' })
      .then(() => window.location.reload());
  };

  const handleRemoveProducto = idx => {
    const updated = [...editingProductos];
    updated.splice(idx, 1);
    setEditingProductos(updated);
  };

  const handleAddProducto = () => {
    setEditingProductos([...editingProductos, {
      cantidad: 1,
      nombre: '',
      precio_unitario: 0,
      productoId: '',
      total_comprado: 0
    }]);
  };

  return (
    <div>
      <h2>Pedidos</h2>
      <form onSubmit={handleSubmit}>
        <input name="clienteId" placeholder="ID Cliente" value={form.clienteId} onChange={handleChange} required />
        <input name="codigo_pedido" placeholder="Código Pedido" value={form.codigo_pedido} onChange={handleChange} required />
        <button type="button" onClick={handleAddProducto}>Agregar producto</button>
        {editingProductos.map((prod, idx) => (
          <div key={idx} style={{ border: '1px solid #ccc', margin: '10px 0', padding: '10px', borderRadius: '6px' }}>
            <input placeholder="Nombre" value={prod.nombre} onChange={e => handleProductoChange(idx, 'nombre', e.target.value)} required />
            <input type="number" placeholder="Cantidad" value={prod.cantidad} onChange={e => handleProductoChange(idx, 'cantidad', e.target.value)} required />
            <input type="number" placeholder="Precio unitario" value={prod.precio_unitario} onChange={e => handleProductoChange(idx, 'precio_unitario', e.target.value)} required />
            <input placeholder="Producto ID" value={prod.productoId} onChange={e => handleProductoChange(idx, 'productoId', e.target.value)} required />
            <input type="number" placeholder="Total comprado" value={prod.total_comprado} onChange={e => handleProductoChange(idx, 'total_comprado', e.target.value)} required />
            <button type="button" onClick={() => handleRemoveProducto(idx)} style={{ background: '#dc3545', color: 'white', marginLeft: 10 }}>Eliminar producto</button>
          </div>
        ))}
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
              <td>
                <ul>
                  {Array.isArray(p.productos) && p.productos.map((prod, idx) => (
                    <li key={idx}>
                      {prod.cantidad} x {prod.nombre} (${prod.precio_unitario} c/u) - Total: ${prod.total_comprado}
                    </li>
                  ))}
                </ul>
              </td>
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
