# Alternate futures — named assumption groups

The routine's standing set (see `project/conventions/project-schemas.md` and D-10). The Reporter produces
one outlook section per **enabled** future, its assumptions superseding the facts they speak to. Flip
`enabled` to include or exclude a future. The fact-based base outlook is always produced and needs no entry.

### escalation: NATO–Russia escalation
enabled:     true
description: A deliberately ambiguous Russia–NATO incident occurs within six months.
assumptions:
  - A confirmed Article-5-ambiguous incident against a NATO member occurs in the next 6 months.
  - Markets react risk-off fast, as with any Tier-0 shock.

### dovish-pivot: Fed dovish pivot
enabled:     false
description: The Fed signals a clear easing path at the next meeting.
assumptions:
  - The Fed cuts or clearly signals cuts at the September FOMC, ending the current hawkish uncertainty.
  - Real yields and the dollar fall in response.
