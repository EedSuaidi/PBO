import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier


while True:
    print("==================== Analisi Data ====================")

    nama_file = input("Masukkan Nama File Beserta Formatnya : ")

    data = pd.read_excel(nama_file)
    for i in data.columns:
        data[i].fillna(data[i].mode()[0], inplace=True)

    encoder = LabelEncoder()

    data["Air Quality"] = encoder.fit_transform(data[i])

    feature = data.iloc[:, :-1].values
    label = data.iloc[:, -1].values

    scaler = MinMaxScaler()
    feature = scaler.fit_transform(feature)

    # Splitting Data Train and Data Test

    random_state = int(input("Masukkan Random State : "))
    train_size = float(input("Masukkan Train Size : "))

    x_train, x_test, y_train, y_test = train_test_split(
        feature, label, random_state=random_state, train_size=train_size
    )
    print(f"Data Train : {len(x_train)}")
    print(f"Data Test : {len(x_test)}")

    print("Pilih Algoritma : ")
    print("1. Naive Bayes")
    print("2. KNN")
    print("3. Neural Network")
    print("0. Keluar")
    menu = input("Masukkan Pilihan [0-3]: ")

    if menu == "1":
        model = GaussianNB()
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, pred)
        report = classification_report(y_test, pred)

        print("")
        print("Model: Naive Bayes\n")
        print(report)
        print("")

    elif menu == "2":
        model = KNeighborsClassifier()
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, pred)
        report = classification_report(y_test, pred)

        print("")
        print("Model: KNN\n")
        print(report)
        print("")

    elif menu == "3":
        model = MLPClassifier()
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, pred)
        report = classification_report(y_test, pred)

        print("")
        print("Model: Neural Network\n")
        print(report)
        print("")

    elif menu == "0":
        break
