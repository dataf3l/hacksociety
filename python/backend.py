# Sistema de recomendación con productos Financieros:
# Creado por Felipe Valdes, Omar Vergara,
# Juan Sebastian Salinas y Gonzalo Moreno
# Fecha 5 de agosto de 2017
# Importación de librerías
import tensorflow as tf
import numpy as np
import pandas as pd
# import zipfile
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# Extracción de datos
# with zipfile.ZipFile("./datasets/train_ver2.csv.zip") as z:
#   with z.open("train_ver2.csv") as f:
#      dataset = pd.read_csv(f, nrows=10000)
#      print(dataset.head())    # print the first 5 rows
dataset = pd.read_csv('../datasets/train3.csv', low_memory=False)
# Vamos identificar las columnas a usar
dataset.head()

dataset.columns[1:30]

input_train = dataset[['age',
                       'antiguedad',
                       'ind_actividad_cliente',
                       'es_hombre',
                       'es_cliente_activo',
                       'es_cliente_extranjero',

                       'provincia_MADRID',
                       'provincia_BARCELONA',
                       'provincia_PONTEVEDRA',
                       'provincia_SEVILLA',
                       'provincia_VALENCIA',

                       'provincia_MALAGA',
                       'provincia_MURCIA',
                       'provincia_ZARAGOZA',
                       'provincia_CADIZ',
                       'provincia_BADAJOZ',

                       'provincia_ALICANTE',
                       'provincia_CASTELLON',
                       'provincia_HUELVA',
                       'provincia_SALAMANCA',
                       'provincia_CORDOBA',

                       'provincia_TOLEDO',
                       'provincia_CACERES',
                       'provincia_VALLADOLID',
                       'provincia_LERIDA',
                       'provincia_CANTABRIA',

                       'provincia_OURENSE',
                       'provincia_LUGO',
                       'provincia_GIRONA',
                       'provincia_ALBACETE',
                       'provincia_CIUDAD_REAL',
                       'provincia_ASTURIAS',

                       'provincia_BURGOS',
                       'provincia_GRANADA',
                       'provincia_TARRAGONA',
                       'provincia_CUENCA',
                       'provincia_ZAMORA',
                       'provincia_NAVARRA',

                       'provincia_LEON',
                       'provincia_HUESCA',
                       'provincia_BIZKAIA',
                       'provincia_PALENCIA',
                       'provincia_JAEN',
                       'provincia_AVILA',

                       'provincia_SEGOVIA',
                       'provincia_ALMERIA',
                       'provincia_SANTA_CRUZ_DE_TENERIFE',
                       'provincia_GUADALAJARA',
                       'provincia_TERUEL',

                       'provincia_GIPUZKOA',
                       'provincia_SORIA',
                       'provincia_ALAVA',
                       'provincia_MELILLA',
                       'provincia_CEUTA',
                       'es_universitario',

                       'es_particular',
                       'es_top',
                       'renta']]
output_train = dataset[['ind_ahor_fin_ult1',
                        'ind_aval_fin_ult1',
                        'ind_cco_fin_ult1',

                        'ind_cder_fin_ult1',
                        'ind_cno_fin_ult1',
                        'ind_ctju_fin_ult1',

                        'ind_ctma_fin_ult1',
                        'ind_ctop_fin_ult1',
                        'ind_ctpp_fin_ult1',

                        'ind_deco_fin_ult1',
                        'ind_deme_fin_ult1',
                        'ind_dela_fin_ult1',

                        'ind_ecue_fin_ult1',
                        'ind_fond_fin_ult1',
                        'ind_hip_fin_ult1',

                        'ind_plan_fin_ult1',
                        'ind_pres_fin_ult1',
                        'ind_reca_fin_ult1',

                        'ind_tjcr_fin_ult1',
                        'ind_valo_fin_ult1',
                        'ind_viv_fin_ult1',

                        'ind_nomina_ult1',
                        'ind_nom_pens_ult1',
                        'ind_recibo_ult1' ]]
print(input_train.shape)


# Cantidad de nodos de la capa oculta
nodos_hidden = 250
# Es la matriz de inputs. Actualmetne solo hay seis
x = tf.placeholder(tf.float32, [None, 58], name='Inputs')
# 24 productos financieros a recomendar
y_ = tf.placeholder(tf.float32, [None, 24], name='Outputs')
# Matriz de pesos a encontrar. Esta es una variable y por eso no puede ser del tipo
# tf.placeholder, sino que tiene que ser tipo variable para que se entienda que esta es la variable a optimizar
W0 = tf.Variable(tf.constant(value=0.001, shape=[58, nodos_hidden]))
B0 = tf.Variable(tf.constant(value=0.001, shape=[1, nodos_hidden]), name='sesgo_Capa_Oculta1') # Está es la constante o sesgo del perceptron
# W0 = tf.Variable(tf.random_normal([58,24], stddev=0.01), name='Capa_Oculta1') 
# B0 = tf.Variable(tf.random_normal([1,24],stddev=0.01), name='sesgo_Capa_Oculta1') # Está es la constante o sesgo del perceptron

# Esta es la matriz de pesos de la segunda capa
W1 = tf.Variable(tf.constant(value=0.001, shape=[nodos_hidden, 24]), name='Capa_Oculta2')
# Está es la constante o sesgo del perceptron
B1 = tf.Variable(tf.constant(value=0.001, shape=[1, 24]), name='Sesgo_capa_oculta2')
# Vamos ahora a conectarla
capa_oculta = (tf.matmul(x, W0)+B0)
y = tf.nn.softmax(tf.matmul(capa_oculta, W1)+B1)
# y=tf.nn.softmax(tf.matmul(x,W0)+B0)
# Calculamos la función de costo
# cross_entropy= tf.reduce_sum(tf.nn.sigmoid_cross_entropy_with_logits(logits=y, labels=y_))
# softmax = tf.nn.softmax(logits)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])                   
type(cross_entropy)  # should be tensorflow.python.framework.ops.Tensor
# Ahora Vamos a crear la funcion a optimizar
optimizador = tf.train.GradientDescentOptimizer(1e-4).minimize(cross_entropy)
init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
writer = tf.summary.FileWriter('./hackaton_tensorboard', session.graph)
input_train.shape

train_error = []
test_error = []
for i in range(50):
    trainX, testX, trainY, testY = train_test_split(input_train, output_train, random_state=2)
    session.run(optimizador, feed_dict={x: trainX, y_: trainY})  # feed_dict es un diccionario con los datos de entrenamiento
    loss_train = session.run(cross_entropy, {x: trainX, y_: trainY})
    loss_test = session.run(cross_entropy, feed_dict={x: testX, y_: testY})
    train_error.append(loss_train)  # calcula el error sobre datos de training
    test_error.append(loss_test)  # calcula error en los datos de testing

print('Terminó el entrenamiento con Gradiente descendente Estocástico')
# Terminó el entrenamiento con Gradiente descendente Estocástico
train_error1 = np.squeeze(train_error, axis=(1,)).shape
test_error1 = np.squeeze(test_error, axis=(1,)).shape
eje = list(range(1, 151))
plt.plot((train_error), color='red')
# plt.plot(eje, test_error1, color='blue')
plt.title('Gráfica del error versus interacciones de aprendizaje')
plt.xlabel('Número del interacciones')
plt.ylabel('Error= Crossentropy')
plt.show()
