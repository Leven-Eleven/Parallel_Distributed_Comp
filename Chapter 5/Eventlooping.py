import asyncio
import random
"""Asyncio Event Loop Demonstration for Game Engine Runtime"""

async def ai_system_tick(end_time, loop):
    """
    Task A: AI System Update
    """
    print("[AI SYSTEM] Updating enemy AI states...")

    update_time = random.randint(1, 3)
    await asyncio.sleep(update_time)

    print(f"   ✓ AI logic updated in {update_time}s (pathfinding + decisions OK)")

    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: Physics System in 1 second...\n")
        loop.call_later(1, asyncio.create_task, physics_system_tick(end_time, loop))
    else:
        print("\nGame simulation complete. Shutting down engine...")
        loop.stop()


async def physics_system_tick(end_time, loop):
    """
    Task B: Physics System Update
    """
    active_objects = random.randint(10, 50)
    print(f"[PHYSICS] Processing {active_objects} active entities...")

    sim_time = random.randint(1, 3)
    await asyncio.sleep(sim_time)

    print(f"   ✓ Collision & movement resolved (took {sim_time}s)")

    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: World Event System in 1 second...\n")
        loop.call_later(1, asyncio.create_task, world_event_tick(end_time, loop))
    else:
        print("\nGame simulation complete. Shutting down engine...")
        loop.stop()


async def world_event_tick(end_time, loop):
    """
    Task C: World Event System
    """
    events = [
        "Loot Drop Triggered",
        "Enemy Spawned",
        "Day–Night Cycle Updated",
        "Boss Phase Changed",
        "Environmental Hazard Activated"
    ]

    event = random.choice(events)
    print(f"[WORLD EVENT] Processing event: {event}")

    event_time = random.randint(1, 3)
    await asyncio.sleep(event_time)

    print(f"   ✓ Event resolved successfully (took {event_time}s)")

    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: AI System in 1 second...\n")
        print("-" * 55)
        loop.call_later(1, asyncio.create_task, ai_system_tick(end_time, loop))
    else:
        print("\nGame simulation complete. Shutting down engine...")
        loop.stop()


# -------------------------------------------------
# MAIN LOOP
# -------------------------------------------------
if __name__ == '__main__':
    print("=" * 60)
    print("        GAME ENGINE RUNTIME SCHEDULER")
    print("        Asyncio Event Loop Demonstration")
    print("=" * 60)

    print("\nThis engine cycles between core runtime systems:")
    print("  1. AI System Updates")
    print("  2. Physics Simulation")
    print("  3. World Event Processing")

    print("\nRunning simulation for 30 seconds...")
    print("=" * 60 + "\n")

    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 30

    # Kick off the first system
    loop.call_soon(asyncio.create_task, ai_system_tick(end_loop, loop))

    loop.run_forever()
    loop.close()

    print("\n" + "=" * 60)
    print("        GAME ENGINE STOPPED")
    print("        All systems safely halted")
    print("=" * 60)
