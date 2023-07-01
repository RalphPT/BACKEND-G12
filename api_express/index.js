import express from 'express';
import Joi from 'joi';
import swaggerUI from 'swagger-ui-express';
//import swaggerDoc from './swagger.json'
//indicar el tipo de informacion que tendremos en nuestra importacion
import swaggerDoc from './swagger.json' assert {type:'json'};

const servidor = express();
const productos = [];
// Lo que nos llegará a este validador sera un objeto (JSON)
const productoValidator = Joi.object({
    nombre: Joi.string().required().min(5).message('La longitud minima es de 5'),
    precio: Joi.number().min(0).required(),
    descripcion: Joi.string().optional()
});

// indicar middlewares (intermediario)
//ahora nuestra aplicacion entendera y convertira la informacion entrante que sea de tipo JSON (application/json)
servidor.use(express.json())
//tipo form-urlencoded (application/form-url-encoded)
//servidor.use(express.urlencoded())

servidor.use('/docs', swaggerUI.serve, swaggerUI.setup(swaggerDoc))

servidor.get('/inicio', (req, res)=>{
    res.status(200).json({
        message: 'Bienvenido a mi API en Express'
    })
})

servidor.route('/productos'). post((req, res)=>{
    console.log(req.body);
    // const data = req.body es igual al de la línea de abajo
    const { body } = req;

    const validacion = productoValidator.validate(body);
    console.log(validacion);
    if(validacion.error){
        return res.status(400).json({
            message: 'Error al crear el producto',
            content: validacion.error.details
        })
    }
    else{
        productos.push(validacion.value)
        return res.status(201).json({
            message: 'Producto creado exitosamente'
        })
    }
}).get((req,res) => {
    res.json({
        content: productos
    })
})

servidor.route('/producto/:id').get((req, res) => {
    console.log(req.params)
    const { id } = req.params
    const resultado = productos[id]
    console.log(resultado)

    if(!resultado){
        return res.status(400).json({
            message: 'El producto no existe'
        })
    } else{

        return res.json({
            content: resultado
        })
    }
}).put((req,res) =>{
    const id = req.params.id
    const body = req.body
    const productoEncontrado = productos[id]

    if(!productoEncontrado){
        return res.status(404).json({
            message: 'El producto no existe'
        })
    }

    // si es que existe el producto
    const validacion = productoValidator.validate(body)

    if(validacion.error){
        return res.status(400).json({
            message: 'Error al actualizar el producto',
            content: validacion.error.details
        })
    } else{
        productos[id] = validacion.value //igual que validate_data en python

        return res.json({
            message: 'Producto actualizado exitosamente'
        })
    }
}).delete((req, res)=>{
    // primero validar si el producto existe
    // si no existe, retornar que el producto no existe
    // si existe cambiar su valor de la posicion a null
    // retornar el mensaje
    const { id } = req.params
    const productoEncontrado = productos[id]
    if (!productoEncontrado) {
        return res.status(404).json({
            message: 'El producto no existe'
        })
    }
    productos[id] = null
    return res.json({
        message: 'Producto eliminado exitosamente'
    })
});

//npm i --save-dev @types/express
servidor.listen(3000, () => {
    console.log('Servidor corriendo exitosamente')
});