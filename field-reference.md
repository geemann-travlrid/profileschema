# Field reference

The schema has 21 top-level properties. Five are required. Each section below lists the annotated field keys it declares. The schema also defines nested properties, shared types and unannotated structural fields.

## schemaVersion

Required. 

## profileMetadata

Required. 

## localizationSettings

Required. 

## consentSettings

Required. Consent held by the traveller. A value classified sensitive or specialCategory may be disclosed only to a grantee holding an unexpired, unrevoked grant whose scope covers its x-key. JSON Schema cannot enforce this; the disclosing system must. Evaluate each operation against a single valid grant matching grantee, action, purpose, any restricted context and exact key or whole dotted-segment prefix. Use grantedAt inclusively and expiry or revocation exclusively. For delegates verify current authority for the traveller and operation. Deny on missing or unverifiable authority. General consent flags cannot widen a grant. Project only the fulfilment fields requested and strip internal metadata.

## travelerIdentity

Required. 

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `travelerIdentity` | fact | sensitive |  |
| `travelerIdentity.racialIdentity` | fact | specialCategory |  |

## contactInformation

Optional. 

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `contactInformation` | fact | private |  |

## communicationPreferences

Optional. 

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `communicationPreferences` | preference | private |  |

## travelDocuments

Optional. 

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `travelDocuments` | fact | sensitive |  |

## loyaltyPrograms

Optional. 

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `loyaltyPrograms` | fact | sensitive |  |

## preferences

