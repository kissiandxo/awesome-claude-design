# Loadout — Full Advertising Campaign Strategy
**Site analyzed:** https://loadout-3d.vercel.app/ · **Date:** 2026-06-04
**Prepared as:** direct-response / media-buy / CRO deliverable

---

## ⚠️ Read this before spending one dollar

1. **Checkout is dead.** Both buy buttons point to `https://REPLACE.lemonsqueezy.com/buy/...` — placeholder URLs. **Any ad spend right now sends traffic to a broken purchase flow.** Fix the LemonSqueezy links *first*. This single issue invalidates every paid campaign until resolved.
2. **Zero social proof.** No testimonials, logos, counts, or screenshots. A $149 cold purchase from a brand-new, unknown site is a hard ask. The whole strategy below is built to *compensate* for this (founder/transparency angles, free-worker lead magnet, refund-forward messaging) rather than pretend it away.
3. **The "no subscription" claim has an asterisk.** The page also says "Requires Claude Pro ($20/mo)" and you must bring n8n (n8n Cloud is paid, or self-host). Loadout itself is one-time, but the *stack* isn't free. If ads scream "NO SUBSCRIPTION" and buyers discover two dependencies, you get refunds and trust damage. Copy below handles this honestly.
4. **"No code" vs. reality.** "Run three commands, edit `config.env`, add API keys" is *low*-code, not *no*-code. The avatar is corrected to match who can actually succeed with this.

> **Scope & assumptions** (prompt left Objective / Target / Platforms as `[brackets]`): Objective = **Sales + email lead capture**. Primary geo = **US/UK/CA/AU (English Tier-1)**, not literal global. Budget **$120 = a learning budget** to find one winning hook + validate CPA, not to scale. Tell me if any of these are wrong and I'll re-run the affected phases.

---

## PHASE 1 — Deep Website Analysis

**Product reality:** Loadout is a **one-time digital product** that imports **38 prebuilt AI "workers" (n8n workflows) across 6 squads + 4 infrastructure flows** into *your own* n8n instance via a CLI installer (`doctor → setup → go`), in ~15 minutes. It is **not** a SaaS, not an agency, not a course.

| # | Element | What's actually on the page |
|---|---------|------------------------------|
| 1 | **Core offer** | 38 automated workers installed into your own n8n in ~15 min. **$149 one-time** (Full System) / **$497** (Done-With-You + 60-min install call). |
| 2 | **USP** | Own, don't rent: a *curated, deployable* AI ops stack that runs on **your** n8n / **your** keys / **your** data — **one payment, no subscription, no credits, no per-seat**. Curation (38 that matter) vs. the 4,000-template dumps. |
| 3 | **Main benefits** | Reclaim hours of manual admin; respond to leads/reviews/DMs instantly; replace $1,500/mo VA + $3,000/mo agency output; data ownership; flat lifetime cost. |
| 4 | **Features** | 6 squads — **A** Lead Gen & Sales (10), **B** Reputation & Reviews (5), **C** Customer Service (5), **D** Content & Social (7), **E** Operations & Admin (7), **F** Intelligence Cockpit (4); **4 infra flows** (error handler, cost tracker, health digest, **kill-switch**); Docker-free n8n API installer; ~15-min setup guide. |
| 5 | **Pain points addressed** | Drowning in repetitive admin; leads going cold from slow replies; can't afford VA/agency; subscription fatigue; "I keep meaning to automate but never do"; blank-canvas paralysis in n8n. |
| 6 | **Customer desires** | Leverage without headcount; "set-and-forget" systems; own the stack; one flat cost; look bigger than they are; evenings back. |
| 7 | **Risk reversals** | **14-day no-questions refund.** "Beginner-friendly." "If you can copy and paste, you can install it." |
| 8 | **Guarantees** | 14-day money-back; quantified promises (38 workers, ~15 min, $0/mo ongoing). |
| 9 | **Trust signals (present)** | Specificity (38/6/4, exact commands, named workers); transparency about requirements; refund. **(Missing: testimonials, logos, demo video, founder identity, counts.)** |
| 10 | **Objections (live, from FAQ)** | "Do I need to code?" "What do I need before I start?" "Is this a subscription?" "Will it work for *my* business?" "What if I get stuck?" "Can I turn workers off?" *(Several FAQ answers appear empty on the page — fix; see Phase 9.)* |
| 11 | **Buying triggers** | Price anchor vs VA/agency; one-time vs monthly; 15-min speed; refund; "kill-switch" (control); concrete roster. |
| 12 | **Emotional drivers** | Overwhelm → relief; fear of being out-automated; pride of running a lean machine; resentment of subscriptions; desire for control/ownership. |
| 13 | **Competitive advantages** | One-time price; curation over volume; self-hosted/own-data; productized 15-min installer (not raw templates); built-in observability + kill-switch; honest "your infra" stance. |

**Funnel as built:** single long-form landing page (anchors: `#assembly #agents #pricing #systems #faq`) → LemonSqueezy checkout → `/setup` guide. No email capture, no pixel evident, no upsell sequence, no demo.

---

## PHASE 2 — Customer Psychology

### Primary avatar — "The Overloaded Operator" (corrected for who can actually deploy this)
- **Demographics:** 27–45, runs a small but real operation — agency, e-commerce store, local-services business with online ops, freelance practice, info-product/SaaS side-build, or "solopreneur with leverage." 1–10 person team or solo. Already pays for ChatGPT/Claude. Has *heard of* (or dabbled in) n8n / Make / Zapier. Comfortable copy-pasting, editing a config file, creating an API key — not a developer, but "technical enough."
- **Psychographics:** identity = sharp, self-reliant operator who builds systems; allergic to bloat and recurring bills; reads "build in public," automation, and AI content; believes leverage > hours.
- **Fears:** being out-competed by faster, more automated rivals; AI passing them by; burning out; looking small/amateur to customers; buying yet another thing they won't use.
- **Frustrations:** repetitive admin tax (follow-ups, invoices, reviews, inbox, content); leads dying from slow replies; "subscription creep"; opening n8n to a blank canvas and bouncing.
- **Goals:** put the boring 80% on autopilot; respond instantly to every lead; own their data/stack; spend one flat amount and be done.
- **Dreams:** a lean, self-running business that looks like a 20-person team; weekends back; "I built a machine."
- **Objections:** "Will it actually work for *my* niche?"; "Is it really no-code?"; "Hidden subscription?"; "Another template dump?"; "Will I get stuck mid-install?"; "Is $149 worth it if I never finish setting it up?"
- **Purchase triggers:** concrete roster + exact commands; one-time price; refund; the VA/agency anchor; "kill-switch" (feeling of control); a free taste of the product.
- **Hidden motivations:** status as a competent builder; fear of irrelevance; desire for control/ownership over rented dependence; the dopamine of "set it up once, it just runs."
- **Emotional language (their words):** *"I'm drowning in admin." "I keep meaning to automate this." "I can't afford a VA yet." "Not another monthly subscription." "I want to own my stack." "Leads go cold before I reply." "I want my evenings back." "Set it and forget it."*

