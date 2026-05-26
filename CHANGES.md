# Filament Profile Changes — 2026-05-25 19:37

## Phase 0: Cross-printer compat_printers fixes

### EDIT: EconoFil PLA @AC KS1 0.4mm
  - REMOVE 'Kobra X' from compatible_printers
    Before: ['Anycubic Kobra S1 0.4 nozzle', 'Anycubic Kobra S1 0.4 nozzle - Brass', 'Anycubic Kobra S1 0.4 nozzle - Hardened Steel', 'Anycubic Kobra X 0.4 nozzle']
    After:  ['Anycubic Kobra S1 0.4 nozzle', 'Anycubic Kobra S1 0.4 nozzle - Brass', 'Anycubic Kobra S1 0.4 nozzle - Hardened Steel']

### EDIT: Elegoo Rapid PETG @AC KS1 0.4mm
  - REMOVE 'Kobra X' from compatible_printers
    Before: ['Anycubic Kobra S1 0.4 nozzle', 'Anycubic Kobra S1 0.4 nozzle - Brass', 'Anycubic Kobra S1 0.4 nozzle - Hardened Steel', 'Anycubic Kobra X 0.4 nozzle']
    After:  ['Anycubic Kobra S1 0.4 nozzle', 'Anycubic Kobra S1 0.4 nozzle - Brass', 'Anycubic Kobra S1 0.4 nozzle - Hardened Steel']

## Phase 0b: Create EconoFil KSX profiles

### NEW: EconoFil PLA @AC KSX 0.4mm
  Created KSX 0.4mm variant, MVS=13, inherits Anycubic PLA @Anycubic Kobra X 0.4 nozzle

### NEW: EconoFil PLA @AC KSX 0.25mm
  Created nozzle variant MVS=3, PA=0.053, flow=0.99

### NEW: EconoFil PLA @AC KSX 0.6mm
  Created nozzle variant MVS=16.2, PA=0.023, flow=0.97

### NEW: EconoFil PLA @AC KSX 0.8mm
  Created nozzle variant MVS=19.5, PA=0.012, flow=0.96

## Phase 1: Root profile fixes (cool_plate + MVS)

### AzureFilm PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### AzureFilm PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '18' → '13' (KSX reference table)

### Bambu PLA Basic @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Bambu PLA Basic @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '16' → '13' (KSX reference table)

### Bambu PLA Matte @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Bambu PLA Matte @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Creality Hyper PLA Galaxy @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Creality Hyper PLA Galaxy @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '20' → '13' (KSX reference table)

### Creality PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Creality PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '13' (KSX reference table)

### Creality PETG CR @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Creality PETG CR @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '13' (KSX reference table)

### Creality PLA+ @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - CORRECT `filament_max_volumetric_speed` '12' → '19' (was < 65% of table reference 19)

### Creality PLA+ @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '12' → '16' (KSX reference table)

### ESun PETG Translucent @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` None → '13' (no existing override)

### ESun PETG Translucent @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '12' → '11' (KSX reference table)

### ESun PLA-CF @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### ESun PLA-CF @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '15' → '16' (KSX reference table)

### EconoFil PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` None → '16' (no existing override)

### Eleego PLA Metal @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Eleego PLA Metal @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Elegoo PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` None → '16' (no existing override)

### Elegoo PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '12' → '13' (KSX reference table)

### Elegoo Rapid PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - CORRECT `filament_max_volumetric_speed` '10' → '21' (was < 65% of table reference 21)

### Elegoo Rapid PLA+ @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Elegoo Rapid PLA+ @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Geetech PLA Silk @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Geetech PLA Silk @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '16' → '10' (KSX reference table)

### Generic PLA Miniatures @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - CORRECT `filament_max_volumetric_speed` '2.5' → '16' (was < 65% of table reference 16)

### Generic PLA Miniatures @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '2.5' → '13' (KSX reference table)

### Generic Silk PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Generic Silk PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '9' → '10' (KSX reference table)

### IBoss Glitter PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### IBoss Glitter PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '13' (KSX reference table)

### IBoss Matte PLA+ @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### IBoss Matte PLA+ @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '16' → '14' (KSX reference table)

### IBoss PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - CORRECT `filament_max_volumetric_speed` '8' → '15' (was < 65% of table reference 15)

### IBoss Silk Dual PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### IBoss Silk PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### IBoss Silk PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### IEMAI PETG Translucent @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### IEMAI PETG Translucent @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '15' → '11' (KSX reference table)

### Improved PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Improved PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '13' (KSX reference table)

### Improved PETG HS @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Improved PETG HS @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '14' → '18' (KSX reference table)

### Improved PETG Translucent @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` None → '13' (no existing override)

### Improved PETG Translucent @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '12' → '11' (KSX reference table)

### Improved PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` None → '16' (no existing override)

