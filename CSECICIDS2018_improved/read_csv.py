import os
import pandas as pd

EXTRACT_NUM = 1000

daily_csv = ['Wednesday-14-02-2018.csv', 'Friday-16-02-2018.csv', 'Tuesday-20-02-2018.csv', 'Wednesday-21-02-2018.csv', 'Thursday-22-02-2018.csv', 'Friday-23-02-2018.csv', 'Wednesday-28-02-2018.csv', 'Thursday-01-03-2018.csv', 'Thursday-15-02-2018.csv', 'Friday-02-03-2018.csv']

RESULT_DF = None

def extract_csv(file_name):
    global RESULT_DF
    df = pd.read_csv(os.path.join("ori_csv", file_name))

    # print("df.head:")
    # print(df.head())
    # print("\ndf.info:")
    # print(df.info())
    # print("\ndf.describe:")
    # print(df.describe())

    benign_data = df[df["Label"] == "BENIGN"]
    print(f"\tbenign data: {len(benign_data)} rows", end=", ")
    benign_data = benign_data.head(EXTRACT_NUM)
    # print(benign_500)
    malicious_data = df[df["Label"]!="BENIGN"]
    print(f"malicious_data: {len(malicious_data)}", end="... ")
    malicious_data = malicious_data.head(EXTRACT_NUM)
    # print(malicious_500.iloc[:, -2:])

    if (RESULT_DF is None):
        RESULT_DF = pd.concat([benign_data, malicious_data], ignore_index=True)
    else:
        RESULT_DF = pd.concat([RESULT_DF, benign_data, malicious_data], ignore_index=True)


for csv_file in daily_csv:
    print(f"{csv_file} extracting...", end=" ", flush=True)
    extract_csv(csv_file)
    print("DONE!")
RESULT_DF.to_csv("extracted_result.csv")
print("EXTRACTION DONE!!!")