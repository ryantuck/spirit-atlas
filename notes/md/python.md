# Python

## [[regex]] matching

https://www.w3schools.com/python/python_regex.asp

```python
some_text = "blah blah"
re.match(r'blah', some_text)
```

Alternatively, find all matches:

```
re.findall(r'blah', 'blah blah')
```

## Etc

Try typing.

The following is good for debugging apparently:

```python
import pdp
pdp.set_trace()
```

Notes on packaging: https://packaging.python.org/discussions/install-requires-vs-requirements/

This gives you access to python docstrings

```python
help(requests.get)
```

[59 ways to write better python](https://github.com/SigmaQuan/Better-Python-59-Ways)
