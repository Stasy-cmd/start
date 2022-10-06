from collections.abc import Generator, Iterator, Iterable
from types import GeneratorType

print(issubclass(GeneratorType,Iterator))
print(issubclass(Generator, Iterator))
print(issubclass(Iterator, GeneratorType))
print(issubclass(Iterator,Iterable))
