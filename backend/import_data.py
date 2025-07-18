#!/usr/bin/env python3
"""
Script para importar los datos reales de comerciotech
Ejecutar desde el directorio backend con: python import_data.py
"""

from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import json

# Conectar a MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['comerciotech']
    print("✅ Conectado a MongoDB exitosamente")
except Exception as e:
    print(f"❌ Error al conectar con MongoDB: {e}")
    exit(1)

# Colecciones
clientes_collection = db['clientes']
productos_collection = db['productos']
pedidos_collection = db['pedidos']

print("🧹 Limpiando colecciones existentes...")
clientes_collection.drop()
productos_collection.drop()
pedidos_collection.drop()

# ========================================
# 👥 DATOS REALES DE CLIENTES
# ========================================

print("📥 Importando clientes...")

clientes_data = [
    {
        "_id": ObjectId("68782d020f955f3ff6066610"),
        "identificador": "C001",
        "nombre": "Luan",
        "apellidos": "Hernández Alarcón",
        "direccion": {
            "calle": "Los Álamos",
            "numero": "45",
            "ciudad": "San pedro de la paz"
        },
        "fechaRegistro": "2025-07-01"
    },
    {
        "_id": ObjectId("68782d020f955f3ff6066611"),
        "identificador": "C002",
        "nombre": "Jorge",
        "apellidos": "Castillo Altamirano",
        "direccion": {
            "calle": "Las Rosas",
            "numero": "1232",
            "ciudad": "Concepción"
        },
        "fechaRegistro": "2025-10-12"
    },
    {
        "_id": ObjectId("68782d020f955f3ff6066612"),
        "identificador": "C003",
        "nombre": "Pablo",
        "apellidos": "Villa Alarcón",
        "direccion": {
            "calle": "Colo Colo",
            "numero": "112",
            "ciudad": "Chiguayante"
        },
        "fechaRegistro": "2025-12-16"
    },
    {
        "_id": ObjectId("68782d020f955f3ff6066613"),
        "identificador": "C004",
        "nombre": "Luis",
        "apellidos": "Martínez Soto",
        "direccion": {
            "calle": "Brasil",
            "numero": "788",
            "ciudad": "Osorno"
        },
        "fechaRegistro": "2025-12-15"
    },
    {
        "_id": ObjectId("68782d020f955f3ff6066614"),
        "identificador": "C005",
        "nombre": "Angel",
        "apellidos": "Brito Rivas",
        "direccion": {
            "calle": "Maipú",
            "numero": "255",
            "ciudad": "Concepción"
        },
        "fechaRegistro": "2025-12-14"
    },
    {
        "_id": ObjectId("68782d020f955f3ff6066615"),
        "identificador": "C006",
        "nombre": "Felipe",
        "apellidos": "Suarez Vergara",
        "direccion": {
            "calle": "Manuel Rodríguez",
            "numero": "1022",
            "ciudad": "Valdivia"
        },
        "fechaRegistro": "2025-12-13"
    },
    {
        "_id": ObjectId("68782d020f955f3ff6066616"),
        "identificador": "C007",
        "nombre": "Kai",
        "apellidos": "Hernández Alarcón",
        "direccion": {
            "calle": "Lautaro",
            "numero": "778",
            "ciudad": "Concepción"
        },
        "fechaRegistro": "2025-12-12"
    }
]

result = clientes_collection.insert_many(clientes_data)
print(f"✅ {len(result.inserted_ids)} clientes importados")

# ========================================
# 📦 DATOS REALES DE PRODUCTOS
# ========================================

print("📥 Importando productos...")

