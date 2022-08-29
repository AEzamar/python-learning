def build_string(*args):
    return f"I like {args.join()}"

print(build_string("Cheese", "Milk", "Egg"))