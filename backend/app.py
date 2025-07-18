from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timezone
import json

# ========================================
# 🔧 CONFIGURACIÓN DE LA APLICACIÓN
# ========================================

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# ========================================
# 🗄️ CONFIGURACIÓN DE MONGODB
# ========================================

try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['comerciotech']
    
    # Colecciones
    clientes_collection = db['clientes']
    productos_collection = db['productos']
    pedidos_collection = db['pedidos']
    
    print("✅ Conexión exitosa a MongoDB")
    print(f"📊 Base de datos: {db.name}")
    print(f"👥 Clientes: {clientes_collection.count_documents({})}")
    print(f"📦 Productos: {productos_collection.count_documents({})}")
    print(f"🛒 Pedidos: {pedidos_collection.count_documents({})}")
    
except Exception as e:
    print(f"❌ Error al conectar con MongoDB: {e}")
    exit(1)

# ========================================
# 🔧 FUNCIONES HELPER
# ========================================

def serialize_doc(doc):
    """Convierte ObjectId a string para JSON serialization"""
    if doc is None:
        return None
    if isinstance(doc, list):
        return [serialize_doc(item) for item in doc]
    if isinstance(doc, dict):
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                doc[key] = str(value)
            elif isinstance(value, dict):
                doc[key] = serialize_doc(value)
            elif isinstance(value, list):
                doc[key] = serialize_doc(value)
    return doc

def is_valid_objectid(oid):
    """Valida si un string es un ObjectId válido"""
    try:
        ObjectId(oid)
        return True
    except:
        return False

def handle_error(error, code=500):
    """Maneja errores de manera consistente"""
    print(f"❌ Error: {str(error)}")
    return jsonify({'error': str(error)}), code

# ========================================
# 🏠 RUTA PRINCIPAL
# ========================================

