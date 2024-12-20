

# Common Attributes:

tags =  ("type",
    "material",
    "color",
    "style",
    "seating-capacity",
    "reclining-function",
    "size",
    "shape")


furniture = (
    "sofa",
    "beds",
    "chair",
    "dining-table",
    "desk",
    "wardrobe"
)


# Type: (Sofa, Bed, Chair, Table, etc.)
# Material: (Wood, Metal, Fabric, Leather)
# Color: (Black, White, Brown, Red, etc.)
# Size: (Dimensions: Length, Width, Height)
# Style: (Modern, Traditional, Vintage)
# Distinguishing Attributes:

# Sofa: Seating Capacity, Reclining Function
# Bed: Size(Twin, Full, Queen, King)
# Chair: Armrests, Swivel Function
# Table: Shape(Round, Square, Rectangular)


furniture_catalog = {
    "sofa": [
        {
            "image_url": "https://img.freepik.com/free-vector/red-leather-sofa-realistic-illustration_1284-12133.jpg?t=st=1734521475~exp=1734525075~hmac=7a02a512d1227896e7f85203efdb79ff6668c870a9aedcf85f1338d407373e8d&w=1060",
            "tags": ["sofa", "leather", "red", "modern", "comfortable"]
        },
        {
            "image_url": "https://img.freepik.com/premium-photo/stylish-sofa-table-white-background_392895-12504.jpg?w=996",
            "tags": ["sofa", "fabric", "green", "classic", "elegant", "comfortable"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/jaettebo-u-shaped-sofa-7-seat-with-chaise-longue-right-with-headrests-samsala-dark-yellow-green__1179839_pe896112_s5.jpg?f=xl",
            "tags": [
                "sofa", "fabric", "yellow", "modern", "7-seater", "chaise-longue"
            ]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/landskrona-5-seat-sofa-with-chaise-longues-djuparp-dark-blue-wood__0990586_pe819075_s5.jpg?f=xl",
            "tags": [
                "sofa", "fabric", "blue", "modern", "5-seater", "chaise-longue"
            ]
        }
    ],
    "beds": [
        {
            "image_url": "https://www.luxfurniture.com.cy/cdn/shop/files/alexander.jpg?v=1717523223&width=900",
            "tags": ["bed", "wood", "brown", "modern", "king-size", "comfortable"]
        },
        {
            "image_url": "https://www.luxfurniture.com.cy/cdn/shop/files/texas-bed-brown-whitebg-Photoroom.jpg?v=1729671995&width=1000",
            "tags": ["bed", "fabric", "brown", "luxury", "super-double-size", "comfortable", "extra-storage"]
        },
        {
            "image_url": "https://www.luxfurniture.com.cy/cdn/shop/files/kleio-bg.jpg?v=1717511109&width=1000",
            "tags": ["bed", "fabric", "gray", "luxury", "super-double-size", "metal-legs", "leather-lining", "comfortable", "extra-storage"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/smastad-loft-bed-white-pale-pink-with-desk-with-4-drawers__1265273_pe927584_s5.jpg?f=xl",
            "tags": ["bed", "wood", "white", "modern", "loft-bed", "desk-with-storage", "space-saving", "durable", "functional"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/slaekt-nattapa-bed-frm-w-strg-guard-rl-slat-bd-bse-white__1305316_pe939443_s5.jpg?f=xl",
            "tags": ["bed", "wood", "white", "modern", "slatted-bed-base", "bed-with-storage", "guard-rail", "space-saving", "durable", "functional"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/slaekt-bed-frame-with-underbed-and-storage-white__1362803_pe955327_s5.jpg?f=xl",
            "tags": ["bed", "wood", "white", "modern", "slatted-bed-base", "bed-with-underbed-storage", "guard-rail", "space-saving", "durable", "functional"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/slaekt-ext-bed-frame-with-slatted-bed-base-white__0963406_pe808482_s5.jpg?f=xl",
            "tags": ["bed", "wood", "white", "modern", "extendable-bed", "slatted-bed-base", "space-saving", "durable", "functional"]
        }
    ],

    "dining-table": [
        {
            "image_url": "https://www.luxfurniture.com.cy/cdn/shop/files/marble-dining-table-srd-129-bg.jpg?v=1717577937&width=1000",
            "tags": ["dining-table", "marble-surface", "gold-base", "white-marble", "modern", "spacious", "accommodates-6-people"]
        },
        {
            "image_url": "https://www.luxfurniture.com.cy/cdn/shop/files/srd040-2.jpg?v=1717579516&width=1000",
            "tags": ["dining-table", "marble-surface", "metal-base", "black-marble", "modern", "elegant", "timeless-style"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/strandtorp-marenaes-table-and-6-armchairs-brown-black-gunnared-dark-grey__1198508_pe904117_s5.jpg?f=xl",
            "tags": ["dining-table", "extendable-table", "particleboard", "oak-veneer", "steel-frame", "solid-wood", "modern"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/nordviken-skogsbo-table-and-4-chairs-black-dark-brown__1205483_pe907111_s5.jpg?f=xl",
            "tags": ["dining-table", "extendable-table", "particleboard", "ash-veneer", "solid-pine", "durable", "classic-look", "black-and-dark-brown"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/ingatorp-ingolf-table-and-6-chairs-white-white-hallarp-beige__1097686_pe865075_s5.jpg?f=xl",
            "tags": ["dining-table", "extendable-table", "particleboard", "solid-wood", "white-finish", "beige-seats", "family-dining"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/segeroen-table-and-4-chairs-with-armrests-outdoor-dark-green-froesoen-duvholmen-beige__1185536_pe898432_s5.jpg?f=xl",
            "tags": ["dining-table", "outdoor-table-and-chairs", "aluminium", "steel", "dark-green", "beige-cushions", "spacious"]
        }
    ],

    "desk": [
        {
            "image_url": "https://www.ikea.com/in/en/images/products/lagkapten-alex-desk-grey-turquoise-black__1207256_pe907872_s5.jpg?f=xl",
            "tags": ["desk", "fibreboard", "acrylic-paint", "steel", "modern-design"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/alex-desk-grey-turquoise__0977656_pe813724_s5.jpg?f=xl",
            "tags": ["desk", "particleboard", "acrylic-paint", "steel", "modern-design"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/lillasen-desk-bamboo__0736017_pe740344_s5.jpg?f=xl",
            "tags": ["desk", "bamboo", "steel", "modern-design", "sustainable"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/ridspoe-desk-oak__1188767_pe899574_s5.jpg?f=xl",
            "tags": ["desk", "plywood", "oak-veneer", "steel", "modern-design"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/mittzon-desk-black-stained-ash-veneer-black__1206001_pe907335_s5.jpg?f=xl",
            "tags": ["desk", "particleboard", "ash-veneer", "steel", "modern-design"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/fredde-gaming-desk-black__0736008_pe740351_s5.jpg?f=xl",
            "tags": ["desk", "steel", "gaming-desk", "modern-design"]
        }
    ],

    "wardrobes": [
        {
            "image_url": "https://www.ikea.com/in/en/images/products/rakkestad-wardrobe-with-sliding-doors-black-brown__0823992_pe776023_s5.jpg?f=xl",
            "tags": ["particleboard", "paper-foil", "fibreboard", "printed-acrylic-paint", "easy-maintenance", "wipe-clean", "mild-cleaner", "modern-design", "sliding-doors", "wardrobe", "durable"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/smastad-platsa-wardrobe-white-blackboard-surface-with-3-shelves__1099954_pe866019_s5.jpg?f=xl",
            "tags": ["fibreboard", "paper-foil", "particleboard", "recycled-materials", "steel", "epoxy-coating", "soft-closing-hinge", "copper-plated-hinge", "acetal-plastic", "adjustable-leg", "polypropylene-plastic", "clear-lacquer", "acrylic-paint", "blackboard-surface", "easy-maintenance", "wipe-clean", "mild-cleaner", "modern-design", "wardrobe"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/smastad-platsa-wardrobe-white-blackboard-surface-with-2-chest-of-drawers__1102549_pe867025_s5.jpg?f=xl",
            "tags": ["steel", "epoxy-coating", "polypropylene-plastic", "synthetic-rubber", "acetal-plastic", "particleboard", "paper-foil", "fibreboard", "recycled-materials", "copper-plated-hinge", "soft-closing-device", "clear-lacquer", "acrylic-paint", "blackboard-surface", "adjustable-clothes-rail", "wire-basket", "modern-design", "wardrobe", "easy-maintenance", "wipe-clean", "mild-cleaner"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/sundvik-wardrobe-white__0626568_pe692872_s5.jpg?f=xl",
            "tags": ["solid-pine", "stain", "clear-acrylic-lacquer", "fibreboard", "paper-foil", "particleboard", "plastic-foil", "printed-acrylic-paint", "modern-design", "wardrobe", "easy-maintenance", "wipe-clean", "durable", "functional"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/smastad-platsa-wardrobe-white-white-with-2-clothes-rails__1266837_pe928321_s5.jpg?f=xl",
            "tags": ["fibreboard", "paper-foil", "particleboard", "recycled-materials", "steel", "epoxy-coating", "acetal-plastic", "polypropylene-plastic", "synthetic-rubber", "adjustable-clothes-rail", "copper-plated-hinge", "soft-closing-device", "adjustable-leg", "modern-design", "wardrobe", "easy-maintenance", "wipe-clean", "durable"]
        },
        {
            "image_url": "https://www.ikea.com/in/en/images/products/skytta-pax-walk-in-wardrobe-with-sliding-doors-black-hokksund-high-gloss-light-grey__1319447_pe940955_s5.jpg?f=xl",
            "tags": ["aluminium", "anodized", "fibreboard", "plastic-foil", "steel", "acetal-plastic", "reinforced-polyamide-plastic", "solid-pine", "stain", "epoxy-coating", "acetal-plastic", "pigmented-powder-coating", "particleboard", "melamine-foil", "plastic-edging", "recycled-materials", "modern-design", "wardrobe", "sliding-doors", "easy-maintenance", "wipe-clean", "mild-cleaner"]
        }
    ],

    "chair": [
        {
            "image_url": "https://www.luxfurniture.com.cy/cdn/shop/files/dining-chair-2217-ivory.jpg?v=1717318206&width=1000",
            "tags": ["dining-chair", "beige", "pvc-material", "stainless-steel-legs", "modern", "comfortable"]
        },
        {
            "image_url": "https://www.luxfurniture.com.cy/cdn/shop/files/ace-black_1_6ca8cdb0-77f0-4b3d-86a4-a4f9cc9b3f2c.jpg?v=1717265106&width=1000",
            "tags": ["dining-chair", "black", "bouclé-fabric", "metal-legs", "modern", "ergonomic"]
        }
    ]

}
