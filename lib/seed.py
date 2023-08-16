from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Category, Entry, Tag, engine
from faker import Faker

# creating a session
Session = sessionmaker(bind=engine)
session = Session()
# clearing any existing data in the database
session.query(Entry).delete()
session.query(Category).delete()
session.query(User).delete()
session.commit()

# creating a faker instance
faker = Faker()

# generating 10 sample users to fill the database
users = []

for i in range(10):
    user = User(
        username=faker.user_name(), password=faker.password(), email=faker.email()
    )
    users.append(user)

    users.append(user)

session.add_all(users)
session.commit()

# generating 10 sample categories
categories = []

for _ in range(10):
    category = Category(name=faker.word(), user=faker.random_element(users))
    categories.append(category)

session.add_all(categories)
session.commit()

# Generate sample tags
tags = []
for _ in range(10):
    tag = Tag(name=faker.word())
    tags.append(tag)

session.add_all(tags)
session.commit()

# generating 10 sample entries for a user
entries = []
for _ in range(10):
    entry = Entry(
        website=faker.url(),
        username=faker.user_name(),
        password=faker.password(),
        notes=faker.sentence(),
        user=faker.random_element(users),
        category=faker.random_element(categories),
        created_at=faker.date_time_this_year(),
        updated_at=faker.date_time_this_year(),
    )
    num_tags = faker.random_int(min=1, max=3)
    entry.tags = faker.random_elements(tags, unique=True, length=num_tags)

    entries.append(entry)

session.add_all(entries)
session.commit()

print("Sample data has been seeded.")
