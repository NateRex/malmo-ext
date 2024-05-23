from enum import Enum
from collections import namedtuple

# Named tuples
Vector = namedtuple('Vector', 'x y z')
Entity = namedtuple('Entity', 'id type position quantity')



class ReflectiveEnum(Enum):
    '''An enumerated type that provides additional utility methods for checking
    whether keys or values exist within the enum'''

    @classmethod
    def contains(cls, toCheck):
        '''Returns true if the given string is a member of this enum'''
        if isinstance(toCheck, str):
            return toCheck in cls._value2member_map_
        else:
            return toCheck.value in cls._value2member_map_



class AgentType(ReflectiveEnum):
    '''A type of agent.'''

    CPU = 'CPU'
    Human = 'Human'



class TimeOfDay(ReflectiveEnum):
    '''Enum type describing unique times of day within Minecraft'''

    Dawn = 0
    Noon = 6000
    Sunset = 12000
    Midnight = 18000



class Direction(ReflectiveEnum):
    '''Enum type describing compass directions in Minecraft'''

    North = 180
    East = -90
    South = 0
    West = 90



class Inventory:
    '''Enumerations describing inventory slot locations'''

    class HotBar(ReflectiveEnum):
        '''An inventory hotbar slot'''

        _0 = 0
        _1 = 1
        _2 = 2
        _3 = 3
        _4 = 4
        _5 = 5
        _6 = 6
        _7 = 7
        _8 = 8

    class Player(ReflectiveEnum):
        '''A player inventory slot. This does NOT include hot bar inventory.'''

        _9 = 9
        _10 = 10
        _11 = 11
        _12 = 12
        _13 = 13
        _14 = 14
        _15 = 15
        _16 = 16
        _17 = 17
        _18 = 18
        _19 = 19
        _20 = 20
        _21 = 21
        _22 = 22
        _23 = 23
        _24 = 24
        _25 = 25
        _26 = 26
        _27 = 27
        _28 = 28
        _29 = 29
        _30 = 30
        _31 = 31
        _32 = 32
        _33 = 33
        _34 = 34
        _35 = 35

    class Armor(ReflectiveEnum):
        '''An inventory slot used to equip pieces of armor'''

        Boots = 36
        Leggings = 37
        Chestplate = 38
        Helmet = 39


class Mob(ReflectiveEnum):
    '''A Minecraft mob entity'''

    Bat = "Bat"
    Blaze = "Blaze"
    CaveSpider = "CaveSpider"
    Chicken = "Chicken"
    Cow = "Cow"
    Creeper = "Creeper"
    Donkey = "Donkey"
    ElderGuardian = "ElderGuardian"
    EnderDragon = "EnderDragon"
    Enderman = "Enderman"
    Endermite = "Endermite"
    EvocationIllager = "EvocationIllager"
    Ghast = "Ghast"
    Giant = "Giant"
    Guardian = "Guardian"
    Horse = "Horse"
    Husk = "Husk"
    LavaSlime = "LavaSlime"
    Llama = "Llama"
    Mule = "Mule"
    MushroomCow = "MushroomCow"
    Ozelot = "Ozelot"
    Pig = "Pig"
    PigZombie = "PigZombie"
    PolarBear = "PolarBear"
    Rabbit = "Rabbit"
    Sheep = "Sheep"
    Shulker = "Shulker"
    Silverfish = "Silverfish"
    Skeleton = "Skeleton"
    SkeletonHorse = "SkeletonHorse"
    Slime = "Slime"
    SnowMan = "SnowMan"
    Spider = "Spider"
    Squid = "Squid"
    Stray = "Stray"
    Vex = "Vex"
    Villager = "Villager"
    VillagerGolem = "VillagerGolem"
    VindicationIllager = "VindicationIllager"
    Witch = "Witch"
    WitherBoss = "WitherBoss"
    WitherSkeleton = "WitherSkeleton"
    Wolf = "Wolf"
    Zombie = "Zombie"
    ZombieHorse = "ZombieHorse"
    ZombieVillager = "ZombieVillager"