### Improved PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '12' → '13' (KSX reference table)

### Improved PLA+ @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` None → '19' (no existing override)

### Improved PLA+ @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '15' → '16' (KSX reference table)

### JustMaker PETG GF @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### JustMaker PETG GF @AC KSX 0.4mm
  - SET `cool_plate_temp` '0' → '50'
  - SET `cool_plate_temp_initial_layer` '0' → '50'

### JustMaker Silk PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### JustMaker Silk PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Kingaroon PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` None → '16' (no existing override)

### Kingaroon PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '12' → '13' (KSX reference table)

### Kingaroon PLA Silk @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Kingaroon PLA Silk @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Overture High Speed TPU @AC KSX 0.4mm
  - SET `filament_max_volumetric_speed` '10' → '8' (KSX reference table)

### Overture Matte and Rock PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Overture Matte and Rock PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '18' → '13' (KSX reference table)

### Overture PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - CORRECT `filament_max_volumetric_speed` '8' → '15' (was < 65% of table reference 15)

### Overture PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '13' (KSX reference table)

### Overture PLA Pro @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Overture PLA Pro @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` None → '16' (KSX reference table)

### Overture TPU HS @AC KSX 0.4mm
  - SET `filament_max_volumetric_speed` '10' → '8' (KSX reference table)

### Polymaker PLA Pro @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Polymaker PLA Pro @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '22' → '16' (KSX reference table)

### Polymaker PolyChroma PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Polymaker PolyLite PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Polymaker PolyLite PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '15' → '13' (KSX reference table)

### Polymaker PolyTerra PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Polymaker PolyTerra PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '22' → '13' (KSX reference table)

### Polymaker Polychrome Glow @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Polymaker Polychrome Glow @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '15' → '13' (KSX reference table)

### Prusament Galaxy PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Prusament Galaxy PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '13' (KSX reference table)

### Prusament Galaxy PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Prusament Galaxy PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '21' → '13' (KSX reference table)

### Prusament Matte PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Prusament Matte PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '13' (KSX reference table)

### Prusament PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Prusament PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '14' → '13' (KSX reference table)

### Prusament PETG Translucent @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Prusament PETG Translucent @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '15' → '11' (KSX reference table)

### Soleyin UF PLA @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Soleyin UF PLA @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '15' → '13' (KSX reference table)

### Sovol PETG Translucent @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### Sovol PETG Translucent @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '10' → '11' (KSX reference table)

### Sovol TPU HS @AC KS1 0.4mm
  - CORRECT `filament_max_volumetric_speed` '5' → '10' (was < 65% of table reference 10)

### Sovol TPU HS @AC KSX 0.4mm
  - SET `filament_max_volumetric_speed` '5' → '8' (KSX reference table)

### Sunlu PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` '0' → '50'
  - SET `cool_plate_temp_initial_layer` '0' → '50'
  - CORRECT `filament_max_volumetric_speed` '9' → '15' (was < 65% of table reference 15)

### Sunlu PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'
  - SET `filament_max_volumetric_speed` '9' → '13' (KSX reference table)

### Sunlu PLA+ 2.0 @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '22' → '20' (KSX reference table)

### Sunlu PLA+ @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')

### Sunlu PLA+ @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '17' → '16' (KSX reference table)

### Sunlu TPU 95a @AC KSX 0.4mm
  - SET `filament_max_volumetric_speed` '5' → '4' (KSX reference table)

### TecBears Rapid PETG @AC KS1 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### TecBears Rapid PETG @AC KSX 0.4mm
  - SET `cool_plate_temp` None → '50'
  - SET `cool_plate_temp_initial_layer` None → '50'

### UJoyBio PLA+ @AC KS1 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - CORRECT `filament_max_volumetric_speed` '12' → '19' (was < 65% of table reference 19)

### UJoyBio PLA+ @AC KSX 0.4mm
  - ADD `cool_plate_temp_initial_layer` → '40' (parent has '35')
  - SET `filament_max_volumetric_speed` '12' → '16' (KSX reference table)

## Phase 2: Nozzle variant MVS recalculation + explicit cool_plate fixes

### Anycubic ABS improved @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '9' → '10.0' (8.0×1.25)

### Anycubic ABS improved @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '10' → '12.0' (8.0×1.5)

### AzureFilm PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '22.5' → '16.2' (13.0×1.25)

### AzureFilm PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '27' → '19.5' (13.0×1.5)

### Creality Hyper PLA Galaxy @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '10.0' (20.0×0.5)
  - FIX `cool_plate_temp_initial_layer` '35' → '40' (PLA explicit wrong value)

### Creality Hyper PLA Galaxy @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '24' → '25.0' (20.0×1.25)

### Creality Hyper PLA Galaxy @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '28' → '30.0' (20.0×1.5)

