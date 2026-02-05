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

To prevent this issue, do not trust the MIME type sent by the browser. Validate uploads **on the server** using several checks:

- **Check the file signature (magic bytes)** to confirm it is really a JPEG.
- **Allow only specific extensions** (e.g., `.jpg`, `.jpeg`) and reject everything else.
- **Detect the MIME type server-side** (MIME sniffing) instead of using the client-provided value.

Also reduce the impact of a successful upload:

- **Store uploaded files outside web/executable directories**.
- **Rename files to random names** (do not keep the original filename).
- **Serve uploads as static files only** (no script execution permissions).

Optional hardening:

- Add **size limits**, **type limits**, and **malware scanning** to reduce abuse and DoS (Denial of Service) risk.
