// Ejemplo de lista de productos (simulado)
            var products = [
                { nombre: "Teléfono", categoria: "electronica" },
                { nombre: "Camiseta", categoria: "ropa" },
                { nombre: "Lámpara", categoria: "hogar" },
                // Agrega más productos según sea necesario
            ];
        
            var input = document.getElementById('searchInput');
            var categoryFilter = document.getElementById('categoryFilter');
            var productList = document.getElementById('productList');
        
            // Función para mostrar los productos en la lista
            function showProducts(productsToShow) {
                productList.innerHTML = ''; // Limpiar la lista de productos
        
                productsToShow.forEach(function(product) {
                    var productElement = document.createElement('div');
                    productElement.textContent = product.nombre;
                    productList.appendChild(productElement);
                });
            }
        
            // Función para filtrar productos por categoría y término de búsqueda
            function filterProducts() {
                var searchTerm = input.value.toLowerCase();
                var selectedCategory = categoryFilter.value.toLowerCase();
        
                var filteredProducts = products.filter(function(product) {
                    var matchesSearchTerm = product.nombre.toLowerCase().includes(searchTerm);
                    var matchesCategory = selectedCategory === '' || product.categoria === selectedCategory;
                    return matchesSearchTerm && matchesCategory;
                });
        
                showProducts(filteredProducts);
            }
        
            // Event listeners para el campo de búsqueda y el filtro de categoría
            input.addEventListener('input', filterProducts);
            categoryFilter.addEventListener('change', filterProducts);
        
            // Mostrar todos los productos al cargar la página
            showProducts(products);