### Creality Hyper PLA Galaxy @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Creality Hyper PLA Galaxy @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '24' → '16.2' (13.0×1.25)

### Creality Hyper PLA Galaxy @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '28' → '19.5' (13.0×1.5)

### Creality PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '12.5' → '16.2' (13.0×1.25)

### Creality PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '15' → '19.5' (13.0×1.5)

### Creality PETG CR @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '12.5' → '16.2' (13.0×1.25)

### Creality PETG CR @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '15' → '19.5' (13.0×1.5)

### Creality PLA+ @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '9.5' (19.0×0.5)

### Creality PLA+ @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '23.8' (19.0×1.25)

### Creality PLA+ @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '28.5' (19.0×1.5)

### Creality PLA+ @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Creality PLA+ @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '20.0' (16.0×1.25)

### Creality PLA+ @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '24.0' (16.0×1.5)

### ESun PETG Translucent @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '16.2' (13.0×1.25)

### ESun PETG Translucent @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '19.5' (13.0×1.5)

### ESun PETG Translucent @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '13.8' (11.0×1.25)

### ESun PETG Translucent @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '16.5' (11.0×1.5)

### ESun PLA-CF @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '7.5' (15.0×0.5)

### ESun PLA-CF @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '18.8' (15.0×1.25)

### ESun PLA-CF @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '22.5' (15.0×1.5)

### ESun PLA-CF @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### ESun PLA-CF @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '20.0' (16.0×1.25)

### ESun PLA-CF @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '24.0' (16.0×1.5)

### EconoFil PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### EconoFil PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '20.0' (16.0×1.25)

### EconoFil PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '24.0' (16.0×1.5)

### EconoFil PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Eleego PLA Metal @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### Eleego PLA Metal @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### Eleego PLA Metal @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### Eleego PLA Metal @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### Elegoo PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Elegoo PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '20.0' (16.0×1.25)

### Elegoo PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '24.0' (16.0×1.5)

### Elegoo PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Elegoo PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '16.2' (13.0×1.25)

### Elegoo PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '19.5' (13.0×1.5)

### Elegoo Rapid PETG @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '15' → '26.2' (21.0×1.25)

### Elegoo Rapid PETG @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '18' → '31.5' (21.0×1.5)

### Elegoo Rapid PLA+ @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '10.0' (20.0×0.5)

### Elegoo Rapid PLA+ @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '24' → '25.0' (20.0×1.25)

### Elegoo Rapid PLA+ @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '28' → '30.0' (20.0×1.5)

### Elegoo Rapid PLA+ @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '10.0' (20.0×0.5)

### Elegoo Rapid PLA+ @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '24' → '25.0' (20.0×1.25)

### Elegoo Rapid PLA+ @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '28' → '30.0' (20.0×1.5)

### Geetech PLA Silk @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Geetech PLA Silk @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '19.2' → '20.0' (16.0×1.25)

### Geetech PLA Silk @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '22.4' → '24.0' (16.0×1.5)

### Geetech PLA Silk @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### Geetech PLA Silk @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '19.2' → '12.5' (10.0×1.25)

### Geetech PLA Silk @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '22.4' → '15.0' (10.0×1.5)

### Generic PLA Miniatures @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Generic PLA Miniatures @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '3' → '20.0' (16.0×1.25)

### Generic PLA Miniatures @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '3.5' → '24.0' (16.0×1.5)

### Generic PLA Miniatures @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Generic PLA Miniatures @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '3' → '16.2' (13.0×1.25)

### Generic PLA Miniatures @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '3.5' → '19.5' (13.0×1.5)

### Generic Silk PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '4.5' (9.0×0.5)

### Generic Silk PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '12.6' → '13.5' (9.0×1.5)

### Generic Silk PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### Generic Silk PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '10.8' → '12.5' (10.0×1.25)

### Generic Silk PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '12.6' → '15.0' (10.0×1.5)

### IBoss Glitter PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '12.5' → '16.2' (13.0×1.25)

### IBoss Glitter PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '15' → '19.5' (13.0×1.5)

### IBoss Matte PLA+ @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### IBoss Matte PLA+ @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '19.2' → '20.0' (16.0×1.25)

### IBoss Matte PLA+ @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '22.4' → '24.0' (16.0×1.5)

### IBoss Matte PLA+ @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '7.0' (14.0×0.5)

### IBoss Matte PLA+ @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '19.2' → '17.5' (14.0×1.25)

### IBoss Matte PLA+ @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '22.4' → '21.0' (14.0×1.5)

### IBoss PETG @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '10' → '18.8' (15.0×1.25)

### IBoss PETG @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '12' → '22.5' (15.0×1.5)

### IBoss Silk Dual PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### IBoss Silk Dual PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### IBoss Silk PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### IBoss Silk PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### IBoss Silk PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### IBoss Silk PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### IEMAI PETG Translucent @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '18.8' (15.0×1.25)

