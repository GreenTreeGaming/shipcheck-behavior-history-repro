# ShipCheck Behavior History Repro

Small multi-file fixture for testing ShipCheck Behavior Guards, Behavioral Diff, and historical behavior-origin mining.

The repository models a tenant purge operation with session-based administrator authorization.

The git history intentionally evolves the behavior over several commits so ShipCheck can distinguish the commit that merely adds auth utilities from the later commit that actually enforces authentication on the purge path.
