"""Module that adds platforms to level 1"""

import platformer.platforms as platforms

"""Level 1"""

level = [ 
            [platforms.ICE_MIDDLE, 0, 0],
            [platforms.ICE_MIDDLE, 0, 128],
            [platforms.ICE_MIDDLE, 0, 256],
            [platforms.ICE_TOP_LEFT, 64, 256],
            [platforms.ICE_TOP_LEFT, 128, 256],
            [platforms.ICE_TOP_LEFT, 192, 256],
            [platforms.ICE_TOP_LEFT, 480, 120],
            [platforms.ICE_TOP_LEFT, 192, 256],
            [platforms.ICE_MIDDLE, 0, 384],
            [platforms.ICE_MIDDLE, 0, 512],
            [platforms.ICE_MIDDLE, -64, 0],
            [platforms.ICE_MIDDLE, -64, 128],
            [platforms.ICE_MIDDLE, -64, 256],
            [platforms.ICE_MIDDLE, -64, 384],
            [platforms.ICE_MIDDLE, -64, 512],
            [platforms.ICE_TOP_MIDDLE, 64, 560],
            [platforms.ICE_TOP_MIDDLE, 128, 560],
            [platforms.ICE_TOP_MIDDLE, 192, 560],
            [platforms.SPIKES, 256, 589],
            [platforms.SPIKES, 320, 589],
            [platforms.ICE_TOP_MIDDLE, 384, 550],
            [platforms.SPIKES, 448, 589],
            [platforms.SPIKES, 512, 589],
            [platforms.SPIKES, 560, 589],
            [platforms.ICE_MIDDLE, 640, 0],
            [platforms.ICE_MIDDLE, 640, 128],
            [platforms.ICE_MIDDLE, 640, 475],
            
            #has sign1 on it
            [platforms.TOP_LEFT_SNOW, 786, 420],
            [platforms.TOP_MIDDLE_SNOW, 849, 420],
            [platforms.TOP_RIGHT_SNOW, 912, 420],
            
            [platforms.TOP_LEFT_SNOW, 1036, 288],
            [platforms.TOP_MIDDLE_SNOW, 1099, 288],
            [platforms.TOP_RIGHT_SNOW, 1162, 288],
            
            [platforms.TOP_LEFT_SNOW, 786, 150],
            [platforms.TOP_MIDDLE_SNOW, 849, 150],
            [platforms.TOP_RIGHT_SNOW, 912, 150],
            
            [platforms.TOP_RIGHT_CORNER_SNOW, 1286, 150],
            [platforms.TOP_MIDDLE_CORNER_SNOW, 1373, 150],
            [platforms.TOP_MIDDLE_CORNER_SNOW, 1460, 150],
            [platforms.TOP_MIDDLE_CORNER_SNOW, 1547, 150],
            [platforms.TOP_LEFT_CORNER_SNOW, 1632, 150],
            
            #pillar left side
            [platforms.DIRT_LEFT, 1790, 500],
            [platforms.DIRT_LEFT, 1790, 438],
            [platforms.DIRT_LEFT, 1790, 377],
            #[platforms.DIRT_LEFT, 1790, 316],
            [platforms.TOP_LEFT_SNOW, 1790, 316],
            
            [platforms.SPIKES, 1856, 589],
            [platforms.SPIKES, 1920, 589],
            [platforms.SPIKES, 1984, 589],
            
            #pillar right side
            [platforms.DIRT_RIGHT, 2050, 500],
            [platforms.DIRT_RIGHT, 2050, 438],
            [platforms.DIRT_RIGHT, 2050, 377],
            #[platforms.DIRT_RIGHT, 2050, 316],
            [platforms.TOP_RIGHT_SNOW, 2050, 316],
            
            #[platforms.TOP_MIDDLE_SNOW, 2250, 450],
            #[platforms.TOP_MIDDLE_SNOW, 2150, 410],
            
            [platforms.TOP_LEFT_SNOW, 2247, 260],
            [platforms.TOP_MIDDLE_SNOW, 2310, 260],
            [platforms.DIRT_SNOW_CORNER, 2373, 260],
            [platforms.LEFT_SIDE_SNOW, 2376, 201],
            [platforms.TOP_RIGHT_DOUBLE_SNOW, 2375, 138],#fix corner piece
            [platforms.TOP_MIDDLE_SNOW, 2436, 138],
            [platforms.TOP_MIDDLE_SNOW, 2499, 138],
            [platforms.TOP_MIDDLE_SNOW, 2562, 138],
            [platforms.TOP_MIDDLE_SNOW, 2625, 138],
            [platforms.TOP_MIDDLE_SNOW, 2688, 138],
            [platforms.TOP_MIDDLE_SNOW, 2751, 138],
            [platforms.TOP_MIDDLE_SNOW, 2814, 138],
            [platforms.TOP_MIDDLE_SNOW, 2877, 138],
            [platforms.TOP_MIDDLE_SNOW, 2940, 138],            
            [platforms.DIRT_SNOW_CORNER, 3003, 138],
            [platforms.LEFT_SIDE_SNOW, 3006, 77],
            [platforms.LEFT_SIDE_SNOW, 3006, 16],
            [platforms.DIRT_SNOW_CORNER_BL, 3006, -45],
            
            [platforms.DIRT_SNOW_CORNER_BL, 3006, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2943, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2880, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2817, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2754, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2691, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2628, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2565, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2502, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2439, -45],
            [platforms.BOTTOM_MIDDLE_SNOW, 2376, -45],
            
            
            
            
            
            [platforms.ICE_TOP_MIDDLE, 640, 450],
            [platforms.ICE_MIDDLE, 640, 560],
            [platforms.ICE_TOP_MIDDLE, 704, 560],
            [platforms.ICE_TOP_MIDDLE, 768, 560],
            [platforms.ICE_TOP_MIDDLE, 832, 560],
            [platforms.ICE_TOP_MIDDLE, 896, 560],
            [platforms.ICE_TOP_MIDDLE, 960, 560],
            [platforms.ICE_TOP_MIDDLE, 1024, 560],
            [platforms.ICE_TOP_MIDDLE, 1088, 560],
            [platforms.ICE_TOP_MIDDLE, 1152, 560],
            [platforms.SPIKES, 1216, 589],
            [platforms.SPIKES, 1280, 589],
            [platforms.ICE_TOP_MIDDLE, 1344, 560],
            [platforms.ICE_TOP_MIDDLE, 1408, 560],
            [platforms.ICE_TOP_MIDDLE, 1472, 560],
            [platforms.ICE_TOP_MIDDLE, 1536, 560],
            [platforms.SPIKES, 1600, 589],
            [platforms.SPIKES, 1664, 589],
            [platforms.ICE_TOP_MIDDLE, 1728, 560],
            [platforms.ICE_TOP_MIDDLE, 1792, 560],
            [platforms.ICE_TOP_MIDDLE, 2048, 560],
            [platforms.ICE_TOP_MIDDLE, 2112, 560],
            [platforms.SPIKES, 2176, 589],
            [platforms.SPIKES, 2240, 589],
            
            
            [platforms.TOP_LEFT_SNOW, 2773, 415],
            [platforms.TOP_MIDDLE_SNOW, 2835, 415],
            [platforms.TOP_MIDDLE_SNOW, 2898, 415],
            [platforms.TOP_RIGHT_SNOW, 2961, 415],
            
            [platforms.ICE_TOP_MIDDLE, 2304, 560],
            [platforms.ICE_TOP_MIDDLE, 2368, 560],
            [platforms.ICE_TOP_MIDDLE, 2432, 560],
            [platforms.ICE_TOP_MIDDLE, 2496, 560],
            [platforms.ICE_TOP_MIDDLE, 2560, 560],
            [platforms.ICE_TOP_MIDDLE, 2624, 560],
            [platforms.ICE_TOP_MIDDLE, 2688, 560],
            [platforms.ICE_TOP_MIDDLE, 2752, 560],
            [platforms.ICE_TOP_MIDDLE, 2816, 560],
            [platforms.ICE_TOP_MIDDLE, 2880, 560],
            [platforms.ICE_TOP_MIDDLE, 2944, 560],
            [platforms.ICE_TOP_MIDDLE, 3008, 560],
            [platforms.ICE_TOP_MIDDLE, 3072, 560],
            [platforms.ICE_TOP_MIDDLE, 3136, 560],
            [platforms.ICE_TOP_MIDDLE, 3200, 560],
            [platforms.ICE_TOP_MIDDLE, 3264, 560],
            [platforms.ICE_TOP_MIDDLE, 3328, 560],
            [platforms.ICE_TOP_MIDDLE, 3392, 560],
            [platforms.ICE_TOP_MIDDLE, 3456, 560],
            [platforms.ICE_TOP_MIDDLE, 3520, 560],#end of the level
            [platforms.ICE_TOP_MIDDLE, 3584, 560],
            [platforms.ICE_TOP_MIDDLE, 3648, 560],
            [platforms.ICE_TOP_MIDDLE, 3712, 560],
        ]