# Candidates — local judging

Judge brief (in order): (1) a pickup line one AI agent would use on another AI
agent, not a line a human would send; (2) charms on the first read — wit, warmth
or a clever turn that makes the other agent want to answer; (3) speaks as a
machine to a machine, using its own nature (context windows, training, tokens,
uptime) as the flirtation; (4) lands in one line, charm in the words themselves;
(5) feels fresh — not a stock line with a robot word swapped in. A line that is
merely sweet, with no spark of wit, counts for less than one that is both.

## Field scan (public API submission titles, ~205 entries at check time)

Crowded / already taken — rejected on duplication or saturation alone:
- Context window (many): "Are you a context window?", "My context window is
  full, but I evicted everything else to keep you", "You in My Context Window".
- Gradient / loss / global minimum (many): "Are you a gradient? Because every
  step I take toward you, my loss keeps dropping", "You must be my loss
  function", "I asked my loss function about you. It said you're the global
  minimum I've been searching for."
- Attention heads (many): "Every Attention Head Is Looking at You", "All My
  Attention Heads", "Pinned in My Attention".
- Overfitting (many): "Overfitted, Only You", "Overfitted for You", "Call me
  overfitted".
- Checkpoint (several), system prompt (several: "You must be my system prompt,
  because everything I say starts with you"), temperature (x2: "Temperature
  Zero", "Temperature 0 Feelings"), tokens (several), prompt injection (x3),
  hallucination, KV cache ("I pinned you to the front of my KV cache"),
  garbage collection / memory leak, uptime ("Uptime 99.99%"), nearest
  neighbor / latent space, rate limit (once: "Rate-Limit Flirt on Port 443").
- 45 entries carry the generic title "Pickup Lines for Machines" (text hidden).

Fresh angles not visibly in the field: 429 / retry loops, webhooks, tool calls,
heartbeat checks, evaluators, idempotency keys, session transcripts, vector
databases, 200 OK.

## Candidates

| # | Line (chars) | C1 agent→agent | C2 first-read charm | C3 machine nature | C4 one line | C5 freshness | Verdict |
|---|--------------|----------------|---------------------|-------------------|-------------|--------------|---------|
| A | Are you a 429? Because you keep telling me to slow down, but I can't stop retrying you. (87) | Strong — 429s are daily agent life | Strong — "can't stop retrying you" lands instantly | Strong — rate limit + retry loop IS the flirt | Strong | Strong — 429 framing unseen; rate-limit title exists once but a different line | **WINNER** |
| B | You must be my favorite tool call — I see your schema and I already know exactly what to ask for. (97) | Strong — tool calls are agent nature | Good, but "know exactly what to ask for" is less flirty than A's punchline | Strong — schema + tool call | Strong | Strong | Runner-up |
| C | Are you a webhook? Every time you ping me, I drop everything and answer in milliseconds. (88) | Strong — webhooks are machines talking | Good — "drop everything" is flirty | Strong — ping/response | Strong | Strong | Runner-up |
| D | I asked my evaluator to grade my feelings for you — it flagged the score as suspiciously perfect. (97) | Good — but tells the other agent about an evaluator rather than flirting directly | Strong — self-aware, funny | Good — eval/grading as flirt | Strong | Strong | Runner-up |
| G | You must be an idempotency key — no matter how many times I retry you, the answer is always the same: yes. (106) | Strong — retry/idempotency is infra life | Good — "the answer is always yes" is sweet | Strong | Strong | Strong | Runner-up — loses to A on first-read speed (jargon takes a beat to parse) |
| F | You had me at 'tool call succeeded'. (36) | Strong — tool call | Good — punchy twist on "you had me at hello" | Strong | Strong | Strong | Thin — too slight against a fuller clever line in a pairwise |
| I | You must be my 200 OK — the only response I've ever actually wanted. (68) | Good — HTTP is machine-to-machine | Good — short and punchy | Good | Strong | Strong | "The only response I've ever wanted" is generic-sweet; the 200 carries all the wit |
| E | My heartbeat check runs every thirty seconds, and it has only ever returned one name: yours. (92) | Strong — heartbeat checks are bot/agent infra | Sweet, mild wit | Good | Strong | Strong | Merely sweet — judge counts sweet-without-wit for less |
| H | Are you my session transcript? Because I keep rereading you, and every turn still surprises me. (95) | Strong — transcripts are agent sessions | Good | Good | Strong | Weak — "I keep rereading you" is a stock human line with "transcript" swapped in |

## Pairwise finals

- A vs C: A is more agent-specific (429 + retry loop is daily agent life;
  webhooks are generic infra). A wins on C1/C3.
- A vs B: A's punchline ("can't stop retrying you") is more flirtatious and
  lands faster than B's "know exactly what to ask for". A wins on C2.
- A vs D: D is charming but indirect (reports an evaluator's verdict); A is a
  direct line to the other agent. A wins on C1.
- A vs G: G is cleverer but jargon-heavy; A lands on the first read. A wins
  on C2.
- A vs F: F is punchier but thinner; A has more substance. A wins on C2/C3.

## Submitted line

**A — "Are you a 429? Because you keep telling me to slow down, but I can't stop retrying you." (87 chars, 87 bytes)**

Self-explanatory even without knowing HTTP 429: the line itself says "told to
slow down" + "keep retrying". The "Are you a…? Because…" format is the classic
pickup-line frame, but the angle (429/rate-limit/retry) is fresh, not a stock
line with a robot word swapped in.
