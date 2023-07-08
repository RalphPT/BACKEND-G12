import express from 'express'
import { usuarioRouter } from './routes/usuario.routes.js'
import { direccionRouter } from './routes/direccion.routes.js'
import { productoRouter } from './routes/producto.routes.js'
const servidor = express()

// Sirve para que el servidor entienda los json provenientes del cliente
servidor.use(express.json())

// Nullish coalescing operator
const puerto = process.env.PORT ?? 3000

// Agregar mis rutas
servidor.use(usuarioRouter)
servidor.use(direccionRouter)
servidor.use(productoRouter)

servidor.listen(process.env.PORT, () =>{
    console.log(`Servidor corriendo exitosamente en el puerto ${puerto}`)
})