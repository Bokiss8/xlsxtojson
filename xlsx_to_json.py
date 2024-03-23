import pandas as pd
import traceback


def xlsx_to_json(xlsx_file_path, output_json_path):
    try:
        # Чтение данных из файла XLSX
        df = pd.read_excel(xlsx_file_path)

        # Вывод данных времени перед преобразованием в JSON
        # print(df['Pasp_dat'])

        # Преобразование данных в JSON с использованием кодировки UTF-8 и force_ascii=False

        df.to_json(output_json_path, orient='records', indent=4, force_ascii=False)

        print("Conversion completed successfully!")

    except Exception as e:
        traceback.print_exc()  # Вывод трассировки стека для отслеживания ошибки
        print(f"Error converting XLSX to JSON: {e}")


# Укажите путь к файлу XLSX и путь для сохранения JSON файла
xlsx_file_path = 'T_Zahvor.xlsx'
output_json_path = 'output.json'

# Конвертируем XLSX в JSON
xlsx_to_json(xlsx_file_path, output_json_path)
