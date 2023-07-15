# aca tiene que ir la imagen que la buscaremops en el docker hub
FROM node:20-alpine3.17

# declaramos las variables de entorno para utilizar esta imagen
ENV PORT=8000
ENV NOMBRE=Rafael

# que la imagen almacene de manera mas facil los archivos del proyecto por al indicar la ubicacion del directorio de trabajo creara una carpeta en la imagen donde guardara todos los archivos copiados
WORKDIR /app

# ahoracopiamos los archivos locales a nuestra imagen
# el nombre del archivo o directorio | en donde o como se llamara en la imagen
COPY "package.json" "package.json"

# o tambien se puede copiar de la siguiente manera
# las primeras posiciones seran los archivos a copiar y la ultima posicion hacia donde se va a copiar, no es necesario volver a poner '/app' ya que ese sera el directorio por defecto
COPY ["package-lock.json", "./", "./"]

# se usa para instalar las librerias
# --production > sirve para solamente instalar las dependencias y no las de desarrollo
RUN npm install --production

CMD ["npm", "start"]