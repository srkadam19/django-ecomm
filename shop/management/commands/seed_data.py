from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shop.models import Category, Product


class Command(BaseCommand):
    help = 'Seed the database with sample e-commerce data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Smartphones, laptops, gadgets and more'},
            {'name': 'Clothing', 'description': 'Fashion for men and women'},
            {'name': 'Books', 'description': 'Bestsellers, fiction and non-fiction'},
            {'name': 'Home & Kitchen', 'description': 'Everything for your home'},
            {'name': 'Sports', 'description': 'Sports equipment and activewear'},
        ]

        categories = {}
        for cat_data in categories_data:
            cat, _ = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat.name] = cat

        # Create products
        products_data = [
            {'category': 'Electronics', 'name': 'iPhone 15 Pro', 'description': 'Latest Apple smartphone with A17 Pro chip, 48MP camera system, and titanium design. Features Dynamic Island and always-on display.', 'price': 999.99, 'stock': 50},
            {'category': 'Electronics', 'name': 'Samsung Galaxy S24', 'description': 'Flagship Android phone with Galaxy AI features, 200MP camera, and Snapdragon 8 Gen 3 processor.', 'price': 849.99, 'stock': 35},
            {'category': 'Electronics', 'name': 'MacBook Air M3', 'description': '13-inch laptop with Apple M3 chip, 18-hour battery life, and Liquid Retina display. Ultra-thin and lightweight.', 'price': 1099.00, 'stock': 20},
            {'category': 'Electronics', 'name': 'Sony WH-1000XM5', 'description': 'Premium wireless noise-cancelling headphones with 30-hour battery life and exceptional sound quality.', 'price': 349.99, 'stock': 100},
            {'category': 'Electronics', 'name': 'iPad Pro 12.9"', 'description': 'Powerful tablet with M2 chip, Liquid Retina XDR display, and Apple Pencil support.', 'price': 1099.99, 'stock': 25},
            {'category': 'Clothing', 'name': 'Classic Denim Jacket', 'description': 'Timeless denim jacket made from premium cotton. Perfect for layering in any season.', 'price': 79.99, 'stock': 200},
            {'category': 'Clothing', 'name': 'Running Sneakers Pro', 'description': 'Lightweight running shoes with responsive cushioning and breathable mesh upper.', 'price': 129.99, 'stock': 150},
            {'category': 'Clothing', 'name': 'Wool Blend Overcoat', 'description': 'Elegant overcoat crafted from premium wool blend. Ideal for formal and casual occasions.', 'price': 199.99, 'stock': 60},
            {'category': 'Clothing', 'name': 'Cotton Polo Shirt', 'description': 'Classic fit polo shirt in soft pique cotton. Available in multiple colors.', 'price': 45.00, 'stock': 300},
            {'category': 'Books', 'name': 'Python Crash Course', 'description': 'A hands-on, project-based introduction to programming in Python. Perfect for beginners.', 'price': 39.99, 'stock': 500},
            {'category': 'Books', 'name': 'Clean Code', 'description': 'A handbook of agile software craftsmanship by Robert C. Martin. Essential reading for developers.', 'price': 34.99, 'stock': 300},
            {'category': 'Books', 'name': 'Atomic Habits', 'description': 'An easy and proven way to build good habits and break bad ones by James Clear.', 'price': 16.99, 'stock': 400},
            {'category': 'Home & Kitchen', 'name': 'Instant Pot Duo', 'description': '7-in-1 electric pressure cooker, slow cooker, rice cooker, steamer, and more. 6-quart capacity.', 'price': 89.99, 'stock': 75},
            {'category': 'Home & Kitchen', 'name': 'Robot Vacuum Cleaner', 'description': 'Smart robot vacuum with laser navigation, 5000Pa suction, and app control.', 'price': 299.99, 'stock': 40},
            {'category': 'Home & Kitchen', 'name': 'Coffee Maker Deluxe', 'description': '12-cup programmable coffee maker with built-in grinder and thermal carafe.', 'price': 149.99, 'stock': 90},
            {'category': 'Sports', 'name': 'Yoga Mat Premium', 'description': 'Extra thick non-slip yoga mat with alignment lines. Eco-friendly TPE material.', 'price': 35.99, 'stock': 200},
            {'category': 'Sports', 'name': 'Adjustable Dumbbell Set', 'description': 'Space-saving adjustable dumbbells from 5 to 52.5 lbs. Quick-change weight system.', 'price': 349.00, 'stock': 30},
            {'category': 'Sports', 'name': 'Fitness Tracker Band', 'description': 'Waterproof fitness tracker with heart rate monitor, sleep tracking, and 14-day battery.', 'price': 49.99, 'stock': 250},
        ]

        for prod_data in products_data:
            Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'category': categories[prod_data['category']],
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'stock': prod_data['stock'],
                }
            )

        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin / admin123'))

        self.stdout.write(self.style.SUCCESS(
            f'Seeded {Category.objects.count()} categories and {Product.objects.count()} products'
        ))
