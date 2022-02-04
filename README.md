# ML_Python_Selector_Caracteristicas_Relevantes
Código necesario para seleccionar las características más relevantes de un conjunto de datos según una función estadística


## CONTENIDO:

### Selector de características más relevantes (SelectKBest)

Se muestra el código necesario para seleccionar las características más relevantes de un conjunto de datos dependiendo de un método de selección según una función estadística. En este caso se muestra un ejemplo para Clasificación con la función _chi2_ (que utiliza la prueba _chi-cuadrado_), que es más adecuada para Clasificación. Para tareas de Regresión sería más adecuada la función _f_regression_ (que utiliza el _estadístico F_). En este ejemplo se muestra cómo de un conjunto que contiene 64 características, nos quedamos con las 20 características más relevantes según la prueba _chi-cuadrado_.



##

_Nota: Todas las variables mostradas con referencia a las letras X o y (X, y, X_test, y_test, ytest, ypred, etc.) hacen referencia al conjunto de datos utilizado, donde los contenidos con la letra X son el conjunto de características disponible y con la letra y son la característica a predecir._