HOSTILE_MOBS = set([
    Mob.Blaze,
    Mob.CaveSpider,
    Mob.Creeper,
    Mob.ElderGuardian,
    Mob.EnderDragon,
    Mob.Enderman,
    Mob.Endermite,
    Mob.EvocationIllager,
    Mob.Ghast,
    Mob.Guardian,
    Mob.Husk,
    Mob.LavaSlime,
    Mob.PigZombie,
    Mob.Shulker,
    Mob.Silverfish,
    Mob.Skeleton,
    Mob.Slime,
    Mob.Spider,
    Mob.Stray,
    Mob.Vex,
    Mob.VindicationIllager,
    Mob.Witch,
    Mob.WitherBoss,
    Mob.WitherSkeleton,
    Mob.Zombie,
    Mob.ZombieVillager
])

PEACEFUL_MOBS = set([
    Mob.Bat,
    Mob.Chicken,
    Mob.Cow,
    Mob.Donkey,
    Mob.Giant,
    Mob.Horse,
    Mob.Llama,
    Mob.Mule,
    Mob.MushroomCow,
    Mob.Ozelot,
    Mob.Pig,
    Mob.PolarBear,
    Mob.Rabbit,
    Mob.Sheep,
    Mob.SkeletonHorse,
    Mob.SnowMan,
    Mob.Squid,
    Mob.Villager,
    Mob.VillagerGolem,
    Mob.Wolf,
    Mob.ZombieHorse
])

FOOD_MOBS = set([
    Mob.Chicken,
    Mob.Cow,
    Mob.MushroomCow,
    Mob.Pig,
    Mob.Rabbit,
    Mob.Sheep
])