### IEMAI PETG Translucent @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '22.5' (15.0×1.5)

### IEMAI PETG Translucent @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '13.8' (11.0×1.25)

### IEMAI PETG Translucent @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '16.5' (11.0×1.5)

### Improved PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '12.5' → '16.2' (13.0×1.25)

### Improved PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '15' → '19.5' (13.0×1.5)

### Improved PETG HS @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '17.5' → '22.5' (18.0×1.25)

### Improved PETG HS @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '27.0' (18.0×1.5)

### Improved PETG Translucent @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '16.2' (13.0×1.25)

### Improved PETG Translucent @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '19.5' (13.0×1.5)

### Improved PETG Translucent @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '13.8' (11.0×1.25)

### Improved PETG Translucent @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '8.4' → '16.5' (11.0×1.5)

### Improved PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Improved PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '20.0' (16.0×1.25)

### Improved PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '24.0' (16.0×1.5)

### Improved PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Improved PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '16.2' (13.0×1.25)

### Improved PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '19.5' (13.0×1.5)

### Improved PLA+ @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '9.5' (19.0×0.5)

### Improved PLA+ @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '23.8' (19.0×1.25)

### Improved PLA+ @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '28.5' (19.0×1.5)

### Improved PLA+ @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Improved PLA+ @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '20.0' (16.0×1.25)

### Improved PLA+ @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '24.0' (16.0×1.5)

### JustMaker PETG GF @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '15.0' (12.0×1.25)

### JustMaker PETG GF @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '21.6' → '18.0' (12.0×1.5)

### JustMaker PETG GF @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '16.5' → '13.8' (11.0×1.25)

### JustMaker PETG GF @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '19.8' → '16.5' (11.0×1.5)

### JustMaker Silk PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### JustMaker Silk PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### JustMaker Silk PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### JustMaker Silk PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### Kingaroon PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Kingaroon PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '20.0' (16.0×1.25)

### Kingaroon PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '24.0' (16.0×1.5)

### Kingaroon PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Kingaroon PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '16.2' (13.0×1.25)

### Kingaroon PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '19.5' (13.0×1.5)

### Kingaroon PLA Silk @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '4.0' (8.0×0.5)

### Kingaroon PLA Silk @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '11.2' → '12.0' (8.0×1.5)

### Kingaroon PLA Silk @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '5.0' (10.0×0.5)

### Kingaroon PLA Silk @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '14' → '15.0' (10.0×1.5)

### Overture High Speed TPU @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '5' → '12.5' (10.0×1.25)

### Overture High Speed TPU @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '15.0' (10.0×1.5)

### Overture High Speed TPU @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '5' → '10.0' (8.0×1.25)

### Overture High Speed TPU @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '12.0' (8.0×1.5)

### Overture Matte and Rock PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '9.0' (18.0×0.5)

### Overture Matte and Rock PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '21.6' → '22.5' (18.0×1.25)

### Overture Matte and Rock PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '25.2' → '27.0' (18.0×1.5)

### Overture Matte and Rock PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Overture Matte and Rock PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '21.6' → '16.2' (13.0×1.25)

### Overture Matte and Rock PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '25.2' → '19.5' (13.0×1.5)

### Overture PETG @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '10' → '18.8' (15.0×1.25)

### Overture PETG @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '12' → '22.5' (15.0×1.5)

### Overture PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '12.5' → '16.2' (13.0×1.25)

### Overture PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '15' → '19.5' (13.0×1.5)

### Overture PLA Pro @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '9.0' (18.0×0.5)

### Overture PLA Pro @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '21.6' → '22.5' (18.0×1.25)

### Overture PLA Pro @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '25.2' → '27.0' (18.0×1.5)

### Overture PLA Pro @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Overture PLA Pro @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '21.6' → '20.0' (16.0×1.25)

### Overture PLA Pro @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '25.2' → '24.0' (16.0×1.5)

### Overture TPU @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '5.6' (3.75×1.5)

### Overture TPU @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '5.6' (3.75×1.5)

### Overture TPU HS @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '5' → '12.5' (10.0×1.25)

### Overture TPU HS @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '15.0' (10.0×1.5)

### Overture TPU HS @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '5' → '10.0' (8.0×1.25)

### Overture TPU HS @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '12.0' (8.0×1.5)

### Polymaker PLA Pro @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '11.0' (22.0×0.5)

### Polymaker PLA Pro @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '26.4' → '27.5' (22.0×1.25)

### Polymaker PLA Pro @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '30.8' → '33.0' (22.0×1.5)

### Polymaker PLA Pro @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Polymaker PLA Pro @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '26.4' → '20.0' (16.0×1.25)

### Polymaker PLA Pro @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '30.8' → '24.0' (16.0×1.5)

