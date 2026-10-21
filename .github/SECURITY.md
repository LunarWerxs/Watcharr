# Security Policy

Watcharr turns public IMDb lists into Radarr and Sonarr links, and it reaches a fair amount from
there: a Cloudflare Worker and its D1 database, the sign-in and session of every account that
signs in, the list snapshots it stores and serves, the GitHub Actions job that reads IMDb and posts
those snapshots, and the Radarr and Sonarr bookmark that runs inside your own apps. A bug in any of
those could expose more than one user's data or let someone change a list, so we want to hear about it.

## Reporting a vulnerability

If you find a security issue (a way to read or change someone else's list, shared list or sign-in,
a session or secret leaking, the Worker or the sync job being reached by something it should not be,
or anything else that looks exploitable) **please report it privately** rather than opening a public
issue, so it can be fixed before it's disclosed:

- **Preferred:** GitHub's private
  **[Report a vulnerability](https://github.com/LunarWerxs/Watcharr/security/advisories/new)**
  (the repository's *Security, Advisories* tab), or
- open a normal issue **asking us to contact you** (don't include the exploit details there), or
- message the maintainers on [Discord](https://discord.gg/PsWpeNUzhk) and ask for a private
  channel.

Please include:

- what triggers it (the steps, request or list, or a link to it),
- the **commit** you tested (`git rev-parse --short HEAD` in your copy) or say that you used the
  hosted site at watcharr.lunarwerx.com, and
- what you observed (what was reachable, leaked or changed).

We'll acknowledge within a few days and keep you updated through to a fix.

## Supported versions

Only the current code on the `main` branch is supported, so please pull it and confirm the issue
still reproduces before reporting.

Thank you for helping keep Watcharr users safe.
