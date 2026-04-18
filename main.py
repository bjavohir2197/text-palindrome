def is_palindrom(matn):
    matn = ''.join(e for e in matn if e.isalnum()).lower()
    return matn == matn[::-1]

print(is_palindrom("A man, a plan, a canal: Panama"))  # True
print(is_palindrom("Not a palindrome"))  # False
```

```python
def is_palindrom(matn):
    matn = ''.join(e for e in matn if e.isalnum()).lower()
    return matn == matn[::-1]

print(is_palindrom("Was it a car or a cat I saw"))  # True
print(is_palindrom("No 'x' in Nixon"))  # True
print(is_palindrom("Not a palindrome"))  # False
