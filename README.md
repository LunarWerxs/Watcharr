<div align="center">

<img alt="Watcharr: your IMDb list, straight into Radarr and Sonarr" src=".github/banner.png" width="880" />

### Keep your list on IMDb. Radarr and Sonarr pick it up within minutes.

Paste a public IMDb watchlist or list and get two links back: one Radarr checks every 15 minutes, one Sonarr checks every 5. Nothing to install, no account needed, free.

[![Website](https://img.shields.io/badge/website-watcharr.lunarwerx.com-f5c518?style=flat-square)](https://watcharr.lunarwerx.com)
[![Free](https://img.shields.io/badge/price-free-f5c518?style=flat-square)](#faq)
[![Works with Radarr and Sonarr](https://img.shields.io/badge/works_with-Radarr_%26_Sonarr-f5c518?style=flat-square)](#set-it-up)
[![Discord](https://img.shields.io/badge/Discord-join_the_community-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/PsWpeNUzhk)

[**▶ Open Watcharr**](https://watcharr.lunarwerx.com) · [Features](#features) · [Set it up](#set-it-up) · [How it works](#how-it-works) · [FAQ](#faq)

<br />

<img src=".github/demo.gif" alt="Watcharr in motion: an IMDb list link pasted and generated, its two links and the Add to Radarr / Sonarr sticker appearing beside a fan of the list's covers, then a title's details opening" width="800" />

</div>

---

**Watcharr imports your IMDb watchlist into Radarr and Sonarr.** Sonarr dropped its built-in IMDb
list import in 2025, and Radarr's IMDb list stopped working when IMDb changed its export format.
Watcharr fills that gap. It reads a public IMDb watchlist or list through IMDb's own API and serves it
back as two links: the movies for Radarr, the shows for Sonarr. Each app adds its link as a list of
its own kind, so a movie or show you add on IMDb lands in Radarr or Sonarr, and from there in Plex,
Jellyfin or Emby, within minutes. No Trakt account in the middle, no script to keep running, nothing
to install.

> **IMDb Watcharr is now Watcharr.** Same tool, shorter name. Your Radarr and Sonarr links live on
> watcharr.lunarwerx.com and keep working, and the old `LunarWerxs/IMDBWatcharr` address redirects here.
>
> Not to be confused with [sbondCo/Watcharr](https://github.com/sbondCo/Watcharr), a self-hosted
> watched-list tracker. This Watcharr syncs IMDb lists into Radarr and Sonarr.

## TL;DR

- 🎬 &nbsp;**One paste, two links.** Movies go to Radarr and shows go to Sonarr, from the same IMDb list.
- ⏱️ &nbsp;**Minutes, not hours.** Radarr checks its link every 15 minutes and Sonarr every 5, because each link answers as a Radarr or Sonarr server. An RSS List or Custom List would wait 12 and 6 hours.
- 🔖 &nbsp;**One-click setup.** Drag the **Add to Radarr / Sonarr** sticker to your bookmarks bar and click it inside Radarr or Sonarr. Your API key never leaves the app.
- 🔁 &nbsp;**Links that never change.** They are built from the IMDb list's own id, so the same list always gives the same two links.
- 🛟 &nbsp;**Never goes blank.** If a read of the list fails, both links keep serving the last good copy.
- 🎟️ &nbsp;**No account to start.** Sign in only if you want the list re-read on its own, about every 15 minutes, or several lists combined into one pair of links. [See it signed in](https://watcharr.lunarwerx.com/?demo) without an account first.
- 💸 &nbsp;**Free.** No ads, no paywall, no paid tier.

> **[Open watcharr.lunarwerx.com →](https://watcharr.lunarwerx.com)** Paste a list, copy two links, done.

---

## Features

|  |  |
|---|---|
| 🎬 **Movies to Radarr, shows to Sonarr** | One IMDb list splits in two: movies and TV movies for Radarr, series and mini-series for Sonarr. The page counts each before you copy anything |
| ⏱️ **Radarr's and Sonarr's own list type** | Each link answers as a small Radarr or Sonarr v3 API, so the apps read it like another Radarr or Sonarr: every 15 and every 5 minutes. The same links still work as an RSS List and a Custom List |
| 🔖 **Add to Radarr / Sonarr in one click** | A bookmark that runs inside your own Radarr or Sonarr, with that page's API key. It asks for a Quality Profile and Root Folder, adds the list with Search on Add on, swaps out an older RSS or Custom List of the same link, and reads it at once. Click it again to remove the list |
| 🧭 **Watchlists and lists** | Any public watchlist or list, from the desktop site, the phone site (`m.imdb.com`) or IMDb's language paths (`imdb.com/de/list/…`) |
| 🔁 **Links that never change** | Built from the IMDb list's id, so you set them up once and pasting the list again gives the same two links |
| 📺 **Shows matched for Sonarr** | Sonarr adds shows by their TheTVDB id, which Watcharr finds through TVMaze and then TMDB. A show neither knows is left out rather than passed along broken, and the page lists which ones and why |
| 🍿 **Covers and details** | The list's covers in a row, each opening TMDB's plot, genres, rating, backdrop and trailer, a View on IMDb link, and a Request with [Askarr](https://askarr.com) step |
| 🔄 **Keeps itself current** | Sign in and the list is re-read about every 15 minutes. Your library shows every feed you follow, and a bell tells you when a list has failed three reads in a row |
| 👪 **Shared lists** | One Radarr link and one Sonarr link for the whole house. Sign in, make a shared list, add as many IMDb lists as you like, and send the join link: everyone who joins adds their own watchlist. A title on two lists is added once |
| 🛟 **Last good copy** | A failed read never empties your Radarr or Sonarr list: the links keep serving the last good snapshot, and the failure is recorded on the feed |
| 📱 **Works on a phone** | Paste, copy and browse from any screen. The one-click sticker shows on bigger screens, where there is a bookmarks bar |

<div align="center">
  <img src=".github/screenshots/result.png" width="88%" alt="A generated list: 70 titles, 48 movies, 19 shows and 1 skipped, a fan of its covers, the Radarr and Sonarr links with their Copy buttons and setup paths, and the Add to Radarr / Sonarr sticker under them" />
  <br /><sub>One list, two links, and the one-click sticker</sub>
  <br /><br />
  <img src=".github/screenshots/title-popup.png" width="72%" alt="A title's popup: Iron Man's backdrop and cover, its year, runtime and rating, genres and plot from TMDB, and the View on IMDb and Request with Askarr buttons" />
  <br /><sub>Any cover opens the title, with details from TMDB</sub>
</div>

<br />

<table align="center">
  <tr>
    <td align="center"><img src=".github/screenshots/phone-home.png" width="230" alt="Watcharr's home page on a phone: the headline, the IMDb link field and the Generate button" /></td>
    <td align="center"><img src=".github/screenshots/phone-result.png" width="230" alt="A generated list on a phone: its covers, counts, and the Radarr and Sonarr links with Copy buttons" /></td>
    <td align="center"><img src=".github/screenshots/phone-popup.png" width="230" alt="A title's details on a phone: The Incredible Hulk, its trailer, plot, and View on IMDb and Request with Askarr buttons" /></td>
  </tr>
  <tr>
    <td align="center"><sub>Paste a link</sub></td>
    <td align="center"><sub>Copy your two links</sub></td>
    <td align="center"><sub>Browse what is on the list</sub></td>
  </tr>
</table>

---

## One link, a whole workaround gone

| Instead of... | You already have it |
|---|---|
| **Radarr's IMDb list import**, which broke when IMDb changed its export format | A link Radarr reads as its own list type, every 15 minutes |
| **Sonarr's IMDb list import**, removed in 2025 | A link Sonarr reads as its own list type, every 5 minutes |
| A **Trakt account** plus a **sync script** to keep running (Traktarr and friends) | Nothing to host and no second account: Watcharr reads IMDb's own API |
| An **RSS List** or **Custom List** the apps read every 12 or 6 hours | The same link, read every 15 or 5 minutes |
| **Copying titles by hand** every time the list changes | A link that follows the IMDb list as it changes |

Nothing gets copied into a second service you have to manage. Your list stays on IMDb; Radarr and
Sonarr pick it up from there.

---

## ⭐ Like it? Help it grow

Free, no ads, no paywall. If Watcharr saves you a chore, a few seconds goes a long way:

- ⭐ **[Star the repo](https://github.com/LunarWerxs/Watcharr)**: the clearest signal that this is worth maintaining.
- 💬 **[Join the Discord](https://discord.gg/PsWpeNUzhk)**: questions, ideas, and somewhere to shout when something breaks.
- 🐛 **[Open an issue](https://github.com/LunarWerxs/Watcharr/issues)**: a list that will not read, a show that should have matched, a step that confused you.

---

## Set it up

### 1. Make the links

Open **[watcharr.lunarwerx.com](https://watcharr.lunarwerx.com)**, paste a public IMDb watchlist or
list, and press **Generate**. Both links come back at once and fill in on the list's first read from
IMDb, usually within a few minutes. The page updates by itself when that lands.

A private list cannot be read. If yours is private, make it public on IMDb and paste it again.

### 2. Add them to Radarr and Sonarr

| App | Where | List type | Full URL | API Key |
|---|---|---|---|---|
| **Radarr** | Settings → Lists → Add List | **Radarr** | your Radarr link | type anything |
| **Sonarr** | Settings → Import Lists → Add List | **Sonarr** | your Sonarr link | type anything |

Pick your Quality Profile and Root Folder as usual, then save. Radarr checks the list every 15
minutes from then on, Sonarr every 5.

### Or: one click, from inside the app

<img src=".github/screenshots/one-click.png" width="640" alt="The Add to Radarr / Sonarr sticker lifting on hover, beside its instructions" />

On a computer, drag the **Add to Radarr / Sonarr** sticker under your links to the bookmarks bar.
Open Radarr or Sonarr, click the bookmark, and it adds the list there for you. It runs in that app's
own page with that page's API key, which never leaves the app.

### Which links work

The links are built from the IMDb id, so the same list always maps to the same two:

| Paste this | Get these |
|---|---|
| A list: `imdb.com/list/ls055592025/` | `…/radarr/l/ls055592025`<br>`…/sonarr/l/ls055592025` |
| A watchlist: `imdb.com/user/p.kdbeq6dtmzzpiin4k7t4fnunf4/watchlist/` | `…/radarr/p/p.kdbeq6dtmzzpiin4k7t4fnunf4`<br>`…/sonarr/p/p.kdbeq6dtmzzpiin4k7t4fnunf4` |

---

## How it works

```
                 paste a list                        every 15 / 5 minutes
   you  ─────────────────────▶   Watcharr   ◀─────────────────────────  Radarr / Sonarr
                                     ▲
                                     │  snapshots
                              the sync job  ─────▶  IMDb's API
```

- **IMDb is read on a schedule.** A sync job reads each list (a pasted one within about five
  minutes, a followed one every 15) and hands the snapshot to Watcharr, which stores it and serves it.
  It runs in this repository's Actions tab, so you can see every run.
- **Each link is a tiny Radarr or Sonarr.** `{link}/api/v3/movie` answers as Radarr's movie list (by
  TMDB id) and `{link}/api/v3/series` as Sonarr's series list (by TVDB id), along with the pickers the
  list form asks for. Any API key is accepted, since the list is public anyway.
- **The ids come from TMDB and TVMaze.** IMDb does not carry Radarr's TMDB ids or Sonarr's TVDB ids,
  so Watcharr looks each title up once and carries the answer across reads.
- **An unchanged list is not rebuilt.** Each snapshot is fingerprinted, so a read that finds nothing
  new writes nothing.

---

## Privacy

- **Making links needs nothing but a public IMDb URL.** No account, no email.
- **Signing in stores one opaque id**, used to remember which lists you follow. No name, no email, no
  profile.
- **The bookmark never sends your API key anywhere.** It runs inside your own Radarr or Sonarr and
  talks only to that app.
- **Analytics are LunarWerx's own:** a page-view pixel that honours Do Not Track and Global Privacy
  Control, and a once-a-session visit ping with a random visitor id. No IP address is stored.

---

## Known limits

- **A brand-new list takes a few minutes.** It is read on the next sync run (about five minutes);
  until then its links answer `503` with a `Retry-After`, and the page fills in by itself when it
  lands.
- **Private lists cannot be read.** IMDb answers them with a permission error, and the page says so.
- **Some shows cannot reach Sonarr.** Sonarr only adds shows listed on TheTVDB. The ones that are
  not are usually shows that were announced and never made; they join the link if they are ever
  listed.
- **A movie reaches Radarr's own list type once TMDB knows it.** The rare one TMDB does not know
  stays in the RSS answer only.
- **Scheduled runs drift.** GitHub delays scheduled jobs under load, so 5 and 15 minutes are floors,
  not a clock.
- **Personal use only.** IMDb's API forbids public and commercial use of its data, so Watcharr feeds
  one household's Radarr and Sonarr, not a public index or a business.

---

## How it compares

- **Trakt bridges** (Radarr's Trakt lists, Traktarr and similar) route an IMDb list through a
  separate Trakt account, and often a script you host, before Radarr or Sonarr ever see it. Watcharr
  reads IMDb directly: no Trakt account, nothing to host.
- **[MDBList](https://mdblist.com)** is a general list aggregator that can also take an IMDb list and
  hand it to Radarr or Sonarr, alongside Trakt, Rotten Tomatoes and other sources. Watcharr does one
  thing: your IMDb list, as Radarr's and Sonarr's own list type, with no account needed.
- **Copying titles by hand** works once. Watcharr's links follow the list as it changes.

---

## FAQ

<details>
<summary><b>How do I import my IMDb watchlist into Radarr?</b></summary>

Paste the watchlist's link into [watcharr.lunarwerx.com](https://watcharr.lunarwerx.com), copy the
Radarr link it gives you, and add it in Radarr under Settings → Lists → Add List → **Radarr**, with
the link as the Full URL and anything as the API Key. Radarr reads it every 15 minutes from then on.

</details>

<details>
<summary><b>Sonarr removed IMDb lists. How do I get my IMDb shows into Sonarr now?</b></summary>

The same way: paste the IMDb list or watchlist into Watcharr and add the Sonarr link under Settings →
Import Lists → Add List → **Sonarr**. Sonarr reads it every 5 minutes and adds each show by its
TheTVDB id, which Watcharr looks up for you.

</details>

<details>
<summary><b>My Radarr IMDb list stopped working. Is this the fix?</b></summary>

Yes. Radarr's built-in IMDb list broke when IMDb changed its export format. Swap it for the Watcharr
link: same list, read every 15 minutes, as Radarr's own list type. The one-click bookmark even
removes the old RSS or Custom List of the same link for you.

</details>

<details>
<summary><b>Is Watcharr free?</b></summary>

Yes. Making links, using them and signing in are all free, with no paid tier and no payment set up
anywhere.

</details>

<details>
<summary><b>Do I need an account?</b></summary>

No. Both links come back at once and serve the list from its first read, usually within a few
minutes. Signing in only adds one thing: the list is re-read about every 15 minutes instead of
staying on that first read.

</details>

<details>
<summary><b>Does it work with Plex, Jellyfin or Emby?</b></summary>

Through Radarr and Sonarr, yes. Watcharr feeds your IMDb list to Radarr and Sonarr, and they fetch the
titles into the library Plex, Jellyfin or Emby already reads. It works next to Overseerr, Jellyseerr,
Prowlarr and the rest of the \*arr stack without touching them.

</details>

<details>
<summary><b>Which list type do I pick in Radarr and Sonarr?</b></summary>

**Radarr** in Radarr and **Sonarr** in Sonarr: paste the link as the Full URL and type anything as
the API Key. The same links also work as a Radarr RSS List and a Sonarr Custom List, but the apps
read those only every 12 and 6 hours.

</details>

<details>
<summary><b>Does the bookmark see my Radarr or Sonarr API key?</b></summary>

It uses it, inside the app's own page, to add the list for you, and it never sends it anywhere else.
The bookmark talks only to the Radarr or Sonarr you clicked it in.

</details>

<details>
<summary><b>Why is a show missing from my Sonarr list?</b></summary>

Sonarr needs a TheTVDB id for every show, and not every IMDb title has one. A show Watcharr cannot
match is left out rather than passed along broken, and the page tells you which ones were skipped.

</details>

<details>
<summary><b>Why does a list I just pasted not show anything yet?</b></summary>

A brand-new list is read on the next sync run, usually within a few minutes; until then its links
answer `503`, which Radarr and Sonarr treat as "try again later". If it never fills in, the list is
probably private on IMDb: make it public and paste it again.

</details>

<details>
<summary><b>Can I self-host Watcharr?</b></summary>

Not any more. Watcharr is a hosted service at watcharr.lunarwerx.com, and its source code is private.
Radarr and Sonarr reach it over the network, so nothing runs on your machine.

</details>

---

## Also from LunarWerx

**Want a single title rather than a whole list?** [Askarr](https://askarr.com) lets you search any
movie or show from any browser and request it; the Askarr Monitor on your Windows PC adds it to your
own Radarr and Sonarr, so neither has to face the internet.

Also by [LunarWerx](https://lunarwerx.com): [RepoYeti](https://repoyeti.com),
[AgentHydra](https://agenthydra.lunarwerx.com), [SageThumbs 2K](https://sagethumbs.lunarwerx.com) and
[DevWebUI](https://devwebui.lunarwerx.com).

## License

Watcharr is free to use at [watcharr.lunarwerx.com](https://watcharr.lunarwerx.com). Its source code
is private, copyright LunarWerx Studios. Copies of the code published here before 2026-10-30 keep the
license they came with: [MIT](LICENSES/MIT-legacy.txt) up to commit `25bc710`, then
[PolyForm Noncommercial 1.0.0](LICENSE). There is no commercial license for sale, because IMDb's API
says commercial use of its data is not allowed.

## Credits

Not affiliated with IMDb; IMDb is a trademark of IMDb.com, Inc. Title details and images come from
[TMDB](https://www.themoviedb.org): this product uses the TMDB API but is not endorsed or certified by
TMDB. Show ids come from [TVMaze](https://www.tvmaze.com) and TMDB.