@app.route('/')
def home():
    """Página principal con documentación de la API"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>ComercioTech API</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0; 
                padding: 20px; 
                background-color: #f5f5f5;
                line-height: 1.6; 
            }
            .container { 
                max-width: 1200px; 
                margin: 0 auto; 
                background: white; 
                padding: 30px; 
                border-radius: 10px; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 { color: #205070; margin-bottom: 10px; }
            h2 { color: #7ebc67; margin-top: 30px; }
            h3 { color: #205070; margin-top: 25px; }
            .endpoint { 
                background: #f8f9fa; 
                padding: 12px 15px; 
                margin: 8px 0; 
                border-radius: 5px; 
                border-left: 4px solid #205070;
                font-family: 'Courier New', monospace;
            }
            .method { 
                display: inline-block;
                font-weight: bold; 
                color: white; 
                padding: 2px 8px;
                border-radius: 3px;
                margin-right: 10px;
                min-width: 60px;
                text-align: center;
            }
            .get { background-color: #28a745; }
            .post { background-color: #007bff; }
            .put { background-color: #ffc107; color: #212529; }
            .delete { background-color: #dc3545; }
            .status { 
                padding: 20px; 
                background: #e8f5e8; 
                border-radius: 5px; 
                margin: 20px 0;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #eee;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 ComercioTech API</h1>
            <p><strong>Backend Flask para sistema de gestión comercial</strong></p>
            
            <div class="status">
                <h3>📊 Estado del Sistema</h3>
                <p>✅ <strong>API funcionando correctamente</strong></p>
                <p>🗄️ <strong>Base de datos:</strong> MongoDB - comerciotech</p>
                <p>🌐 <strong>CORS:</strong> Habilitado para React frontend</p>
                <p>📡 <strong>Puerto:</strong> 5001</p>
            </div>
            
            <h2>📋 Endpoints Disponibles</h2>
            
            <h3>👥 Clientes</h3>
            <div class="endpoint">
                <span class="method get">GET</span> 
                <strong>/clientes</strong> - Obtener todos los clientes
            </div>
            <div class="endpoint">
                <span class="method post">POST</span> 
                <strong>/clientes</strong> - Crear nuevo cliente
            </div>
            <div class="endpoint">
                <span class="method get">GET</span> 
                <strong>/clientes/&lt;id&gt;</strong> - Obtener cliente por ID
            </div>
            <div class="endpoint">
                <span class="method put">PUT</span> 
                <strong>/clientes/&lt;id&gt;</strong> - Actualizar cliente
            </div>
            <div class="endpoint">
                <span class="method delete">DELETE</span> 
                <strong>/clientes/&lt;id&gt;</strong> - Eliminar cliente
            </div>
            
            <h3>📦 Productos</h3>
            <div class="endpoint">
                <span class="method get">GET</span> 
                <strong>/productos</strong> - Obtener todos los productos
            </div>
            <div class="endpoint">
                <span class="method post">POST</span> 
                <strong>/productos</strong> - Crear nuevo producto
            </div>
            <div class="endpoint">
                <span class="method get">GET</span> 
                <strong>/productos/&lt;id&gt;</strong> - Obtener producto por ID
            </div>
            <div class="endpoint">
                <span class="method put">PUT</span> 
                <strong>/productos/&lt;id&gt;</strong> - Actualizar producto
            </div>
            <div class="endpoint">
                <span class="method delete">DELETE</span> 
                <strong>/productos/&lt;id&gt;</strong> - Eliminar producto
            </div>
            
            <h3>🛒 Pedidos</h3>
            <div class="endpoint">
                <span class="method get">GET</span> 
                <strong>/pedidos</strong> - Obtener todos los pedidos
            </div>
            <div class="endpoint">
                <span class="method post">POST</span> 
                <strong>/pedidos</strong> - Crear nuevo pedido
            </div>
            <div class="endpoint">
                <span class="method get">GET</span> 
                <strong>/pedidos/&lt;id&gt;</strong> - Obtener pedido por ID
            </div>
            <div class="endpoint">
                <span class="method put">PUT</span> 
                <strong>/pedidos/&lt;id&gt;</strong> - Actualizar pedido
            </div>
            <div class="endpoint">
                <span class="method delete">DELETE</span> 
                <strong>/pedidos/&lt;id&gt;</strong> - Eliminar pedido
            </div>
            
            <h3>🔧 Utilidades</h3>
            <div class="endpoint">
                <span class="method get">GET</span> 
                <strong>/debug</strong> - Información de debug y estadísticas
            </div>
            
            <div class="footer">
                <p>💻 Desarrollado para ComercioTech</p>
                <p>🔗 Para probar la API: <a href="/debug">Ver datos de debug</a></p>
            </div>
        </div>
    </body>
    </html>
    '''

# ========================================
# 👥 RUTAS DE CLIENTES
# ========================================

@app.route('/clientes', methods=['GET'])
def get_clientes():
    """Obtener todos los clientes"""
    try:
        clientes = list(clientes_collection.find())
        return jsonify(serialize_doc(clientes))
    except Exception as e:
        return handle_error(e)

@app.route('/clientes', methods=['POST'])
def create_cliente():
    """Crear nuevo cliente"""
    try:
        data = request.get_json()
        
        # Validaciones básicas
        if not data:
            return handle_error('No se proporcionaron datos', 400)
        
        required_fields = ['nombre', 'apellidos', 'identificador']
        for field in required_fields:
            if not data.get(field):
                return handle_error(f'El campo {field} es requerido', 400)
        
        # Verificar que no existe un cliente con el mismo identificador
        existing = clientes_collection.find_one({'identificador': data['identificador']})
        if existing:
            return handle_error('Ya existe un cliente con ese identificador', 400)
        
        # Agregar fecha de registro si no existe
        if 'fechaRegistro' not in data:
            data['fechaRegistro'] = datetime.now().strftime('%Y-%m-%d')
        
        # Insertar cliente
        result = clientes_collection.insert_one(data)
        
        # Obtener cliente creado
        cliente = clientes_collection.find_one({'_id': result.inserted_id})
        
        return jsonify(serialize_doc(cliente)), 201
        
    except Exception as e:
        return handle_error(e)

@app.route('/clientes/<cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    """Obtener cliente por ID"""
    try:
        if not is_valid_objectid(cliente_id):
            return handle_error('ID de cliente inválido', 400)
        
        cliente = clientes_collection.find_one({'_id': ObjectId(cliente_id)})
        
        if not cliente:
            return handle_error('Cliente no encontrado', 404)
        
        return jsonify(serialize_doc(cliente))
        
    except Exception as e:
        return handle_error(e)

@app.route('/clientes/<cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    """Actualizar cliente"""
    try:
        if not is_valid_objectid(cliente_id):
            return handle_error('ID de cliente inválido', 400)
        
        data = request.get_json()
        
        if not data:
            return handle_error('No se proporcionaron datos', 400)
        
        # Verificar que el cliente existe
        cliente = clientes_collection.find_one({'_id': ObjectId(cliente_id)})
        if not cliente:
            return handle_error('Cliente no encontrado', 404)
        
        # Si se está actualizando el identificador, verificar que no exista otro con el mismo
        if 'identificador' in data and data['identificador'] != cliente.get('identificador'):
            existing = clientes_collection.find_one({'identificador': data['identificador']})
            if existing:
                return handle_error('Ya existe un cliente con ese identificador', 400)
        
        # Actualizar cliente
        result = clientes_collection.update_one(
            {'_id': ObjectId(cliente_id)},
            {'$set': data}
        )
        
        # Obtener cliente actualizado
        cliente_actualizado = clientes_collection.find_one({'_id': ObjectId(cliente_id)})
        
        return jsonify(serialize_doc(cliente_actualizado))
        
    except Exception as e:
        return handle_error(e)

@app.route('/clientes/<cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    """Eliminar cliente"""
    try:
        if not is_valid_objectid(cliente_id):
            return handle_error('ID de cliente inválido', 400)
        
        # Verificar que no tenga pedidos asociados
        pedidos = pedidos_collection.find({'clienteId': ObjectId(cliente_id)})
        if pedidos_collection.count_documents({'clienteId': ObjectId(cliente_id)}) > 0:
            return handle_error('No se puede eliminar el cliente porque tiene pedidos asociados', 400)
        
        result = clientes_collection.delete_one({'_id': ObjectId(cliente_id)})
        
        if result.deleted_count == 0:
            return handle_error('Cliente no encontrado', 404)
        
        return jsonify({'message': 'Cliente eliminado exitosamente'})
        
    except Exception as e:
        return handle_error(e)

# ========================================
# 📦 RUTAS DE PRODUCTOS
# ========================================

@app.route('/productos', methods=['GET'])
def get_productos():
    """Obtener todos los productos"""
    try:
        productos = list(productos_collection.find())
        return jsonify(serialize_doc(productos))
    except Exception as e:
        return handle_error(e)

@app.route('/productos', methods=['POST'])
def create_producto():
    """Crear nuevo producto"""
    try:
        data = request.get_json()
        
        # Validaciones básicas
        if not data:
            return handle_error('No se proporcionaron datos', 400)
        
        required_fields = ['nombre', 'precio', 'stock', 'categoria']
        for field in required_fields:
            if field not in data:
                return handle_error(f'El campo {field} es requerido', 400)
        
        # Validar tipos de datos
        if not isinstance(data['precio'], (int, float)) or data['precio'] <= 0:
            return handle_error('El precio debe ser un número positivo', 400)
        
        if not isinstance(data['stock'], int) or data['stock'] < 0:
            return handle_error('El stock debe ser un número entero no negativo', 400)
        
        # Insertar producto
        result = productos_collection.insert_one(data)
        
        # Obtener producto creado
        producto = productos_collection.find_one({'_id': result.inserted_id})
        
        return jsonify(serialize_doc(producto)), 201
        
    except Exception as e:
        return handle_error(e)

@app.route('/productos/<producto_id>', methods=['GET'])
def get_producto(producto_id):
    """Obtener producto por ID"""
    try:
        if not is_valid_objectid(producto_id):
            return handle_error('ID de producto inválido', 400)
        
        producto = productos_collection.find_one({'_id': ObjectId(producto_id)})
        
        if not producto:
            return handle_error('Producto no encontrado', 404)
        
        return jsonify(serialize_doc(producto))
        
    except Exception as e:
        return handle_error(e)

@app.route('/productos/<producto_id>', methods=['PUT'])
def update_producto(producto_id):
    """Actualizar producto"""
    try:
        if not is_valid_objectid(producto_id):
            return handle_error('ID de producto inválido', 400)
        
        data = request.get_json()
        
        if not data:
            return handle_error('No se proporcionaron datos', 400)
        
        # Validar tipos de datos si se proporcionan
        if 'precio' in data:
            if not isinstance(data['precio'], (int, float)) or data['precio'] <= 0:
                return handle_error('El precio debe ser un número positivo', 400)
        
        if 'stock' in data:
            if not isinstance(data['stock'], int) or data['stock'] < 0:
                return handle_error('El stock debe ser un número entero no negativo', 400)
        
        # Actualizar producto
        result = productos_collection.update_one(
            {'_id': ObjectId(producto_id)},
            {'$set': data}
        )
        
        if result.matched_count == 0:
            return handle_error('Producto no encontrado', 404)
        
        # Obtener producto actualizado
        producto = productos_collection.find_one({'_id': ObjectId(producto_id)})
        
        return jsonify(serialize_doc(producto))
        
    except Exception as e:
        return handle_error(e)

@app.route('/productos/<producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    """Eliminar producto"""
    try:
        if not is_valid_objectid(producto_id):
            return handle_error('ID de producto inválido', 400)
        
        result = productos_collection.delete_one({'_id': ObjectId(producto_id)})
        
        if result.deleted_count == 0:
            return handle_error('Producto no encontrado', 404)
        
        return jsonify({'message': 'Producto eliminado exitosamente'})
        
    except Exception as e:
        return handle_error(e)

# ========================================
# 🛒 RUTAS DE PEDIDOS
# ========================================

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    """Obtener todos los pedidos"""
    try:
        pedidos = list(pedidos_collection.find())
        return jsonify(serialize_doc(pedidos))
    except Exception as e:
        return handle_error(e)

@app.route('/pedidos', methods=['POST'])
def create_pedido():
    """Crear nuevo pedido"""
    try:
        data = request.get_json()
        
        # Validaciones básicas
        if not data:
            return handle_error('No se proporcionaron datos', 400)
        
        required_fields = ['clienteId', 'productos', 'codigo_pedido']
        for field in required_fields:
            if not data.get(field):
                return handle_error(f'El campo {field} es requerido', 400)
        
        # Validar que el cliente existe
        if not is_valid_objectid(data['clienteId']):
            return handle_error('ID de cliente inválido', 400)
        
        cliente = clientes_collection.find_one({'_id': ObjectId(data['clienteId'])})
        if not cliente:
            return handle_error('Cliente no encontrado', 404)
        
        # Validar productos
        if not isinstance(data['productos'], list) or len(data['productos']) == 0:
            return handle_error('Debe incluir al menos un producto', 400)
        
        # Calcular total si no se proporciona
        total_calculado = 0
        for producto in data['productos']:
            total_calculado += producto.get('total_comprado', 0)
        
        if 'total_compra' not in data:
            data['total_compra'] = total_calculado
        
        # Agregar fecha actual si no se proporciona
        if 'fecha_pedido' not in data:
            data['fecha_pedido'] = datetime.now(timezone.utc)
        
        # Verificar que no existe un pedido con el mismo código
        existing = pedidos_collection.find_one({'codigo_pedido': data['codigo_pedido']})
        if existing:
            return handle_error('Ya existe un pedido con ese código', 400)
        
        # Insertar pedido
        result = pedidos_collection.insert_one(data)
        
        # Obtener pedido creado
        pedido = pedidos_collection.find_one({'_id': result.inserted_id})
        
        return jsonify(serialize_doc(pedido)), 201
        
    except Exception as e:
        return handle_error(e)

@app.route('/pedidos/<pedido_id>', methods=['GET'])
def get_pedido(pedido_id):
    """Obtener pedido por ID"""
    try:
        if not is_valid_objectid(pedido_id):
            return handle_error('ID de pedido inválido', 400)
        
        pedido = pedidos_collection.find_one({'_id': ObjectId(pedido_id)})
        
        if not pedido:
            return handle_error('Pedido no encontrado', 404)
        
        return jsonify(serialize_doc(pedido))
        
    except Exception as e:
        return handle_error(e)

@app.route('/pedidos/<pedido_id>', methods=['PUT'])
def update_pedido(pedido_id):
    """Actualizar pedido"""
    try:
        if not is_valid_objectid(pedido_id):
            return handle_error('ID de pedido inválido', 400)
        
        data = request.get_json()
        
        if not data:
            return handle_error('No se proporcionaron datos', 400)
        
        # Validar clienteId si se proporciona
        if 'clienteId' in data:
            if not is_valid_objectid(data['clienteId']):
                return handle_error('ID de cliente inválido', 400)
            
            cliente = clientes_collection.find_one({'_id': ObjectId(data['clienteId'])})
            if not cliente:
                return handle_error('Cliente no encontrado', 404)
        
        # Actualizar pedido
        result = pedidos_collection.update_one(
            {'_id': ObjectId(pedido_id)},
            {'$set': data}
        )
        
        if result.matched_count == 0:
            return handle_error('Pedido no encontrado', 404)
        
        # Obtener pedido actualizado
        pedido = pedidos_collection.find_one({'_id': ObjectId(pedido_id)})
        
        return jsonify(serialize_doc(pedido))
        
    except Exception as e:
        return handle_error(e)

@app.route('/pedidos/<pedido_id>', methods=['DELETE'])
def delete_pedido(pedido_id):
    """Eliminar pedido"""
    try:
        if not is_valid_objectid(pedido_id):
            return handle_error('ID de pedido inválido', 400)
        
        result = pedidos_collection.delete_one({'_id': ObjectId(pedido_id)})
        
        if result.deleted_count == 0:
            return handle_error('Pedido no encontrado', 404)
        
        return jsonify({'message': 'Pedido eliminado exitosamente'})
        
    except Exception as e:
        return handle_error(e)

# ========================================
# 🔧 RUTAS DE UTILIDADES
# ========================================

@app.route('/debug', methods=['GET'])
def debug_info():
    """Información de debug de la base de datos"""
    try:
        # Contar documentos en cada colección
        clientes_count = clientes_collection.count_documents({})
        productos_count = productos_collection.count_documents({})
        pedidos_count = pedidos_collection.count_documents({})
        
        # Obtener algunos documentos de ejemplo
        clientes_sample = list(clientes_collection.find().limit(3))
        productos_sample = list(productos_collection.find().limit(3))
        pedidos_sample = list(pedidos_collection.find().limit(3))
        
        debug_data = {
            'status': 'API funcionando correctamente',
            'timestamp': datetime.now().isoformat(),
            'database': 'comerciotech',
            'collections': {
                'clientes': {
                    'count': clientes_count,
                    'sample': serialize_doc(clientes_sample)
                },
                'productos': {
                    'count': productos_count,
                    'sample': serialize_doc(productos_sample)
                },
                'pedidos': {
                    'count': pedidos_count,
                    'sample': serialize_doc(pedidos_sample)
                }
            },
            'total_documents': clientes_count + productos_count + pedidos_count,
            'endpoints': {
                'clientes': ['GET /clientes', 'POST /clientes', 'GET /clientes/<id>', 'PUT /clientes/<id>', 'DELETE /clientes/<id>'],
                'productos': ['GET /productos', 'POST /productos', 'GET /productos/<id>', 'PUT /productos/<id>', 'DELETE /productos/<id>'],
                'pedidos': ['GET /pedidos', 'POST /pedidos', 'GET /pedidos/<id>', 'PUT /pedidos/<id>', 'DELETE /pedidos/<id>']
            }
        }
        
        return jsonify(debug_data)
        
    except Exception as e:
        return handle_error(e)

# ========================================
# 🚀 EJECUTAR APLICACIÓN
# ========================================

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 INICIANDO COMERCIOTECH API")
    print("=" * 50)
    print("📄 Documentación: http://localhost:5001")
    print("🔧 Debug Info: http://localhost:5001/debug")
    print("💾 Base de datos: MongoDB - comerciotech")
    print("🌐 CORS: Habilitado para React frontend")
    print("📡 Puerto: 5001")
    print("=" * 50)
    
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )