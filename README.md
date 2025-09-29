# Werkzeug/Flask Session Cookie Decoder

This is a small Python script to **decode Flask/Werkzeug session cookies**.  
Flask stores session data in a signed cookie using [itsdangerous](https://itsdangerous.palletsprojects.com/).  
The data is **signed but not encrypted**, so anyone can read the contents.

This tool:
- Extracts the payload part of the cookie
- Normalizes the Base64 (Werkzeug uses URL-safe encoding)
- Base64-decodes and zlib-decompresses it
- Prints the JSON payload (pretty-formatted if possible)

---

## Example

```bash
$ ./decode_cookie.py ".eJyrVkrJLC7ISaz0TFGyUrJMMjFPNjA0UdJRyix2TMnNzFOySkvMKU4F8eMzcwtSi4rz8xJLMvPS40tSi0tKi1OLkFXAxOITk5PzS_NK4HIgwbzE3FSgHcUlqYm5BaV52Q5wll5yfq5SLQBbNTKK.aNn34Q.Eifshde7vxl0NV25msH8LrFcorU"

{
  "displayId": "9b47c014",
  "isAdmin": false,
  "is_impersonating_testuser": false,
  "is_testuser_account": false,
  "username": "steampunk@steampunk.com"
}