Optional. Standing travel preferences, each expressed on the common strength scale

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `preferences.air.cabin` | preference | private | Cabin |
| `preferences.air.fareStrategy` | preference | private | How to choose a fare when cabin preferences leave it open |
| `preferences.air.seatPosition` | preference | private | Seat position |
| `preferences.air.seatType` | preference | private | Seat type |
| `preferences.air.meals` | preference | private | Meal preferences by IATA special meal code, for example VGML; airline-specific codes allowed |
| `preferences.air.alliance` | preference | private | Airline alliance |
| `preferences.air.airlines` | preference | private | Airline preferences by IATA airline designator |
| `preferences.air.aircraftCategory` | preference | private | Aircraft category |
| `preferences.air.aircraftTypes` | preference | private | Aircraft type preferences by IATA aircraft type code |
| `preferences.air.stops` | preference | private | Number of stops |
| `preferences.air.loungeAccess` | preference | private | Lounge access |
| `preferences.air.earlyBoarding` | preference | private | Early boarding |
| `preferences.air.refundFlexibility` | preference | private | Fare refund flexibility |
| `preferences.air.changeFlexibility` | preference | private | Fare change flexibility |
| `preferences.air.tripDefaults.checkedBagCount` | tripDefault | private | Usual number of checked bags |
| `preferences.lodging.lodgingType.hotel` | preference | private | Hotel |
| `preferences.lodging.lodgingType.fullServiceHotel` | preference | private | Full-service hotel |
| `preferences.lodging.lodgingType.selectServiceHotel` | preference | private | Select-service hotel |
| `preferences.lodging.lodgingType.limitedServiceHotel` | preference | private | Limited-service hotel |
| `preferences.lodging.lodgingType.resort` | preference | private | Resort |
| `preferences.lodging.lodgingType.motel` | preference | private | Motel |
| `preferences.lodging.lodgingType.boutiqueHotel` | preference | private | Boutique hotel |
| `preferences.lodging.lodgingType.hostel` | preference | private | Hostel |
| `preferences.lodging.lodgingType.campsite` | preference | private | Campsite |
| `preferences.lodging.lodgingType.ranch` | preference | private | Ranch |
| `preferences.lodging.lodgingType.bedAndBreakfast` | preference | private | Bed and breakfast |
| `preferences.lodging.lodgingType.glamping` | preference | private | Glamping |
| `preferences.lodging.lodgingType.vacationRentalUnit` | preference | private | Vacation rental unit |
| `preferences.lodging.lodgingType.wholeHomeRental` | preference | private | Whole home rental |
| `preferences.lodging.roomConfiguration.privateRoomWithBath` | preference | private | Private room with bath |
| `preferences.lodging.roomConfiguration.privateRoomWithSharedBath` | preference | private | Private room with shared bath |
| `preferences.lodging.roomConfiguration.sharedHostelRoom` | preference | private | Shared hostel room |
| `preferences.lodging.propertyQuality.luxury` | preference | private | Luxury |
| `preferences.lodging.propertyQuality.upscale` | preference | private | Upscale |
| `preferences.lodging.propertyQuality.midscale` | preference | private | Midscale |
| `preferences.lodging.propertyQuality.economy` | preference | private | Economy |
| `preferences.lodging.propertyQuality.budget` | preference | private | Budget |
| `preferences.lodging.propertyStyle.business` | preference | private | Business |
| `preferences.lodging.propertyStyle.leisure` | preference | private | Leisure |
| `preferences.lodging.propertyStyle.roadside` | preference | private | Roadside |
| `preferences.lodging.propertyStyle.airport` | preference | private | Airport |
| `preferences.lodging.propertyStyle.extendedStay` | preference | private | Extended stay |
| `preferences.lodging.propertyStyle.hourlyStay` | preference | private | Hourly stay |
| `preferences.lodging.propertyFocus.business` | preference | private | Business |
| `preferences.lodging.propertyFocus.groupsAndMeetings` | preference | private | Groups and meetings |
| `preferences.lodging.propertyFocus.families` | preference | private | Families |
| `preferences.lodging.propertyFocus.couples` | preference | private | Couples |
| `preferences.lodging.propertyFocus.singles` | preference | private | Singles |
| `preferences.lodging.propertyFocus.adultsOnly` | preference | private | Adults |
| `preferences.lodging.propertyFocus.lgbtq` | preference | specialCategory | LGBTQ+ |
| `preferences.lodging.propertyFocus.faithBased` | preference | specialCategory | Faith-based |
| `preferences.lodging.propertySize.singleUnit` | preference | private | Single unit |
| `preferences.lodging.propertySize.verySmall` | preference | private | Very small, up to 15 rooms |
| `preferences.lodging.propertySize.small` | preference | private | Small, 16 to 50 rooms |
| `preferences.lodging.propertySize.medium` | preference | private | Medium, 51 to 200 rooms |
| `preferences.lodging.propertySize.large` | preference | private | Large, 201 to 750 rooms |
| `preferences.lodging.propertySize.mega` | preference | private | Mega, more than 750 rooms |
| `preferences.lodging.brands.branded` | preference | private | Branded property |
| `preferences.lodging.brands.independent` | preference | private | Independent property |
| `preferences.lodging.brands.brandPreferences` | preference | private | Preferences for named chains and brands; the brand and sub-brand tree is reference data held outside the profile |
| `preferences.lodging.policies.minimumCheckInAge` | preference | private | Highest minimum check-in age the traveller can meet |
| `preferences.lodging.policies.prepaymentRequired` | preference | private | Prepayment required |
| `preferences.lodging.policies.usablePaymentTypes` | preference | private | Payment types the traveller can use |
| `preferences.lodging.policies.childFreeProperty` | preference | private | Property does not accept children |
| `preferences.lodging.policies.youngestChildAge` | preference | private | Age of the youngest travelling child the property must accept |
| `preferences.lodging.policies.petsAllowed` | preference | private | Pets allowed |
| `preferences.lodging.amenities.frontDesk24Hour` | preference | private | 24-hour front desk |
| `preferences.lodging.amenities.breakfastIncluded` | preference | private | Breakfast included |
| `preferences.lodging.amenities.onSiteRestaurant` | preference | private | On-site restaurant |
| `preferences.lodging.amenities.onSiteBreakfastRestaurant` | preference | private | On-site breakfast restaurant |
| `preferences.lodging.amenities.onSiteLunchRestaurant` | preference | private | On-site lunch restaurant |
| `preferences.lodging.amenities.onSiteDinnerRestaurant` | preference | private | On-site dinner restaurant |
| `preferences.lodging.amenities.onSiteCafe` | preference | private | On-site coffee, snack or sandwich shop |
| `preferences.lodging.amenities.onSiteBar` | preference | private | On-site bar |
| `preferences.lodging.amenities.executiveLounge` | preference | private | Club or executive lounge |
| `preferences.lodging.amenities.elevator` | preference | private | Elevator |
| `preferences.lodging.amenities.gym` | preference | private | Fitness centre |
| `preferences.lodging.amenities.spa` | preference | private | Spa |
| `preferences.lodging.amenities.sauna` | preference | private | Sauna |
| `preferences.lodging.amenities.atm` | preference | private | ATM |
| `preferences.lodging.amenities.foreignExchange` | preference | private | Foreign exchange |
| `preferences.lodging.amenities.luggageStorage` | preference | private | Luggage storage |
| `preferences.lodging.amenities.shop` | preference | private | Gift shop, newsstand or grab-and-go |
| `preferences.lodging.amenities.dailyHousekeeping` | preference | private | Daily housekeeping |
| `preferences.lodging.amenities.limitedHousekeeping` | preference | private | Limited housekeeping |
| `preferences.lodging.amenities.roomService24Hour` | preference | private | 24-hour room service |
| `preferences.lodging.amenities.roomServiceLimitedHours` | preference | private | Room service with limited hours |
| `preferences.lodging.amenities.parking.freeOnsite` | preference | private | Free onsite parking |
| `preferences.lodging.amenities.parking.freeNearby` | preference | private | Free nearby parking |
| `preferences.lodging.amenities.parking.freeStreet` | preference | private | Free street parking |
| `preferences.lodging.amenities.parking.paidOnsite` | preference | private | Paid onsite parking |
| `preferences.lodging.amenities.parking.paidNearby` | preference | private | Paid nearby parking |
| `preferences.lodging.amenities.parking.freeValet` | preference | private | Free valet parking |
| `preferences.lodging.amenities.parking.paidValet` | preference | private | Paid valet parking |
| `preferences.lodging.amenities.laundry.paidSelfService` | preference | private | Paid self-service laundry |
| `preferences.lodging.amenities.laundry.paidLaundryAndDryCleaning` | preference | private | Paid laundry and dry cleaning |
| `preferences.lodging.amenities.bellService` | preference | private | Bell service |
| `preferences.lodging.amenities.conciergeDesk` | preference | private | Concierge desk |
| `preferences.lodging.amenities.casino` | preference | private | Casino |
| `preferences.lodging.amenities.businessCentre` | preference | private | Business centre |
| `preferences.lodging.amenities.gameRoom` | preference | private | Game room |
| `preferences.lodging.amenities.beach.beachfront` | preference | private | Beachfront property |
| `preferences.lodging.amenities.beach.maxDistanceToBeach` | preference | private | Maximum distance to the beach |
| `preferences.lodging.amenities.beach.cabanaRental` | preference | private | Cabana rentals |
| `preferences.lodging.amenities.beach.umbrellaRental` | preference | private | Umbrella rentals |
| `preferences.lodging.amenities.beach.freeUmbrellas` | preference | private | Free beach umbrellas |
| `preferences.lodging.amenities.beach.freeChairs` | preference | private | Free beach chairs |
| `preferences.lodging.amenities.beach.chairRental` | preference | private | Beach chair rental |
| `preferences.lodging.amenities.pool.indoor` | preference | private | Indoor pool |
| `preferences.lodging.amenities.pool.outdoorUnheated` | preference | private | Outdoor unheated pool |
| `preferences.lodging.amenities.pool.outdoorHeated` | preference | private | Outdoor heated pool |
| `preferences.lodging.amenities.pool.minLength` | preference | private | Minimum pool length |
| `preferences.lodging.amenities.pool.reservableLanes` | preference | private | Reservable lanes |
| `preferences.lodging.amenities.pool.minDepth` | preference | private | Minimum pool depth |
| `preferences.lodging.amenities.pool.maxDepth` | preference | private | Maximum pool depth |
| `preferences.lodging.amenities.pool.adultOnlyHours` | preference | private | Adult-only hours |
| `preferences.lodging.amenities.checkIn` | preference | private | Earliest check-in time needed and how much it matters |
| `preferences.lodging.amenities.checkOut` | preference | private | Latest check-out time needed and how much it matters |
| `preferences.lodging.unitTypes.standard` | preference | private | Standard |
| `preferences.lodging.unitTypes.conciergeLevel` | preference | private | Concierge level |
| `preferences.lodging.unitTypes.juniorSuite` | preference | private | Junior suite |
| `preferences.lodging.unitTypes.fullSuite` | preference | private | Full suite |
| `preferences.lodging.unitTypes.premiumSuite` | preference | private | Premium suite |
| `preferences.lodging.unitTypes.connectingRooms` | preference | private | Connecting rooms, when two or more rooms are requested |
| `preferences.lodging.unitTypes.sharedDormitory` | preference | private | Shared hostel, dormitory or bunkroom |
| `preferences.lodging.unitTypes.partialHouse` | preference | private | Partial house |
| `preferences.lodging.unitTypes.fullHouse` | preference | private | Full house |
| `preferences.lodging.unitTypes.cabin` | preference | private | Cabin |
| `preferences.lodging.unitTypes.mobileUnit` | preference | private | Rental RV or trailer, typically on a campsite |
| `preferences.lodging.unitTypes.pullThroughRvSite` | preference | private | Pull-through RV site |
| `preferences.lodging.unitTypes.stubRvSite` | preference | private | Stub RV site |
| `preferences.lodging.unitTypes.tentSite` | preference | private | Tent site |
| `preferences.lodging.unitFeatures.accessibleRoom` | preference | specialCategory | Accessible room |
| `preferences.lodging.unitFeatures.hearingAccessibleRoom` | preference | specialCategory | Hearing-accessible room |
| `preferences.lodging.unitFeatures.bathroom.ensuite` | preference | private | Ensuite bathroom |
| `preferences.lodging.unitFeatures.bathroom.privateOutsideUnit` | preference | private | Private bathroom outside the unit |
| `preferences.lodging.unitFeatures.bathroom.shared` | preference | private | Shared bathroom |
| `preferences.lodging.unitFeatures.bathroom.bathtubWithShower` | preference | private | Bathtub with shower |
| `preferences.lodging.unitFeatures.bathroom.bathtubWithoutShower` | preference | private | Bathtub without shower |
| `preferences.lodging.unitFeatures.bathroom.walkInShower` | preference | private | Walk-in shower |
| `preferences.lodging.unitFeatures.bathroom.jacuzziTub` | preference | private | Jacuzzi tub |
| `preferences.lodging.unitFeatures.bathroom.bidet` | preference | private | Bidet |
| `preferences.lodging.unitFeatures.freeWifi` | preference | private | Free wifi |
| `preferences.lodging.unitFeatures.paidWifi` | preference | private | Paid wifi |
| `preferences.lodging.unitFeatures.cellularSignal` | preference | private | Cellular network signal |
| `preferences.lodging.unitFeatures.balcony` | preference | private | Balcony |
| `preferences.lodging.unitFeatures.walkOutPatio` | preference | private | Walk-out patio |
| `preferences.lodging.unitFeatures.fireplace` | preference | private | Fireplace |
| `preferences.lodging.unitFeatures.kitchen.coffeeMaker` | preference | private | Coffee maker |
| `preferences.lodging.unitFeatures.kitchen.kitchenette` | preference | private | Kitchenette |
| `preferences.lodging.unitFeatures.kitchen.fullKitchen` | preference | private | Full kitchen |
| `preferences.lodging.unitFeatures.kitchen.microwave` | preference | private | Microwave |
| `preferences.lodging.unitFeatures.kitchen.fullRefrigeratorFreezer` | preference | private | Full refrigerator and freezer |
| `preferences.lodging.unitFeatures.kitchen.miniRefrigerator` | preference | private | Mini refrigerator |
| `preferences.lodging.unitFeatures.kitchen.stove` | preference | private | Stove |
| `preferences.lodging.unitFeatures.kitchen.oven` | preference | private | Oven |
| `preferences.lodging.unitFeatures.kitchen.diningTable` | preference | private | Dining table |
| `preferences.lodging.unitFeatures.kitchen.diningTableCapacity` | preference | private | Dining table capacity needed |
| `preferences.lodging.unitFeatures.safe` | preference | private | Safe |
| `preferences.lodging.unitFeatures.ironAndBoard` | preference | private | Iron and ironing board |
| `preferences.lodging.unitFeatures.hairDryer` | preference | private | Hair dryer |
| `preferences.lodging.unitFeatures.television` | preference | private | Television |
| `preferences.lodging.unitFeatures.tvCastingFromGuestDevices` | preference | private | Television supports streaming from guest devices |
| `preferences.lodging.unitFeatures.tvGuestStreamingAccounts` | preference | private | Television gives access to guest streaming accounts |
| `preferences.lodging.unitFeatures.radio` | preference | private | Radio |
| `preferences.lodging.unitFeatures.washingMachine` | preference | private | Washing machine |
| `preferences.lodging.unitFeatures.clothesDryer` | preference | private | Clothes dryer |
| `preferences.lodging.unitFeatures.workDesk` | preference | private | Work desk |
| `preferences.lodging.unitFeatures.seatingArea` | preference | private | Seating area |
| `preferences.lodging.unitFeatures.seatingAreaCapacity` | preference | private | Seating area capacity needed |
| `preferences.lodging.unitFeatures.smokingPermitted` | preference | private | Smoking permitted |
| `preferences.lodging.unitFeatures.interiorHallway` | preference | private | Interior hallway |
| `preferences.lodging.unitFeatures.exteriorEntrance` | preference | private | Exterior entrance |
| `preferences.lodging.unitFeatures.mosquitoNetting` | preference | private | Mosquito netting |
| `preferences.lodging.unitFeatures.beds.oversize` | preference | private | Oversize bed, for example king |
| `preferences.lodging.unitFeatures.beds.oversizeCount` | preference | private | Number of oversize beds |
| `preferences.lodging.unitFeatures.beds.large` | preference | private | Large bed, for example queen |
| `preferences.lodging.unitFeatures.beds.largeCount` | preference | private | Number of large beds |
| `preferences.lodging.unitFeatures.beds.double` | preference | private | Smaller double bed |
| `preferences.lodging.unitFeatures.beds.doubleCount` | preference | private | Number of smaller double beds |
| `preferences.lodging.unitFeatures.beds.single` | preference | private | Single bed, for example twin |
| `preferences.lodging.unitFeatures.beds.singleCount` | preference | private | Number of single beds |
| `preferences.lodging.unitFeatures.beds.sofaBed` | preference | private | Sofa bed |
| `preferences.lodging.unitFeatures.location.nearElevator` | preference | private | Near elevator |
| `preferences.lodging.unitFeatures.location.awayFromElevator` | preference | private | Away from elevator |
| `preferences.lodging.unitFeatures.location.nearExitStairs` | preference | private | Near exit stairs |
| `preferences.lodging.unitFeatures.location.nearVending` | preference | private | Near vending |
| `preferences.lodging.unitFeatures.location.awayFromVending` | preference | private | Away from vending |
| `preferences.lodging.unitFeatures.location.highFloor` | preference | private | High floor |
| `preferences.lodging.unitFeatures.location.lowFloor` | preference | private | Low floor |
| `preferences.lodging.unitFeatures.location.groundFloor` | preference | private | Ground floor |
| `preferences.lodging.unitFeatures.location.nearGym` | preference | private | Near gym |
| `preferences.lodging.unitFeatures.location.nearPool` | preference | private | Near pool |
| `preferences.lodging.unitFeatures.location.awayFromHighway` | preference | private | Away from highway |
| `preferences.lodging.unitFeatures.view.city` | preference | private | City view |
| `preferences.lodging.unitFeatures.view.mountain` | preference | private | Mountain view |
| `preferences.lodging.unitFeatures.view.golfCourse` | preference | private | Golf course view |
| `preferences.lodging.unitFeatures.view.pool` | preference | private | Pool view |
| `preferences.lodging.unitFeatures.view.beachfront` | preference | private | Beachfront unit |
| `preferences.lodging.unitFeatures.view.oceanOrWater` | preference | private | Ocean or water view |
| `preferences.lodging.unitFeatures.view.partialOceanOrWater` | preference | private | Partial ocean or water view |
| `preferences.lodging.unitFeatures.view.orientationDegrees` | preference | private | Preferred view orientation in compass degrees |
| `preferences.lodging.unitFeatures.bedding.foamPillow` | preference | private | Foam pillow |
| `preferences.lodging.unitFeatures.bedding.featherPillow` | preference | private | Feather pillow |
| `preferences.lodging.unitFeatures.bedding.childproofUndersheet` | preference | private | Childproof undersheet |
| `preferences.lodging.unitFeatures.bedding.hypoallergenicBedding` | preference | private | Hypoallergenic bedding (strawman) |
| `preferences.lodging.unitFeatures.bedding.naturalFibreBedding` | preference | private | Natural fibre bedding (strawman) |
| `preferences.lodging.unitFeatures.rvSite.cableTvCoax` | preference | private | Cable TV coax connection |
| `preferences.lodging.unitFeatures.rvSite.electrical` | preference | private | Electrical service needed |
| `preferences.lodging.unitFeatures.rvSite.powerIncluded` | preference | private | Power included in price |
| `preferences.lodging.unitFeatures.rvSite.water` | preference | private | Water supply needed |
| `preferences.lodging.unitFeatures.rvSite.fullSewerHookup` | preference | private | Full sewer hookup |
| `preferences.lodging.unitFeatures.rvSite.dumpStation` | preference | private | Dump station |
| `preferences.lodging.unitFeatures.rvSite.sewerHookupSide` | preference | private | Side of vehicle for the sewer hookup |
| `preferences.lodging.unitFeatures.rvSite.skySatelliteView` | preference | private | Clear sky or satellite view |
| `preferences.lodging.unitFeatures.rvSite.slideOutAwningClearance` | preference | private | Slide-out and awning clearance needed |
| `preferences.lodging.unitFeatures.rvSite.pavedSurface` | preference | private | Paved surface |
| `preferences.lodging.unitFeatures.rvSite.gravelSurface` | preference | private | Gravel surface |
| `preferences.lodging.unitFeatures.rvSite.grassSurface` | preference | private | Grass surface |
| `preferences.lodging.unitFeatures.tentSite.tentProvided` | preference | private | Tent provided |
| `preferences.lodging.unitFeatures.tentSite.naturalSurface` | preference | private | Natural surface |
| `preferences.lodging.unitFeatures.tentSite.platformSurface` | preference | private | Platform surface |
| `preferences.lodging.tripDefaults.guestCount` | tripDefault | private | Usual number of guests |
| `preferences.lodging.tripDefaults.bedroomCount` | tripDefault | private | Usual number of bedrooms for a suite or connecting rooms |
| `preferences.lodging.tripDefaults.rvLength` | tripDefault | private | Length of the traveller's RV |
| `preferences.lodging.tripDefaults.pets` | fact | private | Pets that usually travel |
| `preferences.lodging.tripDefaults.sleepingArrangements` | tripDefault | private | Who sleeps where, for family and group stays (strawman) |
| `preferences.rentalVehicle.sizeClass` | preference | private | Vehicle size class |
| `preferences.rentalVehicle.acrissCodes` | preference | private | Preferences by four-letter ACRISS vehicle code |
| `preferences.rentalVehicle.bodyStyle.sedan4Door` | preference | private | 4-door sedan |
| `preferences.rentalVehicle.bodyStyle.sedan2Door` | preference | private | 2-door sedan |
| `preferences.rentalVehicle.bodyStyle.hatchback4Door` | preference | private | 4-door hatchback |
| `preferences.rentalVehicle.bodyStyle.hatchback2Door` | preference | private | 2-door hatchback |
| `preferences.rentalVehicle.bodyStyle.compactSuv` | preference | private | Compact SUV |
| `preferences.rentalVehicle.bodyStyle.fullSizeSuv` | preference | private | Full-size SUV |
| `preferences.rentalVehicle.bodyStyle.offRoadSuv` | preference | private | Off-road SUV |
| `preferences.rentalVehicle.bodyStyle.minivan` | preference | private | Minivan |
| `preferences.rentalVehicle.bodyStyle.convertible` | preference | private | Convertible |
| `preferences.rentalVehicle.bodyStyle.pickup` | preference | private | Pickup |
| `preferences.rentalVehicle.bodyStyle.van` | preference | private | Van |
| `preferences.rentalVehicle.cover.fullCollision` | preference | private | Full collision cover |
| `preferences.rentalVehicle.cover.collisionWithDeductible` | preference | private | Collision cover with deductible |
| `preferences.rentalVehicle.cover.maxCollisionDeductible` | preference | private | Maximum collision deductible |
| `preferences.rentalVehicle.cover.fullTheft` | preference | private | Full theft cover |
| `preferences.rentalVehicle.cover.theftWithDeductible` | preference | private | Theft cover with deductible |
| `preferences.rentalVehicle.cover.maxTheftDeductible` | preference | private | Maximum theft deductible |
| `preferences.rentalVehicle.cover.fullLiability` | preference | private | Full liability cover |
| `preferences.rentalVehicle.cover.roadsideAssistance` | preference | private | Roadside assistance |
| `preferences.rentalVehicle.equipment.childSeat` | preference | private | Child seat |
| `preferences.rentalVehicle.equipment.gpsNavigation` | preference | private | GPS navigation |
| `preferences.rentalVehicle.equipment.appleCarPlayUsbA` | preference | private | Apple CarPlay over USB-A |
| `preferences.rentalVehicle.equipment.appleCarPlayUsbC` | preference | private | Apple CarPlay over USB-C |
| `preferences.rentalVehicle.equipment.appleCarPlayBluetooth` | preference | private | Apple CarPlay over Bluetooth |
| `preferences.rentalVehicle.equipment.androidAutoUsbA` | preference | private | Android Auto over USB-A |
| `preferences.rentalVehicle.equipment.androidAutoUsbC` | preference | private | Android Auto over USB-C |
| `preferences.rentalVehicle.equipment.androidAutoBluetooth` | preference | private | Android Auto over Bluetooth |
| `preferences.rentalVehicle.prepaidFuel` | preference | private | Prepaid refuelling option |
| `preferences.rentalVehicle.minBootSpace` | preference | private | Minimum boot or trunk space |
| `preferences.rentalVehicle.transmission` | preference | private | Transmission |
| `preferences.rentalVehicle.powertrain` | preference | private | Powertrain |
| `preferences.rentalVehicle.suppliers` | preference | private | Rental company preferences |
| `preferences.rentalVehicle.specialVehicles.motorhome` | preference | private | Motorhome or RV (strawman) |
| `preferences.rentalVehicle.specialVehicles.campervan` | preference | private | Campervan (strawman) |
| `preferences.rentalVehicle.specialVehicles.towableTrailer` | preference | private | Towable trailer or caravan (strawman) |
| `preferences.rentalVehicle.specialVehicles.snowmobile` | preference | private | Snowmobile (strawman) |
| `preferences.rentalVehicle.specialVehicles.motorcycle` | preference | private | Motorcycle (strawman) |
| `preferences.restaurant.seating.booth` | preference | private | Booth (strawman) |
| `preferences.restaurant.seating.chairsWithArms` | preference | private | Chairs with arms (strawman) |
| `preferences.restaurant.seating.chairsWithoutArms` | preference | private | Chairs without arms (strawman) |
| `preferences.restaurant.seating.stableSeating` | preference | private | Stable, non-swivel seating (strawman) |
| `preferences.restaurant.seating.highTop` | preference | private | High-top table (strawman) |
| `preferences.restaurant.seating.bar` | preference | private | Bar seating (strawman) |
| `preferences.restaurant.seating.fixedSeating` | preference | private | Fixed seating (strawman) |

