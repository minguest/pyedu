from faker import Faker
fake= Faker("ko-KR")
test_data= [(fake.name(),fake.address()) for i in range(30)]
print(test_data)
