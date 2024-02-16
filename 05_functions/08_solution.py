def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="Bodhan", power= "lightening")
print_kwargs(name="Bodhan")
print_kwargs(name="Bodhan", power= "lightening", enemy = "God Butcher")