### Polymaker PolyChroma PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '7.5' (15.0×0.5)

### Polymaker PolyChroma PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '18.8' (15.0×1.25)

### Polymaker PolyChroma PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '22.5' (15.0×1.5)

### Polymaker PolyLite PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '7.5' (15.0×0.5)

### Polymaker PolyLite PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '18.8' (15.0×1.25)

### Polymaker PolyLite PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '22.5' (15.0×1.5)

### Polymaker PolyLite PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Polymaker PolyLite PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '16.2' (13.0×1.25)

### Polymaker PolyLite PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '19.5' (13.0×1.5)

### Polymaker PolyTerra PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '11.0' (22.0×0.5)

### Polymaker PolyTerra PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '26.4' → '27.5' (22.0×1.25)

### Polymaker PolyTerra PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '30.8' → '33.0' (22.0×1.5)

### Polymaker PolyTerra PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Polymaker PolyTerra PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '26.4' → '16.2' (13.0×1.25)

### Polymaker PolyTerra PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '30.8' → '19.5' (13.0×1.5)

### Polymaker Polychrome Glow @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '16' → '18.8' (15.0×1.25)

### Polymaker Polychrome Glow @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` None → '22.5' (15.0×1.5)

### Polymaker Polychrome Glow @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` None → '19.5' (13.0×1.5)

### Prusament Galaxy PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '12.5' → '16.2' (13.0×1.25)

### Prusament Galaxy PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '15' → '19.5' (13.0×1.5)

### Prusament Galaxy PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '10.5' (21.0×0.5)

### Prusament Galaxy PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '25.2' → '26.2' (21.0×1.25)

### Prusament Galaxy PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '29.4' → '31.5' (21.0×1.5)

### Prusament Galaxy PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Prusament Galaxy PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '25.2' → '16.2' (13.0×1.25)

### Prusament Galaxy PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '29.4' → '19.5' (13.0×1.5)

### Prusament Matte PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '12.5' → '16.2' (13.0×1.25)

### Prusament Matte PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '15' → '19.5' (13.0×1.5)

### Prusament PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '17.5' → '16.2' (13.0×1.25)

### Prusament PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '19.5' (13.0×1.5)

### Prusament PETG Translucent @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '18.8' (15.0×1.25)

### Prusament PETG Translucent @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '22.5' (15.0×1.5)

### Prusament PETG Translucent @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '13.8' (11.0×1.25)

### Prusament PETG Translucent @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '10.5' → '16.5' (11.0×1.5)

### Soleyin UF PLA @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '7.5' (15.0×0.5)

### Soleyin UF PLA @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '18.8' (15.0×1.25)

### Soleyin UF PLA @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '22.5' (15.0×1.5)

### Soleyin UF PLA @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '6.5' (13.0×0.5)

### Soleyin UF PLA @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '18' → '16.2' (13.0×1.25)

### Soleyin UF PLA @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '21' → '19.5' (13.0×1.5)

### Sovol PETG Translucent @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '7' → '12.5' (10.0×1.25)

### Sovol PETG Translucent @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '15.0' (10.0×1.5)

### Sovol PETG Translucent @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '7' → '13.8' (11.0×1.25)

### Sovol PETG Translucent @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '16.5' (11.0×1.5)

### Sovol TPU HS @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '5' → '12.5' (10.0×1.25)

### Sovol TPU HS @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '15.0' (10.0×1.5)

### Sovol TPU HS @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '5' → '10.0' (8.0×1.25)

### Sovol TPU HS @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '12.0' (8.0×1.5)

### Sunlu PETG @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '11.25' → '18.8' (15.0×1.25)

### Sunlu PETG @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '13.5' → '22.5' (15.0×1.5)

### Sunlu PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '11.25' → '16.2' (13.0×1.25)

### Sunlu PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '13.5' → '19.5' (13.0×1.5)

### Sunlu PLA+ 2.0 @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '11.0' (22.0×0.5)

### Sunlu PLA+ 2.0 @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '26.4' → '27.5' (22.0×1.25)

### Sunlu PLA+ 2.0 @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '30.8' → '33.0' (22.0×1.5)

### Sunlu PLA+ 2.0 @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '10.0' (20.0×0.5)

### Sunlu PLA+ 2.0 @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '26.4' → '25.0' (20.0×1.25)

### Sunlu PLA+ 2.0 @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '30.8' → '30.0' (20.0×1.5)

### Sunlu PLA+ @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.5' (17.0×0.5)

### Sunlu PLA+ @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '20.4' → '21.2' (17.0×1.25)

### Sunlu PLA+ @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '23.8' → '25.5' (17.0×1.5)

### Sunlu PLA+ @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### Sunlu TPU 95a @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '5' → '6.2' (5.0×1.25)

### Sunlu TPU 95a @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '7' → '6.0' (4.0×1.5)