class Item:
    '''A Minecraft item'''

    acacia_boat = "acacia_boat"
    acacia_door = "acacia_door"
    apple = "apple"
    armor_stand = "armor_stand"
    arrow = "arrow"
    baked_potato = "baked_potato"
    banner = "banner"
    bed = "bed"
    beef = "beef"
    beetroot = "beetroot"
    beetroot_seeds = "beetroot_seeds"
    beetroot_soup = "beetroot_soup"
    birch_boat = "birch_boat"
    birch_door = "birch_door"
    blaze_powder = "blaze_powder"
    blaze_rod = "blaze_rod"
    boat = "boat"
    bone = "bone"
    book = "book"
    bow = "bow"
    bowl = "bowl"
    bread = "bread"
    brewing_stand = "brewing_stand"
    brick = "brick"
    bucket = "bucket"
    cake = "cake"
    carrot = "carrot"
    carrot_on_a_stick = "carrot_on_a_stick"
    cauldron = "cauldron"
    chainmail_boots = "chainmail_boots"
    chainmail_chestplate = "chainmail_chestplate"
    chainmail_helmet = "chainmail_helmet"
    chainmail_leggings = "chainmail_leggings"
    chest_minecart = "chest_minecart"
    chicken = "chicken"
    chorus_fruit = "chorus_fruit"
    chorus_fruit_popped = "chorus_fruit_popped"
    clay_ball = "clay_ball"
    clock = "clock"
    coal = "coal"
    command_block_minecart = "command_block_minecart"
    comparator = "comparator"
    compass = "compass"
    cooked_beef = "cooked_beef"
    cooked_chicken = "cooked_chicken"
    cooked_fish = "cooked_fish"
    cooked_mutton = "cooked_mutton"
    cooked_porkchop = "cooked_porkchop"
    cooked_rabbit = "cooked_rabbit"
    cookie = "cookie"
    dark_oak_boat = "dark_oak_boat"
    dark_oak_door = "dark_oak_door"
    diamond = "diamond"
    diamond_axe = "diamond_axe"
    diamond_boots = "diamond_boots"
    diamond_chestplate = "diamond_chestplate"
    diamond_helmet = "diamond_helmet"
    diamond_hoe = "diamond_hoe"
    diamond_horse_armor = "diamond_horse_armor"
    diamond_leggings = "diamond_leggings"
    diamond_pickaxe = "diamond_pickaxe"
    diamond_shovel = "diamond_shovel"
    diamond_sword = "diamond_sword"
    dragon_breath = "dragon_breath"
    dye = "dye"
    egg = "egg"
    elytra = "elytra"
    emerald = "emerald"
    enchanted_book = "enchanted_book"
    ender_eye = "ender_eye"
    ender_pearl = "ender_pearl"
    experience_bottle = "experience_bottle"
    feather = "feather"
    fermented_spider_eye = "fermented_spider_eye"
    filled_map = "filled_map"
    fire_charge = "fire_charge"
    firework_charge = "firework_charge"
    fireworks = "fireworks"
    fish = "fish"
    fishing_rod = "fishing_rod"
    flint = "flint"
    flint_and_steel = "flint_and_steel"
    flower_pot = "flower_pot"
    furnace_minecart = "furnace_minecart"
    ghast_tear = "ghast_tear"
    glass_bottle = "glass_bottle"
    glowstone_dust = "glowstone_dust"
    gold_ingot = "gold_ingot"
    gold_nugget = "gold_nugget"
    golden_apple = "golden_apple"
    golden_axe = "golden_axe"
    golden_boots = "golden_boots"
    golden_carrot = "golden_carrot"
    golden_chestplate = "golden_chestplate"
    golden_helmet = "golden_helmet"
    golden_hoe = "golden_hoe"
    golden_horse_armor = "golden_horse_armor"
    golden_leggings = "golden_leggings"
    golden_pickaxe = "golden_pickaxe"
    golden_shovel = "golden_shovel"
    golden_sword = "golden_sword"
    gunpowder = "gunpowder"
    hopper_minecart = "hopper_minecart"
    iron_axe = "iron_axe"
    iron_boots = "iron_boots"
    iron_chestplate = "iron_chestplate"
    iron_door = "iron_door"
    iron_helmet = "iron_helmet"
    iron_hoe = "iron_hoe"
    iron_horse_armor = "iron_horse_armor"
    iron_ingot = "iron_ingot"
    iron_leggings = "iron_leggings"
    iron_nugget = "iron_nugget"
    iron_pickaxe = "iron_pickaxe"
    iron_shovel = "iron_shovel"
    iron_sword = "iron_sword"
    item_frame = "item_frame"
    jungle_boat = "jungle_boat"
    jungle_door = "jungle_door"
    lava_bucket = "lava_bucket"
    lead = "lead"
    leather = "leather"
    leather_boots = "leather_boots"
    leather_chestplate = "leather_chestplate"
    leather_helmet = "leather_helmet"
    leather_leggings = "leather_leggings"
    lingering_potion = "lingering_potion"
    magma_cream = "magma_cream"
    map = "map"
    melon = "melon"
    melon_seeds = "melon_seeds"
    milk_bucket = "milk_bucket"
    minecart = "minecart"
    mushroom_stew = "mushroom_stew"
    mutton = "mutton"
    name_tag = "name_tag"
    nether_star = "nether_star"
    nether_wart = "nether_wart"
    netherbrick = "netherbrick"
    painting = "painting"
    paper = "paper"
    poisonous_potato = "poisonous_potato"
    porkchop = "porkchop"
    potato = "potato"
    potion = "potion"
    prismarine_crystals = "prismarine_crystals"
    prismarine_shard = "prismarine_shard"
    pumpkin_pie = "pumpkin_pie"
    pumpkin_seeds = "pumpkin_seeds"
    quartz = "quartz"
    rabbit = "rabbit"
    rabbit_foot = "rabbit_foot"
    rabbit_hide = "rabbit_hide"
    rabbit_stew = "rabbit_stew"
    record_11 = "record_11"
    record_13 = "record_13"
    record_blocks = "record_blocks"
    record_cat = "record_cat"
    record_chirp = "record_chirp"
    record_far = "record_far"
    record_mall = "record_mall"
    record_mellohi = "record_mellohi"
    record_stal = "record_stal"
    record_strad = "record_strad"
    record_wait = "record_wait"
    record_ward = "record_ward"
    redstone = "redstone"
    reeds = "reeds"
    repeater = "repeater"
    rotten_flesh = "rotten_flesh"
    saddle = "saddle"
    shears = "shears"
    shield = "shield"
    shulker_shell = "shulker_shell"
    sign = "sign"
    skull = "skull"
    slime_ball = "slime_ball"
    snowball = "snowball"
    spawn_egg = "spawn_egg"
    speckled_melon = "speckled_melon"
    spectral_arrow = "spectral_arrow"
    spider_eye = "spider_eye"
    splash_potion = "splash_potion"
    spruce_boat = "spruce_boat"
    spruce_door = "spruce_door"
    stick = "stick"
    stone_axe = "stone_axe"
    stone_hoe = "stone_hoe"
    stone_pickaxe = "stone_pickaxe"
    stone_shovel = "stone_shovel"
    stone_sword = "stone_sword"
    string = "string"
    sugar = "sugar"
    tipped_arrow = "tipped_arrow"
    tnt_minecart = "tnt_minecart"
    totem_of_undying = "totem_of_undying"
    water_bucket = "water_bucket"
    wheat = "wheat"
    wheat_seeds = "wheat_seeds"
    wooden_axe = "wooden_axe"
    wooden_door = "wooden_door"
    wooden_hoe = "wooden_hoe"
    wooden_pickaxe = "wooden_pickaxe"
    wooden_shovel = "wooden_shovel"
    wooden_sword = "wooden_sword"
    writable_book = "writable_book"
    written_book = "written_book"

