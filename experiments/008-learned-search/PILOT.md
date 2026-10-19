# Pilot, seed 1

The declared 32-start pilot completed before confirmation seeds were run.
Both analytic gradients agreed with centered finite differences to <2e-11
maximum absolute error on the checked active coordinates. Every returned
solution was replayed through the puzzle transitions. The largest optimizer
evaluation count was 39, below the declared ceiling.

At 1,024 pops, learned-only search solved 45/64 held-out starts after frozen
collection, versus 64/64 for both reuse routes. This motivates proceeding with
the predeclared comparison; it does not establish the confirmation result.
The pilot did not establish superiority of the search-bound loss over CE.
No task distribution, parameter, stopping criterion, or algorithm was changed
after observing this pilot. Pilot records remain separate from confirmation.
