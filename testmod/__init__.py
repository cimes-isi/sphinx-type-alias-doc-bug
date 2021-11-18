from typing import Union

# type aliases:

#: Custom int type - this string isn't being documented (but should be), but the alias is
FieldInt = int

FieldInt2 = int
"""Custom int type 2 - this string isn't being documented (but should be), but the alias is"""

#: Custom Union type - this string is being documented, and so is the alias
FieldIntFloatUnion = Union[int, float]

FieldIntFloatUnion2 = Union[int, float]
"""Custom Union type 2 - this string is being documented, and so is the alias"""


# For comparison, non-type aliases:

#: foo - this string is being documented
documented_data_foo = 'foo'

documented_data_foo2 = 'foo'
"""foo2 - this string is being documented"""

# this is not being documented (nor should it be)
undocumented_data = 'foo'
