## how to find the flag

The vulnerability was found on the **survey page**, where a select field restricts the user
to predefined values in the browser.

By manually modifying the value of this field, it was possible to submit an unexpected
value that was accepted by the server and resulted in the flag being returned.

```html
<option value="modify the value here">1</option>
```

![client-side select value modified before submission](image.png)

This represents a security issue because client-side restrictions can be bypassed and
must not be trusted without server-side validation.

## how to avoid

This vulnerability occurs because the application relies on client-side controls, such
as select fields, to restrict user input.

An attacker can easily bypass these controls by modifying the request before it is sent
to the server. If the server does not validate the received value, it may process invalid
or malicious input.

In real-world applications, this can lead to logic bypasses, unauthorized actions, or
unexpected behavior.

To prevent this issue, all user input must be validated server-side, even if it appears
restricted in the user interface.
