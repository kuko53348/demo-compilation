echo "🧹 Limpiando archivos temporales..."
find src -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find src -name "__cache__" -type d -exec rm -rf {} + 2>/dev/null
find src -name "build" -type d -exec rm -rf {} + 2>/dev/null
find src -name "*.c" -delete 2>/dev/null
find src -name "*.so" -delete 2>/dev/null
