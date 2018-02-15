# Generated by Django 2.0.1 on 2018-02-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0016_auto_20180211_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(choices=[('Abyssinian', 'Abyssinian'), ('Aegean', 'Aegean'), ('American Curl', 'American Curl'), ('American Bobtail', 'American Bobtail'), ('American Shorthair', 'American Shorthair'), ('American Wirehair', 'American Wirehair'), ('Arabian Mau', 'Arabian Mau'), ('Australian Mist', 'Australian Mist'), ('Asian', 'Asian'), ('Asian Semi-longhair', 'Asian Semi-longhair'), ('Balinese', 'Balinese'), ('Bambino', 'Bambino'), ('Bengal', 'Bengal'), ('Birman', 'Birman'), ('Bombay', 'Bombay'), ('Brazilian Shorthair', 'Brazilian Shorthair'), ('British Longhair', 'British Longhair'), ('British Shorthair', 'British Shorthair'), ('British Longhair', 'British Longhair'), ('Burmese', 'Burmese'), ('Burmilla', 'Burmilla'), ('California Spangled', 'California Spangled'), ('Chantilly-Tiffany', 'Chantilly-Tiffany'), ('Chartreux', 'Chartreux'), ('Chausie', 'Chausie'), ('Cheetoh', 'Cheetoh'), ('Colorpoint Shorthair', 'Colorpoint Shorthair'), ('Cornish Rex', 'Cornish Rex'), ('Cymric', 'Cymric'), ('Cyprus', 'Cyprus'), ('Devon Rex', 'Devon Rex'), ('Donskoy', 'Donskoy'), ('Dragon Li', 'Dragon Li'), ('Dwarf', 'Dwarf'), ('Egyptian Mau', 'Egyptian Mau'), ('European Shorthair', 'European Shorthair'), ('Exotic Shorthair', 'Exotic Shorthair'), ('Foldex', 'Foldex'), ('German Rex', 'German Rex'), ('Havana Brown', 'Havana Brown'), ('Highlander', 'Highlander'), ('Himalayan', 'Himalayan'), ('Japanese Bobtail', 'Japanese Bobtail'), ('Javanese', 'Javanese'), ('Karelian Bobtail', 'Karelian Bobtail'), ('Khao Manee', 'Khao Manee'), ('Korat', 'Korat'), ('Korean Bobtail', 'Korean Bobtail'), ('Korn Ja', 'Korn Ja'), ('Kurilian Bobtail', 'Kurilian Bobtail'), ('LaPerm', 'LaPerm'), ('Lykoi', 'Lykoi'), ('Maine Coon', 'Maine Coon'), ('Manx', 'Manx'), ('Mekong Bobtail', 'Mekong Bobtail'), ('Minskin', 'Minskin'), ('Munchkin', 'Munchkin'), ('Nebelung', 'Nebelung'), ('Napoleon', 'Napoleon'), ('Norwegian Forest', 'Norwegian Forest'), ('Ocicat', 'Ocicat'), ('Ojos Azules', 'Ojos Azules'), ('Oregon Rex', 'Oregon Rex'), ('Oriental Bicolor', 'Oriental Bicolor'), ('Oriental Shorthair', 'Oriental Shorthair'), ('Oriental Longhair', 'Oriental Longhair'), ('PerFold', 'PerFold'), ('Persian', 'Persian'), ('Peterbald', 'Peterbald'), ('Pixie-bob', 'Pixie-bob'), ('Raas', 'Raas'), ('Ragamuffin', 'Ragamuffin'), ('Ragdoll', 'Ragdoll'), ('Russian Blue', 'Russian Blue'), ('Russian Black', 'Russian Black'), ('Russian Tabby', 'Russian Tabby'), ('Russian White', 'Russian White'), ('Sam Sawet', 'Sam Sawet'), ('Savannah', 'Savannah'), ('Scottish Fold', 'Scottish Fold'), ('Selkirk Rex', 'Selkirk Rex'), ('Serengeti', 'Serengeti'), ('Serrade petit', 'Serrade petit'), ('Siamese', 'Siamese'), ('Siberian', 'Siberian'), ('Singapura', 'Singapura'), ('Snowshoe', 'Snowshoe'), ('Sokoke', 'Sokoke'), ('Somali', 'Somali'), ('Sphynx', 'Sphynx'), ('Suphalak', 'Suphalak'), ('Thai', 'Thai'), ('Thai Lilac', 'Thai Lilac'), ('Tonkinese', 'Tonkinese'), ('Toyger', 'Toyger'), ('Turkish Angora', 'Turkish Angora'), ('Turkish Van', 'Turkish Van'), ('Ukrainian Levkoy', 'Ukrainian Levkoy'), ('Other', 'Other')], default='American Shorthair', max_length=30),
        ),
        migrations.AlterField(
            model_name='cat',
            name='profilepic',
            field=models.URLField(blank=True, help_text='Optional. This will be clipped to a 1:1 aspect ratio.', null=True, verbose_name='profile picture'),
        ),
    ]