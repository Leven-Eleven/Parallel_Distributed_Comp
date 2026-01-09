import asyncio
import random


async def ai_scan(end_time, loop):
    """
    Task A: AI Scan
    
    Game scenario:
    - Scans nearby enemies
    - Evaluates threat levels
    - Triggers combat logic if needed
    """
    print("[AI] Scanning nearby enemies...")

    scan_time = random.randint(1, 3)
    await asyncio.sleep(scan_time)
    threat_level = random.randint(0, 100)

    if threat_level > 70:
        print(f"⚠ High threat detected ({threat_level}) - Preparing combat AI!")
    else:
        print(f"✓ Area secure (threat level {threat_level})")

    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: Resource System in 1 second...\n")
        asyncio.create_task(resource_update(end_time, loop))
    else:
        print("\n⏰ Simulation complete. Shutting down...")


async def resource_update(end_time, loop):
    """
    Task B: Resource Update
    
    Game scenario:
    - Regenerates mana/energy
    - Updates stamina for entities
    """
    entities = ["Player", "Mage NPC", "Boss Enemy", "Companion"]
    entity = random.choice(entities)
    resource_gain = random.randint(5, 20)

    print(f"[RESOURCES] Updating {entity} (+{resource_gain} energy)")

    update_time = random.randint(1, 3)
    await asyncio.sleep(update_time)

    print(f"✓ {entity} resources updated (took {update_time}s)")

    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: Environment Monitor in 1 second...\n")
        asyncio.create_task(environment_monitor(end_time, loop))
    else:
        print("\n⏰ Simulation complete. Shutting down...")


async def environment_monitor(end_time, loop):
    """
    Task C: Environment Monitor
    
    Game scenario:
    - Tracks world conditions
    - Triggers environmental effects
    """
    zones = ["Dungeon", "Forest", "Volcano", "Frozen Tundra"]
    zone = random.choice(zones)
    intensity = random.randint(0, 100)

    print(f"[ENVIRONMENT] Monitoring {zone} conditions...")

    check_time = random.randint(1, 3)
    await asyncio.sleep(check_time)

    if intensity > 75:
        print(f"⚡ Environmental hazard active in {zone}!")
    elif intensity < 30:
        print(f"🌿 {zone} is calm and stable.")
    else:
        print(f"✓ {zone} operating under normal conditions.")

    if (loop.time() + 1.0) < end_time:
        print("   → Scheduling: AI Scan in 1 second...\n")
        print("-" * 50)
        asyncio.create_task(ai_scan(end_time, loop))
    else:
        print("\n⏰ Simulation complete. Shutting down...")


async def main():
    """
    Runs the game runtime systems for 30 seconds using ordered async execution.
    """
    print("=" * 60)
    print("GAME RUNTIME SYSTEM")
    print("Async Ordered Processing Demonstration")
    print("=" * 60)

    print("\nThis system rotates through core game subsystems:")
    print("1. AI Scan")
    print("2. Resource Update")
    print("3. Environment Monitoring")

    print("\nRunning simulation for 30 seconds...")
    print("=" * 60 + "\n")

    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 30

    # Kick off the first subsystem
    asyncio.create_task(ai_scan(end_loop, loop))

    # Keep the event loop alive for the duration
    await asyncio.sleep(30)

    print("\n" + "=" * 60)
    print("GAME RUNTIME STOPPED")
    print("All systems safely halted")
    print("=" * 60)


if __name__ == '__main__':
    asyncio.run(main())
