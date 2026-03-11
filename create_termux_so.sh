#!/bin/bash

# 01_make_python_so.sh
# ORDEN: 
# 1. Eliminar todos los __init__.py
# 2. Mover main.py (backup)
# 3. Compilar a .so
# 4. Eliminar todos los .py
# 5. Restaurar main.py
# 6. Crear __init__.py en todas las carpetas

echo "🔒 Iniciando compilación..."

# PASO 1: Eliminar todos los __init__.py
echo "🗑️ Eliminando todos los __init__.py..."
find src -name "__init__.py" -delete

# PASO 2: Mover main.py (backup)
echo "📦 Respaldando main.py..."
cp src/main.py src/main.py.backup

# PASO 3: Compilar a .so
echo "🔨 Compilando a .so..."
cythonize -i src/*.py -X language_level=3
cythonize -i src/**/*.py -X language_level=3
cythonize -i src/**/**/*.py -X language_level=3
cythonize -i src/**/**/**/*.py -X language_level=3

echo "🗑️ Eliminando todos el main.so"
rm src/main.cpython-313-aarch64-linux-android.so

# PASO 4: Eliminar todos los .py
# echo "🗑️ Eliminando todos los .py..."
# find src -name "*.py" ! -name "main.py.backup" -delete

# PASO 5: Restaurar main.py
echo "📦 Restaurando main.py..."
mv src/main.py.backup src/main.py

# PASO 6: Crear __init__.py en todas las carpetas
echo "📁 Creando __init__.py en todas las carpetas..."
find src -type d -exec touch {}/__init__.py \;

# Limpieza final
echo "🧹 Limpiando archivos temporales..."
find src -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find src -name "__cache__" -type d -exec rm -rf {} + 2>/dev/null
find src -name "build" -type d -exec rm -rf {} + 2>/dev/null
find src -name "*.c" -delete 2>/dev/null

echo "✅ Compilación completada"
echo "📊 Archivos .so generados:"
find src -name "*.so" | sort