### TecBears Rapid PETG @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '27' → '22.5' (18.0×1.25)

### TecBears Rapid PETG @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '32.4' → '27.0' (18.0×1.5)

### TecBears Rapid PETG @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '27' → '22.5' (18.0×1.25)

### TecBears Rapid PETG @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '32.4' → '27.0' (18.0×1.5)

### UJoyBio PLA+ @AC KS1 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '9.5' (19.0×0.5)

### UJoyBio PLA+ @AC KS1 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '23.8' (19.0×1.25)

### UJoyBio PLA+ @AC KS1 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '28.5' (19.0×1.5)

### UJoyBio PLA+ @AC KSX 0.25mm
  - RECALC `filament_max_volumetric_speed` '3' → '8.0' (16.0×0.5)

### UJoyBio PLA+ @AC KSX 0.6mm
  - RECALC `filament_max_volumetric_speed` '14.4' → '20.0' (16.0×1.25)

### UJoyBio PLA+ @AC KSX 0.8mm
  - RECALC `filament_max_volumetric_speed` '16.8' → '24.0' (16.0×1.5)

## Phase 3: Format simplification (remove redundant/header keys)

### Anycubic ABS improved @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFABS" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["ASA"] (header field)

### Anycubic ABS improved @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFABS" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["ASA"] (header field)

### Anycubic ABS improved @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFABS" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["ASA"] (header field)

### AzureFilm PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### AzureFilm PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### AzureFilm PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### AzureFilm PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### AzureFilm PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### AzureFilm PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Bambu PLA Basic @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Bambu PLA Basic @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `hot_plate_temp` (matches parent: ["60"])
  - REMOVE `hot_plate_temp_initial_layer` (matches parent: ["60"])
  - REMOVE `textured_plate_temp` (matches parent: ["60"])
  - REMOVE `textured_plate_temp_initial_layer` (matches parent: ["60"])
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Bambu PLA Matte @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.96"])
  - REMOVE `filament_z_hop_types` (matches parent: ["Slope Lift"])

### Bambu PLA Matte @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `filament_flow_ratio` (matches parent: ["0.96"])
  - REMOVE `hot_plate_temp` (matches parent: ["60"])
  - REMOVE `hot_plate_temp_initial_layer` (matches parent: ["60"])
  - REMOVE `textured_plate_temp` (matches parent: ["60"])
  - REMOVE `textured_plate_temp_initial_layer` (matches parent: ["60"])
  - REMOVE `nozzle_temperature_initial_layer` (matches parent: ["220"])
  - REMOVE `fan_min_speed_BRASS` (matches parent: ["60"])
  - REMOVE `fan_min_speed_HS` (matches parent: ["60"])

### Creality Hyper PLA Galaxy @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality Hyper PLA Galaxy @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality Hyper PLA Galaxy @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality Hyper PLA Galaxy @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality Hyper PLA Galaxy @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality Hyper PLA Galaxy @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality Hyper PLA Galaxy @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality Hyper PLA Galaxy @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality PETG CR @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality PETG CR @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality PETG CR @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality PETG CR @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality PETG CR @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality PETG CR @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Creality PLA+ @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Creality PLA+ @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Creality PLA+ @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["210"])

### Creality PLA+ @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Creality PLA+ @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Creality PLA+ @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Creality PLA+ @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Creality PLA+ @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### ESun PETG Translucent @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### ESun PETG Translucent @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### ESun PETG Translucent @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["235"])

### ESun PETG Translucent @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### ESun PETG Translucent @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### ESun PETG Translucent @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["235"])

### ESun PLA-CF @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)

### ESun PLA-CF @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)

### ESun PLA-CF @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)

### ESun PLA-CF @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)

### ESun PLA-CF @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)

### ESun PLA-CF @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### ESun PLA-CF @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### ESun PLA-CF @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA-CF"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### EconoFil PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### EconoFil PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### EconoFil PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### EconoFil PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### EconoFil PLA @AC KSX 0.4mm
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_retraction_length` (matches parent: ["0.8"])
  - REMOVE `hot_plate_temp` (matches parent: ["60"])
  - REMOVE `hot_plate_temp_initial_layer` (matches parent: ["60"])

### Eleego PLA Metal @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Eleego PLA Metal @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Eleego PLA Metal @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Eleego PLA Metal @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Eleego PLA Metal @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Eleego PLA Metal @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### Eleego PLA Metal @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Eleego PLA Metal @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Metal" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Elegoo PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Elegoo PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Elegoo PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Elegoo PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo Rapid PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Elegoo Rapid PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Elegoo Rapid PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Elegoo Rapid PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Elegoo Rapid PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Elegoo Rapid PLA+ @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo Rapid PLA+ @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo Rapid PLA+ @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo Rapid PLA+ @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo Rapid PLA+ @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo Rapid PLA+ @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Elegoo Rapid PLA+ @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Elegoo Rapid PLA+ @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Geetech PLA Silk @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Geetech PLA Silk @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Geetech PLA Silk @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Geetech PLA Silk @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Geetech PLA Silk @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Geetech PLA Silk @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Geetech PLA Silk @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Geetech PLA Silk @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic PLA Miniatures @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic PLA Miniatures @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_HS` (matches parent: ["220"])

