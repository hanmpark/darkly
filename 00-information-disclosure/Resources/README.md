## how to find the flag

The vulnerability was found on the **password recovery page**.

No visible input field was present on the page, but by inspecting the HTML source, a
hidden input field containing a sensitive email address was discovered.

This value could be modified directly by the user and submitted to the server without
any server-side verification. By changing this hidden field, it was possible to retrieve
the flag.

![hidden email field exposed in the page source](image.png)

This represents a security issue because hidden inputs are controlled by the client and
must never be trusted to handle sensitive information.

## how to avoid

This vulnerability is caused by an incorrect configuration of the web application,
which allows sensitive information to be exposed publicly without access control.

Even though no active exploitation technique is required, information disclosure is
dangerous because attackers can gather valuable data passively. Such information can
be used to understand the application's structure, identify entry points, or prepare
more complex attacks.

In a real-world environment, this type of issue is often the result of forgotten files,
debug resources, or misconfigured web servers.

To prevent this issue, never expose sensitive values (emails, tokens, internal paths)
in client-visible HTML or publicly reachable files. Keep recovery logic server-side,
protect related endpoints with authentication and authorization, and separate public
assets from private data. Add deployment checks (secret scanning and file audits) to
catch debug artifacts before they reach production.
