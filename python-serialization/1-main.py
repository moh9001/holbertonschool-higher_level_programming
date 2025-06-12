#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize to file
obj.serialize("object.pkl")

# Deserialize into a new object
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
if new_obj:
    new_obj.display()
else:
    print("Deserialization failed.")
