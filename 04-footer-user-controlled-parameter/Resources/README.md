## how to find the flag

The vulnerability was found in the **footer of the home page**, where links to social media
platforms were present.

The destination of one of these links was controlled by a user-accessible value.
By modifying this value, it was possible to trigger unintended behavior and retrieve
the flag.

![footer](image.png)

This represents a security issue because user-controlled values must not be trusted
without server-side validation.

## how to avoid

This issue is caused by the application trusting a user-controlled value to build or
select an external resource.

Even if the change is performed in the browser, it changes the HTTP request sent to the
server. An attacker can craft and share a modified link so that any victim who opens it
will send the same manipulated request.

In real applications, this can lead to open redirects (phishing) or abuse of server-side
logic if the parameter is used to choose pages or actions.

To prevent this issue, avoid using raw request parameters as redirect URLs or action
selectors. Use a server-side mapping of trusted IDs to allowed destinations, and reject
any value outside the allow-list. For external redirects, restrict targets to trusted
domains and display an interstitial confirmation page to reduce phishing risk.
