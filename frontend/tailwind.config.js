/** 
 * Configuración de Tailwind CSS.
 * @type {import('tailwindcss').Config}
 */
module.exports = {
  // Rutas de contenido para buscar archivos HTML
  content: [
    './templates/**/*.html',
    './templates/*.html',
    './**/templates/**/*.html',
    './**/templates/*.html',
  ],

  // Configuración extendida del tema
  theme: {
    extend: {
      colors: {
        // Define el color azul aqua
        'blue-aqua': '#00FFFF',
      },
      // Agrega más ajustes de tema aquí si es necesario
    },
  },

  // Plugins adicionales (si los hay)
  plugins: [],
};

