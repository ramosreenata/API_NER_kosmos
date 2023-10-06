# API_NER_kosmos
Esta es una API de Flask que realiza reconocimiento de entidades nombradas con Python
## Instrucciones

### 1. Requerimientos
Asegurate de contar con las librerias de Spacy y Flask, puedes descargarlas de requirements.txt:
```bash
  pip install -r requirements.txt
```

Además hay que descargar el modelo en español
```bash
  python -m spacy download es_core_news_sm
```

### 2. Clonar repositorio
Lo primero que tenemos que hacer es clonar el repositorio a nuestra computadora
```bash
   git clone https://github.com/ramosreenata/
```

### 3. Correr la API
Después de clonar el repo, en el prompt vamos al directorio en donde lo descargamos y corremos la API:
```bash
   python API_NER.py
```
Para probar mi código yo use Postman, se puede descargar de [aquí](https://www.postman.com/downloads/)

- Hacemos un nuevo request de tipo POST
- Usamos el URL 'http://127.0.0.1:5000/ner'
- En la sección Body, selecionamos "raw" y escogemos JSON, ahí colocamos el JSON para el reconocimiento de entidades, por ejemplo:
```bash
{
"oraciones": [
 "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
 "San Francisco considera prohibir los robots de entrega en la acera."
 ]
}
```