## otherPreferences

Optional. Keyed preferences for travel categories that do not yet have a structured section. Graduates into preferences once the keys are agreed.

## accessibility

Optional. Accessibility information and needs. Every item is special category data and may only be disclosed under an explicit consent grant

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `accessibility.needs` | requirement | specialCategory | Summary flags for systems that only accept coarse categories |
| `accessibility.ssrCodes` | requirement | specialCategory | IATA special service request codes to send, for example WCHR |
| `accessibility.assistiveTechnology` | requirement | specialCategory | Assistive technologies the traveller uses, for example screen readers |
| `accessibility.notes` | requirement | specialCategory | Free-text assistance notes |
| `accessibility.arrivalEntryExit.stepFreeRoute` | requirement | specialCategory | Step-free route |
| `accessibility.arrivalEntryExit.maxStepHeight` | requirement | specialCategory | Maximum height of steps, kerbs or lips on a step-free route |
| `accessibility.arrivalEntryExit.levelDropOffSideRamp` | requirement | specialCategory | Drop-off on a level surface with room to deploy a side ramp or lift |
| `accessibility.arrivalEntryExit.levelDropOffRearRamp` | requirement | specialCategory | Drop-off on a level surface with room to deploy a rear ramp or lift |
| `accessibility.arrivalEntryExit.parkingExtraWidth` | requirement | specialCategory | Parking with extra width |
| `accessibility.arrivalEntryExit.parkingAccessAisle` | requirement | specialCategory | Parking with access aisle |
| `accessibility.arrivalEntryExit.minParkingClearance` | requirement | specialCategory | Minimum parking vertical clearance |
| `accessibility.arrivalEntryExit.minEntryDoorWidth` | requirement | specialCategory | Minimum entry door width |
| `accessibility.arrivalEntryExit.automaticOrLowForceEntryDoor` | requirement | specialCategory | Automatic or low-force entry door |
| `accessibility.arrivalEntryExit.nonRevolvingDoor` | requirement | specialCategory | Non-revolving door always usable |
| `accessibility.arrivalEntryExit.maxRampSlope` | requirement | specialCategory | Maximum ramp slope |
| `accessibility.arrivalEntryExit.rampHandrails` | requirement | specialCategory | Ramp handrails |
| `accessibility.arrivalEntryExit.rampEdgeProtection` | requirement | specialCategory | Ramp edge protection |
| `accessibility.arrivalEntryExit.rampRestLandings` | requirement | specialCategory | Ramp rest landings |
| `accessibility.arrivalEntryExit.minLiftWidth` | requirement | specialCategory | Minimum elevator or lift width |
| `accessibility.arrivalEntryExit.minLiftDepth` | requirement | specialCategory | Minimum elevator or lift depth |
| `accessibility.arrivalEntryExit.liftControlsReachableSeated` | requirement | specialCategory | Elevator or lift controls reachable from a seated position |
| `accessibility.arrivalEntryExit.fallbackRouteIfLiftFails` | requirement | specialCategory | Fallback route if the elevator or lift fails |
| `accessibility.arrivalEntryExit.maxWalkingDistanceWithoutRest` | requirement | specialCategory | Maximum walking distance without rest points |
| `accessibility.arrivalEntryExit.queueSeating` | requirement | specialCategory | Seating areas at any queues |
| `accessibility.arrivalEntryExit.seatedHeightServiceCounter` | requirement | specialCategory | Desk or counter service suitable for a seated guest |
| `accessibility.arrivalEntryExit.stairHandrailsBothSides` | requirement | specialCategory | Stair handrails on both sides |
| `accessibility.arrivalEntryExit.slipResistantSurfaces` | requirement | specialCategory | Slip-resistant surfaces |
| `accessibility.arrivalEntryExit.noRoughSurfaces` | requirement | specialCategory | No rough surfaces such as deep pile carpet, gravel or sand |
| `accessibility.arrivalEntryExit.weatherProtectedRoutes` | requirement | specialCategory | Weather-protected routes with snow and ice cleared |
| `accessibility.arrivalEntryExit.transportForLongerDistances` | requirement | specialCategory | Transport available for longer distances |
| `accessibility.mobilityIndoors.minDoorCorridorWidth` | requirement | specialCategory | Minimum door and corridor width |
| `accessibility.mobilityIndoors.noHeavyManualDoors` | requirement | specialCategory | No heavy doors without automation |
| `accessibility.mobilityIndoors.manoeuvringSpaceAtDoors` | requirement | specialCategory | Manoeuvring space on both sides of doors |
| `accessibility.mobilityIndoors.restaurantTableAndRestroomAccess` | requirement | specialCategory | Access to tables and restroom in restaurants |
| `accessibility.mobilityIndoors.tablesWithKneeClearance` | requirement | specialCategory | Tables with knee clearance |
| `accessibility.mobilityIndoors.minTurningSpace` | requirement | specialCategory | Minimum turning space within a room |
| `accessibility.mobilityIndoors.clearFloorTransferSideOfBed` | requirement | specialCategory | Clear floor space on the transfer side of the bed |
| `accessibility.mobilityIndoors.minBedSurfaceHeight` | requirement | specialCategory | Minimum bed surface height |
| `accessibility.mobilityIndoors.maxBedSurfaceHeight` | requirement | specialCategory | Maximum bed surface height |
| `accessibility.mobilityIndoors.controlsReachableSeated` | requirement | specialCategory | Room controls, switches, peephole, closet rods and hooks reachable from a seated position |
| `accessibility.mobilityIndoors.controlsReachableFromBed` | requirement | specialCategory | Room controls and light switches reachable from the bed |
| `accessibility.mobilityIndoors.controlsOperableWithoutGrip` | requirement | specialCategory | Controls operable with one hand, a closed fist or no grip strength, without pinching or twisting |
| `accessibility.mobilityIndoors.leverHandles` | requirement | specialCategory | Lever handles instead of knobs |
| `accessibility.mobilityIndoors.deskCounterKneeClearance` | requirement | specialCategory | Desk and counters with knee clearance |
| `accessibility.mobilityIndoors.bedRails` | requirement | specialCategory | Bed rails |
| `accessibility.mobilityIndoors.bedAssistHandles` | requirement | specialCategory | Bed assist handles |
| `accessibility.mobilityIndoors.operableWithLimitedGrip` | requirement | specialCategory | Doors, buttons, switches, touchscreens and payment terminals operable with limited grip |
| `accessibility.mobilityIndoors.operableWithOneHand` | requirement | specialCategory | Doors, buttons, switches, touchscreens and payment terminals operable with one hand |
| `accessibility.mobilityIndoors.operableWithNoHandFunction` | requirement | specialCategory | Doors, buttons, switches, touchscreens and payment terminals operable with no hand function |
| `accessibility.mobilityIndoors.luggageAssistance` | requirement | specialCategory | Luggage assistance |
| `accessibility.eating.carryingAndOpeningAssistance` | requirement | specialCategory | Help carrying trays, plates and drinks and opening condiments and sealed containers |
| `accessibility.eating.adaptiveCutlery` | requirement | specialCategory | Adaptive cutlery |
| `accessibility.eating.cupsWithHandles` | requirement | specialCategory | Cups with handles |
| `accessibility.eating.cupsWithLids` | requirement | specialCategory | Cups with lids |
| `accessibility.eating.plateGuards` | requirement | specialCategory | Plate guards |
| `accessibility.eating.nonSlipMats` | requirement | specialCategory | Non-slip mats |
| `accessibility.eating.buffetWithinReachOrServed` | requirement | specialCategory | Buffet items within reach, or staff to serve |
| `accessibility.eating.oneHandedServingUtensils` | requirement | specialCategory | Lids, tongs and utensils usable one-handed |
| `accessibility.eating.alternativesToQrOrdering` | requirement | specialCategory | Alternatives to QR code ordering |
| `accessibility.eating.nearRestroom` | requirement | specialCategory | Seating near the restroom |
| `accessibility.eating.awayFromDraughts` | requirement | specialCategory | Seating away from draughts |
| `accessibility.eating.awayFromHeat` | requirement | specialCategory | Seating away from heat |
| `accessibility.eating.awayFromDoorTraffic` | requirement | specialCategory | Seating away from door traffic |
| `accessibility.eating.awayFromStrongSmells` | requirement | specialCategory | Seating away from strong smells |
| `accessibility.eating.foodCutUp` | requirement | specialCategory | Food cut up |
| `accessibility.eating.drinksThickened` | requirement | specialCategory | Drinks thickened |
| `accessibility.eating.formulaPreparationFacilities` | requirement | specialCategory | Hot water and a clean space for formula preparation, including tube feeding |
| `accessibility.general.formAssistance` | requirement | specialCategory | Help completing handwritten forms, or an alternative to a signature |
| `accessibility.general.priorityQueueOrPreboarding` | requirement | specialCategory | Priority or separate queues, preboarding or similar |
| `accessibility.general.minWeightCapacity` | requirement | specialCategory | Minimum weight capacity of seats, beds and toilets |
| `accessibility.general.raisableArmrests` | requirement | specialCategory | Raisable armrests on chairs |
| `accessibility.general.noTurnstiles` | requirement | specialCategory | No turnstiles |
| `accessibility.transport.seatBeltExtender` | requirement | specialCategory | Seat belt extender |
| `accessibility.transport.extraSeatWidthOrSecondSeat` | requirement | specialCategory | Extra seat width or a second seat |
| `accessibility.transport.lavatoryAssistance` | requirement | specialCategory | Bathroom assistance |
| `accessibility.bathroom.rollInShower` | requirement | specialCategory | Curbless roll-in shower |
| `accessibility.bathroom.transferShower` | requirement | specialCategory | Transfer shower |
| `accessibility.bathroom.bathWithTransferSeat` | requirement | specialCategory | Bath with transfer seat |
| `accessibility.bathroom.foldDownShowerSeat` | requirement | specialCategory | Fold-down shower seat |
| `accessibility.bathroom.freestandingShowerChair` | requirement | specialCategory | Freestanding shower chair |
| `accessibility.bathroom.minShowerChairWidth` | requirement | specialCategory | Minimum shower chair width |
| `accessibility.bathroom.minShowerChairWeightCapacity` | requirement | specialCategory | Minimum shower chair weight capacity |
| `accessibility.bathroom.handheldShowerOnSlideBar` | requirement | specialCategory | Handheld shower head on slide bar |
| `accessibility.bathroom.reachableShowerControls` | requirement | specialCategory | Reachable shower and bath controls |
| `accessibility.bathroom.grabBarShowerSideVertical` | requirement | specialCategory | Vertical grab bar on the side shower or bath wall |
| `accessibility.bathroom.grabBarShowerSideHorizontal` | requirement | specialCategory | Horizontal grab bar on the side shower or bath wall |
| `accessibility.bathroom.grabBarShowerRearVertical` | requirement | specialCategory | Vertical grab bar on the rear shower or bath wall |
| `accessibility.bathroom.grabBarShowerRearHorizontal` | requirement | specialCategory | Horizontal grab bar on the rear shower or bath wall |
| `accessibility.bathroom.grabBarBehindToilet` | requirement | specialCategory | Grab bar behind the toilet |
| `accessibility.bathroom.grabBarToiletTransferSide` | requirement | specialCategory | Toilet grab bar on the transfer side |
| `accessibility.bathroom.minGrabBarLoadRating` | requirement | specialCategory | Minimum grab bar load rating |
| `accessibility.bathroom.raisedToiletSeat` | requirement | specialCategory | Raised toilet seat |
| `accessibility.bathroom.overToiletFrameOrCommode` | requirement | specialCategory | Over-toilet frame or commode chair |
| `accessibility.bathroom.minToiletSideClearance` | requirement | specialCategory | Minimum toilet side clearance on the transfer side |
| `accessibility.bathroom.flushReachableFromSeat` | requirement | specialCategory | Toilet flush control reachable from the seat |
| `accessibility.bathroom.caregiverSpace` | requirement | specialCategory | Additional space for a caregiver |
| `accessibility.bathroom.sinkKneeClearance` | requirement | specialCategory | Sink with knee clearance |
| `accessibility.bathroom.leverTaps` | requirement | specialCategory | Lever taps on the sink |
| `accessibility.bathroom.reachableSoap` | requirement | specialCategory | Reachable soap at the sink |
| `accessibility.bathroom.mirrorUsableSeatedOrStanding` | requirement | specialCategory | Mirror usable seated or standing |
| `accessibility.bathroom.reachableTowelHooks` | requirement | specialCategory | Reachable towel hooks |
| `accessibility.bathroom.slipResistantFloor` | requirement | specialCategory | Slip-resistant floor |
| `accessibility.bathroom.noRaisedThreshold` | requirement | specialCategory | No raised floor threshold |
| `accessibility.bathroom.floorDrainage` | requirement | specialCategory | Drainage for standing water |
| `accessibility.bathroom.emergencyPullCord` | requirement | specialCategory | Emergency pull cord reachable from the shower, toilet and floor |
| `accessibility.sleeping.adjustableBed` | requirement | specialCategory | Adjustable bed, head and foot |
| `accessibility.sleeping.spaceForOwnBed` | requirement | specialCategory | Room for the traveller's own hospital-style bed |
| `accessibility.sleeping.firmOrPressureRelievingMattress` | requirement | specialCategory | Firm or pressure-relieving mattress |
| `accessibility.sleeping.extraPillowsOrWedges` | requirement | specialCategory | Extra pillows or wedges |
| `accessibility.guestRoom.tactileAudibleOrVoiceControls` | requirement | specialCategory | In-room controls with tactile or audible markings or voice control |
| `accessibility.mobilityEquipment` | fact | specialCategory | Mobility equipment the traveller brings |
| `accessibility.equipmentHandling.storageSpace` | requirement | specialCategory | Parking or storage space for the equipment |
| `accessibility.equipmentHandling.chargingPower` | requirement | specialCategory | Power available for charging |
| `accessibility.equipmentHandling.vehicleLoadingRamp` | requirement | specialCategory | Vehicle loading ramp |
| `accessibility.equipmentHandling.vehicleTieDowns` | requirement | specialCategory | Vehicle device tie-downs |
| `accessibility.equipmentHandling.vehicleRideInChair` | requirement | specialCategory | Vehicle avoids the need to transfer out of the chair |
| `accessibility.equipmentHandling.standPivotTransfer` | requirement | specialCategory | Stand-pivot transfer |
| `accessibility.equipmentHandling.slideBoardTransfer` | requirement | specialCategory | Slide board transfer |
| `accessibility.equipmentHandling.personalHoistTransfer` | requirement | specialCategory | Personal hoist transfer |
| `accessibility.equipmentHandling.providerHoistTransfer` | requirement | specialCategory | Provider hoist transfer |
| `accessibility.equipmentHandling.staffTrainedForTransfer` | requirement | specialCategory | Staff trained in the transfer technique |
| `accessibility.equipmentHandling.aisleChairOrBoardingLift` | requirement | specialCategory | Aisle chair, boarding ramp or lift for narrow aisles |
| `accessibility.equipmentHandling.deliveredAtAircraftDoor` | requirement | specialCategory | Equipment delivered at the aircraft door after the flight |
| `accessibility.equipmentHandling.loanerIfDamagedOrLost` | requirement | specialCategory | Loaner if the device is damaged, delayed or lost |
| `accessibility.vision.orientationWalkThrough` | requirement | specialCategory | Walk-through of relevant facilities on arrival |
| `accessibility.vision.tactileOrBrailleSignage` | requirement | specialCategory | Tactile or Braille signage |
| `accessibility.vision.liftFloorAnnouncements` | requirement | specialCategory | Elevator floor announcements |
| `accessibility.vision.accessibleMaterials` | requirement | specialCategory | Printed materials available in an accessible format |
| `accessibility.vision.accessibleFormats` | requirement | specialCategory | Accessible formats the traveller can use |
| `accessibility.vision.accessibleKiosksOrAlternative` | requirement | specialCategory | Kiosks enabled for low vision, or alternatives |
| `accessibility.vision.verbalSafetyAnnouncements` | requirement | specialCategory | Verbal safety announcements and warnings |
| `accessibility.vision.litPathToBathroom` | requirement | specialCategory | Lit path to the bathroom at night |
| `accessibility.vision.seatingAwayFromGlare` | requirement | specialCategory | Seating away from windows and glare |
| `accessibility.vision.sightedGuide` | requirement | specialCategory | Sighted guide (strawman) |
| `accessibility.hearing.signLanguageInterpreters` | requirement | specialCategory | Sign language interpreters by ISO 639-3 code, for example ase, bfi, fsl |
| `accessibility.hearing.liveCaptioning` | requirement | specialCategory | Live captioning |
| `accessibility.hearing.nonVoiceAlternatives` | requirement | specialCategory | Alternatives to intercom-only entry, voice-only ordering or spoken-only announcements |
| `accessibility.hearing.hearingLoops` | requirement | specialCategory | Hearing loops |
| `accessibility.hearing.guideMicrophones` | requirement | specialCategory | Tour guides use microphones |
| `accessibility.hearing.guideWrittenMaterials` | requirement | specialCategory | Tour guides provide written scripts or visual materials |
| `accessibility.hearing.quietRestaurantTable` | requirement | specialCategory | Quiet table in restaurants |
| `accessibility.hearing.quietRoom` | requirement | specialCategory | Quiet room |
| `accessibility.hearing.visualOrVibratingDoorAlerts` | requirement | specialCategory | Visual or vibrating alert for door knock, doorbell and room phone |
| `accessibility.hearing.vibratingOrFlashingWakeAlarm` | requirement | specialCategory | Vibrating or flashing alarm clock, bed shaker or pillow vibrator |
| `accessibility.hearing.visualAndVibratingFireAlarms` | requirement | specialCategory | Visual and vibrating fire and emergency alarms in room and bathroom |
| `accessibility.hearing.textAlerts` | requirement | specialCategory | Text alerts for urgent announcements |
| `accessibility.medicalLogistics.continuousBedsidePower` | requirement | specialCategory | Continuous power at the bed for medical devices |
| `accessibility.medicalLogistics.distilledWater` | requirement | specialCategory | Distilled water source |
| `accessibility.medicalLogistics.portableOxygen` | requirement | specialCategory | Portable oxygen equipment |
| `accessibility.medicalLogistics.medicationStorage` | requirement | specialCategory | Medication and supply storage |
| `accessibility.medicalLogistics.medicationStorageMinTemp` | requirement | specialCategory | Minimum storage temperature |
| `accessibility.medicalLogistics.medicationStorageMaxTemp` | requirement | specialCategory | Maximum storage temperature |
| `accessibility.medicalLogistics.freezerForIcePacks` | requirement | specialCategory | Freezer for ice packs |
| `accessibility.medicalLogistics.backupFreezer` | requirement | specialCategory | Backup freezer if the main freezer fails |
| `accessibility.medicalLogistics.sharpsDisposal` | requirement | specialCategory | Sharps container and disposal |
| `accessibility.medicalLogistics.privateSpaceForMedication` | requirement | specialCategory | Private clean place to inject or take medication |
| `accessibility.medicalLogistics.lockableMedicineStorage` | requirement | specialCategory | Secure lockable storage for controlled or valuable medicines |
| `accessibility.medicalLogistics.nearbyPharmacy` | requirement | specialCategory | Nearby backup pharmacy |
| `accessibility.medicalLogistics.medicalWasteDisposal` | requirement | specialCategory | Waste disposal for catheter, ostomy and injection supplies |
| `accessibility.medicalLogistics.handheldBidet` | requirement | specialCategory | Handheld bidet |
| `accessibility.medicalLogistics.unrestrictedNearbyRestroom` | requirement | specialCategory | Nearby unrestricted restroom |
| `accessibility.medicalLogistics.roomTemperatureControl` | requirement | specialCategory | Control of room temperature |
| `accessibility.medicalLogistics.bathroomDoorOpenableFromOutside` | requirement | specialCategory | Bathroom door openable from outside |
| `accessibility.medicalLogistics.lowOrPaddedSleepingSurface` | requirement | specialCategory | Low or padded sleeping surface |
| `accessibility.medicalLogistics.snacksOrGlucoseAvailable` | requirement | specialCategory | Snacks or glucose available in every setting |
| `accessibility.medicalLogistics.alternativeSecurityScreening` | requirement | specialCategory | Alternative security screening for implanted devices |
| `accessibility.serviceAnimals` | fact | specialCategory | Service animals that travel with the traveller |
| `accessibility.serviceAnimalFacilities.reliefArea` | requirement | specialCategory | Relief area |
| `accessibility.serviceAnimalFacilities.accessibleReliefArea` | requirement | specialCategory | Relief area the traveller can reach given their own limitations |
| `accessibility.serviceAnimalFacilities.waitingArea` | requirement | specialCategory | Waiting area for service animals, for example near rides |
| `accessibility.equipmentLoanOrRental` | requirement | specialCategory | Equipment the traveller needs the provider to lend or rent (strawman) |
| `accessibility.oxygen.ownConcentratorOnBoard` | requirement | specialCategory | Traveller's own portable oxygen concentrator permitted and usable on board (strawman) |
| `accessibility.oxygen.providerOxygenInTransit` | requirement | specialCategory | Oxygen supplied by the carrier during the journey (strawman) |
| `accessibility.oxygen.oxygenDeliveredAtDestination` | requirement | specialCategory | Oxygen delivered to the accommodation (strawman) |
| `accessibility.oxygen.flowRate` | requirement | specialCategory | Prescribed flow rate (strawman) |
| `accessibility.medicalSupplies.medicalBaggageAllowance` | requirement | specialCategory | Extra baggage allowance for medical supplies and equipment (strawman) |
| `accessibility.medicalSupplies.suppliesKeptInCabin` | requirement | specialCategory | Medication and medical supplies kept with the traveller in the cabin (strawman) |
| `accessibility.medicalSupplies.medicalLiquidsThroughSecurity` | requirement | specialCategory | Medical liquids, feeds and gels above the standard limit carried through security (strawman) |
| `accessibility.medicalSupplies.suppliesDeliveredAhead` | requirement | specialCategory | Property accepts and stores medical supplies delivered before arrival (strawman) |
| `accessibility.medicalSupplies.dedicatedMedicalFridge` | requirement | specialCategory | Refrigerator reserved for medical items, not a minibar (strawman) |
| `accessibility.medicalSupplies.minRefrigeratedVolume` | requirement | specialCategory | Minimum refrigerated storage volume (strawman) |
| `accessibility.medicalSupplies.powerAtSeat` | requirement | specialCategory | Power at the seat for a medical device (strawman) |
| `accessibility.medicalSupplies.devices` | fact | specialCategory | Medical devices the traveller brings (strawman) |
| `accessibility.nutritionAndInfusion.parenteralNutritionStorage` | requirement | specialCategory | Refrigerated storage for parenteral nutrition bags (strawman) |
| `accessibility.nutritionAndInfusion.enteralFeedStorage` | requirement | specialCategory | Storage for enteral feeds (strawman) |
| `accessibility.nutritionAndInfusion.dripStand` | requirement | specialCategory | Drip stand or IV pole (strawman) |
| `accessibility.nutritionAndInfusion.cleanSurfaceAndSinkForLineCare` | requirement | specialCategory | Clean wipeable surface and hand-washing sink for aseptic line care (strawman) |
| `accessibility.nutritionAndInfusion.visitingNurseAccess` | requirement | specialCategory | Visiting nurse or carer given access to the room (strawman) |
| `accessibility.nutritionAndInfusion.clinicalWasteCollection` | requirement | specialCategory | Clinical waste collection (strawman) |
| `accessibility.continenceAndOstomy.toiletAtShortNotice` | requirement | specialCategory | Access to a toilet at short notice (strawman) |
| `accessibility.continenceAndOstomy.seatNearLavatory` | requirement | specialCategory | Seat near a lavatory (strawman) |
| `accessibility.continenceAndOstomy.stomaFriendlyToilet` | requirement | specialCategory | Toilet with shelf, hook, mirror and disposal bin for changing a stoma bag (strawman) |
| `accessibility.continenceAndOstomy.adultChangingFacility` | requirement | specialCategory | Changing facility with adult-sized bench and hoist (strawman) |
| `accessibility.continenceAndOstomy.privateChangingSpace` | requirement | specialCategory | Private space to change a bag or pad (strawman) |
| `accessibility.continenceAndOstomy.waterproofMattressProtector` | requirement | specialCategory | Waterproof mattress protector (strawman) |
| `accessibility.continenceAndOstomy.extraLinenAndTowels` | requirement | specialCategory | Extra linen and towels (strawman) |
| `accessibility.continenceAndOstomy.laundryAtShortNotice` | requirement | specialCategory | Laundry access at short notice (strawman) |
| `accessibility.careAndProximity.carerInSameOrAdjoiningRoom` | requirement | specialCategory | Parent or carer in the same or an adjoining room (strawman) |
| `accessibility.careAndProximity.carerSeatedAdjacent` | requirement | specialCategory | Parent or carer seated next to the traveller (strawman) |
| `accessibility.careAndProximity.carerAdmittedEverywhere` | requirement | specialCategory | Carer admitted wherever the traveller goes, including treatment and security areas (strawman) |
| `accessibility.careAndProximity.cotOrCrib` | requirement | specialCategory | Cot or crib (strawman) |
| `accessibility.careAndProximity.hospitalNearby` | requirement | specialCategory | Hospital with relevant specialist care nearby (strawman) |
| `accessibility.careAndProximity.dialysisCentreNearby` | requirement | specialCategory | Dialysis centre nearby (strawman) |
| `accessibility.careAndProximity.enhancedCleaning` | requirement | specialCategory | Enhanced cleaning for an immunocompromised traveller (strawman) |
| `accessibility.cognitiveAndSensory.quietSpace` | requirement | specialCategory | Quiet space available (strawman) |
| `accessibility.cognitiveAndSensory.lowStimulationRoom` | requirement | specialCategory | Room with low noise, light and smell (strawman) |
| `accessibility.cognitiveAndSensory.avoidCrowdsAndQueues` | requirement | specialCategory | Routes and timings that avoid crowds and queues (strawman) |
| `accessibility.cognitiveAndSensory.advanceNoticeOfChanges` | requirement | specialCategory | Advance notice of changes to plans (strawman) |
| `accessibility.cognitiveAndSensory.plainLanguageInformation` | requirement | specialCategory | Information in plain language (strawman) |
| `accessibility.cognitiveAndSensory.easyReadMaterials` | requirement | specialCategory | Easy-read materials (strawman) |
| `accessibility.cognitiveAndSensory.visualGuideBeforeArrival` | requirement | specialCategory | Pictures or a visual guide of the place before arrival (strawman) |
| `accessibility.cognitiveAndSensory.stepByStepInstructions` | requirement | specialCategory | Written step-by-step instructions (strawman) |
| `accessibility.cognitiveAndSensory.extraTime` | requirement | specialCategory | Extra time for check-in, boarding and similar processes (strawman) |
| `accessibility.cognitiveAndSensory.singleNamedContact` | requirement | specialCategory | One named staff contact throughout (strawman) |
| `accessibility.cognitiveAndSensory.staffTrainedInHiddenDisabilities` | requirement | specialCategory | Staff trained in non-visible disabilities (strawman) |
| `accessibility.cognitiveAndSensory.hiddenDisabilityIdentifierRecognised` | requirement | specialCategory | Hidden disability identifier recognised by staff (strawman) |
| `accessibility.cognitiveAndSensory.companionStaysWithTraveller` | requirement | specialCategory | Companion stays with the traveller at all times (strawman) |
| `accessibility.cognitiveAndSensory.privateOrInRoomCheckIn` | requirement | specialCategory | Private or in-room check-in (strawman) |
| `accessibility.cognitiveAndSensory.clearWayfinding` | requirement | specialCategory | Clear, consistent signage and wayfinding (strawman) |
| `accessibility.cognitiveAndSensory.noFlashingLights` | requirement | specialCategory | No flashing or strobe lighting (strawman) |
| `accessibility.cognitiveAndSensory.warningOfLoudNoises` | requirement | specialCategory | Warning before alarms tests and other loud noises (strawman) |
| `accessibility.cognitiveAndSensory.dimmableLighting` | requirement | specialCategory | Dimmable lighting (strawman) |
| `accessibility.cognitiveAndSensory.blackoutCurtains` | requirement | specialCategory | Blackout curtains (strawman) |

