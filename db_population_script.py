# populate_items.py
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_food_management.settings.local")
django.setup()

from meals.models import Item

def populate_items():
    items_data = [
        {"id": "item_1", "name": "Basmati Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_2", "name": "Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_3", "name": "Orange Juice", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_4", "name": "Chicken Biryani", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_5", "name": "Blueberry Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_6", "name": "Lemonade", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_7", "name": "Brown Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_8", "name": "Banana Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_9", "name": "Iced Tea", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_10", "name": "Fried Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_11", "name": "Chocolate Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_12", "name": "Coffee", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_13", "name": "Steamed Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_14", "name": "Plain Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_15", "name": "Smoothie", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_16", "name": "Egg Fried Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_17", "name": "Apple Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_18", "name": "Mango Shake", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_19", "name": "Sushi Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_20", "name": "Cinnamon Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_21", "name": "Hot Chocolate", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_22", "name": "Bamboo Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_23", "name": "Strawberry Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_24", "name": "Ginger Tea", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_25", "name": "Jasmine Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_26", "name": "Maple Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_27", "name": "Milkshake", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
        {"id": "item_28", "name": "Wild Rice", "category": "RICE", "base_size_unit": "KG", "serving_size_unit": "LADDLE"},
        {"id": "item_29", "name": "Coconut Pancake", "category": "PANCAKE", "base_size_unit": "PISCES", "serving_size_unit": "PISCES"},
        {"id": "item_30", "name": "Herbal Tea", "category": "BEVERAGES", "base_size_unit": "LITTERS", "serving_size_unit": "GLASS"},
    ]

    for item_data in items_data:
        item, created = Item.objects.get_or_create(
            id=item_data["id"],
            defaults=item_data
        )
        if created:
            print(f"Created item: {item.name}")
        else:
            print(f"Item already exists: {item.name}")

if __name__ == "__main__":
    populate_items()
