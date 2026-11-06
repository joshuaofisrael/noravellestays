"""Page data for scripts/best_rooms_page.py. Every 'confirms' claim must link the exact official page it comes from."""

def a(url, text):
    return f'<a href="{url}" rel="noopener noreferrer" target="_blank">{text}</a>'

WC = "https://thewindsorcourt.com/rooms/"
WCG = "https://thewindsorcourt.com/rooms/guest-room/"
WCP = "https://thewindsorcourt.com/rooms/premium-suite/"
PV = "https://www.pontevedra.com/stay/inn-club/rooms-suites"
PVSO = "https://www.pontevedra.com/stay/inn-club/rooms-suites/superior-oceanfront"
PVPO = "https://www.pontevedra.com/stay/inn-club/rooms-suites/preferred-oceanfront-room"
PVM = "https://www.pontevedra.com/stay/inn-club"

PAGES = [
  {
    "slug": "windsor-court-new-orleans",
    "hotel": "The Windsor Court",
    "city": "New Orleans",
    "city_url": "/hotels/new-orleans/",
    "dest_url": "/guides/where-to-stay-in-new-orleans/",
    "official_url": "https://thewindsorcourt.com/",
    "checked": "2026-11-06", "checked_human": "6 November 2026",
    "title": "Best Rooms at The Windsor Court, New Orleans: Which Room to Request",
    "description": "Which room to ask for at The Windsor Court in New Orleans: Guest Rooms vs Deluxe and Premium Suites, Club Level floors 19 to 22, balconies and how to ask.",
    "coverage": "This guide covers every room category listed on the official rooms page.",
    "quick": {
      "confirms": f"Deluxe Suites are 600 square feet with a private balcony, while 400 square foot Guest Rooms say only that many include a balcony ({a(WC, 'rooms page')}, {a(WCG, 'Guest Rooms page')}). Club Level is on floors 19 to 22 ({a(WC, 'rooms page')}).",
      "recommend": "For most couples, book a Deluxe Suite. Book Club Level if lounge breakfast, afternoon tea and evening drinks matter to you.",
      "ask": "Whether a higher floor, or a room facing the river, is available in the category you booked.",
    },
    "compare": [
      ("Guest Room", "400 sq ft", "1 king or 2 queens", "Not stated", "Many, not all, include a private balcony; sofa bed in many king rooms", WCG),
      ("Deluxe Suite", "600 sq ft", "1 king", "Not stated", "Private balcony; dining table or reading chair", WC),
      ("Premium Suite", "800 sq ft", "1 king or 2 queens", "Not stated", "French doors between living area and bedroom; many include a balcony; two bedroom versions available", WCP),
      ("Two Bedroom Corner Suite", "1,250 sq ft", "1 canopy king plus 2 queens", "Not stated", "Club Level; balcony; two full baths; large wet bar", WC),
      ("Club Level rooms and suites", "Varies", "Varies", "Skyline views", "Floors 19 to 22; lounge access", WC),
      ("Presidential Suite", "2,780 sq ft", "Two bedrooms", "Mississippi River and French Quarter", "22nd floor; private rooftop terraces; private gym", WC),
    ],
    "floors": {
      "confirms": f"Club Level occupies floors 19 to 22 with skyline views, a dedicated concierge and a Club Level Lounge. The James J. Coleman, Jr. Presidential Suite is on the 22nd floor with views across the Mississippi River and the French Quarter ({a(WC, 'rooms page')}). The hotel does not publish which other rooms face the river.",
      "recommend": "If the view matters, Club Level is the only floor range the hotel names. Below it, a higher floor is a sensible request, not a published plan.",
      "ask": "Which side of the building your room faces, and whether a river facing room is open in your category.",
    },
    "request": [
      {"label": "Deluxe Suite",
       "confirms": f"600 square feet, one king bed and a private balcony ({a(WC, 'rooms page')}).",
       "recommend": "The smallest category the hotel lists with a balcony on every unit."},
      {"label": "Club Level, floors 19 to 22",
       "confirms": f"Lounge access with breakfast, afternoon tea, evening cocktails and nightly desserts ({a(WC, 'rooms page')}).",
       "recommend": "Book it for the lounge and the highest floors the hotel names."},
      {"label": "Two Bedroom Corner Suite or connecting rooms",
       "confirms": f"The corner suite is 1,250 square feet with two baths and a balcony, and many Deluxe and Premium Suites connect to adjoining Guest Rooms or suites ({a(WC, 'rooms page')}).",
       "ask": "Reservations to map a connecting layout for your group."},
    ],
    "avoid": [
      {"label": "A Guest Room, if a balcony is the point",
       "confirms": f"Many Guest Rooms include a private balcony, not all ({a(WCG, 'Guest Rooms page')}).",
       "recommend": "Book a Deluxe Suite, or get a balcony confirmed in writing."},
      {"label": "Rooms near elevators or service areas",
       "confirms": f"The hotel describes double paned windows and a quieter setting just beyond the French Quarter ({a(WC, 'rooms page')}). We found no published report of noisy rooms.",
       "recommend": "As a general precaution for light sleepers at any hotel, not a finding about this one, ask for a room away from elevators and service areas."},
    ],
    "ask": [
      "<strong>At booking:</strong> book the category that guarantees what you care about (a Deluxe Suite for a balcony, Club Level for floors 19 to 22), then add a note such as \"Higher floor, river facing if possible.\"",
      f"<strong>By phone:</strong> the hotel asks guests to call reservations at (888) 596 0955 for specific room inventory and accessibility details ({a(WC, 'rooms page')}).",
      f"<strong>Accessibility:</strong> ADA rooms include roll in showers, grab bars and visual alerts ({a(WC, 'rooms page')}).",
      "<strong>At check in:</strong> ask politely whether a higher floor or river facing room is open in your category before you take the key.",
    ],
    "faq": [
      ("What is the best room at The Windsor Court?", "For most couples, a Deluxe Suite. The hotel lists it at 600 square feet with a private balcony. For a lounge and the highest named floors, book Club Level on floors 19 to 22."),
      ("Which floors are Club Level at The Windsor Court?", "The hotel says Club Level occupies floors 19 through 22, with a dedicated concierge and a Club Level Lounge."),
      ("Do all rooms at The Windsor Court have a balcony?", "No. The hotel says many Guest Rooms and many Premium Suites include a private balcony. Deluxe Suites list a private balcony."),
      ("Can I request a river view at The Windsor Court?", "You can ask, but the hotel does not publish which rooms face the river, apart from the Presidential Suite. A request is not a guarantee, so confirm the view with the hotel if it matters."),
    ],
    "sources": [
      ("The Windsor Court: Rooms and Suites (official)", WC),
      ("The Windsor Court: Guest Rooms (official)", WCG),
      ("The Windsor Court: Premium Suites (official)", WCP),
    ],
  },
  {
    "slug": "ponte-vedra-inn-and-club",
    "hotel": "Ponte Vedra Inn & Club",
    "city": "Jacksonville",
    "city_url": "/hotels/jacksonville/",
    "dest_url": "/destinations/us/jacksonville/",
    "official_url": PVM,
    "checked": "2026-11-06", "checked_human": "6 November 2026",
    "title": "Best Rooms at Ponte Vedra Inn & Club: Which Room to Request",
    "description": "Which room to ask for at Ponte Vedra Inn & Club: Superior Oceanfront vs Preferred Oceanfront vs Beachside, oceanfront suites, Historic Inn and Island View rooms, and how to ask.",
    "coverage": "This guide covers the Inn &amp; Club categories on the official rooms page; the suites list only short descriptions there, so we compare what is published.",
    "quick": {
      "confirms": f"Superior Oceanfront rooms are the resort's newest and most popular rooms, with panoramic Atlantic views and an oceanfront balcony or terrace ({a(PVSO, 'Superior Oceanfront page')}). Preferred Beachside rooms have limited or no ocean views ({a(PV, 'rooms page')}).",
      "recommend": "Book Superior Oceanfront if the ocean view is why you are going. Preferred Oceanfront also faces the ocean and adds a kitchenette.",
      "ask": "Which building your category is in, before you pay.",
    },
    "compare": [
      ("Superior Oceanfront", "Not stated", "1 king or 2 queens", "Panoramic ocean", "Newest and most popular per the resort; oceanfront balcony or terrace; soaking tub", PVSO),
      ("Superior Oceanfront Suite", "Not stated", "1 king", "Not stated beyond oceanfront", "Balcony or terrace; up to 5 guests", PV),
      ("Oceanfront Suite", "Not stated", "1 king", "Not stated beyond oceanfront", "Described as premium location and spacious; balcony or terrace", PV),
      ("Preferred Oceanfront", "Not stated", "1 king or 2 queens", "Ocean view from balcony or patio", "Kitchenette; connecting rooms; parking near the room", PVPO),
      ("Superior Beachside", "Not stated", "1 king", "Side ocean views", "Up to 3 guests; balcony or terrace", PV),
      ("Preferred Beachside", "Not stated", "1 king or 2 queens", "Limited or no ocean view", "Close to the beach; kitchenette", PV),
      ("Historic Inn Room", "Not stated", "1 king or 2 queens", "Resort or lagoon", "Above the Great Lounge and lobby; balcony", PV),
      ("Island View Room", "Not stated", "1 king or 2 queens", "Inland lagoons and the 9th Island Hole", "Island House; balcony or terrace", PV),
      ("Penthouse Suite", "Not stated", "1 king", "Ocean and the signature fountain", "High atop the Inn; private elevator access", PV),
      ("Presidential Suite", "Not stated", "1 king", "Panoramic ocean", "Two at the resort; patio or balcony", PV),
    ],
    "floors": {
      "confirms": f"The resort has 262 rooms and suites in ten low rise buildings ({a(PV, 'rooms page')}). The Penthouse Suite is located high atop the Inn with private elevator access ({a(PV, 'rooms page')}). The resort map names buildings such as the Atlantic House and the Historic Inn ({a(PVM, 'resort overview')}), but the official pages do not say which room types sit in which building.",
      "recommend": "In low rise buildings, the category and outlook matter more than the floor. Choose by view first.",
      "ask": "Which building and outlook your category comes with.",
    },
    "request": [
      {"label": "Superior Oceanfront",
       "confirms": f"Panoramic Atlantic views and an oceanfront balcony or terrace ({a(PVSO, 'Superior Oceanfront page')}).",
       "recommend": "The room to book for the ocean view."},
      {"label": "Preferred Oceanfront",
       "confirms": f"Ocean views from the private balcony or patio, a kitchenette and connecting rooms ({a(PVPO, 'Preferred Oceanfront page')}).",
       "recommend": "A good choice for families who want the ocean and a kitchenette."},
      {"label": "Superior Oceanfront Suite, Oceanfront Suite or Presidential Suite",
       "confirms": f"Each lists one king bed and a balcony or terrace; the two Presidential Suites have panoramic Atlantic views ({a(PV, 'rooms page')}).",
       "ask": "For the layout and view of the specific suite, since the resort publishes only short descriptions."},
      {"label": "Penthouse Suite",
       "confirms": f"High atop the Inn, with private elevator access and views of the ocean and the signature fountain ({a(PV, 'rooms page')}).",
       "recommend": "For a one of a kind stay, the Penthouse Suite."},
    ],
    "avoid": [
      {"label": "Preferred Beachside, if you want a sea view",
       "confirms": f"Limited or no ocean views ({a(PV, 'rooms page')}).",
       "recommend": "Book an Oceanfront category instead."},
      {"label": "Superior Beachside, if you want a straight on view",
       "confirms": f"Side views of the Atlantic ({a(PV, 'rooms page')}).",
       "recommend": "Expect that some of these rooms may see only part of the ocean."},
      {"label": "Island View or Historic Inn rooms, for a beach view",
       "confirms": f"Island View rooms overlook the lagoons and the 9th Island Hole; Historic Inn rooms look over the resort or lagoon ({a(PV, 'rooms page')})."},
      {"label": "Historic Inn rooms, for noise sensitive guests",
       "confirms": f"These rooms are located above the Great Lounge and lobby ({a(PV, 'rooms page')}).",
       "ask": "If you are sensitive to noise, ask about the exact position of your room before arrival."},
    ],
    "ask": [
      "<strong>At booking:</strong> choose the category that guarantees the view. A request note will not turn a Beachside booking into an Oceanfront room.",
      f"<strong>By phone:</strong> resort reservations are listed at (888) 839 9145 ({a(PVM, 'resort overview')}); ask which building your category is in.",
      f"<strong>Families:</strong> Superior Oceanfront and Preferred Oceanfront rooms list connecting rooms ({a(PVSO, 'Superior Oceanfront')}, {a(PVPO, 'Preferred Oceanfront')}); request them when you book.",
      "<strong>At check in:</strong> ask whether a room with a better ocean outlook is open in your category.",
    ],
    "faq": [
      ("What is the best room at Ponte Vedra Inn & Club?", "For most guests who want the ocean, a Superior Oceanfront room. The resort calls it the newest and most popular room, with panoramic Atlantic views and an oceanfront balcony or terrace."),
      ("Which rooms at Ponte Vedra Inn & Club do not have an ocean view?", "The resort says Preferred Beachside rooms have limited or no ocean views. Historic Inn rooms face the resort or lagoon, and Island View rooms face the lagoons and golf course. Superior Beachside rooms have side views."),
      ("Does Ponte Vedra Inn & Club have connecting rooms?", "Yes. The resort lists connecting rooms for Preferred Oceanfront and Superior Oceanfront rooms. Request them when you book."),
      ("Where is the Penthouse Suite at Ponte Vedra Inn & Club?", "The resort says it is high atop the Inn, with private elevator access and views of the ocean and the signature fountain."),
    ],
    "sources": [
      ("Ponte Vedra Inn & Club: Rooms and Suites (official)", PV),
      ("Ponte Vedra Inn & Club: Superior Oceanfront (official)", PVSO),
      ("Ponte Vedra Inn & Club: Preferred Oceanfront Room (official)", PVPO),
      ("Ponte Vedra Inn & Club: resort overview and map (official)", PVM),
    ],
  },
]
