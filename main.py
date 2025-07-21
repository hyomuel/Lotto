import asyncio, random

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from utils import get_data, get_all_numbers, json_data_path, preprocess_data

if __name__ == "__main__":
    print("아래의 숫자 입력\n1: 파일 다시 생성 후 번호 생성\n2: 있는 파일로 번호 생성\n3: 종료")

    while True:
        try:
            choice = int(input())
            if choice == 1:
                asyncio.run(get_data())

                all_num = get_all_numbers(json_data_path)
                X, y = preprocess_data(all_num)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                model = RandomForestClassifier(n_estimators=100, random_state=42)
                model.fit(X_train, y_train)

                last_draw = all_num.iloc[-1][['num1', 'num2', 'num3', 'num4', 'num5', 'num6']].values

                predictions = []

                for _ in range(6):
                    prediction = model.predict([last_draw])
                    predictions.append(prediction[0].tolist())

                    last_draw = random.sample(range(1, 46), 6)
                
                for i in predictions:
                    print(", ".join(map(str, i)))
            
            elif choice == 2:
                all_num = get_all_numbers(json_data_path)
                X, y = preprocess_data(all_num)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                model = RandomForestClassifier(n_estimators=100, random_state=42)
                model.fit(X_train, y_train)

                last_draw = all_num.iloc[-1][['num1', 'num2', 'num3', 'num4', 'num5', 'num6']].values

                predictions = []

                for _ in range(6):
                    prediction = model.predict([last_draw])
                    predictions.append(prediction[0].tolist())

                    last_draw = random.sample(range(1, 46), 6)
                
                for i in predictions:
                    print(", ".join(map(str, i)))

            elif choice == 3:
                break
            else:
                print("1, 2, 3 중에 선택해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")