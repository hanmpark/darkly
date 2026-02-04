## how to find the flag

The vulnerability was found in a page parameter that is used by the application to load
files dynamically.

By modifying the "page" parameter and injecting traversal sequences such as "../../",

```
http://10.11.200.34/index.php?page=../../../../../../../etc/passwd
```

it was possible to escape the intended directory and access arbitrary files on the
server, including "/etc/passwd", which led to the flag.

This represents a Path Traversal vulnerability, as user-controlled input is used directly
to access files without proper validation or restriction.

## how to avoid

This vulnerability occurs because the application relies on a user-controlled parameter
to determine which file should be loaded, without validating or sanitizing the provided
path.

An attacker can exploit this by using directory traversal sequences to navigate outside
of the intended directory and read sensitive system files.

In real-world applications, Path Traversal vulnerabilities can lead to the disclosure of
configuration files, credentials, or other sensitive information.

To prevent this issue, applications should restrict file access to a specific directory,
normalize and validate paths before use, and rely on strict allow-lists instead of direct
user input.