### Generic PLA Miniatures @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Generic PLA Miniatures @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Generic PLA Miniatures @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic PLA Miniatures @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_HS` (matches parent: ["220"])

### Generic PLA Miniatures @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic PLA Miniatures @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic Silk PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic Silk PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic Silk PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic Silk PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic Silk PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic Silk PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Generic Silk PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Generic Silk PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Glitter PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### IBoss Glitter PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### IBoss Glitter PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### IBoss Glitter PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### IBoss Glitter PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### IBoss Glitter PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### IBoss Matte PLA+ @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)

### IBoss Matte PLA+ @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)
  - REMOVE `filament_z_hop_types` (matches parent: ["Slope Lift"])

### IBoss Matte PLA+ @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["210"])

### IBoss Matte PLA+ @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)

### IBoss Matte PLA+ @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)

### IBoss Matte PLA+ @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### IBoss Matte PLA+ @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)

### IBoss Matte PLA+ @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA+"] (header field)

### IBoss PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA09" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### IBoss PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA09" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["245"])

### IBoss PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA10" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### IBoss Silk Dual PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["215"])

### IBoss Silk Dual PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk Dual PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk Dual PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["215"])

### IBoss Silk PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### IBoss Silk PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IBoss Silk PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### IEMAI PETG Translucent @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### IEMAI PETG Translucent @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### IEMAI PETG Translucent @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### IEMAI PETG Translucent @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### IEMAI PETG Translucent @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### IEMAI PETG Translucent @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PETG HS @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PETG HS @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PETG HS @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PETG HS @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PETG Translucent @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PETG Translucent @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PETG Translucent @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_HS` (matches parent: ["230"])
  - REMOVE `nozzle_temperature_HS` (matches parent: ["230"])

### Improved PETG Translucent @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PETG Translucent @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Improved PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA+ @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA+ @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA+ @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA+ @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA+ @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA+ @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Improved PLA+ @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Improved PLA+ @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### JustMaker PETG GF @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG-CF" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["250"])

### JustMaker PETG GF @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG-CF" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### JustMaker PETG GF @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG-CF" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### JustMaker PETG GF @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG-CF" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### JustMaker PETG GF @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG-CF" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### JustMaker PETG GF @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG-CF" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### JustMaker Silk PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### JustMaker Silk PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### JustMaker Silk PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### JustMaker Silk PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### JustMaker Silk PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### JustMaker Silk PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### JustMaker Silk PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["225"])

### JustMaker Silk PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_HS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_HS` (matches parent: ["220"])

### Kingaroon PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Kingaroon PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Kingaroon PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_HS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_HS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Kingaroon PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA Silk @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA Silk @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA Silk @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Kingaroon PLA Silk @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["215"])

### Kingaroon PLA Silk @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA Silk @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Kingaroon PLA Silk @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Kingaroon PLA Silk @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Silk" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture High Speed TPU @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)

### Overture High Speed TPU @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.985"])

### Overture High Speed TPU @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture High Speed TPU @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture High Speed TPU @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.985"])
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Overture High Speed TPU @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Overture Matte and Rock PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.98"])

### Overture Matte and Rock PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture Matte and Rock PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture Matte and Rock PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture Matte and Rock PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.98"])

### Overture Matte and Rock PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture Matte and Rock PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture Matte and Rock PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Matte" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Overture PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["245"])
  - REMOVE `fan_max_speed` (matches parent: ["100"])

### Overture PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `fan_max_speed` (matches parent: ["100"])

### Overture PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Overture PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Overture PLA Pro @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture PLA Pro @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture PLA Pro @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture PLA Pro @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture PLA Pro @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture PLA Pro @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Overture PLA Pro @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture PLA Pro @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Overture TPU @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)

### Overture TPU @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.98"])

### Overture TPU @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture TPU @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture TPU @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.98"])
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Overture TPU @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Overture TPU HS @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)

### Overture TPU HS @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.985"])

