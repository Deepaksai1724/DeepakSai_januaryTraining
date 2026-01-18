#Question3
def save_error(error, errors=None):
    if errors is None:
        errors = []
    errors.append(error)
    return errors

print(save_error("Invalid Input"))
print(save_error("unrecnognised string"))
print(save_error("E3"))
