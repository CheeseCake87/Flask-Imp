# generate_alphanumeric_validator

```python
from flask_imp.auth import generate_alphanumeric_validator
```

```python
generate_alphanumeric_validator(length: int = 8) -> str
```

---

Generates a random alphanumeric string of the given length.

(letters are capitalized)

*Example:*

```python
generate_alphanumeric_validator(8)  # >>> 'A1B2C3D4'
```

