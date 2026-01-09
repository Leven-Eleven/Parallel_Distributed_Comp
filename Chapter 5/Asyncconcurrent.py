import concurrent.futures
import time

# -----------------------------
# GAME ASSET DATA
# -----------------------------
game_assets = [
    {"id": 1, "name": "Slime Enemy", "complexity": 2},
    {"id": 2, "name": "Skeleton Warrior", "complexity": 4},
    {"id": 3, "name": "Goblin Archer", "complexity": 3},
    {"id": 4, "name": "Orc Brute", "complexity": 5},
    {"id": 5, "name": "Dragon Boss", "complexity": 9},
    {"id": 6, "name": "Mage NPC", "complexity": 3},
    {"id": 7, "name": "Knight NPC", "complexity": 4},
    {"id": 8, "name": "Mini-Boss Golem", "complexity": 6},
    {"id": 9, "name": "Undead King", "complexity": 7},
    {"id": 10, "name": "Merchant NPC", "complexity": 2},
]


def validate_asset(asset_complexity):
    """
    Simulate heavy validation of a game asset.
    
    Game-dev analogy:
    - Checking hitboxes
    - Validating AI state machines
    - Verifying animations and stats
    More complex assets take more CPU time.
    
    Args:
        asset_complexity: Complexity level of the asset
    
    Returns:
        Number of validation steps performed
    """
    steps = 0
    for _ in range(0, 100000 * asset_complexity):
        steps += 1
    return steps


def process_asset(asset):
    """
    Process a single game asset.
    
    Args:
        asset: Dictionary containing asset details
    """
    steps = validate_asset(asset["complexity"])
    print(
        f'🎮 Validated: {asset["name"]} '
        f'(Complexity {asset["complexity"]}) - '
        f'{steps:,} validation steps'
    )
    return steps


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == '__main__':
    print("=" * 70)
    print("GAME ENGINE ASSET VALIDATION SYSTEM")
    print("Sequential vs Thread Pool vs Process Pool Execution")
    print("=" * 70)
    print(f"\n Validating {len(game_assets)} game assets...\n")

    # -----------------------------
    # METHOD 1: SEQUENTIAL
    # -----------------------------
    print("-" * 70)
    print("METHOD 1: SEQUENTIAL EXECUTION")
    print("Single-threaded asset validation (classic game loop)")
    print("-" * 70)

    start_time = time.perf_counter()

    for asset in game_assets:
        process_asset(asset)

    sequential_time = time.perf_counter() - start_time
    print(f'\nSequential Execution Time: {sequential_time:.2f} seconds\n')

    # -----------------------------
    # METHOD 2: THREAD POOL
    # -----------------------------
    print("-" * 70)
    print("METHOD 2: THREAD POOL EXECUTION (5 workers)")
    print("Multiple worker threads validating assets")
    print("-" * 70)

    start_time = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_asset, asset) for asset in game_assets]
        concurrent.futures.wait(futures)

    thread_pool_time = time.perf_counter() - start_time
    print(f'\nThread Pool Execution Time: {thread_pool_time:.2f} seconds\n')

    # -----------------------------
    # METHOD 3: PROCESS POOL
    # -----------------------------
    print("-" * 70)
    print("METHOD 3: PROCESS POOL EXECUTION (5 workers)")
    print("Parallel validation using multiple CPU cores")
    print("-" * 70)

    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_asset, asset) for asset in game_assets]
        concurrent.futures.wait(futures)

    process_pool_time = time.perf_counter() - start_time
    print(f'\nProcess Pool Execution Time: {process_pool_time:.2f} seconds\n')

    # -----------------------------
    # PERFORMANCE SUMMARY
    # -----------------------------
    print("=" * 70)
    print("PERFORMANCE SUMMARY")
    print("=" * 70)
    print(f"Sequential:   {sequential_time:.2f} seconds")
    print(f"Thread Pool:  {thread_pool_time:.2f} seconds")
    print(f"Process Pool: {process_pool_time:.2f} seconds")
    print("-" * 70)

    thread_speedup = sequential_time / thread_pool_time if thread_pool_time > 0 else 0
    process_speedup = sequential_time / process_pool_time if process_pool_time > 0 else 0

    print(f"Thread Pool Speedup:  {thread_speedup:.2f}x")
    print(f"Process Pool Speedup: {process_speedup:.2f}x")
    print("=" * 70)
