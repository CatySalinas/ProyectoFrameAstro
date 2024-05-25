/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './templates/*.html',
    './**/templates/**/*.html',
    './**/templates/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'blue-aqua': '#00FFFF', // Define el color azul aqua
      },
    },
  },
  plugins: [],
}

