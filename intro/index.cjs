// CommonJS
// Cuando el archivo tenga la extension cjs indicara que este esta escrito en commonJS
const {saludar} = require('./funcionabilidad.cjs')

console.log('Hola mundo')

const resultado = saludar()

console.log(resultado)