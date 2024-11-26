import inspect
from locators import locators

# Collect all locators from locators.py like {friendly_name: selector}
def collect_all_locators():

    element_mapping = {}
    
    # Находим все классы локаторов в модуле
    locator_classes = inspect.getmembers(locators, 
        lambda member: inspect.isclass(member) and member.__module__ == locators.__name__)
    
    # Собираем локаторы из всех найденных классов
    for _, locator_class in locator_classes:
        for attr_name, value in vars(locator_class).items():
            if not attr_name.startswith('__'):  # Пропускаем магические методы
                friendly_name, selector = value
                element_mapping[friendly_name] = selector
                
    return element_mapping 