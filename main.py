from data_generator import DataGenerator
from data_packer import DataPacker

# Создаем генератор данных
generator = DataGenerator()

# Генерируем данные
data = generator.generate_data()

# Создаем упаковщик данных
packer = DataPacker(data)

# Упаковываем данные в архив zip
packer.pack_data('data.zip')

# Разбиваем данные на части и упаковываем их в архив zip
packer.split_and_pack_data(1024 * 1024, 'output')