productos_data = [
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c93"),
        "nombre": "MacBook Air M2",
        "descripcion": "Portátil Apple con chip M2, 8GB RAM, 256GB SSD",
        "precio": 1200000,
        "stock": 15,
        "categoria": "Computadoras"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c94"),
        "nombre": "Cámara Fotográfica Canon EOS R6",
        "descripcion": "Cámara mirrorless profesional con sensor full-frame",
        "precio": 1800000,
        "stock": 8,
        "categoria": "Cámaras"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c95"),
        "nombre": "Cámara Fotográfica Sony Alpha A7 III",
        "descripcion": "Cámara mirrorless full-frame con excelente desempeño en video",
        "precio": 1750000,
        "stock": 10,
        "categoria": "Cámaras"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c96"),
        "nombre": "Laptop Asus Intel Core i7",
        "descripcion": "Laptop Asus con procesador Intel i7, 16GB RAM, 512GB SSD",
        "precio": 900000,
        "stock": 12,
        "categoria": "Computadoras"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c97"),
        "nombre": "PlayStation 5",
        "descripcion": "Consola de videojuegos de última generación con SSD ultra rápido",
        "precio": 550000,
        "stock": 5,
        "categoria": "Consolas"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c98"),
        "nombre": "iPhone 14 Pro",
        "descripcion": "Smartphone Apple con cámara triple y pantalla Super Retina XDR",
        "precio": 850000,
        "stock": 20,
        "categoria": "Smartphones"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c99"),
        "nombre": "Samsung Galaxy S22 Ultra",
        "descripcion": "Smartphone Samsung con cámara de 108MP y S-Pen incorporado",
        "precio": 800000,
        "stock": 18,
        "categoria": "Smartphones"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c9a"),
        "nombre": "Tablet iPad Pro 12.9\"",
        "descripcion": "Tablet Apple con chip M1 y pantalla Liquid Retina XDR",
        "precio": 950000,
        "stock": 10,
        "categoria": "Tablets"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c9b"),
        "nombre": "Apple Watch Series 8",
        "descripcion": "Smartwatch con monitoreo avanzado de salud y deporte",
        "precio": 300000,
        "stock": 25,
        "categoria": "Wearables"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c9c"),
        "nombre": "Auriculares Bose QuietComfort 45",
        "descripcion": "Auriculares inalámbricos con cancelación activa de ruido",
        "precio": 220000,
        "stock": 30,
        "categoria": "Audio"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c9d"),
        "nombre": "Monitor LG UltraFine 5K",
        "descripcion": "Monitor de alta resolución para profesionales del diseño",
        "precio": 1300000,
        "stock": 7,
        "categoria": "Monitores"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c9e"),
        "nombre": "Disco SSD Samsung 1TB",
        "descripcion": "Disco sólido de alta velocidad para almacenamiento",
        "precio": 120000,
        "stock": 40,
        "categoria": "Almacenamiento"
    },
    {
        "_id": ObjectId("687854a1519fb2b1e9e63c9f"),
        "nombre": "Teclado mecánico Logitech G Pro",
        "descripcion": "Teclado mecánico para gamers con retroiluminación RGB",
        "precio": 90000,
        "stock": 50,
        "categoria": "Accesorios"
    }
]

result = productos_collection.insert_many(productos_data)
print(f"✅ {len(result.inserted_ids)} productos importados")

# ========================================
# 🛒 DATOS REALES DE PEDIDOS
# ========================================

print("📥 Importando pedidos...")

