def build_string(*args):
    return f"I like {', '.join(args)}"

print(build_string("Cheese", "Milk", "Eggs"))