
from polls.models import Weather
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



class TrainTest:
    X = Weather.objects.all().values('airTemperature', 'humidity', 'precipitation', 'visibility','waveDirection',
                                     'waveHeight','windDirection', 'windSpeed','waterTemperature', 'cloudCover',
                                     'wavePeriod')
    y = Weather.objects.all().values('windWavePeriod')


    X_lista = []
    y_lista = []

    for i in X:
        X_lista.append(i)

    for i in y:
        y_lista.append(i)

    X_train, X_test, y_train, y_test = train_test_split(X_lista, y_lista,test_size=0.2)

    #clf = LinearRegression()

    #clf.fit(X_test,y_train)
    #clf.predict(X_test)