## exposureSensitivities

Optional. Air, chemical and allergen exposure. Special category data

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `exposureSensitivities.fragranceAndChemicalFree` | requirement | specialCategory | No air fresheners, scented cleaning or laundry products, potpourri, pesticide spraying, fresh paint or new carpet |
| `exposureSensitivities.awayFromSmokeChlorineKitchenLaundry` | requirement | specialCategory | Not near smoking rooms or areas, chlorinated pools, kitchens or laundries |
| `exposureSensitivities.openableWindows` | requirement | specialCategory | Windows that open |
| `exposureSensitivities.airFiltration` | requirement | specialCategory | Air filtration |
| `exposureSensitivities.hardFlooring` | requirement | specialCategory | Hard flooring |
| `exposureSensitivities.featherFreeBedding` | requirement | specialCategory | Feather and down-free bedding |
| `exposureSensitivities.dustMiteCovers` | requirement | specialCategory | Dust-mite covers |
| `exposureSensitivities.noRecentPets` | requirement | specialCategory | No recent pets in the unit |
| `exposureSensitivities.latexFree` | requirement | specialCategory | No latex |
| `exposureSensitivities.fragranceFreeSoap` | requirement | specialCategory | No soap fragrances or additives |
| `exposureSensitivities.aloeFree` | requirement | specialCategory | No aloe |
| `exposureSensitivities.nonAllergenicSoap` | requirement | specialCategory | Non-allergenic soap provided (strawman) |
| `exposureSensitivities.cleaningProductsDisclosed` | requirement | specialCategory | Cleaning products used disclosed on request (strawman) |

