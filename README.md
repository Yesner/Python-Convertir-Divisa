# Python-Convertir-Divisa

Con este pequeño proyecto puedes hacer la conversión de divisa de las siguientes monedas:
- Cordoba a dolar
- Dolar a cordoba

Las instrucciones para que el proyecto te funcione son las siguientes:

``` 
    git clone
    env/Scripts/activate
    py install -r requirements.txt
    py convert.py
    
 ```

 Si decides crear la imagen en Docker con la finalidad de tener un espacio aislado para correr la aplicacion debes de seguir las siguientes instrucciones:

 ```
    docker-compose build
    docker-compose ps
    docker-compose up -d
    docker-compose exec app-divisa bash
    ls -l
    python convert.py

 ```

 El resultado al final, sera el siguiente:



 https://github.com/Yesner/Python-Convertir-Divisa/blob/68fcbb6302455e73924e3f74febe30d3bcc7c7f0/assets/result.png




https://github.com/Yesner/Python-Convertir-Divisa/blob/e84a6ac7653de47a4247f4fe585e4ca11bdfc407/assets/Container.png