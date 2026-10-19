# Distribution-shift follow-up

Written after the four initial runs, before generating or evaluating the new
cohort. Initial reuse policies solved almost all random-walk starts at 1,024
pops; common-target students also approached that ceiling. This leaves the
size and persistence of the advantage on harder starts unresolved.

Freeze every saved parameter and algorithm. For each seed, generate 128 new
uniformly shuffled permutations with even inversion parity (the solvable 3x3
states), excluding every original start from every seed and the new starts
already drawn. Use RNG seed `100000 + seed`. No distance oracle or filtering
by solver success is used. Evaluate at 64,256,1,024 pops. The focal comparison
is reuse_ce versus frozen_ce at 256 pops; inspect both the final solvers and
the common-target students. Also assess the existing local/portfolio harnesses.

This is a new task-sampling distribution in the same puzzle domain, not a new
domain or independent preregistration of the initial research hypothesis.
It is a declared follow-up motivated by ceiling effects. It supplies no new
training, selection or hyperparameter choices. Preserve its tasks and results
separately, and report the full cap curve rather than selecting a winning cap.
