import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django_seed import Seed
from api.models import Employee

seeder = Seed.seeder()
positions = ['Junior', 'Middle', 'Senior', 'TeamLead', 'Director']

seeder.add_entity(Employee, 50000, {
    'position': lambda x: random.choice(positions)
})

seeder.execute()