## dietary

Optional. Food allergies, intolerances and diets. Airline meal codes sit in preferences.air.meals

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `dietary.prescribedDiets` | requirement | specialCategory | Medically prescribed diets; others go in restrictions (strawman) |
| `dietary.sensoryFoodNeeds.plainPredictableFoods` | requirement | specialCategory | Plain, predictable foods (strawman) |
| `dietary.sensoryFoodNeeds.itemsServedSeparately` | requirement | specialCategory | Items served separately (strawman) |
| `dietary.sensoryFoodNeeds.noMixedOrTouchingFoods` | requirement | specialCategory | No mixed or touching foods (strawman) |
| `dietary.sensoryFoodNeeds.ownFoodPermitted` | requirement | specialCategory | Traveller's own food permitted (strawman) |
| `dietary.sensoryFoodNeeds.ownFoodStorageAndHeating` | requirement | specialCategory | Storage and heating for the traveller's own food (strawman) |
| `dietary.restrictions` | requirement | specialCategory |  |

## health

Optional. Free-text health conditions and needs not covered by the structured accessibility section.

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `health` | requirement | specialCategory | Free-text health conditions and needs not covered by the structured accessibility section. |

## culturalAndReligiousInformation

Optional. 

| Canonical key | Kind | Classification | Definition |
| --- | --- | --- | --- |
| `culturalAndReligiousInformation` | fact | specialCategory |  |

## travelCharacteristics

Optional. 

## relationships

Optional. 

## platformIDs

Optional. 

## securitySettings

Optional. 

## extensions

Optional. Namespaced custom data.

