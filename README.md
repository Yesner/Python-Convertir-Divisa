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



![Image text](https://github.com/Yesner/Python-Convertir-Divisa/blob/e7d7714f6d655f58ecd8c6524175a2b4ddbdb3cc/assets/Container.png)


![Image text](https://github.com/Yesner/Python-Convertir-Divisa/blob/e7d7714f6d655f58ecd8c6524175a2b4ddbdb3cc/assets/result.png)