### Secondary avatar — "The Agency / Freelance Builder"
Sells automation/marketing/ops services. $149 is a rounding error against billable value. Wants a **productized stack to deploy fast for clients** (speed-to-delivery, margin). Angle = "install this in 15 min, charge $1,500 to set it up." (Note: site doesn't grant resell rights — don't imply it; sell it as *their internal delivery accelerator*.)

### Tertiary avatar — "AI-curious side-hustler"
From the n8n/AI YouTube–TikTok niche. Loves the "38 agents" novelty, the roster, the kill-switch. Cheap to reach organically; lower buy-rate but great for content engagement and list-building.

### Ranking tables

**Most painful problems**
| Rank | Problem | Intensity (1–10) |
|---|---|---|
| 1 | Leads go cold because replies are slow / manual | 9 |
| 2 | Buried in repetitive admin (invoices, follow-ups, inbox, reviews) | 9 |
| 3 | Can't justify $1.5k–3k/mo for a VA/agency | 8 |
| 4 | "I keep meaning to automate and never do" (blank-canvas paralysis) | 8 |
| 5 | Subscription fatigue / metered "credits" | 7 |
| 6 | Looking small/amateur vs. competitors | 6 |

**Most desired outcomes**
| Rank | Outcome | Pull (1–10) |
|---|---|---|
| 1 | Every lead answered instantly, automatically | 9 |
| 2 | The boring 80% runs without me | 9 |
| 3 | Own my stack/data, one flat cost | 8 |
| 4 | Evenings/weekends back | 8 |
| 5 | Look like a much bigger operation | 7 |

**Most persuasive promises**
| Rank | Promise | Persuasion (1–10) |
|---|---|---|
| 1 | "38 workers running in *your* n8n in 15 minutes — one payment, $149" | 9 |
| 2 | "Cheaper than one month of a VA, runs forever" | 9 |
| 3 | "Reply to every lead in 4 seconds, automatically" | 8 |
| 4 | "Own it, don't rent it — no subscription, no credits, your data" | 8 |
| 5 | "If you can copy-paste, it's installed — 14-day refund if not" | 7 |

---

## PHASE 3 — Competitor Research

Real landscape (sourced, not invented). Loadout sits in a gap between **cheap undifferentiated template dumps** and **expensive recurring SaaS/agencies**.

| Competitor / category | Offer | Positioning | Strengths | Weaknesses | Their ad angle |
|---|---|---|---|---|---|
| **Gumroad n8n megapacks** (2,000–4,000 templates, $30–$100) | Giant JSON vaults | "Everything, dirt cheap" | Volume, price, instant | Overwhelming, unsupported, most never installed, no curation | "4,000 workflows worth $3,500 — today $30" |
| **AgentEmpire / "agency-in-a-box"** (70+ agents, one-time + resell) | Prebuilt agents + client-getting playbook | "Start an AI agency, charge $1,500/client" | Business model + resell rights | Hype-heavy, MMO crowd, deliverability of promise | "Charge $1,500+/client without coding" |
| **n8n agencies** (n8nlab, m8l) | Done-for-you builds | "We build your automations" | Custom, high-touch | $$$$, slow, not productized | "Custom AI workflows for your business" |
| **Lindy** ($49.99–$199.99/mo) | AI assistants/agents SaaS | "AI employees, native" | Polished, no infra, templates | Recurring, metered credits, their cloud/your data | "Build an AI team in minutes" |
| **Gumloop** ($37/mo+) | Visual AI workflow SaaS | "No-code AI automation" | Strong UX, free tier | Recurring, credit caps, lock-in | "Automate work with AI, no code" |
| **Relay.app** ($27/mo+) | Human-in-the-loop automation | "Reliable AI automations" | Approvals, reliability | Recurring, build-it-yourself | "AI automation you can trust" |
| **Make / Zapier** (freemium → $$$) | General automation platforms | "Connect everything" | Ecosystem, trust | DIY, task/credit pricing, no curated ops stack | "Automate without developers" |
| **GoHighLevel** (~$97–497/mo) | All-in-one SMB CRM/marketing | "Agency OS" | Missed-call-textback, CRM, all-in-one | Recurring, bloated, learning curve | "Replace your whole stack" |
| **MindStudio** (usage-based) | AI app/agent builder | "Build AI workers" | Flexible | Build-it-yourself, recurring | "Ship AI agents fast" |
| **n8n.io itself** (free OSS / Cloud paid) | The underlying platform + free templates | "Powerful, fair-code" | Free, powerful, owns the runtime | Blank canvas, you assemble it | "Flexible AI workflow automation" |

**Market gaps Loadout can own**
- **Curation, not volume:** "38 that actually run" beats "4,000 you'll never open." This is the single strongest wedge.
- **Own-it economics:** one-time + self-hosted + your-data, in a sea of metered monthly credits.
- **Productized install (not raw JSON):** a `doctor→setup→go` installer with health checks + kill-switch = far less abandonment than a Gumroad zip.
- **Honest, no-hype operator brand:** the MMO/agency-in-a-box space is hype-saturated; a calm, specific, transparent voice is a differentiator.

**Untapped opportunities:** the "I have n8n open but bounced at the blank canvas" segment; the "I refuse another $50/mo tool" segment; agencies wanting a fast internal delivery kit.

**Differentiation line to repeat everywhere:** *"Not 4,000 templates you'll never use. Not another monthly bill. 38 workers that install into your own n8n in 15 minutes, once."*

