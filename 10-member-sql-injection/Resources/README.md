## how to find the flag

The vulnerability was found in the `Search Member by ID` functionality on the **member page**.

The application directly concatenates the user-provided `id` parameter into a SQL query
without proper sanitization, making it vulnerable to a UNION-based SQL injection.

First, the number of columns used in the original query was identified using `ORDER BY`,
which revealed that the query returns two columns.
```sql
5 ORDER BY 3 --
```

A `UNION SELECT` was then used to
determine which column was reflected in the page output.
```sql
-1 UNION SELECT 1, 2 --
```

Once the injectable column was identified, it was possible to extract data from the
database. By dumping the `Commentaire` column considered as non-sensitive by the
application, a message containing instructions for generating the flag was discovered.
```sql
-1 UNION SELECT 1, group_concat(Commentaire) FROM users --
```

![instructions](image.png)

Following these instructions, the corresponding password hash stored in the
`countersign` column for the user named `Flag` was retrieved. The instructions specified
that the value had to be decrypted, converted to lowercase, and hashed again using
**SHA-256** in order to obtain the final flag.

```sql
-1 UNION SELECT first_name, countersign FROM users --
```

## how to avoid

This vulnerability occurs because user input is directly injected into a SQL query
without the use of prepared statements or strict input validation.

The SQL injection allowed not only the extraction of authentication-related data, but
also the disclosure of application logic stored in database fields. In this case, the
`Commentaire` column contained instructions required to transform a stored password hash
into the final flag.

In real-world applications, SQL injection vulnerabilities can lead to full database
compromise, including data exfiltration, authentication bypass, and leakage of business
logic.

To prevent this issue, parameterized queries must be used, and database content should
never be relied upon to store sensitive logic or secrets.
