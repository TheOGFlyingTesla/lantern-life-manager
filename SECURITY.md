# Security

Lantern contains instructions and templates. It does not contain a hosted service, telemetry, credentials, or executable runtime code.

## Report a vulnerability or private-data leak

Use this repository's **Security → Report a vulnerability** flow when available. Do not put credentials, personal information, private documents, or exploit details in a public issue.

If private reporting is temporarily unavailable, open a public issue that says only that you need a private reporting channel. Do not include the sensitive details.

## Scope

Useful reports include:

- personal or confidential information accidentally included in source or release files;
- instructions that can cause unintended sharing or consequential actions without approval;
- package contents that differ from reviewed source;
- prompt-injection paths that bypass Lantern's untrusted-content rules; and
- misleading claims about files, apps, messages, submissions, or background jobs succeeding.

Third-party service availability, ChatGPT account access, and upstream OpenAI product behavior should be reported to the relevant provider unless Lantern's instructions make the issue worse.

## Safe handling

Do not test with another person's account or data. Use synthetic examples and the smallest proof needed. Remove secrets from screenshots and logs.
