## how to find the flag

The vulnerability was found on the **image upload page**.

The application restricts uploads to JPEG images and blocks files based on their
extension. Attempts to upload PHP files directly were rejected by the server.

However, it was observed that the server relies on the client-provided MIME type to
validate the uploaded file. By sending a PHP file while declaring its MIME type as
"image/jpeg" in the upload request, the server accepted the file.

```bash
curl -X POST "http://x.x.x.x/?page=upload" -F "Upload=Upload" -F "uploaded=@script.php;type=image/jpeg"
```

This demonstrates that the file validation is based solely on user-controlled metadata,
which allows an attacker to bypass the upload restrictions.

## how to avoid

This vulnerability occurs because the application trusts the MIME type provided by the
client during file uploads.

MIME types can be easily forged and should never be used alone to determine whether a
file is safe. An attacker can upload arbitrary files by disguising them as allowed file
types.

In real-world applications, this can lead to severe issues such as remote code execution
or stored XSS if uploaded files are executed or interpreted by the server.

To prevent this issue, file uploads must be validated server-side using multiple checks,
including file signature (magic bytes), strict extension validation, and storage of
uploaded files outside of executable directories.