pedidos_data = [
    {
        "_id": ObjectId("68787bd5d7295c52a76dab17"),
        "codigo_pedido": "P001",
        "clienteId": ObjectId("68782d020f955f3ff6066610"),
        "fecha_pedido": datetime(2025, 7, 17),
        "productos": [
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c93"),
                "nombre": "MacBook Air M2",
                "cantidad": 1,
                "precio_unitario": 1200000,
                "total_comprado": 1200000
            },
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c9c"),
                "nombre": "Auriculares Bose QuietComfort 45",
                "cantidad": 2,
                "precio_unitario": 220000,
                "total_comprado": 440000
            }
        ],
        "total_compra": 1640000,
        "metodo_pago": "Tarjeta de crédito"
    },
    {
        "_id": ObjectId("68787bd5d7295c52a76dab18"),
        "codigo_pedido": "P002",
        "clienteId": ObjectId("68782d020f955f3ff6066611"),
        "fecha_pedido": datetime(2025, 7, 17),
        "productos": [
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c9a"),
                "nombre": "Tablet iPad Pro 12.9\"",
                "cantidad": 1,
                "precio_unitario": 950000,
                "total_comprado": 950000
            },
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c9e"),
                "nombre": "Disco SSD Samsung 1TB",
                "cantidad": 2,
                "precio_unitario": 120000,
                "total_comprado": 240000
            }
        ],
        "total_compra": 1190000,
        "metodo_pago": "Transferencia"
    },
    {
        "_id": ObjectId("68787bd5d7295c52a76dab19"),
        "codigo_pedido": "P003",
        "clienteId": ObjectId("68782d020f955f3ff6066612"),
        "fecha_pedido": datetime(2025, 7, 17),
        "productos": [
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c97"),
                "nombre": "PlayStation 5",
                "cantidad": 1,
                "precio_unitario": 550000,
                "total_comprado": 550000
            },
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c9e"),
                "nombre": "Disco SSD Samsung 1TB",
                "cantidad": 1,
                "precio_unitario": 120000,
                "total_comprado": 120000
            }
        ],
        "total_compra": 670000,
        "metodo_pago": "Débito"
    },
    {
        "_id": ObjectId("68787bf7d7295c52a76dab1a"),
        "codigo_pedido": "P004",
        "clienteId": ObjectId("68782d020f955f3ff6066613"),
        "fecha_pedido": datetime(2025, 7, 17),
        "productos": [
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c99"),
                "nombre": "Samsung Galaxy S22 Ultra",
                "cantidad": 1,
                "precio_unitario": 800000,
                "total_comprado": 800000
            }
        ],
        "total_compra": 800000,
        "metodo_pago": "Tarjeta de débito"
    },
    {
        "_id": ObjectId("68787bf7d7295c52a76dab1b"),
        "codigo_pedido": "P005",
        "clienteId": ObjectId("68782d020f955f3ff6066614"),
        "fecha_pedido": datetime(2025, 7, 17),
        "productos": [
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c9d"),
                "nombre": "Monitor LG UltraFine 5K",
                "cantidad": 1,
                "precio_unitario": 1300000,
                "total_comprado": 1300000
            },
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c95"),
                "nombre": "Cámara Fotográfica Sony Alpha A7 III",
                "cantidad": 1,
                "precio_unitario": 1750000,
                "total_comprado": 1750000
            }
        ],
        "total_compra": 3050000,
        "metodo_pago": "Crédito en cuotas"
    },
    {
        "_id": ObjectId("68787bf7d7295c52a76dab1c"),
        "codigo_pedido": "P006",
        "clienteId": ObjectId("68782d020f955f3ff6066615"),
        "fecha_pedido": datetime(2025, 7, 17),
        "productos": [
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c9f"),
                "nombre": "Teclado mecánico Logitech G Pro",
                "cantidad": 2,
                "precio_unitario": 90000,
                "total_comprado": 180000
            },
            {
                "productoId": ObjectId("687854a1519fb2b1e9e63c98"),
                "nombre": "iPhone 14 Pro",
                "cantidad": 1,
                "precio_unitario": 850000,
                "total_comprado": 850000
            }
        ],
        "total_compra": 1030000,
        "metodo_pago": "Pago en efectivo"
    }
]

result = pedidos_collection.insert_many(pedidos_data)
print(f"✅ {len(result.inserted_ids)} pedidos importados")

# ========================================
# 📊 VERIFICACIÓN FINAL
# ========================================

print("\n" + "="*50)
print("📊 VERIFICACIÓN FINAL")
print("="*50)

clientes_count = clientes_collection.count_documents({})
productos_count = productos_collection.count_documents({})
pedidos_count = pedidos_collection.count_documents({})

print(f"👥 Clientes importados: {clientes_count}")
print(f"📦 Productos importados: {productos_count}")
print(f"🛒 Pedidos importados: {pedidos_count}")
print(f"📈 Total documentos: {clientes_count + productos_count + pedidos_count}")

print("\n🎉 ¡Importación completada exitosamente!")
print("🔄 Reinicia tu API (python app.py) para ver los cambios")
print("🌐 Visita: http://localhost:5001/debug")

# Cerrar conexión
client.close()