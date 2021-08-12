### Example usage
Let's assume that we have a file named input_1
```
aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbsome data 11      some data 2Y
aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbsome data 12      some data 2Y
aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbsome data 13      some data 2N
```
Then code that will map data into proper places will look like that

```python
from kigo.etl.engine.mapping import bind_id


@bind_id(object_id='input_1')
class SomeClass:
    data_1 = '[31:43]'
    data_2 = '[49:61]'
```
What we expect is to have 3 instances of classes SomeClass where data_1 and data_2 will have proper ranges of data. For example first instance will look like:
```
data_1 -> 'some data 11'
data_2 -> 'some data 2Y'
```