**Sources:** [Gumroad n8n packs](https://usamaakrm.gumroad.com/l/n8n-templates) · [Gumroad megapack](https://vfocus.gumroad.com/l/mrjajc?layout=profile) · [Lindy pricing](https://www.lindy.ai/blog/gumloop-pricing) · [Gumloop pricing](https://www.godofprompt.ai/blog/ai-workflow-automation-tools-pricing-comparison) · [Relay alternatives](https://www.gumloop.com/blog/relay-app-alternatives) · [AgentEmpire](https://agentempire.ai/) · [n8n AI agents](https://n8n.io/ai-agents/) · [n8nlab agency](https://n8nlab.io/)

---

## PHASE 4 — Ad Strategy (full-funnel)

> Strategic pivot (justified in Phase 10 self-critique): for a $149 cold offer with **no social proof**, do **not** push direct cold purchase as the only path. Run a **free lead magnet — "Get 3 of the 38 workers, free"** — capture email, nurture, then sell the full 38. This de-risks cold traffic, builds a retargeting list, and *demonstrates* the product instead of asserting it.

| Stage | Objective | Audience | Angle | Hook | Offer | CTA | Funnel |
|---|---|---|---|---|---|---|---|
| **Awareness** | Cheap reach + watch-time/engagement | Broad: AI-automation, n8n, "build in public," solopreneur, agency-owner interests (Tier-1 EN) | Education + identity ("operators who own their stack") | "38 AI workers, one n8n, 15 minutes" | Free roster / 3 free workers | Watch / Learn more | Reel/Short → profile + retarget pool |
| **Consideration** | Email opt-in (lead) | Engagers + video-viewers + site visitors | Free taste + curiosity | "Take 3 of the 38 for free and see if it even works on your stack" | **3 free workers** (email) | Get the 3 free | Lead form → email nurture (5–7 emails) |
| **Conversion** | Purchase ($149) | Email list + add-to-cart + 7-day site visitors | Value-stack + risk reversal + ownership | "You installed the 3 free ones. The other 35 are $149, once." | $149 full system (+$497 DWY upsell) | Get Loadout — $149 | Checkout → `/setup` → upsell DWY |
| **Retargeting** | Recover + upsell | Visited pricing/checkout, opened emails, no buy | Objection-killing + scarcity + proof (once it exists) | "Still doing it by hand? Here's the 14-day-refund version of just trying it." | $149 + refund reminder; DWY for the stuck | Finish setup / Get Loadout | Dynamic retarget → checkout |

---

## PHASE 5 — Meta Ads

Scoring legend: **E** = emotional pull, **C** = click potential, **V** = conversion potential (each /10). 10 psychological angles × 2 = **20 primary texts**.

### 20 Primary Text variations

**Fear**
1. *(E8 C8 V7)* It's 7:42pm and you're still sending invoices and chasing the lead who emailed at 9am — and went cold by noon. Every day you do this by hand, a faster competitor's bot did it in 4 seconds. 38 workers install into *your* n8n in 15 minutes. $149 once. Then they just… run.
2. *(E9 C8 V7)* The scary part of AI isn't that it takes your job. It's that the operator down the street installed 38 AI workers for $149 and now answers every lead, review, and DM before you've finished your coffee. You're not behind because you're lazy — you're behind because you're still doing it manually.

**Desire**
3. *(E8 C8 V7)* Imagine logging in tomorrow to: 11 leads replied to, 3 reviews answered, this week's content scheduled, invoices sent, a churn alert flagged — and you touched none of it. That's 38 workers running in your own n8n. One payment, $149.
4. *(E8 C7 V7)* You didn't start a business to spend Sundays on follow-ups. Loadout drops 38 "employees" into your own n8n in ~15 min so the repetitive 80% runs itself. You get the evenings back. They never call in sick.

**Social proof** *(honest substitute — no fake numbers until you have real ones)*
5. *(E7 C7 V6)* No "10,000 happy customers" here — Loadout just launched, built by an operator who got tired of paying agencies $3k/mo to do what a workflow can. 38 workers, your own n8n, $149 once, 14-day no-questions refund. Be early. Judge it yourself.
6. *(E7 C8 V7)* Everyone selling "AI for business" wants $50–200/month forever. The people who actually run lean ops are quietly installing 38 one-time workers into their own n8n instead. No credits. No seats. $149.

**Authority**
7. *(E7 C8 V7)* 38 workers. 6 squads. 4 infra flows with a built-in error handler, cost tracker, and kill-switch — running entirely on your n8n, your keys, your data. This isn't a "prompt pack." It's a deployable AI ops stack. $149, ~15-min install.
8. *(E7 C8 V7)* Three commands: `doctor → setup → go`. The installer imports, activates, and verifies 38 workers in your own n8n — no Docker, no code. If you can copy-paste, it's already done.

**Scarcity** *(only run if literally true)*
9. *(E7 C7 V6)* Launch price: $149 for all 38 workers, one payment. The Done-With-You install (I jump on a 60-min call and build it into your stack) is capped by how many calls fit in a week. When the slots are gone, they're gone.
10. *(E7 C8 V6)* Every "AI employee" platform is a meter running on your card. Lock in 38 workers for one flat $149 before this becomes a subscription like everything else.

**Curiosity**
11. *(E8 C9 V6)* There are 38 of them. One answers leads in 4 seconds. One texts back missed calls. One quietly watches for the word "cancel" and flags churn before it happens. One is a literal kill-switch. Here's the full roster →
12. *(E7 C8 V6)* What can 38 AI workers in your own n8n actually do for one payment of $149? Lead response, review replies, content, invoicing, and a daily digest of your entire business. See the roster before you decide.

**Urgency**
13. *(E8 C8 V7)* Do the math on one missed lead. If a $500 customer slips because you replied 6 hours late, that's 3× Loadout — gone, today. The instant-response worker installs in 15 minutes. $149 once.
14. *(E7 C7 V6)* Every day Loadout isn't installed, your "38 employees" aren't working — and you are. That's the only deadline that matters.

**Problem agitation**
15. *(E8 C8 V7)* The follow-up you meant to send. The review you didn't reply to. The invoice in drafts. The DM from Tuesday. None of it is hard. All of it is on you. That's the manual tax — and it compounds. 38 workers pay it for you.
16. *(E8 C8 V7)* You keep saying "I should automate that." Then a customer needs you, and "later" becomes never. Loadout is the 15-minute version of finally doing it: 38 workers, installed, running, done.

**Solution awareness**
17. *(E8 C8 V7)* You've heard n8n is powerful. You also opened it once, saw a blank canvas, and closed the tab. Loadout fills that canvas with 38 working employees in ~15 minutes — the power of n8n without the "where do I start."
18. *(E7 C8 V7)* n8n is free. Knowing *which* 38 automations actually move a business — and wiring them so they don't break — is the part that costs you weeks. That part is $149.

**Competitor comparison**
19. *(E8 C9 V8)* A VA: $1,500+/mo. An agency: $3,000/mo. A pile of 4,000 random n8n templates you'll never open: $30 and useless. 38 curated workers that actually install and run: $149, once. Pick the one that's still cheaper next month.
20. *(E7 C8 V7)* Lindy, Gumloop, Relay — good tools, $40–200/month forever, your data on their cloud, metered by "credits." Loadout runs on *your* n8n, *your* keys. No credits. No monthly. One payment: $149.

### 20 Headlines *(≤40 chars where possible)*
1. Put your business on autopilot — $149
2. 38 AI workers. Your n8n. 15 minutes.
3. Stop doing $15/hr work at 11pm
4. Your competitor automated this already
5. One payment. No subscription. 38 workers.
6. The agency does this for $3,000/mo
7. Reply to every lead in 4 seconds
8. n8n — but the blank canvas is built
9. Hire 38 staff for $149. They don't quit.
10. Cancel the VA. Keep the output.
11. See the 38 workers →
12. Missed a call? It texts them back.
13. Your whole business in a daily digest
14. Not a template dump. A working stack.
15. Install your AI ops in 15 minutes
16. $149 once vs $50/mo forever
17. The 4,000-template packs are a trap
18. Your data. Your keys. Your n8n.
19. Finally automate what you keep ignoring
20. 14-day refund. Just try it.

### 20 Descriptions *(≤90 chars)*
1. 38 workers installed into your own n8n in ~15 min. One payment, $149.
2. No Docker, no subscription. Copy-paste, run three commands, done.
3. Leads, reviews, content, invoicing, reporting — on autopilot.
4. Cheaper than one month of a VA. Runs on your own infrastructure.
5. 6 squads, 38 workers, 4 infra flows, built-in kill-switch.
6. Stop paying $50–200/mo for metered "AI employees." Pay once.
7. For operators who'd rather own their stack than rent it.
8. 14-day no-questions refund. Install it, judge it, keep it.
9. One saved sale pays for the whole thing.
10. n8n's power without the "where do I even start."
11. Not 4,000 templates you'll never open. 38 that run.
12. Your keys, your data, your server. No lock-in.
13. From lead capture to KPI reports — all 38 wired up.
14. Answer every lead in seconds, automatically.
15. Replace $3,000/mo of agency busywork for $149 once.
16. Beginner-friendly install. If you can copy-paste, you're set.
17. Missed-call text-back, auto follow-ups, review replies, more.
18. Done-With-You option: I install it live in 60 minutes.
19. No monthly bill. No credits. No surprises.
20. Built for n8n. Deploys in about 15 minutes.

> **Creative QA note:** "social proof" and "scarcity" sets are conditional — don't run #5/#9/#10 claims unless literally true. Lead testing with **#19 (competitor math), #11 (curiosity roster), #15 (problem agitation), #3 (desire)** — these don't depend on proof you don't have yet.

---

## PHASE 6 — Google Search Ads

### 30 Headlines *(≤30 chars)*, grouped by intent

**Brand intent** *(thin until brand awareness exists — run defensively, low budget)*
1. Loadout — Official Site
2. Get Loadout for n8n
3. Loadout: 38 n8n Workers
4. Loadout AI Workforce

**Commercial intent**
5. 38 n8n Workers, $149 Once
6. Done-For-You n8n Stack
7. AI Workers For Your n8n
8. No-Code n8n Automation Kit
9. Install AI Ops in 15 Min
10. One-Time, No Subscription
11. Prebuilt n8n AI Agents
12. n8n Automation, Done
13. 38 Agents, One Payment
14. Self-Hosted AI Workforce

**Problem intent**
15. Reply To Leads In Seconds
16. Stop Replying To Leads Late
17. Automate Your Admin Today
18. Too Busy? Automate It
19. Missed-Call Text-Back
20. Get Your Evenings Back
21. Kill Repetitive Busywork
22. Auto Follow-Up Every Lead

**Competitor intent**
23. Cheaper Than a VA
24. Skip the $3k/mo Agency
25. n8n Templates That Work
26. Better Than Template Dumps
27. Own It, Don't Rent It
28. No Monthly AI Credits
29. Lindy/Gumloop Alternative
30. One-Time vs Subscription

### 20 Descriptions *(≤90 chars)*
1. 38 AI workers installed into your own n8n in ~15 min. One payment of $149.
2. No code, no Docker, no subscription. Run three commands and you're live.
3. Lead response, reviews, content, invoicing, reporting — all automated.
4. Cheaper than one month of a VA. Runs forever on your infrastructure.
5. Curated stack, not a 4,000-template dump. 38 workers that actually run.
6. Your n8n, your keys, your data. No lock-in, no metered credits.
7. 14-day no-questions refund. Install it, test it, keep it or don't.
8. Done-With-You: we install all 38 on a live 60-minute call.
9. Built-in error handler, cost tracker, and kill-switch included.
10. Answer every lead in 4 seconds — automatically, day and night.
11. Replace $3,000/mo of agency busywork for a single $149 payment.
12. 6 squads: sales, reviews, support, content, ops, intelligence.
13. Beginner-friendly. If you can copy-paste, you can install it.
14. Stop paying $50–200/mo for "AI employees." Pay once, own it.
15. From the blank n8n canvas to 38 working agents in 15 minutes.
16. Missed-call text-back, auto follow-ups, cart recovery, and more.
17. One saved sale pays for the entire system. $149 once.
18. Skip the build. Skip the subscription. Deploy the stack.
19. Self-hosted AI workforce for operators who own their tools.
20. See the full 38-worker roster, then decide. 14-day refund.

### Keywords (seed) + match types
| Intent | Keywords | Match type |
|---|---|---|
| Commercial | `n8n templates`, `n8n workflow pack`, `n8n automation templates`, `prebuilt n8n workflows`, `buy n8n workflows` | Phrase / Exact |
| Commercial | `done for you n8n`, `n8n automation kit`, `ai agents for n8n`, `n8n ai agent template` | Phrase |
| Problem | `automate small business`, `automate lead follow up`, `missed call text back`, `auto review replies`, `automate invoicing` | Phrase |
| Competitor/alt | `lindy alternative`, `gumloop alternative`, `make vs n8n automation`, `cheaper than a virtual assistant` | Phrase |
| Builder | `ai automation for agency`, `productized automation service`, `client automation templates` | Phrase |

**Negative keywords:** `free`, `tutorial`, `course`, `jobs`, `salary`, `hiring`, `resume`, `gun loadout`, `warzone`, `cod loadout`, `gaming`, `3d printing`, `fortnite`, `pdf`, `crack`, `download free`, `nulled`, `reddit` *(monitor, may keep)*, `meaning`, `definition`, `n8n docs`, `self host guide` *(unless you want top-funnel)*.

> ⚠️ **"loadout" is a gaming term** (weapon loadouts in Call of Duty/Warzone/Fortnite). Aggressive gaming/3D-printing negatives are mandatory or you'll pay for irrelevant clicks. Lean on **exact/phrase**, not broad, at this budget.

---

## PHASE 7 — Video Creative Ideas

> 80 concepts below as **shoot-ready briefs** (Hook / Script beat / Shot list / CTA). I deliberately kept them concept-dense rather than 80 full scripts — that's how you actually test: concept first, then fully script the 3–5 winners. Say the word and I'll expand any into a full shot-by-shot script. **Testimonial concepts** are *capture templates* — you have no customers yet, so these are what to film the moment you do (or to brief beta users).

### 20 UGC concepts *(talking-to-camera / screen-record, founder or creator)*
1. **Hook:** "I replaced my $1,500/mo VA with this." **Script:** show the VA invoice, then the 15-min install. **Shots:** invoice close-up → screen record install → dashboard of workers. **CTA:** "Link's in bio — $149 once."
2. **Hook:** "It's 11pm and I'm not doing admin for the first time in a year." **Script:** dark room, laptop glow, list of tasks auto-completing. **Shots:** clock → tired face → screen of completed tasks. **CTA:** "38 workers. Your n8n."
3. **Hook:** "POV: a lead emails you at 2am." **Script:** phone buzzes, worker auto-replies in 4s. **Shots:** phone on nightstand → notification → auto-reply sent. **CTA:** "Stop losing leads while you sleep."
4. **Hook:** "Everyone's selling 4,000 n8n templates. Here's why that's a scam." **Script:** scroll endless template list, overwhelmed, vs 38 curated. **Shots:** screen scroll → eye-roll → clean roster. **CTA:** "38 that run > 4,000 you won't."
5. **Hook:** "Three commands and my business runs itself." **Script:** type `doctor → setup → go`, workers light up. **Shots:** terminal → green checks → coffee sip. **CTA:** "If you can copy-paste…"
6. **Hook:** "I added up every tool I pay monthly. I almost threw up." **Script:** list subscriptions totaling $X, then one $149 payment. **Shots:** subscription list → total → single receipt. **CTA:** "Own it, don't rent it."
7. **Hook:** "My n8n was a blank canvas for 6 months." **Script:** open empty n8n, then full of 38 workers. **Shots:** empty canvas → install → full canvas. **CTA:** "The blank-canvas fix."
8. **Hook:** "The 'cancel' detector saved me a customer today." **Script:** churn radar flags the word "cancel," founder reaches out, saved. **Shots:** alert → outreach → "stayed." **CTA:** "One of 38 workers."
9. **Hook:** "I don't reply to reviews anymore. Something else does." **Script:** review posts → AI reply drafted → approved. **Shots:** review → draft → posted. **CTA:** "Reputation, on autopilot."
10. **Hook:** "Watch me install an entire AI ops team in 15 minutes." **Script:** real-time timer install. **Shots:** timer start → steps → timer stop at ~15:00. **CTA:** "$149, once."
11. **Hook:** "Stop paying for 'AI employees' by the credit." **Script:** show metered SaaS bill vs flat one-time. **Shots:** credit meter → flat price. **CTA:** "No credits. Ever."
12. **Hook:** "The thing nobody tells you about hiring a VA." **Script:** onboarding, sick days, turnover vs workers that never quit. **Shots:** chaotic vs calm dashboard. **CTA:** "They don't call in sick."
13. **Hook:** "I gave 3 of these workers away free. Here's what happened." **Script:** lead magnet → list growth → upsell. **Shots:** opt-in → inbox → install. **CTA:** "Grab the 3 free ones."
14. **Hook:** "My whole business in one morning email." **Script:** open the daily digest. **Shots:** phone → digest → smile. **CTA:** "The Intelligence Cockpit."
15. **Hook:** "If you've ever said 'I'll automate that later'…" **Script:** the pile of 'later' tasks, then done. **Shots:** sticky notes → cleared desk. **CTA:** "15 minutes beats 'later.'"
16. **Hook:** "Reading the roster of 38 workers like a menu." **Script:** scroll squads A–F, react. **Shots:** roster scroll + reactions. **CTA:** "Pick your squad."
17. **Hook:** "I let it run my follow-ups for a week. Results:" **Script:** before/after reply times + booked calls. **Shots:** metrics screen. **CTA:** "Auto follow-up engine."
18. **Hook:** "This is the kill-switch. This is why I trust it." **Script:** show the kill-switch flow = control. **Shots:** toggle → all stop. **CTA:** "You're always in control."
19. **Hook:** "$149 vs my last month of agency invoices." **Script:** stack agency invoices next to one receipt. **Shots:** invoice stack → single receipt. **CTA:** "Do the math."
20. **Hook:** "Things my 38 AI workers did before 9am." **Script:** rapid montage of completed tasks. **Shots:** fast cuts of notifications. **CTA:** "Put your business on autopilot."

### 20 Founder video concepts *(authority + story, builds the missing trust)*
21. **Hook:** "I built Loadout because I was the bottleneck in my own business." **Script:** origin story → the 38 workers. **Shots:** founder to camera, b-roll of work. **CTA:** "Here's the roster."
22. **Hook:** "Why I made this one-time instead of a subscription." **Script:** anti-subscription philosophy. **Shots:** founder + pricing graphic. **CTA:** "Own it for $149."
23. **Hook:** "I'll show you exactly what you get. No hype." **Script:** screen-share all 38. **Shots:** full screen tour. **CTA:** "See it all before you buy."
24. **Hook:** "The 3 workers I'd install first if I were you." **Script:** prioritized picks. **Shots:** founder + 3 demos. **CTA:** "Start with these."
25. **Hook:** "Here's the honest part: you need n8n and Claude." **Script:** transparent about requirements. **Shots:** founder, requirement list. **CTA:** "Now you know exactly what you need."
26. **Hook:** "Why I curated 38 and deleted 200." **Script:** curation philosophy. **Shots:** founder + before/after list. **CTA:** "Quality over a dump."
27. **Hook:** "Let me install it live, mistakes and all." **Script:** unedited install. **Shots:** real screen record. **CTA:** "It really is ~15 min."
28. **Hook:** "What I'd charge an agency client to build this: $3,000." **Script:** value framing. **Shots:** founder + invoice mockup. **CTA:** "$149 to do it yourself."
29. **Hook:** "I made the Done-With-You option for one reason." **Script:** for the non-technical, I'll do it on a call. **Shots:** founder + calendar. **CTA:** "Book the install call."
30. **Hook:** "The kill-switch exists because I don't trust black boxes either." **Script:** control philosophy. **Shots:** founder + toggle demo. **CTA:** "You stay in control."
31. **Hook:** "Ask me anything about the 38 workers." **Script:** Q&A format. **Shots:** founder answering comments. **CTA:** "Comment your use case."
32. **Hook:** "I refunded someone today. Here's why that's the point." **Script:** 14-day refund integrity. **Shots:** founder to camera. **CTA:** "No-questions refund."
33. **Hook:** "The exact tech stack Loadout runs on." **Script:** n8n + Anthropic + your server. **Shots:** architecture diagram. **CTA:** "All yours, all transparent."
34. **Hook:** "I built this for operators, not 'gurus.'" **Script:** anti-hype positioning. **Shots:** founder, plain talk. **CTA:** "No hype. Just the stack."
35. **Hook:** "Squad by squad: what each does." **Script:** walk A–F. **Shots:** six quick demos. **CTA:** "Pick what you need first."
36. **Hook:** "The mistake I see everyone make with n8n." **Script:** building from scratch vs deploying. **Shots:** founder + canvas. **CTA:** "Skip to the finished version."
37. **Hook:** "Here's what 'no subscription' actually means for your wallet." **Script:** 12-month cost math. **Shots:** founder + spreadsheet. **CTA:** "Pay once, run forever."
38. **Hook:** "I'm one person. This is how I compete with teams." **Script:** leverage story. **Shots:** founder + dashboard. **CTA:** "38 workers = your team."
39. **Hook:** "If you've never touched n8n, watch this first." **Script:** beginner reassurance. **Shots:** founder + simplest path. **CTA:** "Beginner-friendly, promise."
40. **Hook:** "What happens after you pay (full walkthrough)." **Script:** delivery → setup → live. **Shots:** post-purchase flow. **CTA:** "No surprises."

### 20 Testimonial concepts *(capture-ready — film when you have users/beta testers)*
41. **Hook:** "I installed it in 12 minutes and I'm not technical." → beginner relief story. Shots: user screen + face. CTA: "If they can, you can."
42. **Hook:** "It booked me 3 calls the first day." → results. Shots: calendar fill. CTA: "Auto follow-up works."
43. **Hook:** "I cancelled my VA after one week." → cost savings. Shots: cancel screen. CTA: "Keep the output, cut the cost."
44. **Hook:** "The review replies alone are worth it." → reputation. Shots: review feed. CTA: "On autopilot."
45. **Hook:** "I'm an agency — I install this for clients now." → builder use case. Shots: client dashboard. CTA: "Your delivery accelerator."
46. **Hook:** "It caught a customer about to churn." → churn radar win. Shots: alert + save. CTA: "It pays for itself."
47. **Hook:** "I finally use n8n instead of staring at it." → activation. Shots: full canvas. CTA: "The blank-canvas fix."
48. **Hook:** "One missed-call-text-back recovered a $900 job." → ROI. Shots: text thread. CTA: "One sale > $149."
49. **Hook:** "My mornings start with the daily digest now." → habit. Shots: phone digest. CTA: "Your whole biz at a glance."
50. **Hook:** "I was skeptical of another 'AI' thing. This one runs." → skeptic-converted. Shots: candid. CTA: "Try it, 14-day refund."
51. **Hook:** "Setup support actually answered." → support. Shots: chat. CTA: "You won't get stuck."
52. **Hook:** "Cheaper than the dinner I bought debating whether to buy it." → price reframe. Shots: receipt. CTA: "$149, once."
53. **Hook:** "I run a store — cart recovery paid for it day one." → e-com. Shots: recovered carts. CTA: "Squad A earns its keep."
54. **Hook:** "I sound like a 10-person team now." → status. Shots: polished comms. CTA: "Look bigger than you are."
55. **Hook:** "The kill-switch is why I trusted it." → control. Shots: toggle. CTA: "Always in control."
56. **Hook:** "From skeptical to 'set and forget' in a weekend." → journey. Shots: before/after. CTA: "Set it, forget it."
57. **Hook:** "I gave the 3 free workers a shot. Bought the rest that night." → lead-magnet→sale. Shots: opt-in→buy. CTA: "Start free."
58. **Hook:** "My follow-up game went from 'whenever' to 'instant.'" → speed. Shots: timestamps. CTA: "4-second replies."
59. **Hook:** "No subscription is the whole reason I said yes." → anti-sub. Shots: pricing. CTA: "Pay once."
60. **Hook:** "I do client work — this saved me 6 build hours per client." → agency margin. Shots: time log. CTA: "Deploy in 15 min."

### 20 TikTok / Reels concepts *(native, fast, pattern-interrupt)*
61. **Hook (0–3s):** "n8n template packs are a scam and I can prove it." → fast scroll of 4,000 useless templates vs 38. CTA: "38 > 4,000."
62. "POV: you hired 38 employees for $149 and none of them sleep." → text-on-screen montage. CTA: "Roster in bio."
63. "Tell me you're drowning in admin without telling me…" → relatable admin chaos → install. CTA: "15-min fix."
64. "Things AI does for my business before I wake up." → green-check montage. CTA: "Autopilot."
65. "Rating my 38 AI workers like Pokémon cards." → roster react. CTA: "Which squad are you?"
66. "I let AI reply to a lead in 4 seconds. Here's the reply." → screen demo. CTA: "Never lose a lead."
67. "Stop paying $50/month for this. Seriously." → SaaS bill rip. CTA: "$149 once."
68. "The most underrated worker: the 'cancel' detector." → churn radar demo. CTA: "Saves customers."
69. "Watch a blank n8n canvas become an AI team in 15 min." → timelapse. CTA: "Deploy it."
70. "If you say 'I'll automate it later' one more time…" → callout humor. CTA: "Do it in 15 min."
71. "Green screen over the 38-worker roster, reacting." → creator react. CTA: "Tap the link."
72. "My agency charges $3k for this. Here it is for $149." → reveal. CTA: "Do it yourself."
73. "3 free AI workers, no catch. Here's the link." → lead magnet. CTA: "Grab the free 3."
74. "Day in the life of a solo founder who automated everything." → vlog cuts. CTA: "Be this person."
75. "The kill-switch demo that made me trust AI again." → toggle. CTA: "You're in control."
76. "Rich vs lean: how lean operators actually run." → side-by-side. CTA: "Own your stack."
77. "I asked AI to handle my whole inbox for a day." → results. CTA: "Smart inbox triage."
78. "n8n in 2026 if you skip the hard part." → fast tutorial vibe. CTA: "Skip to finished."
79. "Reading mean comments about automating my business 😌." → comment-react + flex results. CTA: "Haters automate too."
80. "What $149 actually buys you (full roster speedrun)." → fast roster tour. CTA: "See all 38."

---

## PHASE 8 — Creative Testing Matrix (ranked by expected ROAS)

**20 Hooks** (1 = highest expected ROAS)
1. "A VA is $1,500/mo. An agency is $3,000/mo. This is $149, once." 2. "There are 38 of them. One replies to leads in 4 seconds." 3. "The 4,000-template packs are a scam — here's why." 4. "I replaced my $1,500/mo VA with this." 5. "It's 11pm and you're still doing admin." 6. "Your competitor automated this already." 7. "My n8n was a blank canvas for 6 months." 8. "Watch me install an AI ops team in 15 minutes." 9. "Stop paying for AI by the credit." 10. "3 free AI workers, no catch." 11. "Things my 38 workers did before 9am." 12. "POV: a lead emails you at 2am." 13. "The 'cancel' detector saved me a customer." 14. "Own it, don't rent it." 15. "My whole business in one morning email." 16. "Three commands and it runs itself." 17. "If you've ever said 'I'll automate that later'…" 18. "The kill-switch is why I trust it." 19. "I sound like a 10-person team now." 20. "14-day refund. Just try it."

**20 Angles** (ranked)
1. Competitor cost math (VA/agency/dump vs $149) 2. Curiosity — the roster of 38 3. Problem agitation — late-night admin 4. Own-it/anti-subscription 5. Instant lead response ROI 6. Fear — out-automated by rivals 7. Blank-canvas n8n rescue 8. Speed — 15-minute install 9. Free 3-worker lead magnet 10. Control — kill-switch/your data 11. Founder/transparency trust 12. Status — look like a big team 13. Churn-radar "saved a customer" 14. Anti-hype vs gurus 15. Daily digest / cockpit 16. Refund-forward risk reversal 17. Subscription-fatigue 18. Agency delivery accelerator 19. "I'll automate later" guilt 20. Beginner reassurance

**20 Offers** (ranked)
1. **3 workers free → email → $149** (best for cold + no proof) 2. $149 full system, 14-day refund 3. $149 + bonus "first 3 to install" setup checklist 4. Launch price $149 (price goes up) 5. $149 + free 15-min "which 5 workers first" mini-call 6. Bundle: $149 now, DWY upgrade credit later 7. $497 DWY (live install) for non-technical 8. "Install-or-refund" guarantee 9. $149 + private setup community access 10. Free roster PDF → retarget 11. Free "n8n readiness check" → sell 12. $149 + quarterly new-worker drops 13. Money-back + "I'll install one worker with you free" 14. Annual "agency license" framing for builders 15. $149 + swipe file of the AI prompts inside 16. Pay-what-you-want intro for first 20 (data-gathering) 17. $149 + office-hours week 18. Referral: give a worker, get a worker 19. $129 email-capture coupon 20. $149 + "uninstall script" peace-of-mind bonus

**20 CTAs** (ranked)
1. "Grab the 3 free workers" 2. "See the 38 workers →" 3. "Get Loadout — $149" 4. "Do the math" 5. "Put your business on autopilot" 6. "Install it in 15 minutes" 7. "Start free" 8. "Get instant access" 9. "Book the install call" 10. "Try it — 14-day refund" 11. "Own your stack" 12. "Stop losing leads" 13. "Pick your squad" 14. "Watch the live install" 15. "Cancel the VA" 16. "Claim launch price" 17. "Finish your setup" 18. "Read the roster" 19. "Deploy now" 20. "See what $149 buys"

---

## PHASE 9 — Landing Page / Funnel Audit

**Conversion bottlenecks**
- 🔴 **Broken checkout** (`REPLACE.lemonsqueezy.com`) — fix before anything else.
- 🔴 **No email capture** — cold $149 traffic that doesn't buy is lost forever. Add the **3-free-workers** opt-in + exit-intent.
- 🔴 **No proof** — add: a real install demo video, founder face/name, GitHub or build-in-public link, beta-user quotes, "be one of the first" honest framing, and the n8n logo/"works with" badges.

**Messaging issues**
- "No subscription" collides with "Requires Claude Pro $20/mo" + bring-your-own-n8n. **Reframe:** "One payment to us. You bring n8n + an Anthropic key — here's exactly what that costs ($0–$20/mo)." Pre-empt the refund.
- "No code" overpromises vs CLI/`config.env`. **Reframe:** "No-code-*needed* — copy, paste, run 3 commands," with a 20-second screen clip proving it.
- Vague counts ("+4 more," "+1 more") undercut the "38" specificity. List all 38 by name.

**Trust issues**
- Empty FAQ answers (several questions show no answer). Fill every one — especially "Will it work for my business?" (answer with concrete niches) and "What if I get stuck?" (support promise + DWY option).
- Anonymous founder. A face + name + "why I built this" closes the credibility gap better than any badge.

**Design / UX**
- Add sticky CTA + price on scroll; a comparison table (Loadout vs VA vs agency vs SaaS vs template dump); a visible 14-day-refund seal near both buttons; a short looping install demo above the fold.
- The gaming connotation of "loadout" — make the hero unmistakably "AI workers for your business" in the first 2 seconds.

**Funnel leaks (in order of $ impact)**
1. Dead checkout → **100% leak.** 2. No email capture → ~95% of non-buyers lost. 3. No retargeting pixel/CAPI → can't recover warm traffic. 4. No post-purchase upsell sequence for DWY ($497). 5. No abandoned-cart flow on LemonSqueezy. 6. No "which worker first" onboarding → setup abandonment → refunds.

---

## PHASE 10 — Final Deliverable

### Best Meta campaign
**"Own It, Don't Rent It" — Lead-magnet → nurture → sell.** Broad Advantage+ audience (Tier-1 EN, AI/automation/n8n/solopreneur signals). Top creative: **#19 competitor-math** primary text + **TikTok concept #61** ("template packs are a scam") video. Optimize for **lead** (3 free workers) to build a cheap retargeting list, then convert on email + retargeting. *Why it wins:* sidesteps the no-proof problem and the cold-$149 friction.

### Best Google campaign
**Bottom-funnel exact/phrase search** on `n8n templates`, `prebuilt n8n workflows`, `done for you n8n`, `lindy/gumloop alternative`, with the gaming negative list locked in. Tiny budget, highest intent, lowest CPA. *Why it wins:* these searchers already want exactly this; you just have to show up cheaper-and-curated.

### Best video campaign
**Founder-led transparency**: concept **#27** ("install it live, mistakes and all") + **#23** ("exactly what you get, no hype"). *Why it wins:* manufactures the trust the site is missing, and the unedited install *proves* the 15-min / no-code claims.

### Best retargeting campaign
**Objection-killer dynamic retargeting** to pricing/checkout visitors + email openers: refund-forward (#20), competitor-math (#19), and DWY rescue ("stuck? I'll install it for you"). Add abandoned-cart email. *Why it wins:* warm, already-interested, cheapest conversions you'll get.

### $120 budget allocation (a TEST, not a scale)
| Channel | Spend | Goal |
|---|---|---|
| Meta lead-gen (3 free workers) | **$60** | Cheapest possible emails + find the winning hook (read CTR/CPL, not just sales) |
| Google Search (exact/phrase, bottom-funnel) | **$35** | Capture existing high-intent demand at lowest CPA |
| Retargeting (Meta, site + openers) | **$25** | Convert the warm — turns on once pixel has data |
| Organic Reels/TikTok/Shorts | **$0** | Highest-leverage channel for this niche — post 3–5×/wk from Phase 7 |

> $120 buys *signal, not scale*. Expect maybe 1–3 sales and a small email list — the real deliverable at this budget is **a validated hook + CPL/CPA benchmarks** to justify scaling.

### Ranked by expected profitability
1. **Organic short-form** (n8n/AI niche is hot; $0 cost) 2. **Email nurture off the free-worker magnet** 3. **Google bottom-funnel search** 4. **Meta retargeting** 5. **Meta cold lead-gen** 6. **Meta cold direct-purchase** 7. **DWY $497 upsell** to warm buyers.

---

### Self-critique (challenged assumptions, weaknesses, improvements)
- **Assumption I rejected:** the site's "non-technical SMB owner." The CLI/API-key reality means that buyer churns and refunds. I re-aimed the entire avatar at technically-comfortable operators/agencies. *If you genuinely want non-technical buyers, the hero offer must become the $497 Done-With-You, and the ad math changes — tell me and I'll re-cut it.*
- **Biggest weakness in my own plan:** it leans on a **free-worker lead magnet that doesn't exist yet**. If you can't carve 3 workers out as a free taste, fall back to a **free roster PDF + install-demo video** as the opt-in, and lead retargeting with the refund + competitor-math angles.
- **Second weakness:** no creative proof assets exist. The founder/UGC concepts are doing the heavy lifting *in place of* testimonials — film 2–3 founder videos *before* launch.
- **Honesty pass:** I removed/flagged every "social proof" and "scarcity" claim that isn't literally true yet. Don't fake reviews or fake "slots left" — at this stage your credibility *is* the product.
- **De-generic-ified:** cut "unlock/supercharge/revolutionize/seamless." Rewrote in operator language ("drowning in admin," "leads go cold," "not another subscription," "own your stack," "I'll automate it later").
- **The uncomfortable truth:** with a dead checkout, no proof, and $120, the highest-ROI action this week isn't ads at all — it's **fix checkout → add email capture → film one honest install video → post organically.** Spend the $120 only after those four are done.

---

### Immediate next-action checklist
1. ☐ Replace `REPLACE.lemonsqueezy.com` with live product URLs (blocks everything).
2. ☐ Add email capture (3 free workers *or* roster PDF) + Meta Pixel/CAPI + Google tag.
3. ☐ Fill all FAQ answers; add the "$0–$20/mo, here's the real cost" honesty box.
4. ☐ Film: one 15-min real install (founder) + one 30-sec "scam packs vs 38" short.
5. ☐ Launch Google exact/phrase ($35) + Meta lead-gen ($60) with the gaming negatives.
6. ☐ Turn on retargeting + abandoned-cart once pixel/list has data.
