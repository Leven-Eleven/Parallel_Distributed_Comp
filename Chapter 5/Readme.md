## Async

# Asyncconcurrent.py

Sequential vs Thread Pool vs Process Pool (CPU-bound parallelism)
Simulates a game engine validating assets such as enemies, NPCs, and bosses before a level loads.
More complex assets require more computation.
The same workload is executed using three methods:
* Sequential execution (single worker)
* ThreadPoolExecutor (multiple threads)
* ProcessPoolExecutor (multiple processes)


This mirrors real-world engine pipelines where heavy validation or preprocessing must scale across cores. It clearly shows when multiprocessing beats multithreading.


<img width="600" height="646" alt="image" src="https://github.com/user-attachments/assets/9a79e762-ad70-4a56-b05c-379305760097" />




<img width="613" height="541" alt="image" src="https://github.com/user-attachments/assets/fc42835a-12e9-4f53-8c40-64e06e5ef891" />



# Eventlooping.py

Async Event Loop Scheduling (non-blocking orchestration)
Simulates a game engine runtime that rotates between:
* AI system updates
* Physics simulation
* World event processing
Each subsystem runs asynchronously and schedules the next system using the event loop.

Game engines often rely on a single main loop that must stay responsive. Async allows multiple systems to make progress without blocking, even though everything runs on one thread.


<img width="527" height="633" alt="image" src="https://github.com/user-attachments/assets/10305177-f316-495e-8f7a-8ad9dff285da" />
<img width="566" height="619" alt="image" src="https://github.com/user-attachments/assets/c6a83cc4-206a-4107-80ee-dff887bc786d" />





# Orderproc.py
Async Ordered Execution (deterministic workflow)

Runs core game systems in a fixed order:
1. AI scan
2. Resource update
3. Environment monitoring
Each async task schedules the next, forming a controlled execution pipeline.

Parallel & Distributed Computing Concept
* Asynchronous but **not parallel**
* Deterministic task ordering
* Cooperative scheduling without race conditions

Many simulations require strict ordering (e.g., AI before physics). This demonstrates how async can be used for coordination, not just concurrency.



<img width="490" height="571" alt="image" src="https://github.com/user-attachments/assets/a8afcc3a-0281-4440-a4f1-a432e29b0d73" />
<img width="566" height="628" alt="image" src="https://github.com/user-attachments/assets/85f9da66-7dc9-4c5d-b061-6030edf6b172" />





# ParellelAnalytics.py
Async Parallel Analytics (concurrent pipelines)

Runs multiple analytics pipelines in parallel:
* Match score calculation
* Player activity tracking
* Loot distribution analysis
All tasks start together and execute concurrently using a shared event loop.

Parallel & Distributed Computing Concept
* Asynchronous parallel execution
* Independent tasks sharing a single event loop
* Non-blocking analytics pipelines