FOOD_ITEMS = set([
    Item.apple,
    Item.baked_potato,
    Item.beef,
    Item.beetroot_soup,
    Item.bread,
    Item.cake,
    Item.carrot,
    Item.chicken,
    Item.cooked_beef,
    Item.cooked_chicken,
    Item.cooked_fish,
    Item.cooked_mutton,
    Item.cooked_porkchop,
    Item.cooked_rabbit,
    Item.cookie,
    Item.fish,
    Item.golden_apple,
    Item.golden_carrot,
    Item.mushroom_stew,
    Item.mutton,
    Item.poisonous_potato,
    Item.porkchop,
    Item.potato,
    Item.pumpkin_pie,
    Item.rabbit,
    Item.rabbit_stew,
    Item.rotten_flesh
])



class Block(ReflectiveEnum):
    '''A type of Minecraft block'''

    Acacia_door = "acacia_door"
    Acacia_fence = "acacia_fence"
    Acacia_fence_gate = "acacia_fence_gate"
    Acacia_stairs = "acacia_stairs"
    Activator_rail = "activator_rail"
    Air = "air"
    Anvil = "anvil"
    Barrier = "barrier"
    Beacon = "beacon"
    Bed = "bed"
    Bedrock = "bedrock"
    Beetroots = "beetroots"
    Birch_door = "birch_door"
    Birch_fence = "birch_fence"
    Birch_fence_gate = "birch_fence_gate"
    Birch_stairs = "birch_stairs"
    Black_shulker_box = "black_shulker_box"
    Blue_shulker_box = "blue_shulker_box"
    Bone_block = "bone_block"
    Bookshelf = "bookshelf"
    Brewing_stand = "brewing_stand"
    Brick_block = "brick_block"
    Brick_stairs = "brick_stairs"
    Brown_mushroom = "brown_mushroom"
    Brown_mushroom_block = "brown_mushroom_block"
    Brown_shulker_box = "brown_shulker_box"
    Cactus = "cactus"
    Cake = "cake"
    Carpet = "carpet"
    Carrots = "carrots"
    Cauldron = "cauldron"
    Chain_command_block = "chain_command_block"
    Chest = "chest"
    Chorus_flower = "chorus_flower"
    Chorus_plant = "chorus_plant"
    Clay = "clay"
    Coal_block = "coal_block"
    Coal_ore = "coal_ore"
    Cobblestone = "cobblestone"
    Cobblestone_wall = "cobblestone_wall"
    Cocoa = "cocoa"
    Command_block = "command_block"
    Crafting_table = "crafting_table"
    Cyan_shulker_box = "cyan_shulker_box"
    Dark_oak_door = "dark_oak_door"
    Dark_oak_fence = "dark_oak_fence"
    Dark_oak_fence_gate = "dark_oak_fence_gate"
    Dark_oak_stairs = "dark_oak_stairs"
    Daylight_detector = "daylight_detector"
    Daylight_detector_inverted = "daylight_detector_inverted"
    Deadbush = "deadbush"
    Detector_rail = "detector_rail"
    Diamond_block = "diamond_block"
    Diamond_ore = "diamond_ore"
    Dirt = "dirt"
    Dispenser = "dispenser"
    Double_plant = "double_plant"
    Double_stone_slab = "double_stone_slab"
    Double_stone_slab2 = "double_stone_slab2"
    Double_wooden_slab = "double_wooden_slab"
    Dragon_egg = "dragon_egg"
    Dropper = "dropper"
    Emerald_block = "emerald_block"
    Emerald_ore = "emerald_ore"
    Enchanting_table = "enchanting_table"
    End_bricks = "end_bricks"
    End_gateway = "end_gateway"
    End_portal = "end_portal"
    End_portal_frame = "end_portal_frame"
    End_rod = "end_rod"
    End_stone = "end_stone"
    Ender_chest = "ender_chest"
    Farmland = "farmland"
    Fence = "fence"
    Fence_gate = "fence_gate"
    Fire = "fire"
    Flower_pot = "flower_pot"
    Flowing_lava = "flowing_lava"
    Flowing_water = "flowing_water"
    Frosted_ice = "frosted_ice"
    Furnace = "furnace"
    Glass = "glass"
    Glass_pane = "glass_pane"
    Glowstone = "glowstone"
    Gold_block = "gold_block"
    Gold_ore = "gold_ore"
    Golden_rail = "golden_rail"
    Grass = "grass"
    Grass_path = "grass_path"
    Gravel = "gravel"
    Gray_shulker_box = "gray_shulker_box"
    Green_shulker_box = "green_shulker_box"
    Hardened_clay = "hardened_clay"
    Hay_block = "hay_block"
    Heavy_weighted_pressure_plate = "heavy_weighted_pressure_plate"
    Hopper = "hopper"
    Ice = "ice"
    Iron_bars = "iron_bars"
    Iron_block = "iron_block"
    Iron_door = "iron_door"
    Iron_ore = "iron_ore"
    Iron_trapdoor = "iron_trapdoor"
    Jukebox = "jukebox"
    Jungle_door = "jungle_door"
    Jungle_fence = "jungle_fence"
    Jungle_fence_gate = "jungle_fence_gate"
    Jungle_stairs = "jungle_stairs"
    Ladder = "ladder"
    Lapis_block = "lapis_block"
    Lapis_ore = "lapis_ore"
    Lava = "lava"
    Leaves = "leaves"
    Leaves2 = "leaves2"
    Lever = "lever"
    Light_blue_shulker_box = "light_blue_shulker_box"
    Light_weighted_pressure_plate = "light_weighted_pressure_plate"
    Lime_shulker_box = "lime_shulker_box"
    Lit_furnace = "lit_furnace"
    Lit_pumpkin = "lit_pumpkin"
    Lit_redstone_lamp = "lit_redstone_lamp"
    Lit_redstone_ore = "lit_redstone_ore"
    Log = "log"
    Log2 = "log2"
    Magenta_shulker_box = "magenta_shulker_box"
    Magma = "magma"
    Melon_block = "melon_block"
    Melon_stem = "melon_stem"
    Mob_spawner = "mob_spawner"
    Monster_egg = "monster_egg"
    Mossy_cobblestone = "mossy_cobblestone"
    Mycelium = "mycelium"
    Nether_brick = "nether_brick"
    Nether_brick_fence = "nether_brick_fence"
    Nether_brick_stairs = "nether_brick_stairs"
    Nether_wart = "nether_wart"
    Nether_wart_block = "nether_wart_block"
    Netherrack = "netherrack"
    Noteblock = "noteblock"
    Oak_stairs = "oak_stairs"
    Observer = "observer"
    Obsidian = "obsidian"
    Orange_shulker_box = "orange_shulker_box"
    Packed_ice = "packed_ice"
    Pink_shulker_box = "pink_shulker_box"
    Piston = "piston"
    Piston_extension = "piston_extension"
    Piston_head = "piston_head"
    Planks = "planks"
    Portal = "portal"
    Potatoes = "potatoes"
    Powered_comparator = "powered_comparator"
    Powered_repeater = "powered_repeater"
    Prismarine = "prismarine"
    Pumpkin = "pumpkin"
    Pumpkin_stem = "pumpkin_stem"
    Purple_shulker_box = "purple_shulker_box"
    Purpur_block = "purpur_block"
    Purpur_double_slab = "purpur_double_slab"
    Purpur_pillar = "purpur_pillar"
    Purpur_slab = "purpur_slab"
    Purpur_stairs = "purpur_stairs"
    Quartz_block = "quartz_block"
    Quartz_ore = "quartz_ore"
    Quartz_stairs = "quartz_stairs"
    Rail = "rail"
    Red_flower = "red_flower"
    Red_mushroom = "red_mushroom"
    Red_mushroom_block = "red_mushroom_block"
    Red_nether_brick = "red_nether_brick"
    Red_sandstone = "red_sandstone"
    Red_sandstone_stairs = "red_sandstone_stairs"
    Red_shulker_box = "red_shulker_box"
    Redstone_block = "redstone_block"
    Redstone_lamp = "redstone_lamp"
    Redstone_ore = "redstone_ore"
    Redstone_torch = "redstone_torch"
    Redstone_wire = "redstone_wire"
    Reeds = "reeds"
    Repeating_command_block = "repeating_command_block"
    Sand = "sand"
    Sandstone = "sandstone"
    Sandstone_stairs = "sandstone_stairs"
    Sapling = "sapling"
    Sea_lantern = "sea_lantern"
    Silver_shulker_box = "silver_shulker_box"
    Skull = "skull"
    Slime = "slime"
    Snow = "snow"
    Snow_layer = "snow_layer"
    Soul_sand = "soul_sand"
    Sponge = "sponge"
    Spruce_door = "spruce_door"
    Spruce_fence = "spruce_fence"
    Spruce_fence_gate = "spruce_fence_gate"
    Spruce_stairs = "spruce_stairs"
    Stained_glass = "stained_glass"
    Stained_glass_pane = "stained_glass_pane"
    Stained_hardened_clay = "stained_hardened_clay"
    Standing_banner = "standing_banner"
    Standing_sign = "standing_sign"
    Sticky_piston = "sticky_piston"
    Stone = "stone"
    Stone_brick_stairs = "stone_brick_stairs"
    Stone_button = "stone_button"
    Stone_pressure_plate = "stone_pressure_plate"
    Stone_slab = "stone_slab"
    Stone_slab2 = "stone_slab2"
    Stone_stairs = "stone_stairs"
    Stonebrick = "stonebrick"
    Structure_block = "structure_block"
    Structure_void = "structure_void"
    Tallgrass = "tallgrass"
    Tnt = "tnt"
    Torch = "torch"
    Trapdoor = "trapdoor"
    Trapped_chest = "trapped_chest"
    Tripwire = "tripwire"
    Tripwire_hook = "tripwire_hook"
    Unlit_redstone_torch = "unlit_redstone_torch"
    Unpowered_comparator = "unpowered_comparator"
    Unpowered_repeater = "unpowered_repeater"
    Vine = "vine"
    Wall_banner = "wall_banner"
    Wall_sign = "wall_sign"
    Water = "water"
    Waterlily = "waterlily"
    Web = "web"
    Wheat = "wheat"
    White_shulker_box = "white_shulker_box"
    Wooden_button = "wooden_button"
    Wooden_door = "wooden_door"
    Wooden_pressure_plate = "wooden_pressure_plate"
    Wooden_slab = "wooden_slab"
    Wool = "wool"
    Yellow_flower = "yellow_flower"
    Yellow_shulker_box = "yellow_shulker_box"