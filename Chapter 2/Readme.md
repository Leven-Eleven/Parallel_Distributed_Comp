To ensure that threads which are accessing shared resources execute safely without any corruptions or race conditions, we synchronize them using different mechanisms.
The mechanisms explored here are Locks, RLocks, and Semaphores.
Each mechanism is tested on mulitiple threads doing the same task.

Locks:


<img width="569" height="143" alt="image" src="https://github.com/user-attachments/assets/bfde2f92-0ca7-439c-b444-b7fb7cd2c050" />

RLocks:


<img width="571" height="128" alt="image" src="https://github.com/user-attachments/assets/f70a9e2b-7187-4909-a69d-034fa7a7a2cf" />

Semaphores:


<img width="569" height="136" alt="image" src="https://github.com/user-attachments/assets/75b107b4-e57c-4efa-bb2f-8ef110eb8458" />

Ultimately, all these mechanisms prevent race condition. While its easy to judge which mechanism is the most efficient, we also have to remember that each mechanism provides its own niche uses and drawbacks. To highlight some:
Semaphores are a great way to limit the amount of threads accessing shared resource(like a waiting list).
Rlocks provide ownership of the lock to a thread that is given access to it, allowing it to lock multiple times, but this comes with the disadvantage of overhead.