### Overture TPU HS @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture TPU HS @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Overture TPU HS @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["0.985"])
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Overture TPU HS @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Polymaker PLA Pro @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PLA Pro @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PLA Pro @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PLA Pro @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PLA Pro @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PLA Pro @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Polymaker PLA Pro @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PLA Pro @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyChroma PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyChroma PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyChroma PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyChroma PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyLite PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyLite PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyLite PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Polymaker PolyLite PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Polymaker PolyLite PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyLite PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Polymaker PolyLite PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyLite PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyTerra PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyTerra PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyTerra PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Polymaker PolyTerra PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Polymaker PolyTerra PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyTerra PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Polymaker PolyTerra PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker PolyTerra PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker Polychrome Glow @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Glow" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker Polychrome Glow @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Glow" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker Polychrome Glow @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Glow" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker Polychrome Glow @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Glow" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Polymaker Polychrome Glow @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Glow" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Polymaker Polychrome Glow @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Glow" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Prusament Galaxy PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament Galaxy PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament Galaxy PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament Galaxy PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_HS` (matches parent: ["230"])
  - REMOVE `nozzle_temperature_HS` (matches parent: ["230"])

### Prusament Galaxy PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament Galaxy PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament Galaxy PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Prusament Galaxy PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Prusament Galaxy PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Prusament Galaxy PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Prusament Galaxy PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Prusament Galaxy PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Prusament Galaxy PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Prusament Galaxy PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA Galaxy" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Prusament Matte PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament Matte PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament Matte PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament Matte PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_HS` (matches parent: ["230"])
  - REMOVE `nozzle_temperature_HS` (matches parent: ["230"])

### Prusament Matte PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament Matte PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_HS` (matches parent: ["230"])
  - REMOVE `nozzle_temperature_HS` (matches parent: ["230"])

### Prusament PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament PETG Translucent @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament PETG Translucent @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament PETG Translucent @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Prusament PETG Translucent @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_HS` (matches parent: ["230"])
  - REMOVE `nozzle_temperature_HS` (matches parent: ["230"])

### Prusament PETG Translucent @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Prusament PETG Translucent @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Soleyin UF PLA @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Soleyin UF PLA @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Soleyin UF PLA @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Soleyin UF PLA @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Soleyin UF PLA @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Soleyin UF PLA @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_max_volumetric_speed` (matches parent: ["13"])
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["220"])
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Soleyin UF PLA @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Soleyin UF PLA @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sovol PETG Translucent @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Sovol PETG Translucent @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sovol PETG Translucent @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sovol PETG Translucent @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sovol PETG Translucent @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Sovol PETG Translucent @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Sovol TPU HS @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)

### Sovol TPU HS @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["1.029"])

### Sovol TPU HS @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sovol TPU HS @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sovol TPU HS @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["1.029"])
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Sovol TPU HS @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Sunlu PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Sunlu PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["245"])

### Sunlu PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["250"])

### Sunlu PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sunlu PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### Sunlu PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["245"])

### Sunlu PLA+ 2.0 @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ 2.0 @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ 2.0 @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ 2.0 @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ 2.0 @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ 2.0 @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Sunlu PLA+ 2.0 @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ 2.0 @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `nozzle_temperature_initial_layer_BRASS` (matches parent: ["220"])

### Sunlu PLA+ @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu PLA+ @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### Sunlu TPU 95a @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)

### Sunlu TPU 95a @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["1.029"])

### Sunlu TPU 95a @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sunlu TPU 95a @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### Sunlu TPU 95a @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `filament_flow_ratio` (matches parent: ["1.029"])
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### Sunlu TPU 95a @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFTPU" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["TPU"] (header field)
  - REMOVE `fan_min_speed` (matches parent: ["100"])

### TecBears Rapid PETG @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `pressure_advance` (matches parent: ["0.04"])

### TecBears Rapid PETG @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### TecBears Rapid PETG @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `bed_type` = ["High Temp Plate"] (header field)
  - REMOVE `filament_load_time` = ["42"] (header field)
  - REMOVE `filament_unload_time` = ["0"] (header field)

### TecBears Rapid PETG @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### TecBears Rapid PETG @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### TecBears Rapid PETG @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPETG" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PETG"] (header field)

### UJoyBio PLA+ @AC KS1 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["200"])

### UJoyBio PLA+ @AC KS1 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### UJoyBio PLA+ @AC KS1 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### UJoyBio PLA+ @AC KS1 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### UJoyBio PLA+ @AC KSX 0.25mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `nozzle_temperature_BRASS` (matches parent: ["200"])

### UJoyBio PLA+ @AC KSX 0.4mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
  - REMOVE `compatible_printers` (matches parent: ["Anycubic Kobra X 0.4 nozzle"])

### UJoyBio PLA+ @AC KSX 0.6mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)

### UJoyBio PLA+ @AC KSX 0.8mm
  - REMOVE `type` = "filament" (header field)
  - REMOVE `setting_id` = "GFSA04" (header field)
  - REMOVE `filament_id` = "GFPLA+" (header field)
  - REMOVE `instantiation` = "true" (header field)
  - REMOVE `filament_type` = ["PLA"] (header field)
